from django.urls import path
from .views import login_,logout_,signup

app_name = "paneluser"
urlpatterns = [
    path('', login_),
    path('logout/', logout_, name="logout_"),
    path('signup/', signup, name="signup"),
]