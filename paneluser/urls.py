from django.urls import path
from .views import login_,logout_,signup,AdminPanel,AdminOrders,AdminProducts,AdminTickets,AdminUsers,ProductsDeleteView,ProductsUpdateView,ProductsCreateView,OrdersDeleteView,OrdersUpdateView
from django.views.generic import TemplateView

app_name = "paneluser"
urlpatterns = [
    path('', login_),
    path('logout/', logout_, name="logout_"),
    path('signup/', signup, name="signup"),
    path('administrator/', AdminPanel.as_view() ,name="AdminPanel"),
    path('administrator/products/', AdminProducts.as_view() ,name="products"),
    path('administrator/products/delete/<int:pk>', ProductsDeleteView.as_view() ,name="products_delete"),
    path('administrator/products/update/<int:pk>', ProductsUpdateView.as_view() ,name="products_update"),
    path('administrator/products/create/', ProductsCreateView.as_view() ,name="products_create"),
    path('administrator/orders/', AdminOrders.as_view() ,name="orders"),
    path('administrator/orders/delete/<int:pk>', OrdersDeleteView.as_view() ,name="orders_delete"),
    path('administrator/orders/update/<int:pk>', OrdersUpdateView.as_view() ,name="orders_update"),
    path('administrator/tickets/', AdminTickets.as_view() ,name="tickets"),
    path('administrator/users/', AdminUsers.as_view() ,name="users"),
]