from django.shortcuts import render

# Create your views here.
# manager views
def view_employees(request):
    return render(request, 'emp.html')

