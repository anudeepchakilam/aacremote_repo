from django.db import models

# Create your models here.
class Comment(models.Model):
    #post=models.ForeignKey()
    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    #created=models.DateTimeField(auto_now_add=True)
    #updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    #class Meta:
    #    ordering=('-created')
    def __str__(self):
        return 'Commented by {}'.format(self.name)
