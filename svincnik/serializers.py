from rest_framework import serializers
from svincnik.models import Jed
from django.contrib.auth.models import User


class JediSerializers(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name='jed-detail', format='json')

    class Meta:
        model = Jed
        fields = ('url', 'ime', 'recept', 'poreklo', 'user', 'vrsta')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    jedi = serializers.HyperlinkedRelatedField(many=True, view_name='jed-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'jedi')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

