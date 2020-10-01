from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
            path('',views.home,name="home"),
            path ('index/',views.index,name='index' ),
            path('auth_register/', views.auth_register, name="auth_register"),
            path('register/',views.register,name="register"),
            path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="login"),
            path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
            path('profile/',views.profile,name='profile'),
            path('profile_view/<int:profile_id>/',views.profile_view,name='profile_view')
]