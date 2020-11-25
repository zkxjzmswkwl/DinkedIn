from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from members.views import MemberViewSet, TeamViewSet, ConnectionViewSet

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'connections', ConnectionViewSet)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    path(r'api/api-token-auth/', views.obtain_auth_token)
]
