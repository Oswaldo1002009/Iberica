from django.shortcuts import render
from .models import Program

#def index(request):
#    return render(request, 'schedule/schedule.html')

def index(request):
    programs_list = Program.objects.order_by('name')
    context = {
        'programs_list': programs_list,
    }
    return render(request, 'schedule/schedule.html', context)

