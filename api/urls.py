from django.urls import path
from api.views import get_languages

urlpatterns = [
    path('api/languages/<str:date>', get_languages)

]
