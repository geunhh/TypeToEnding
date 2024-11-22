
from django.urls import path,include
from . import views

urlpatterns = [
    path('test/',views.test),   #postman 시험용
    path('movielist/',views.movielist),
    path('record/<int:game_id>/',views.get_movie),
    path('user_record/<int:user_id>/',views.get_user_game_record), # 특정 유저가 플레이한 전적조회

    path('start_game/', views.start_game, name='start_game'), 
    # initial_question 들고와야하니까 구분함
    
    path('play_game/<int:game_id>/', views.play_game, name='play_game'),
    path('recommend/<int:game_id>/', views.recommend_movie),

    path('game-summary/<int:game_id>/',views.get_game_summary, name='game_summary'),
]
