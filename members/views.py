from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework import permissions, viewsets
from members.models import Member, Team, Connection
from members.serializers import MemberSerializer, TeamSerializer, ConnectionSerializer, NewMemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            pass # TODO: Log ip here

        if self.action == 'create':
            return NewMemberSerializer
        else:
            return MemberSerializer
    

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

