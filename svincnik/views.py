from django.contrib.auth.models import User
from svincnik.models import Jed, Komentar
from svincnik.serializers import (JediSerializer,
                                  UserSerializer,
                                  KomentarSerializer)
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, CannotBeChanged
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets


class JedViewSet(viewsets.ModelViewSet):
    queryset = Jed.objects.all()
    serializer_class = JediSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class KomentarViewSet(viewsets.ModelViewSet):
    queryset = Komentar.objects.all()
    serializer_class = KomentarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          CannotBeChanged,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'jedi': reverse('jedi-list', request=request, format=format),
        'komentarji': reverse('komentarji-list',
                              request=request,
                              format=format)
    })
