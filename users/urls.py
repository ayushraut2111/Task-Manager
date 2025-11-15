from django.urls import path
from users.views import AuthViewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('user',AuthViewset,basename="user-auth-apis")


urlpatterns = [

]+router.urls
