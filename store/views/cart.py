from itertools import product
from store.models.product import Product
from store.models.category import Category
from os import error

from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.views import View
from  store.models.customer import Customer


class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_id(ids)
        print(products)
        return render(request,"cart.html",{'products': products})
     


