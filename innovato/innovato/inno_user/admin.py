from django.contrib import admin
from .models import Comment, Video_up, like, profile, Skill, Portfo

# Register your models here.
admin.site.register(Comment)
admin.site.register(Video_up)
admin.site.register(like)
admin.site.register(profile)
admin.site.register(Skill)
admin.site.register(Portfo)
