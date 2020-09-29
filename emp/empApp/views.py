from django.shortcuts import render
from empApp.models import Employee

def emp_view(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request, 'empApp/emp.html', context=my_dict)