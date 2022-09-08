from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from custom_renderer import views

urlpatterns = [
    path('', views.DataList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

