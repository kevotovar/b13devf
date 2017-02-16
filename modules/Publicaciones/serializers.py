from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            )
        #todos los campos field = ('__ALL__')
class UserSecondSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_active',)



