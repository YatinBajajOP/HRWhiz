from django.shortcuts import render, redirect
from employee.models import Employee

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Employee.objects.get(email=email, password=password)
            if user is not None:
                request.session['name'] = user.name
                request.session['id'] = user.id
                request.session['url'] = user.id

                if user.designation == "Employee":
                    return redirect('/employee')
                elif user.designation == "Manager":
                    return redirect('/manager')
                elif user.designation == "HR":
                    return redirect('/hr')
        except Exception as e:
            print(e)
    return render(request, 'login.html')

def logout(request):
    del request.session['name']
    return redirect('/')