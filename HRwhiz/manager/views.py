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
    return render(request, 'mgr.html', {'name': request.session['name'], 'id': request.session['id'], 'designation': request.session['designation'], 'annual_leave': int(request.session['annual_leave']), 'casual_leave': int(request.session['casual_leave']), 'sick_leave': int(request.session['sick_leave'])})

# @session_login_required
# def assign_dep_project(request):
#     if request.method == 'POST':
#         employee_id = request.POST['employee_id']
#         department_id = request.POST['department_id']
#         project_id=request.POST['project_id']

#         try:
#             # Retrieve the employee and manager instances
#             employee = Employee.objects.get(id=employee_id)
#             department = Department.objects.get(id=department_id)
#             project=Project.objects.get(id=project_id)

#             # Assign the manager to the employee
#             employee.pid = project
#             employee.did= department
#             employee.save()

#             return HttpResponse('Finally Department and Project Assigned to Employee')  
#         except Employee.DoesNotExist or Department.DoesNotExist or Project.DoesNotExist:
#             # Handle the case where employee or manager is not found
#             return HttpResponse('Either Emloyee or Department or Project not existing in Company ')

#     return render(request, 'adddep&project.html',{'designation': request.session['designation']})

@session_login_required
def mgr_requests_view(request):
    # Assuming you have stored the HR's ID in the session as 'hr_id'
    manager_id = request.session.get('id', None)
    
    if manager_id is not None:
        manager_requests = LeaveRequest.objects.filter(req_to=manager_id)
        
        return render(request, 'mgrreq.html', {'manager_requests': manager_requests,'designation': request.session['designation']})
    else:
        # Handle the case where the HR is not logged in or the session is not set
        # You can redirect to a login page or handle it as per your application's logic.
        return render(request, 'mgr.html')
    
@session_login_required  
def mgr_feedback_view(request):
    # Assuming you have stored the HR's ID in the session as 'hr_id'
    manager_id = request.session.get('id', None)
    
    if manager_id is not None:
        # Filter requests where req_to matches the logged-in HR's ID
        mgr_requests = Feedback.objects.filter(fed_to=manager_id)
        
        return render(request, 'mgrreqfeedback.html', {'mgr_requests': mgr_requests,'designation': request.session['designation']})
    else:
        # Handle the case where the HR is not logged in or the session is not set
        # You can redirect to a login page or handle it as per your application's logic.
        return render(request, 'mgr.html')
    
@session_login_required
def employee_view_status(request):
    # Get the manager_id from the session, assuming you've set it in a previous view.
    id = request.session.get('id')
    
    # Query all employees under the given manager_id
    employees = Employee.objects.filter(manager_id=id)

    if request.method == 'POST':
        # Handle the form submission to mark employees as active or passive
        employee_ids = request.POST.getlist('employee_ids')
        

    return render(request, 'empstatus.html', {'employees': employees,'designation':request.session['designation']})

@session_login_required
def assign_pro_dept(request):
    employees = Employee.objects.filter(designation="Employee")
    departments=Department.objects.all()
    projects=Project.objects.all()

    mapping = {}

    for department in departments:
        projects = Project.objects.filter(did = department.id)
        mapping[department.id] = [{"name": project.name, "id": project.id} for project in projects]


    if request.method=="POST":
        data=Employee.objects.all()
        pid=request.POST.get('project')
        did=request.POST.get('department')
        data.update(pid=pid,did=did)
    
    print(mapping)

    return render(request,'assignprodept.html', {"employees": employees,"departments":departments,"projects":projects, "mapping":mapping,'designation':request.session['designation']})


@session_login_required
def edit_profile(request):
    data= Employee.objects.filter(id=request.session.get('id', None))
    name=data.first().name
    password=data.first().password
    email=data.first().email
    address=data.first().address
    phone_number=data.first().phone_number

    if request.method=="POST":
        print("Editing")
        name=request.POST.get("name")
        password=request.POST.get("password")
        email=request.POST.get("email")
        address=request.POST.get("address")
        phone_number=request.POST.get("phone_number")
        data.update(name=name,password=password,email=email,address=address,phone_number=phone_number)
    
    return render(request,"profile.html",{"name":name,"password":password,"email":email,"address":address,"phone_number":phone_number, "designation":request.session['designation']})