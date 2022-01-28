
from os import error
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password
from django.views import View
from  store.models.customer import Customer


from store.models.product import Product
from store.models.category import Category


class Login(View):
    return_url = None
    def get(self,request):
        print("abc")
        print(request.GET.get('return_url'))
        Login.return_url=request.GET.get('return_url')
        return render(request,"login.html")

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_email(email)
        if customer:
            flag = check_password(password , customer.password)
            if flag:
                request.session['customer'] = customer.id 
                print("suet")
                if Login.return_url:
                    print("sujeet")
                    print(Login.return_url)
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')

            else:
                error_message = "Email or Password invalid"
        else:
            error_message = "Email or Password invalid"
        print(request.session['customer'])
        print(customer)
        return render(request,'login.html',{'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('login')