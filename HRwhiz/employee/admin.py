from django.contrib import admin
from .models import Employee, Department,Project,Feedback,LeaveRequest
# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Feedback)
#admin.site.register(Requests)
admin.site.register(LeaveRequest)
