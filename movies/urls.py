""" from django.urls import path
from . import views
app_name = 'movies'
urlpatterns = [
    path('', views.index, name='movies.index'),
     path('<int:id>/', views.show, name='movies.show'),
     path('<int:id>/review/create/', views.create_review,
        name='movies.create_review'),
    path('<int:id>/review/create/', views.create_review,
        name='movies.create_review'),
           path('<int:id>/review/<int:review_id>/edit/',
        views.edit_review, name='movies.edit_review'),
        path('<int:id>/review/<int:review_id>/delete/',
        views.delete_review, name='movies.delete_review'), 
    path('hidden/', views.hidden_movies, name='hidden'),
    path('<int:id>/hide/', views.hide_movie, name='hide'),
    path('<int:id>/unhide/', views.unhide_movie, name='unhide'),
    

] """
from django.urls import path
from . import views

# Namespace for reverse lookups
app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/review/create/', views.create_review, name='create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('hidden/', views.hidden_movies, name='hidden'),
    path('<int:id>/hide/', views.hide_movie, name='hide'),
    path('<int:id>/unhide/', views.unhide_movie, name='unhide'),
    
]