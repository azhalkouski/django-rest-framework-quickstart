from django.contrib.auth.models import User, Group
from rest_framework import serializers


"""
Notice that we're using huperlinked relations in this case with
HyperlinkedModelSerializer. You can also use primary key and various
other relationships, but hyperlinking is good RESTful design.
"""


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
