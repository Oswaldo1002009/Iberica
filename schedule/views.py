from django.shortcuts import render
from .models import Program, Groups, Enrolled

#def index(request):
#    return render(request, 'schedule/schedule.html')

def index(request):
    programs_list = Program.objects.order_by('name')
    context = {
        'programs_list': programs_list,
    }
    return render(request, 'schedule/schedule.html', context)

def group_inv(request):
    group_list = Groups.objects.order_by('code')
    context = {
        'group_list': group_list,
    }
    return render(request, 'schedule/schedule.html', context)