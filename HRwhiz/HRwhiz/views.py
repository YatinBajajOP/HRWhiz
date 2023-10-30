from django.shortcuts import render, redirect
from employee.models import Employee

from functools import wraps
def session_login_required(function=None, session_key='id'):
    def decorator(view_func):
        @wraps(view_func)
        def f(request, *args, **kwargs):
            print(request.session.keys())
            if session_key in request.session:
                return view_func(request, *args, **kwargs)
            return redirect('/')
        return f
    if function is not None:
        return decorator(function)
    return decorator

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Employee.objects.get(email=email, password=password)
            if user is not None:
                request.session['name'] = user.name
                request.session['id'] = user.id
                request.session['url'] = user.profile_url
                request.session['designation'] = user.designation

                # Updating the status of logged in user
                obj = Employee.objects.get(id=user.id)
                obj.status = True

                obj.save()

                if user.designation == "Employee":
                    return redirect('/employee')
                elif user.designation == "Manager":
                    return redirect('/manager')
                elif user.designation == "HR":
                    return redirect('/HR')
            
        except Exception as e:
            print(e)
    return render(request, 'login.html')
    

def log_out(request):
    obj = Employee.objects.get(id=request.session.get('id', None))
    obj.status = False

    obj.save()
    del request.session['name']
    del request.session['id']

    return redirect('/')