from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)     
    description = models.TextField()            # 줄거리 및 설명
    context = models.TextField()                # 세계관
    poster_path = models.ImageField(upload_to='movie_posters/',null=True, blank=True)

    def __str__(self):
        return self.title
    
class InitialQuestion(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='initial_questions')
    question = models.TextField()



class GameRecord(models.Model):
    COMPLETION_CHOICES = [              # 게임 종료 상태 정의
        ('COMPLETED', '정상 종료'),
        ('FORCED_QUIT', '강제 종료'),
        ('INCOMPLETE', '미완료'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                             related_name='game_records')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='game_records')
    history = models.JSONField(default=list)
    total_score = models.IntegerField(default=0, null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    end_status = models.CharField(max_length=20, choices=COMPLETION_CHOICES, default='INCOMPLETE')
    recommend_movie = models.TextField(max_length=50)

    