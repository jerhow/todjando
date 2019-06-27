from django.db import models

# Create your models here.

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item 
        # ^^ Remember, we implement __str__ on a class so that the object can return 
        # the string representation of itself. We have defined that as simply the 'item' field,
        # but it can be anything.
