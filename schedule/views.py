# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ClassEnrolled, Program, Level, Classes, Groups, Enrolled, Intensivo, Independiente, Inter, TallerGuitarra
from .forms import ClassEnrolledForm, TallerGuitarraForm, ObservadoresForm, InterForm, IntensivoForm, ElementalForm, \
    IndependienteForm

#Cupos programa Interdisciplinario
def eInter1_12(c):
    if 'Cristóbal Reyes "Valoración del Flamenco"' in c and Inter.objects.filter(week1_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Cristóbal Reyes "Valoración del Flamenco", semana 1 a las 12 está lleno'
    if 'Eduardo Alves "Técnica de Danza Clásica" Nivel Intermedio' in c and Inter.objects.filter(week1_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Eduardo Alves "Técnica de Danza Clásica" Nivel Intermedio semana 1 a las 12 está lleno'
    if 'Nuria Balbaneda "Técnica de Danza Clásica" Nivel Avanzado' in c and Inter.objects.filter(week1_12=c).count() >= 1:
        return 'Lo sentimos, el cupo del curso Nuria Balbaneda "Técnica de Danza Clásica" Nivel Avanzado semana 1 a las 12 está lleno'
    if 'La Truco "Certificaciones de la EFA para Nivel Básico" Solo Avanzados (NUEVO)' in c and Inter.objects.filter(week1_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso La Truco "Certificaciones de la EFA para Nivel Básico" Solo Avanzados (NUEVO) semana 1 a las 12 está lleno'
    if 'Juan Paredes "Siente el Flamenco"' in c and Inter.objects.filter(week1_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Juan Paredes "Siente el Flamenco" semana 1 a las 12 está lleno'
    if 'Carlos López Aragón "Danza Flamenca Urbana"' in c and Inter.objects.filter(week1_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Carlos López Aragón "Danza Flamenca Urbana" semana 1 a las 12 está lleno'
    if 'Maribel Gallardo "Técnica de Danza Española" Castañuelas, Vueltas y Braceos' in c and Inter.objects.filter(week1_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Maribel Gallardo "Técnica de Danza Española" Castañuelas, Vueltas y Braceos semana 1 a las 12 está lleno'
    if 'José Galán "Flamenco Inclusivo" Dirigido a Niveles Intermedio y Avanzado (NUEVO)' in c and Inter.objects.filter(week1_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso José Galán "Flamenco Inclusivo" Dirigido a Niveles Intermedio y Avanzado (NUEVO) semana 1 a las 12 está lleno'
    return False

def eInter1_13(c):
    if 'Cristóbal Reyes "Valoración del Flamenco"' in c and Inter.objects.filter(week1_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Cristóbal Reyes "Valoración del Flamenco", semana 1 a las 13:35 está lleno'
    if 'Eduardo Alves "Técnica de Danza Clásica" Nivel Básico' in c and Inter.objects.filter(week1_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Eduardo Alves "Técnica de Danza Clásica" Nivel Básico, semana 1 a las 13:35 está lleno'
    if 'Nuria Balbaneda "Coreografía de Danza Clásica" Nivel Intermedio y Avanzado' in c and Inter.objects.filter(week1_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Nuria Balbaneda "Coreografía de Danza Clásica" Nivel Intermedio y Avanzado, semana 1 a las 13:35 está lleno'
    if 'Ana López "Estilización y Escuela Bolera"' in c and Inter.objects.filter(week1_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Ana López "Estilización y Escuela Bolera", semana 1 a las 13:35 está lleno'
    if 'María Juncal "Técnica de Brazos y Cuerpo"' in c and Inter.objects.filter(week1_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso María Juncal "Técnica de Brazos y Cuerpo", semana 1 a las 13:35 está lleno'
    if 'Carlos López Aragón "Acrodanza"' in c and Inter.objects.filter(week1_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Carlos López Aragón "Acrodanza", semana 1 a las 13:35 está lleno'
    if 'Maribel Gallardo "Repertorio de la Danza Española" Goyescas (Abanico) y La Vida Breve (Castañuelas)' in c and Inter.objects.filter(week1_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Maribel Gallardo "Repertorio de la Danza Española" Goyescas (Abanico) y La Vida Breve (Castañuelas), semana 1 a las 13:35 está lleno'
    return False

def eInter2_12(c):
    if 'Eduardo Alves "Técnica de Danza Clásica" Nivel Intermedio' in c and Inter.objects.filter(week2_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Eduardo Alves "Técnica de Danza Clásica" Nivel Intermedio, semana 2 a las 12 está lleno'
    if 'Nuria Balbaneda "Técnica de Danza Clásica" Nivel Avanzado' in c and Inter.objects.filter(week2_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Nuria Balbaneda "Técnica de Danza Clásica" Nivel Avanzado, semana 2 a las 12 está lleno'
    if 'Cristóbal Reyes "Valoración del Flamenco"' in c and Inter.objects.filter(week2_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Cristóbal Reyes "Valoración del Flamenco", semana 2 a las 12 está lleno'
    if 'María Juncal "Técnica de Pies"' in c and Inter.objects.filter(week2_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso María Juncal "Técnica de Pies", semana 2 a las 12 está lleno'
    if 'José Galán "Flamenco Inclusivo" Dirigido a Niveles Intermedio y Avanzado (NUEVO)' in c and Inter.objects.filter(week2_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso José Galán "Flamenco Inclusivo" Dirigido a Niveles Intermedio y Avanzado (NUEVO), semana 2 a las 12 está lleno'
    if 'Maribel Gallardo "Técnica de Danza Española" Castañuelas, Vueltas y Braceos' in c and Inter.objects.filter(week2_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Maribel Gallardo "Técnica de Danza Española" Castañuelas, Vueltas y Braceos, semana 2 a las 12 está lleno'
    if 'Raquel Ruiz "Neo Folk"' in c and Inter.objects.filter(week2_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Raquel Ruiz "Neo Folk", semana 2 a las 12 está lleno'
    if 'Ana López "Estilización y Escuela Bolera"' in c and Inter.objects.filter(week2_12=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Ana López "Estilización y Escuela Bolera", semana 2 a las 12 está lleno'
    return False

def eInter2_13(c):
    if 'Cristóbal Reyes "Valoración del Flamenco"' in c and Inter.objects.filter(week2_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Cristóbal Reyes "Valoración del Flamenco", semana 2 a las 13:35 está lleno'
    if 'Eduardo Alves "Técnica de Danza Clásica" Nivel Básico' in c and Inter.objects.filter(week2_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Eduardo Alves "Técnica de Danza Clásica" Nivel Básico, semana 2 a las 13:35 está lleno'
    if 'Nuria Balbaneda "Coreografía de Danza Clásica" Nivel Intermedio y Avanzado' in c and Inter.objects.filter(week2_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Nuria Balbaneda "Coreografía de Danza Clásica" Nivel Intermedio y Avanzado, semana 2 a las 13:35 está lleno'
    if 'Juan Paredes "Siente el Flamenco"' in c and Inter.objects.filter(week2_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Juan Paredes "Siente el Flamenco", semana 2 a las 13:35 está lleno'
    if 'La Truco "Certificaciones de la EFA para Nivel Intermedio" Solo Avanzados (NUEVO)' in c and Inter.objects.filter(week2_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso La Truco "Certificaciones de la EFA para Nivel Intermedio" Solo Avanzados (NUEVO), semana 2 a las 13:35 está lleno'
    if 'Maribel Gallardo "Repertorio de la Danza Española" Goyescas (Abanico) y La Vida Breve (Castañuelas)' in c and Inter.objects.filter(week2_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Maribel Gallardo "Repertorio de la Danza Española" Goyescas (Abanico) y La Vida Breve (Castañuelas), semana 2 a las 13:35 está lleno'
    if 'Raquel Ruiz "Neo Folk"' in c and Inter.objects.filter(week2_13=c).count() >= 10:
        return 'Lo sentimos, el cupo del curso Raquel Ruiz "Neo Folk", semana 2 a las 13:35 está lleno'
    return False

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
                # All empty
                if not inter.week1_12 and not inter.week1_13 and not inter.week2_12 and not inter.week2_13:
                    error = "Necesitas inscribir al menos una semana completa"
                    return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                  'error': error})
                # At least a week incomplete
                if (inter.week1_12 and not inter.week1_13) or (not inter.week1_12 and inter.week1_13) or \
                        (inter.week2_12 and not inter.week2_13) or (not inter.week2_12 and inter.week2_13):
                    error = "No puedes inscribir semanas incompletas"
                    return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                  'error': error})
                # Week 1 completed
                if inter.week1_12 and inter.week1_13 and not inter.week2_12:
                    if eInter1_12(inter.week1_12):
                        error = eInter1_12(inter.week1_12)
                        return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                      'error': error})
                    if eInter1_13(inter.week1_13):
                        error = eInter1_13(inter.week1_13)
                        return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                      'error': error})
                    inter.weeks = "Primera semana"
                    inter.save()
                    return redirect(reverse('userprofile'))
                # Week 2 completed
                if inter.week2_12 and inter.week2_13 and not inter.week1_12:
                    if eInter2_12(inter.week2_12):
                        error = eInter2_12(inter.week2_12)
                        return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                      'error': error})
                    if eInter2_13(inter.week2_13):
                        error = eInter2_13(inter.week2_13)
                        return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                      'error': error})
                    inter.weeks = "Segunda semana"
                    inter.save()
                    return redirect(reverse('userprofile'))
                # Both weeks completed
                if eInter1_12(inter.week1_12):
                    error = eInter1_12(inter.week1_12)
                    return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                  'error': error})
                if eInter1_13(inter.week1_13):
                    error = eInter1_13(inter.week1_13)
                    return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                  'error': error})
                if eInter2_12(inter.week2_12):
                    error = eInter2_12(inter.week2_12)
                    return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                  'error': error})
                if eInter2_13(inter.week2_13):
                    error = eInter2_13(inter.week2_13)
                    return render(request, 'schedule/4-Interdisciplinario.html', {'enrolled': enrolled, 'form': form,
                                                                                  'error': error})
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
                i = 0
                #Cupos programa Taller de Guitarra
                if new_class.s1:
                    if TallerGuitarra.objects.filter(s1='8-12 julio, 9:00 am - 12:00 pm: Román Vicenti').count() >= 10:
                        error = 'Lo sentimos, el cupo del primer taller está lleno'
                        return render(request, 'schedule/6-TalleresDeGuitarra.html', {'enrolled': enrolled, 'form': form, 'error': error})
                    i = i + 1
                if new_class.s2:
                    if TallerGuitarra.objects.filter(s2='15-17 julio, 9:00 am - 12:00 pm: Oscar Lagos').count() >= 10:
                        error = 'Lo sentimos, el cupo del segundo taller está lleno'
                        return render(request, 'schedule/6-TalleresDeGuitarra.html', {'enrolled': enrolled, 'form': form, 'error': error})
                    i = i + 1
                if new_class.s3:
                    if TallerGuitarra.objects.filter(s3='18-20 julio, 9:00 am - 12:00 pm: Antonio Campos y Jose Luis Medina').count() >= 10:
                        error = 'Lo sentimos, el cupo del tercer taller está lleno'
                        return render(request, 'schedule/6-TalleresDeGuitarra.html', {'enrolled': enrolled, 'form': form, 'error': error})
                    i = i + 1
                if i == 0:
                    error = "Necesitas inscribir al menos una clase"
                    return render(request, 'schedule/6-TalleresDeGuitarra.html', {'enrolled': enrolled, 'form': form,
                                                                             'error': error})
                new_class.classes = i
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


def ins_Elemental(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None

        # Niños básico primera semana
        if request.method == 'POST' and 'nP' in request.POST:
            form = ElementalForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.n1:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/2-Elemental.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Niños Básico"
                new_class.weeks = "Primera semana"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/2-Elemental.htmll', {'enrolled': enrolled, 'form': form})

        # Niños básico segunda semana
        if request.method == 'POST' and 'nS' in request.POST:
            form = ElementalForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.n2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/2-Elemental.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Niños Básico"
                new_class.weeks = "Segunda semana"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/2-Elemental.htmll', {'enrolled': enrolled, 'form': form})

        # Niños básico dos semanas
        if request.method == 'POST' and 'nD' in request.POST:
            form = ElementalForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.n2 or not new_class.n1:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/2-Elemental.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Niños Básico"
                new_class.weeks = "Dos semanas"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/2-Elemental.htmll', {'enrolled': enrolled, 'form': form})

        # Jóvenes y Adultos básico primera semana
        if request.method == 'POST' and 'jP' in request.POST:
            form = ElementalForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.j1:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/2-Elemental.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Jóvenes y Adultos"
                new_class.weeks = "Primera semana"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/2-Elemental.htmll', {'enrolled': enrolled, 'form': form})

        # Jóvenes y Adultos básico segunda semana
        if request.method == 'POST' and 'jS' in request.POST:
            form = ElementalForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.j2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/2-Elemental.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Jóvenes y Adultos"
                new_class.weeks = "Segunda semana"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/2-Elemental.htmll', {'enrolled': enrolled, 'form': form})

        # Jóvenes y Adultos básico dos semanas
        if request.method == 'POST' and 'jD' in request.POST:
            form = ElementalForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.j2 or not new_class.j1:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/2-Elemental.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Jóvenes y Adultos"
                new_class.weeks = "Dos semanas"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/2-Elemental.htmll', {'enrolled': enrolled, 'form': form})

        form = ElementalForm()
        return render(request, 'schedule/2-Elemental.html', {'enrolled': enrolled, 'form': form})
    return render(request, 'schedule/2-Elemental.html', {'form': form})


def ins_Intensivo(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None

        # Niños intermedio primera semana
        if request.method == 'POST' and 'nP' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.n1m1 or not new_class.n1m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Niños Intermedio"
                new_class.weeks = "Primera semana"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Niños intermedio segunda semana
        if request.method == 'POST' and 'nS' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.n2m1 or not new_class.n2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Niños Intermedio"
                new_class.weeks = "Segunda semana"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Niños intermedio dos semanas
        if request.method == 'POST' and 'nD' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.n1m1 or not new_class.n1m2 and not new_class.n2m1 or not new_class.n2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Niños Intermedio"
                new_class.weeks = "Dos semanas"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Básico primera semana
        if request.method == 'POST' and 'bP' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.b1m1 or not new_class.b1m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Básico"
                new_class.weeks = "Primera semana"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Básico segunda semana
        if request.method == 'POST' and 'bS' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.b2m1 or not new_class.b2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Básico"
                new_class.weeks = "Segunda semana"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Básico dos semanas
        if request.method == 'POST' and 'bD' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.b1m1 or not new_class.b1m2 and not new_class.b2m1 or not new_class.b2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Básico"
                new_class.weeks = "Dos semanas"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Intermedio primera semana matutino
        if request.method == 'POST' and 'iPm' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.i1m1 or not new_class.i1m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Intermedio"
                new_class.weeks = "Primera semana"
                new_class.turn = "Matutino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Intermedio primera semana vespertino
        if request.method == 'POST' and 'iPv' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.i1v1 or not new_class.i1v2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Intermedio"
                new_class.weeks = "Primera semana"
                new_class.turn = "Vespertino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Intermedio segunda semana matutino
        if request.method == 'POST' and 'iSm' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.i2m1 or not new_class.i2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Intermedio"
                new_class.weeks = "Segunda semana"
                new_class.turn = "Matutino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Intermedio segunda semana vespertino
        if request.method == 'POST' and 'iSv' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.i2v1 or not new_class.i2v2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Intermedio"
                new_class.weeks = "Segunda semana"
                new_class.turn = "Vespertino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Intermedio dos semanas matutino y matutino
        if request.method == 'POST' and 'iDmm' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.i1m1 or not new_class.i1m2 or not new_class.i2m1 or not new_class.i2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Intermedio"
                new_class.weeks = "Dos semanas"
                new_class.turn = "Matutino y matutino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Intermedio dos semanas matutino y vespertino
        if request.method == 'POST' and 'iDmv' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.i1m1 or not new_class.i1m2 or not new_class.i2v1 or not new_class.i2v2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Intermedio"
                new_class.weeks = "Dos semanas"
                new_class.turn = "Matutino y vespertino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Intermedio dos semanas vespertino y matutino
        if request.method == 'POST' and 'iDvm' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.i1v1 or not new_class.i1v2 or not new_class.i2m1 or not new_class.i2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Intermedio"
                new_class.weeks = "Dos semanas"
                new_class.turn = "Vespertino y matutino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Intermedio dos semanas vespertino y vespertino
        if request.method == 'POST' and 'iDvv' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.i1v1 or not new_class.i1v2 or not new_class.i2v1 or not new_class.i2v2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Intermedio"
                new_class.weeks = "Dos semanas"
                new_class.turn = "Vespertino y vespertino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Avanzado primera semana matutino
        if request.method == 'POST' and 'aPm' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.a1m1 or not new_class.a1m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Avanzado"
                new_class.weeks = "Primera semana"
                new_class.turn = "Matutino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Avanzado primera semana vespertino
        if request.method == 'POST' and 'aPv' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.a1v1 or not new_class.a1v2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Avanzado"
                new_class.weeks = "Primera semana"
                new_class.turn = "Vespertino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Avanzado segunda semana matutino
        if request.method == 'POST' and 'aSm' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.a2m1 or not new_class.a2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Avanzado"
                new_class.weeks = "Segunda semana"
                new_class.turn = "Matutino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Avanzado segunda semana vespertino
        if request.method == 'POST' and 'aSv' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.a2v1 or not new_class.a2v2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Avanzado"
                new_class.weeks = "Segunda semana"
                new_class.turn = "Vespertino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Avanzado dos semanas matutino y matutino
        if request.method == 'POST' and 'aDmm' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.a1m1 or not new_class.a1m2 or not new_class.a2m1 or not new_class.a2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Avanzado"
                new_class.weeks = "Dos semanas"
                new_class.turn = "Matutino y matutino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Avanzado dos semanas matutino y vespertino
        if request.method == 'POST' and 'aDmv' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.a1m1 or not new_class.a1m2 or not new_class.a2v1 or not new_class.a2v2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Avanzado"
                new_class.weeks = "Dos semanas"
                new_class.turn = "Matutino y vespertino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Avanzado dos semanas vespertino y matutino
        if request.method == 'POST' and 'aDvm' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.a1v1 or not new_class.a1v2 or not new_class.a2m1 or not new_class.a2m2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Avanzado"
                new_class.weeks = "Dos semanas"
                new_class.turn = "Vespertino y matutino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        # Avanzado dos semanas vespertino y vespertino
        if request.method == 'POST' and 'aDvv' in request.POST:
            form = IntensivoForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                if not new_class.a1v1 or not new_class.a1v2 or not new_class.a2v1 or not new_class.a2v2:
                    error = "Necesitas llenar todo el formulario"
                    return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.level = "Avanzado"
                new_class.weeks = "Dos semanas"
                new_class.turn = "Vespertino y vespertino"
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})

        form = IntensivoForm()
        return render(request, 'schedule/3-Intensivo.html', {'enrolled': enrolled, 'form': form})
    return render(request, 'schedule/3-Intensivo.html', {'form': form})


def ins_Independiente(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None

        # Primera semana
        if request.method == 'POST' and 'p' in request.POST:
            form = IndependienteForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                i = 0
                if new_class.p9:
                    i = i + 1
                if new_class.p10:
                    i = i + 1
                if new_class.p3:
                    i = i + 1
                if new_class.p5:
                    i = i + 1
                if i == 0:
                    error = "Necesitas inscribir al menos una clase"
                    return render(request, 'schedule/1-Independiente.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.weeks = "Primera semana"
                new_class.classes = i
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/1-Independiente.html', {'enrolled': enrolled, 'form': form})

        # Primera semana
        if request.method == 'POST' and 's' in request.POST:
            form = IndependienteForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.id_enrolled = request.user
                i = 0
                if new_class.s9:
                    i = i + 1
                if new_class.s10:
                    i = i + 1
                if new_class.s3:
                    i = i + 1
                if new_class.s5:
                    i = i + 1
                if i == 0:
                    error = "Necesitas inscribir al menos una clase"
                    return render(request, 'schedule/1-Independiente.html', {'enrolled': enrolled, 'form': form,
                                                                         'error': error})
                new_class.weeks = "Segunda semana"
                new_class.classes = i
                new_class.save()
                return redirect(reverse('userprofile'))
            return render(request, 'schedule/1-Independiente.html', {'enrolled': enrolled, 'form': form})

        form = IndependienteForm()
        return render(request, 'schedule/1-Independiente.html', {'enrolled': enrolled, 'form': form})
    return render(request, 'schedule/1-Independiente.html', {'form': form})


def inscription(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
        # Program not selected
        return render(request, 'schedule/schedule.html', {'enrolled': enrolled})
    # Session not started
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
