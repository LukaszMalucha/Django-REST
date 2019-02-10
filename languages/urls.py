from django.urls import path, include
from languages import views
from rest_framework import routers

app_name = 'languages'

router = routers.DefaultRouter()
router.register('list', views.LanguageView)

urlpatterns = [
    path('', include(router.urls)),
]