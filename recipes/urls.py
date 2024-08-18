from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mexican/', views.cuisine_page, {'cuisine': 'mexican'}, name='mexican'),
    path('ethiopian/', views.cuisine_page, {'cuisine': 'ethiopian'}, name='ethiopian'),
    path('chinese/', views.cuisine_page, {'cuisine': 'chinese'}, name='chinese'),
    path('spanish/', views.cuisine_page, {'cuisine': 'spanish'}, name='spanish'),
    path('italian/', views.cuisine_page, {'cuisine': 'italian'}, name='italian'),
    path('feedback/', views.feedback, name='feedback'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]