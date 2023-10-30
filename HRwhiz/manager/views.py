from django.shortcuts import render
from django.shortcuts import HttpResponse
from employee.models import *

# Create your views here.
# manager views
def view_employees(request):
    return render(request, 'emp.html')

def dashboard(request):
    return render(request, 'mgr.html')

def dep_project(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        department_id = request.POST['department_id']
        project_id=request.POST['project_id']

        try:
            # Retrieve the employee and manager instances
            employee = Employee.objects.get(id=employee_id)
            department = Department.objects.get(id=department_id)
            project=Project.objects.get(id=project_id)

            # Assign the manager to the employee
            employee.pid = project
            employee.did= department
            employee.save()

            return HttpResponse('Finally DEpartment and Project Assigned to Employee')  
        except Employee.DoesNotExist or Department.DoesNotExist or Project.DoesNotExist:
            # Handle the case where employee or manager is not found
            return HttpResponse('Either Emloyee or Department or Project not existing in Company ')

    return render(request, 'adddep&project.html')

