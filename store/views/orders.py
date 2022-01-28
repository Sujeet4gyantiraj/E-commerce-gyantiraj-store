
from django.shortcuts import redirect, render
from store.models.orders import Orders
from django.views import View




class OrderView(View):
   
    def get(self,request):
        customer = request.session.get('customer')
        orders = Orders.get_orders_by_customer(customer)     
        return render(request,'orders.html',{'orders':orders})

       

