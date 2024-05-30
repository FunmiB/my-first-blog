from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# class: defines object; Post: model name-uppercase no space nor special character.
# models.Model: django model, should be stored in db


class Post(models.Model):
    # Define properties and state text type.;

    # .ForeignKey- property with link to another model.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # .CharField- text with limited no. of charcaters.
    title = models.CharField(max_length=200)

    # .TextField- long text no limit.
    text = models.TextField()

    # .DateTimeField- date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Method/action: indented in class to belong to class. publish- lowercase and underscore.
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # Returns text string with a Post title.

    def __str__(self):
        return self.title
