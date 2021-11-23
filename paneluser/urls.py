from django.urls import path
from .views import login_,logout_,signup,AdminPanel,AdminOrders,AdminProducts,AdminTickets,AdminUsers,ProductsDeleteView,ProductsUpdateView,ProductsCreateView,OrdersDeleteView,OrdersUpdateView,UserDeleteView,UserUpdateView,TicketDeleteView,UserDashboard,ProductsDetailView,UserOrders,OrdersDetailView,OrderPurchase,UserTickets,TicketCreateView,AdminTicketCreateView,UserUpdateTicketView,AdminUpdateTicketView
from django.views.generic import TemplateView

app_name = "paneluser"
urlpatterns = [
    path('', login_,name="login"),
    path('logout/', logout_, name="logout_"),
    path('signup/', signup, name="signup"),
    #Administrator
    path('administrator/', AdminPanel.as_view() ,name="AdminPanel"),
    path('administrator/products/', AdminProducts.as_view() ,name="products"),
    path('administrator/products/delete/<int:pk>', ProductsDeleteView.as_view() ,name="products_delete"),
    path('administrator/products/update/<int:pk>', ProductsUpdateView.as_view() ,name="products_update"),
    path('administrator/products/create/', ProductsCreateView.as_view() ,name="products_create"),
    path('administrator/orders/', AdminOrders.as_view() ,name="orders"),
    path('administrator/orders/delete/<int:pk>', OrdersDeleteView.as_view() ,name="orders_delete"),
    path('administrator/orders/update/<int:pk>', OrdersUpdateView.as_view() ,name="orders_update"),
    path('administrator/tickets/', AdminTickets.as_view() ,name="tickets"),
    path('administrator/tickets/create/', AdminTicketCreateView.as_view() ,name="AdminTicketCreateView"),
    path('administrator/tickets/delete/<int:pk>', TicketDeleteView.as_view() ,name="ticket_delete"),
    path('administrator/tickets/update/<int:ticketid>', AdminUpdateTicketView.as_view() ,name="ticket_update"),
    path('administrator/users/', AdminUsers.as_view() ,name="users"),
    path('administrator/users/delete/<int:pk>', UserDeleteView.as_view() ,name="users_delete"),
    path('administrator/users/update/<int:pk>', UserUpdateView.as_view() ,name="users_update"),
    # User
    path('usercp/', UserDashboard.as_view() ,name="UserDashboard"),
    path('usercp/purchase/<int:orderid>', OrderPurchase.as_view() ,name="OrderPurchase"),
    path('usercp/product/<int:pk>', ProductsDetailView.as_view() ,name="ProductsDetailView"),
    path('usercp/orders/order/<int:pk>', OrdersDetailView.as_view() ,name="OrdersDetailView"),
    path('usercp/orders/', UserOrders.as_view() ,name="UserOrders"),
    path('usercp/tickets/', UserTickets.as_view() ,name="UserTickets"),
    path('usercp/tickets/create/', TicketCreateView.as_view() ,name="TicketCreateView"),
    path('usercp/tickets/update/<int:ticketid>', UserUpdateTicketView.as_view() ,name="ticket_update"),
    path('accounts/login/', login_),
]