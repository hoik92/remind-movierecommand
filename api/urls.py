from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

app_name = 'api'

urlpatterns = [
    path('genres/', views.genre_list, name='genre_list'),

    path('docs/', get_swagger_view(title='API')),
]