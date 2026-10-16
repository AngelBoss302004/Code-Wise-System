from django.db import models

# Create your models here.
class QuestionsDb(models.Model):
    title=models.CharField(max_length=200)

    LANGUAGE_CHOICE=(
        ("python","Python"),
        ("java","Java"),
        ("javascript","Javascript"),

    )
    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICE,default="python")


    DIFFICULATY_CHOICES=(
        ("easy","Easy"),
        ("medium","Medium"),
        ("hard","Hard"),

    )
    difficulaty_level=models.CharField(max_length=100,choices=DIFFICULATY_CHOICES,default="easy")

    topic=models.CharField(max_length=200)

    notes=models.TextField()

    published_date=models.DateTimeField(auto_now_add=True)

    sample_input=models.CharField()

    sample_output=models.CharField()

    is_active=models.BooleanField()

