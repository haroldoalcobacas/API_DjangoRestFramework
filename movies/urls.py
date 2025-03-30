from django.urls import path
from .import views


urlpatterns = [

    path('movies/',
         views.MovieCreateListView.as_view(),
         name='actors-create-list'),
    path('movies/<int:pk>/',
         views.MovieRetrieveUpdateDestroyView.as_view(),
         name='genre-detail-view'),
    path('movies/stats/', views.MovieStatsView.as_view(),
         name='movie-stats-view'),
]
