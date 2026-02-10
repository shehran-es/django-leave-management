from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)

# Create your models here.
class UserManager(BaseUserManager): 
    def create_user(self, userId, password = None, **kwargs):
        user = self.model(userId = userId, password = None, **kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user


class User(AbstractBaseUser):
    userId = models.BigIntegerField(primary_key = True)
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    designation = models.CharField(max_length = 200)
    dateOfBirth = models.DateField()
    supervisor = models.CharField(max_length = 200)

    objects = UserManager()

    USERNAME_FIELD = 'userId'
    REQUIRED_FIELDS = ['email', 'firstName', 'lastName']

    class Meta:
        db_table = 'leave_user'


class Leave(models.Model):
    leaveId = models.BigIntegerField(primary_key = True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaves')
    from_date = models.DateField(name = "from")
    to = models.DateField()
    typeOfLeave = models.CharField(name = "type", max_length = 50)
    reason = models.TextField()
    emergencyContact = models.CharField(max_length = 100)

    class Meta: 
        db_table = 'leave_leave'