from django.contrib import admin
from .models import User # model 임포트

# Register your models here.
admin.site.register(User) # admin 페이지에 등록