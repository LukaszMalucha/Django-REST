from django.urls import path, include
from languages import views
from rest_framework import routers

app_name = 'languages'

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paradigms', views.ParadigmView)
router.register('programmers', views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls)),
]