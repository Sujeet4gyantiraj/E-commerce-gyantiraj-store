from itertools import product
from traceback import print_exception

from django.shortcuts import redirect
from store.models.orders import Orders
from store.models.product import Product
from store.models.customer import Customer
from os import error

from django.views import View



class Checkout(View):
    def post(self,request):
       address = request.POST.get('address')
       phone = request.POST.get('phone')
       customer = request.session.get('customer')
       cart = request.session.get('cart')
       products =Product.get_products_id(list(cart.keys()))

       for product in products:
           order = Orders(
               customer = Customer(id = customer),
               product = product,
               price = product.price,
               address = address,
               phone = phone,
               quantity= cart.get(str(product.id))
           )


       order.placeorder()
       request.session['cart'] = {}
       return redirect('cart')


