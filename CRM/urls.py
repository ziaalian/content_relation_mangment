from django.urls import path
from .views import searchCustomer, addCustomer, updateCustomer, deleteCustomer, listCustomers

urlpatterns = [
    path('', searchCustomer.as_view(), name='search_customer'),
    path('add/', addCustomer.as_view(), name='add_customer'),
    path('update/', updateCustomer.as_view(), name='update_customer'),
    path('delete/', deleteCustomer.as_view(), name='delete_customer'),
    path('list/', listCustomers.as_view(), name='list_customers'),
    
]

