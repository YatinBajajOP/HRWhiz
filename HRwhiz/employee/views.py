from django.shortcuts import render, redirect
from .models import Feedback, askHR, LeaveRequest, Employee

import uuid
from HRwhiz.views import session_login_required

# Create your views here.\
@session_login_required
def dashboard(request):
    return render(request, 'emp.html', {'name': request.session['name'], 'id': request.session['id'], 'designation': request.session['designation']})

@session_login_required
def feedback(request):
    if request.method == 'POST':       
        des=request.POST.get('description')
        employee = Employee.objects.filter(id=request.session.get('id', None)).first()
        
        if request.POST.get('selection-value') == 'HR':
            if employee:
                fed_to = employee.hr_id
            else:
                fed_to = None
        else:
           if employee:
                fed_to = employee.manager_id
           else:
                fed_to = None

        res=Feedback(id=str(uuid.uuid4()),fed_to=fed_to,fed_by=employee,fed_body=des, type='Feedback')
        res.save()
    
    return render(request, 'feedback.html')

session_login_required
def ask_hr(request):
    if request.method == 'POST':   
        text=request.POST.get('query')
        employee = Employee.objects.filter(id=request.session.get('id', None)).first()
        hr=employee.hr_id
        res=askHR(id=str(uuid.uuid4()),text=text, hr_id = hr)
        res.save()
    return render(request,'askHR.html')

session_login_required
def leave_request(request):
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        reason = request.POST.get('reason')

        employee = Employee.objects.filter(request.session.get('id', None)).first()
        mgr_id = employee.manager_id

        # Create and save a new LeaveRequest object
        new_leave_request = LeaveRequest(id=str(uuid.uuid4()),date_from=date_from, date_to=date_to, reason=reason, req_to = mgr_id)
        new_leave_request.save()

    
    return render(request, 'leaverequest.html')
