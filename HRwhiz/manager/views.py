from django.shortcuts import render
from django.shortcuts import HttpResponse
from employee.models import *
from HRwhiz.views import session_login_required

# Create your views here.
# manager views
@session_login_required
def view_employees(request):
    return render(request, 'emp.html')

@session_login_required
def dashboard(request):
    return render(request, 'mgr.html', {'name': request.session['name'], 'id': request.session['id'], 'designation': request.session['designation']})

@session_login_required
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

            return HttpResponse('Finally Department and Project Assigned to Employee')  
        except Employee.DoesNotExist or Department.DoesNotExist or Project.DoesNotExist:
            # Handle the case where employee or manager is not found
            return HttpResponse('Either Emloyee or Department or Project not existing in Company ')

    return render(request, 'adddep&project.html')

@session_login_required
def mgr_requests_view(request):
    # Assuming you have stored the HR's ID in the session as 'hr_id'
    manager_id = request.session.get('id', None)
    
    if manager_id is not None:
        manager_requests = askHR.objects.filter(req_to=manager_id)
        
        return render(request, 'mgrreq.html', {'manager_requests': manager_requests})
    else:
        # Handle the case where the HR is not logged in or the session is not set
        # You can redirect to a login page or handle it as per your application's logic.
        return render(request, 'mgr.html')
@session_login_required  
def mgr_Feedback_view(request):
    # Assuming you have stored the HR's ID in the session as 'hr_id'
    manager_id = request.session.get('id', None)
    
    if manager_id is not None:
        # Filter requests where req_to matches the logged-in HR's ID
        mgr_requests = Feedback.objects.filter(fed_to=manager_id)
        
        return render(request, 'mgrreqfeedback.html', {'mgr_requests': mgr_requests})
    else:
        # Handle the case where the HR is not logged in or the session is not set
        # You can redirect to a login page or handle it as per your application's logic.
        return render(request, 'mgr.html')
    
@session_login_required
def Employee_view_Status(request):
    # Get the manager_id from the session, assuming you've set it in a previous view.
    id = request.session.get('id')
    
    # Query all employees under the given manager_id
    employees = Employee.objects.filter(manager_id=id)

    if request.method == 'POST':
        # Handle the form submission to mark employees as active or passive
        employee_ids = request.POST.getlist('employee_ids')
        

    return render(request, 'empstatus.html', {'employees': employees})

