from django.urls import path
from .views import SuperAdminUserListView

urlpatterns = [
    path('superadmin/users/', SuperAdminUserListView.as_view(), name='superadmin-users'),
]
