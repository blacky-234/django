from django.urls import path
from . import views

app_name = "users"

urlpatterns = [ 
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="create"),
    # path("signup/newsignup/", views.newsignup, name="signup"),
    path("login/alogin/", views.alogin, name="verify"),
    # path("logout/", views.logout_view, name="logout"),
]