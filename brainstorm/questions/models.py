from django.db import models
from django.contrib.auth import get_user_model


class Question(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_questions',
    )

class Answer(models.Model):
    comment = models.TextField()
    anonymous = models.BooleanField()
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        related_name='answers',
    )
    provider = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='answers',
    )
