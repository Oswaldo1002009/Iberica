from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ClassEnrolled, Program, Level, Classes, Groups, Enrolled
from .forms import ClassEnrolledForm, TallerGuitarraForm, ObservadoresForm, InterForm

def ins_Inter(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
        if request.method == 'POST':
            form = InterForm(request.POST)
            if form.is_valid():
                inter = form.save(commit=False)
                inter.id_enrolled = request.user
                #All empty
                if not inter.week1_12 and not inter.week1_13 and not inter.week2_12 and not inter.week2_13:
                    error = "Necesitas inscribir al menos una semana completa"
                    return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                  'error': error})
                #At least a week incomplete
                if (inter.week1_12 and not inter.week1_13) or (not inter.week1_12 and inter.week1_13) or \
                   (inter.week2_12 and not inter.week2_13) or (not inter.week2_12 and inter.week2_13):
                    error = "No puedes inscribir semanas incompletas"
                    return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                  'error': error})
                #Week 1 completed
                if inter.week1_12 and inter.week1_13 and not inter.week2_12:
                    inter.weeks = "Primera semana"
                    inter.save()
                    return redirect(reverse('userprofile'))
                #Week 2 completed
                if inter.week2_12 and inter.week2_13 and not inter.week1_12:
                    inter.weeks = "Segunda semana"
                    inter.save()
                    return redirect(reverse('userprofile'))
                #Both weeks completed
                inter.weeks = "Dos semanas"
                inter.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form})
        form = InterForm()
        return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form})
    return render(request, 'schedule/4-Interdisciplinario.html', {'form': form})

def ins_TallerGuitarra(request):
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
            return render(request, 'schedule/6-TalleresDeGuitarra.html', {'enrolled': enrolled, 'form': form})
        form = TallerGuitarraForm()
        return render(request, 'schedule/6-TalleresDeGuitarra.html', {'enrolled': enrolled, 'form': form})
    return render(request, 'schedule/6-TalleresDeGuitarra.html', {'form': form})


def ins_Observadores(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
        if request.method == 'POST':
            form = ObservadoresForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/5-ObservadoresSemana.html', {'enrolled': enrolled, 'form': form})
        form = ObservadoresForm()
        return render(request, 'schedule/5-ObservadoresSemana.html', {'enrolled': enrolled, 'form': form})
    return render(request, 'schedule/5-ObservadoresSemana.html', {'form': form})


def ins_Intensivo(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled})

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
