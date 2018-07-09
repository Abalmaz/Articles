from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Post(models.Model):

    STATUS_REVIEW = 0
    STATUS_LIVE = 100

    STATUSES = (
        (STATUS_REVIEW, 'Review'),
        (STATUS_LIVE, 'Live')
    )

    status = models.SmallIntegerField(choices=STATUSES, default=STATUS_REVIEW)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

