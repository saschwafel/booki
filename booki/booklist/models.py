from django.db import models

# Create your models here.

class Book_Entry(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    date_added = models.DateTimeField('Date Added')
    date_started = models.DateTimeField('Date Started')
    date_finished = models.DateTimeField('Date Finished')
    
    def __str__(self):
        return str(self.title)+' - '+ str(self.author)

#class Booklist(models.Model):
#    pass
