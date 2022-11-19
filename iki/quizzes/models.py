from django.db import models

# Create your models here.
from django.utils.timezone import now

from users.models import User


class QuesModel(models.Model):
    question = models.CharField(
        max_length=200,
        null=True
    )
    op1 = models.CharField(
        max_length=200,
        null=True
    )
    op2 = models.CharField(
        max_length=200,
        null=True
    )
    op3 = models.CharField(
        max_length=200,
        null=True
    )
    op4 = models.CharField(
        max_length=200,
        null=True
    )
    ans = models.CharField(
        max_length=200,
        null=True
    )

    image = models.ImageField(
        upload_to='question/',
        verbose_name='image'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='author'
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='is published'
    )
    date_published = models.DateTimeField(
        default=now(),
        verbose_name='date published'
    )



    def __str__(self):
        return self.question