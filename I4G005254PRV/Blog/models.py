from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    # when the foreign key is deleted all referenced object will be deleted
    author = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_date = models.DateTimeField('date created')
    pubblished_date = models.DateTimeField('date published')

