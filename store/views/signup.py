from os import error
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer





class Signup(View):
    def get(self,request):
        return render(request,"signup.html")
    def post(self,request):
     postData = request.POST
     first_name = postData.get('firstname')
     last_name = postData.get('lastname')
     phone =  postData.get('phone')
     email = postData.get('email')
     password = postData.get('password')
     value = {
          'first_name' : first_name,
          'last_name': last_name,
          'phone' : phone,
          'email': email
        }
     customer = Customer(
            first_name =first_name,
            last_name = last_name,
            phone = phone,
            email = email,
            password = password
           )
     error_message = None
        
     error_message = self.ValidateCustomer(customer)
     if not error_message: 
           customer.password = make_password(customer.password)
           customer.register()
           return redirect('login')
     else:
           data = {
              'error' : error_message,
              'value': value
           }
           return render(request,'signup.html',data)

    def ValidateCustomer(self,customer):
        if (not customer.first_name):
            error_message = "First name required!!"
        elif len(customer.first_name) <4:
                error_message = "first should more than 4 character"
        elif not customer.last_name:
                error_message = "last name required"
        elif len(customer.first_name) <4:
            error_message = "lastname should more than 4 character"
        elif not customer.phone:
             error_message = "phone no. required"
        elif customer.is_Exist():
            error_message = "Email Allready exist"

