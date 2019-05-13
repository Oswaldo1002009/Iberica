from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ClassEnrolled, Program, Level, Classes, Groups, Enrolled
from .forms import ClassEnrolledForm, TallerGuitarraForm


def ins_TallerGuitarra(request):
    # Case for Taller de Guitarra
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
    if request.method == 'POST':
        form = TallerGuitarraForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.id_enrolled = request.user
            new_class.save()
            return redirect(reverse('userprofile'))
    form = TallerGuitarraForm()
    return render(request, 'schedule/6-TalleresDeGuitarra.html', {'enrolled': enrolled, 'form': form})


def inscription(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
        #Program not selected
        return render(request, 'schedule/schedule.html', {'enrolled': enrolled})
    #Session not started
    return render(request, "schedule/schedule.html")


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


class ClassListView(ListView):
    model = ClassEnrolled
    context_object_name = 'students'


class ClassCreateView(CreateView):
    model = ClassEnrolled
    form_class = ClassEnrolledForm
    success_url = reverse_lazy('enrolled_student')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.id_enrolled = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('enrolled_student'))


class ClassUpdateView(UpdateView):
    model = ClassEnrolled
    form_class = ClassEnrolledForm
    success_url = reverse_lazy('enrolled_student')


def load_levels(request):
    program_id = request.GET.get('id_program')
    levels = Level.objects.filter(program_id=program_id).order_by('level')
    return render(request, 'schedule/level_dropdown_list_options.html', {'levels': levels})


def load_classes(request):
    level_id = request.GET.get('id_level')
    classes = Classes.objects.filter(level_id=level_id).order_by('name')
    return render(request, 'schedule/class_dropdown_list_options.html', {'classes': classes})
