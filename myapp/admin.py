from django.contrib import admin
from .models import  *

# Register your models here.
admin.site.register(UserType)
admin.site.register(User)
admin.site.register(Level)
admin.site.register(LevelPack)
admin.site.register(LevelType)
admin.site.register(WrongAnswer)
admin.site.register(Stars)
admin.site.register(LevelImage)