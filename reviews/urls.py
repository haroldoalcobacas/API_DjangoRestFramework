from django.urls import path
from .import views


urlpatterns = [

    path('reviews/', views.MovieCreateListView.as_view(),
         name='actors-create-list'),
    path('reviews/<int:pk>/',
         views.MovieRetrieveUpdateDestroyView.as_view(),
         name='genre-detail-view'),

]
