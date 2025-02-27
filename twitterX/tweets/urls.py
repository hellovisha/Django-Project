from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_tweets, name='get_list_of_tweets'),
    path('<int:id>/edit_tweet/', views.edit_tweet, name='edit_tweet'),
    path('<int:id>/delete_tweet/', views.delete_tweet, name='delete_tweet'),
    path('create/', views.add_tweet, name='create_tweet'),
    path('register/', views.register, name='register'),
    
]