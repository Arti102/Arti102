# scraper/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape_and_save_data, name='scrape_and_save_data'),
]
