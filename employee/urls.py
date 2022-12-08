
from django.contrib import admin
from django.urls import path, include

from work import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('branch', views.BranchViewSet)
router.register('employees', views.EmployeesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
