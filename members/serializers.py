from members.models import Team, Member, Connection
from django.core.validators import RegexValidator
from rest_framework import serializers

alpha_only = RegexValidator('^[A-Za-z0-9_]+$', message='Alphanumerics only :^)')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = ('password', 'email',)


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'


class NewMemberSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[alpha_only])
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, data):
        user_name = data.pop('username', None)
        pass_word = data.pop('password', None)
        e_mail = data.pop('email', None)

        does_exist = Member.objects.filter(username__iexact=user_name)
        if len(does_exist) > 0:
            return # TODO:  Actual error response
        
        instance = Member(email=e_mail, username=user_name)

        if pass_word is not None:
            instance.set_password(pass_word)
        instance.save()

        return instance