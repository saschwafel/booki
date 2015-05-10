from django.db import models

# Create your models here.

class Book_Entry(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    date_added = models.DateField('Date Added')
    date_started = models.DateField('Date Started', blank=True, null=True)
    date_finished = models.DateField('Date Finished', blank=True, null=True)
    
    def __str__(self):
        return str(self.title)+' - '+ str(self.author)

#class Booklist(models.Model):
#    pass
