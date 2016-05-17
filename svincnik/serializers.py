from rest_framework import serializers
from svincnik.models import Jed, Komentar
from django.contrib.auth.models import User


class KomentarSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='komentar-detail',
                                               format='json',
                                               read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Komentar
        exclude = ('url',)
        read_only_fields = ('id',)


class JediSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    url = serializers.HyperlinkedIdentityField(view_name='jed-detail',
                                               format='json')
    komentarji = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Jed
        read_only_fields = ('id',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    jedi = serializers.HyperlinkedRelatedField(many=True,
                                               view_name='jed-detail',
                                               read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'jedi')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
