from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer


class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST

        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password
        )

        error_message = self.validateCustomer(customer)

        if not error_message:
            customer.register()
            return redirect('homepage')

        data = {
            'error': error_message,
            'values': value
        }

        return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if not customer.first_name:
            error_message = "Please Enter your First Name !!"

        elif len(customer.first_name) < 3:
            error_message = "First Name must be 3 characters long or more"

        elif not customer.last_name:
            error_message = "Please Enter your Last Name"

        elif len(customer.last_name) < 3:
            error_message = "Last Name must be 3 characters long or more"

        return error_message