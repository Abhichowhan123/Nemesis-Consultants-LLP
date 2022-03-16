from django.urls import path, include

from Nemesis import views

urlpatterns = [
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("",views.home,name="home"),
    path("logout",views.logout,name="logout")

]
