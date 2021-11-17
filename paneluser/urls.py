from django.urls import path
from .views import login_,logout_,signup,AdminPanel,AdminOrders,AdminProducts,AdminTickets,AdminUsers
from django.views.generic import TemplateView

app_name = "paneluser"
urlpatterns = [
    path('', login_),
    path('logout/', logout_, name="logout_"),
    path('signup/', signup, name="signup"),
    path('administrator/', AdminPanel.as_view() ,name="AdminPanel"),
    path('administrator/products/', AdminProducts.as_view() ,name="AdminProducts"),
]