from django.urls import path
from companies import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'companies'

urlpatterns = [
    path('stocks/', views.StockListView.as_view(), name='stocks'),
]