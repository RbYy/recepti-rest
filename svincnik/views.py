from django.contrib.auth.models import User
from svincnik.models import Jed
from svincnik.serializers import JediSerializers, UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets


class JedViewSet(viewsets.ModelViewSet):

    queryset = Jed.objects.all()
    serializer_class = JediSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    print('ddd')
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'jedi': reverse('jedi-list', request=request, format=format)
    })
