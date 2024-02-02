from rest_framework import serializers
from .models import *

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class LevelPackSerializer(serializers.ModelSerializer):
	class Meta:
		model = LevelPack
		fields = '__all__'
        
class LevelTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = LevelType
		fields = '__all__'
            
class LevelSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Level
		fields = '__all__'

class LevelImageSerializer(serializers.ModelSerializer):

	class Meta:
		model = LevelImage
		fields = '__all__'


class WrongAnswerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = WrongAnswer
		fields = '__all__'

class PlayHistorySerializer(serializers.ModelSerializer):
	
	class Meta:
		model = PlayHistory
		fields = '__all__'
