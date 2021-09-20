from django.urls import path, include

from cohort import views

urlpatterns = [
    path('create-cohort', views.create_cohort),
    path('create-native', views.create_native),
    path('display-natives', views.display_natives),
    path('', views.home),
]
