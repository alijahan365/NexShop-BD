from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


class Login(View):

    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')

        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        error_message = None

        if not email:
            error_message = 'Please enter your email'

        elif not password:
            error_message = 'Please enter your password'

        else:
            customer = Customer.get_customer_by_email(email)

            if customer:
                flag = check_password(password, customer.password)

                if flag:
                    request.session['customer'] = customer.id

                    if Login.return_url:
                        return_url = Login.return_url
                        Login.return_url = None

                        return HttpResponseRedirect(return_url)

                    return redirect('homepage')

                else:
                    error_message = 'Invalid email or password'

            else:
                error_message = 'Invalid email or password'

        return render(request, 'login.html', {
            'error': error_message,
            'values': {
                'email': email
            }
        })


def logout(request):
    return redirect('login')