from django.http import HttpResponse,request
from employee.models import Employee,Requests
from django.shortcuts import redirect, render

def dashboard(request):
    return render(request, 'hr.html', {'name': request.session['name'], 'id': request.session['id'], 'designation': request.session['designation']})

def add_employee(request):
    if request.method == 'POST':
        # Retrieve data from the form
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        designation = request.POST.get('designation')
        sick_leave = request.POST.get('sick_leave')
        casual_leave = request.POST.get('casual_leave')
        annual_leave = request.POST.get('annual_leave')
        phone_number = request.POST.get('phone_number')
        profile_url = request.POST.get('profile_url')

        # Create and save the Employee object
        employee = Employee(
            id=id,
            name=name,
            email=email,
            password=password,
            address=address,
            designation=designation,
            sick_leave=sick_leave,
            casual_leave=casual_leave,
            annual_leave=annual_leave,
            phone_number=phone_number,
            profile_url=profile_url
        )
        employee.save()

        # You can also redirect to a success page or return a success message
        return redirect('/success_page')  # Replace 'success_page' with your actual URL name

    return render(request, 'addemp.html')  # Show the form

def success_page(request):
    return HttpResponse("Employee added successfully!")  # You can create a success page here

def delete_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('id')

        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()
            return HttpResponse('Employee removed')  # Redirect to a list view or another page
        except Employee.DoesNotExist:
            error_message = "Employee not found"
    else:
        error_message = None

    return render(request, 'deleteemp.html', {'error_message': error_message})
def hr_requests_view(request):
    hr_requests = Requests.objects.filter(req_body='HR')
    return render(request, 'req.html',{'hr_requests':hr_requests})
def addmanager(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        manager_id = request.POST['manager_id']

        try:
            # Retrieve the employee and manager instances
            employee = Employee.objects.get(id=employee_id)
            manager = Employee.objects.get(id=manager_id)

            # Assign the manager to the employee
            employee.manager_id = manager
            employee.save()

            return HttpResponse('Manager Assigned')  
        except Employee.DoesNotExist:
            # Handle the case where employee or manager is not found
            return HttpResponse('Employee or Manager Not Exists')

    return render(request, 'addmanager.html')