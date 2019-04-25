from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Program, ClassEnrolled, Program, Level, Classes
from .forms import ClassEnrolledForm

def index(request):
    programs_list = Program.objects.order_by('name')
    context = {
        'programs_list': programs_list,
    }
    return render(request, 'schedule/schedule.html', context)

class ClassListView(ListView):
    model = ClassEnrolled
    context_object_name = 'students'

class ClassCreateView(CreateView):
    model = ClassEnrolled
    form_class = ClassEnrolledForm
    success_url = reverse_lazy('enrolled_student')

class ClassUpdateView(UpdateView):
    model = ClassEnrolled
    form_class = ClassEnrolledForm
    success_url = reverse_lazy('enrolled_student')

def load_levels(request):
    program_id = request.GET.get('id_program')
    levels = Level.objects.filter(program_id=program_id).order_by('level')
    return render(request, 'schedule/level_dropdown_list_options.html', {'levels': levels})
