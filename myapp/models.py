from django.db import models
import uuid

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
    starNum = models.IntegerField()
    namePlate = models.CharField(max_length=50)
    # foreign key
    userTypeName = models.ForeignKey(UserType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.namePlate} {self.stars}'

#
# Level, LevelPack, LevelType, LevelImage, WrongAnswer
# 
class LevelPack(models.Model):
    '''
    This class represents the LevelPack model
	'''
    levelPackId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return f'{self.name} {self.levelPackId}'
    
class LevelType(models.Model):
    '''
    This class represents the LevelType model
    '''
    levelTypeId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='default')
    description = models.TextField()
    def __str__(self):
        return f'Id: {self.levelTypeId}, name: {self.name} '
    
class Level(models.Model):
    '''
    This class represents the Level model
    '''
    levelId = models.AutoField(primary_key=True)
    LevelTypeId = models.ForeignKey(LevelType, on_delete=models.CASCADE)
    levelPackId = models.ForeignKey(LevelPack, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    difficulty = models.IntegerField()
    prompt = models.TextField()
    answerNum = models.IntegerField()
    imageId = models.TextField()
    audio = models.CharField(max_length=50)
    allotedTime = models.IntegerField()
    rightAnswer = models.TextField()


class LevelImage(models.Model):
    '''
    This class represents the LevelImage model
	'''
    levelImageId = models.AutoField(primary_key=True)
    levelId = models.ForeignKey(Level, on_delete=models.CASCADE)
    path = models.CharField(max_length=50)
    imageName = models.CharField(max_length=50)
    extension = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.imageName} {self.levelImageId}'
		
class WrongAnswer(models.Model):
    '''
    This class represents the WrongAnswer model
    '''
    WrongAnswerId = models.AutoField(primary_key=True)
    levelId = models.ForeignKey(Level, on_delete=models.CASCADE)
    answer = models.TextField()



#
# PlayHistory
#
    
class PlayHistory(models.Model):
    ''' 
    This class represents the PlayHistory model
    '''
    passResultId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    levelId = models.ForeignKey(Level, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField()
    completionTime = models.IntegerField()
    correctGuess = models.BooleanField()
    incorrectGuess = models.BooleanField()
    def __str__(self):
        return f'{self.passResultId} {self.userId} {self.levelId} {self.timeStamp} {self.completionTime} {self.correctGuess} {self.incorrectGuess}'
    

#
# Stars
#
class Stars(models.Model):
    '''
    This class represents the Stars model
    '''
    trackId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    received = models.IntegerField()

    def __str__(self):
        return f'{self.trackId} {self.userId} {self.received}'
    
