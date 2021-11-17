from django.urls import path
from .views import login_,logout_,signup,AdminPanel,AdminOrders,AdminProducts,AdminTickets,AdminUsers
from django.views.generic import TemplateView

app_name = "paneluser"
urlpatterns = [
    path('', login_),
    path('logout/', logout_, name="logout_"),
    path('signup/', signup, name="signup"),
    path('administrator/', AdminPanel.as_view() ,name="AdminPanel"),
    path('administrator/products/', AdminProducts.as_view() ,name="products"),
    path('administrator/orders/', AdminOrders.as_view() ,name="orders"),
    path('administrator/tickets/', AdminTickets.as_view() ,name="tickets"),
    path('administrator/users/', AdminUsers.as_view() ,name="users"),
]