from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from schedule.models import Enrolled, ClassEnrolled, TallerGuitarra, Observador, Inter, Intensivo, Elemental
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CompleteProfile
from core.models import UserProfileInfo


def index(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
        if enrolled is not None:
            talleres_guitarra = TallerGuitarra.objects.filter(id_enrolled=user)
            observadores = Observador.objects.filter(id_enrolled=user)
            interdisciplinario = Inter.objects.filter(id_enrolled=user)
            intensivo = Intensivo.objects.filter(id_enrolled=user)
            elemental = Elemental.objects.filter(id_enrolled=user)
            context = {
                'elemental': elemental,
                'intensivo': intensivo,
                'interdisciplinario': interdisciplinario,
                'talleres_guitarra': talleres_guitarra,
                'enrolled': enrolled,
                'observadores': observadores,
            }
            return render(request, 'userprofile/profile.html', context)
    return render(request, 'userprofile/profile.html')


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        #Case logged user with enrolled form completed
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
        if enrolled is not None:
            context = {
                'enrolled': enrolled,
            }
            return render(request, 'schedule/already_enrolled.html', context)

        #Case logged user completing enrolled form
        if request.method == 'POST':
            form = CompleteProfile(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return HttpResponseRedirect(reverse_lazy('userprofile'))
            return render(request, 'schedule/enrolled_form.html', {'form': form})

        #Case logged user but enrolled form has not been completed
        form = CompleteProfile()
        return render(request, 'schedule/enrolled_form.html', {'form': form})

    #Case not logged
    return render(request, 'schedule/enrolled_form.html')
