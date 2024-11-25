from django.contrib import admin
from .models import Movie, GameRecord, InitialQuestion, Comment

# Register your models here.
admin.site.register(Movie)
admin.site.register(GameRecord)
admin.site.register(InitialQuestion)
admin.site.register(Comment)
