from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

#difines our model as an object class is a keyword that indicatese that we are defining an object post is the name of our model modelsModel meants that the post is a Django medel so it should be saved in the database
class Post(models.Model):
    #link to another model
    author = models.ForeignKey('auth.User')
    #define text with limited number of characters
    title = models.CharField(max_length=200)
    #long text without a limit
    text = models.TextField()
    #date and time
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #def means a function and publish is the name of the method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
