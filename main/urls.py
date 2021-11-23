from django.urls import path
from . import views

urlpatterns = [
    path('detection',views.detection, name='detection'),
    path('angry/movie',views.angry_movie,name='angry_movie'),
    path('angry/games',views.angry_games,name='angry_games'),
    path('angry/motivation', views.angry_motivation, name='angry_motivation'),
    path('angry/books', views.angry_books, name='angry_books'),
    path('angry/music', views.angry_music, name='angry_music'),
    path('happy/movie',views.happy_movie,name='happy_movie'),
    path('happy/games',views.happy_games,name='happy_games'),
    path('happy/motivation', views.happy_motivation, name='happy_motivation'),
    path('happy/books', views.happy_books, name='happy_books'),
    path('happy/music', views.happy_music, name='happy_music'),
    path('sad/movie',views.sad_movie,name='sad_movie'),
    path('sad/games',views.sad_games,name='sad_games'),
    path('sad/motivation', views.sad_motivation, name='sad_motivation'),
    path('sad/books', views.sad_books, name='sad_books'),
    path('sad/music', views.sad_music, name='sad_music'),
    path('neutral/movie',views.neutral_movie,name='neutral_movie'),
    path('neutral/games',views.neutral_games,name='neutral_games'),
    path('neutral/motivation', views.neutral_motivation, name='neutral_motivation'),
    path('neutral/books', views.neutral_books, name='neutral_books'),
    path('neutral/music', views.surprise_music, name='neutral_music'),
    path('surprise/movie',views.surprise_movie,name='surprise_movie'),
    path('surprise/games',views.surprise_games,name='surprise_games'),
    path('surprise/motivation', views.surprise_motivation, name='surprise_motivation'),
    path('surprise/books', views.surprise_books, name='surprise_books'),
    path('surprise/music', views.surprise_music, name='surprise_music')

]