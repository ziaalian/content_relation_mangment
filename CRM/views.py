from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import customer
from .serializers import customerSerializer

#create add customer view for store owner
class addCustomer(generics.CreateAPIView):
    serializer_class = customerSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = customer.objects.all()

#update customer view for store owner
class updateCustomer(generics.UpdateAPIView):
    serializer_class = customerSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = customer.objects.all()
    lookup_field = 'id'


#delete customer
class deleteCustomer(generics.DestroyAPIView):
    serializer_class = customerSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = customer.objects.all()
    lookup_field = 'id'


#list all customers
class listCustomers(generics.ListAPIView):
    serializer_class = customerSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = customer.objects.all()

#search customer by name
class searchCustomer(generics.ListAPIView):
    serializer_class = customerSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = customer.objects.all()
    lookup_field = 'id'
    def get_queryset(self):
        queryset = customer.objects.all()
        query = self.request.query_params.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset