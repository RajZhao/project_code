from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,logout_then_login

urlpatterns = [
    # post views
    # url(r"^login/$", views.user_login, name="login")
    url(r"^login/$", login, name="login"),
    url(r"^logout/$", logout, name="logout"),
    url(r"^logout-then-login/$", logout_then_login, name="logout_then_login"),
    url(r"^$", views.dashboard, name="dashboard"),
]
