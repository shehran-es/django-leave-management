from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import (
    include,
    path,
)

from leave_management.views import (
    UserViewSet,
    LeaveViewSet,
)


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'leaves', LeaveViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('', include(router.urls))
]

