"""
URL configuration for finance_dashboard_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from finance.views import FinancialRecordViewSet
from dashboard.views import DashboardSummary
from django.http import HttpResponse
from users.views import UserViewSet

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
    openapi.Info(
        title="Finance Dashboard API",
        default_version='v1',
        description="API for managing financial records and dashboard",
    ),
    public=True,
    permission_classes=[AllowAny],
)

router = DefaultRouter()
router.register(r'records', FinancialRecordViewSet,basename='records')
router.register(r'users', UserViewSet)


def home(request):
    return HttpResponse("Finance Backend API is running")


urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/dashboard/', DashboardSummary.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api/token/', TokenObtainPairView.as_view(permission_classes=[AllowAny])),
    path('api/token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny])),
    
]


