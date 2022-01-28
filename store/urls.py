
from django.urls import path
from .views.orders import OrderView
from .views.login import logout
from .views import login, signup
from .views.cart import Cart
from .views.checkout import Checkout
from store.views.home import Index
from .middlewares.auth import auth_middleware
urlpatterns = [
   
    path('',Index.as_view(),name= 'homepage'),
    path('signup',signup.Signup.as_view(),name= 'signup'),
    path('login',login.Login.as_view(),name= 'login'),
    path('logout',logout,name= 'logout'),
    path('cart',Cart.as_view(),name= 'cart'),
    path('checkout',Checkout.as_view(),name= 'checkout'),
    path('orders',auth_middleware(OrderView.as_view()),name= 'orders'),
    
   
]
