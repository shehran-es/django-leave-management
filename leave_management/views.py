from rest_framework import (
    permissions,
    status,
    viewsets,
)
from rest_framework.response import Response

from .models import (
    Leave,
    User, 
)
from .serializers import (
    LeaveSerializer,
    UserSerializer, 
)


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'userId'

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        self.perform_destroy(instance)
        return Response(data, status = status.HTTP_200_OK)
    
class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    lookup_field = 'leaveId'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data        
        self.perform_destroy(instance)
        return Response(data, status = status.HTTP_200_OK)

    