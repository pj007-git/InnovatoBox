from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video_up(models.Model):
    v_id = models.AutoField(primary_key=True)
    v_title = models.CharField(max_length=30, default='')
    v_file = models.FileField(upload_to='inno_user/videos/') #media/videos
    v_image = models.ImageField(upload_to= 'inno_user/images/')
    v_gif = models.ImageField(upload_to= 'inno_user/Gif/')
    v_desc = models.CharField(max_length=120, default='')
    v_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.v_title

class Comment(models.Model):
    cmt_id = models.AutoField(primary_key=True)
    cmt_user  = models.ForeignKey(User, on_delete=models.CASCADE)
    cmt_msg = models.CharField(max_length=30, default='')
    cmt_vid = models.ForeignKey(Video_up, on_delete=models.CASCADE)
    def __str__(self):
        return self.cmt_user.username 


class like(models.Model):
    l_id = models.AutoField(primary_key=True)
    l_postid =models.ForeignKey(Video_up, on_delete=models.CASCADE)
    l_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.l_user.username

class profile(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=20,default='')
    p_image = models.ImageField(upload_to='inno_user/profile/')
    p_about = models.CharField(max_length=120,default='')
    p_contact = models.IntegerField(default=0)
    p_email = models.CharField(max_length=120,default='')
    #p_email= models.EmailField()

    def __str__(self):
         return self.p_name

class Skill(models.Model):
    sk_id = models.AutoField(primary_key=True)
    sk_user = models.CharField(max_length=30, default='')
    Html = models.CharField(max_length=10, default='')
    Css = models.CharField(max_length=10, default='')
    Js = models.CharField(max_length=10, default='')
    Python = models.CharField(max_length=10, default='')
    Database = models.CharField(max_length=10, default='')
    Wordpress = models.CharField(max_length=10, default='')
    Mongodb = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.sk_user

class Portfo(models.Model):
    port_id = models.AutoField(primary_key=True)
    port_user = models.CharField(max_length=20, default='')
    port_img = models.ImageField(upload_to='inno_user/portfolio/')
    port_url = models.URLField(max_length=200, default='')

    def __str__(self):
        return self.port_user

