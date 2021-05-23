from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index_page'), #registration page
    path('login/', views.signin, name ="signin"), #login page
    path('dashbord/<int:vid>/',views.dashbord, name="dash"), #dashbord
    path('signout/',views.signout,name="signout"), #signout and redirect to registration page
    path('up_video/',views.up_video, name="upload_video"), #upload video 
    path('cmt_upld/<int:vid>/', views.cmt_upld, name='cmt_upload'), #comment upload logic and redirect to dashbord
    path('like_l/<int:vid>/',views.like_l,name="like"),
    path('unlike/<int:lid>/<int:vid>/',views.unlike,name="unlike"),
    path('delete_post/<int:idd>/',views.delete_post,name="delete_post"),
    path('homepage/',views.homepage,name="home"),
    path('searchpage/',views.searchpage,name="search"), 
    path('profilepage/<int:pid>/', views.profilepage,name="profile"),
    path('up_profile/<int:pid>/', views.up_profile,name="upload_profile"),
    path('up_skills/<int:pid>/<int:sid>/', views.up_skill, name="upload_skills"),
    path('portfolio/<pid>/',views.portfo,name='portfolio'),
    path('delete_project/',views.del_project,name="delete_project"),
    path('delete_this_project/<delid>/',views.del_this_project,name="delete_this_project"),
    path('likedvideo/',views.likedvideo,name="likedvideo"),
    path('trendingpage/',views.Trend,name="Trending"),
    path('welcomepage/',views.welcome,name="welcome"),
    path('guest/' ,views.guest,name="guest"),
    path('unfollowing/<int:pid>/' ,views.unfollowing,name="unfollowing"),
    path('following/<int:pid>/' ,views.following,name="following"),
    path('subscription/' ,views.follow,name="follow"),

    path('reset_password/', 
		auth_views.PasswordResetView.as_view(template_name='inno_user/password_reset.html'),
		name='reset_password'),

	path('reset_password_sent/', 
		auth_views.PasswordResetDoneView.as_view(template_name='inno_user/password_reset_done.html'), 
		name='password_reset_done'),
	
	path('reset/<uidb64>/<token>/', 
		auth_views.PasswordResetConfirmView.as_view(template_name='inno_user/password_reset_confirm.html'), 
		name='password_reset_confirm'),
	
	path('reset_password_complete/', 
		auth_views.PasswordResetCompleteView.as_view(template_name='inno_user/password_reset_complete.html'), 
		name='password_reset_complete')


]
