from django.urls import path
from .views import *

urlpatterns = [
    path('', request_url, name='request_url'),
    path('final/', final_url, name='final_url'),
    path('scrape_remote_jobs/', scrape_remote_jobs, name='scrape_remote_jobs'),
]