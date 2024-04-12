from django.db import models

class CreateUser(models.Model):
    '''
    '''
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)
    numbers = models.CharField()
    password = models.CharField()
    password2 = models.CharField()
    created_at = models.DateField(auto_created=True)
    is_active = models.BooleanField(default=True)
    images = models.ImageField(upload_to='user')

    def __str__(self):
        return f'{self.name}'