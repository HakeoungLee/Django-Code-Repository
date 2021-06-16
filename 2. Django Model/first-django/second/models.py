from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) #생설될 때 시각
    updated_at = models.DateTimeField(auto_now=True) #수정될 때 시각

    # num_stars = models.IntegerField() #숫자필드는 이렇게 선언한다.

