"""
URL configuration for owt_back_end project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from owt_api.views import UserModelViewSet, PersonModelViewSet, InitialDataModelViewSet, WeightRecordModelViewSet, \
<<<<<<< HEAD
    BodyMassIndexModelViewSet, register_user_view, set_initial_data_first_connexion_view
=======
    BodyMassIndexModelViewSet, register_user_view
>>>>>>> ce2b312 (Feature 'register' in progress)

router = routers.SimpleRouter()
router.register('users', UserModelViewSet, basename='users')
router.register('persons', PersonModelViewSet, basename='person')
router.register('initialdata', InitialDataModelViewSet, basename='initialdata')
router.register('weights', WeightRecordModelViewSet, basename='weights')
router.register('bmi', BodyMassIndexModelViewSet, basename='bmi')

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/', include(router.urls)),
    path('api/register/', register_user_view, name='register'),
    path('api/init/first-connexion/', set_initial_data_first_connexion_view, name='set_initial_data_first_connexion'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

=======
    path('api/register/', register_user_view, name='register'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
>>>>>>> ce2b312 (Feature 'register' in progress)
]
