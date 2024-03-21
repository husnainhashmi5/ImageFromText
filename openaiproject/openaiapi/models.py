from django.db import models

# Create your models here.

class Openai(models.Model):
    user_input=models.CharField(max_length=200,null=False,blank=False)
    image=models.ImageField(null=False,blank=False)

    def __str__(self):
        return self.user_input