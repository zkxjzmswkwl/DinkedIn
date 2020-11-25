from django.contrib import admin
from members.models import Team, Connection, Member

admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Connection)