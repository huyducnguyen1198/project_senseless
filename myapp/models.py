from django.db import models


class UserType(models.Model):
    '''
    This class represents the UserType model

    '''

    userTypeName = models.CharField(max_length=15, primary_key=True)
    userTypeDesc = models.TextField()



class User(models.Model):
    '''
    This class represents the User model

    '''

    userId = models.AutoField(primary_key=True)
    stars = models.IntegerField()
    namePlate = models.CharField(max_length=50)
    # foreign key
    userTypeName = models.ForeignKey(UserType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.namePlate} {self.stars}'