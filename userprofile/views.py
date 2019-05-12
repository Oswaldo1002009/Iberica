from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from schedule.models import Enrolled, ClassEnrolled
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CompleteProfile
from core.models import UserProfileInfo


def index(request):
    classes_list = ClassEnrolled.objects.order_by('id_class')
    context = {
        'classes_list': classes_list,
    }
    return render(request, 'userprofile/profile.html', context)


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        #Case logged user with enrolled form completed
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
        if enrolled is not None:
            return render(request, 'schedule/already_enrolled.html', {'enrolled': enrolled})

        #Case logged user completing enrolled form
        if request.method == 'POST':
            form = CompleteProfile(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return HttpResponseRedirect(reverse_lazy('profileform'))

        #Case logged user but enrolled form has not been completed
        form = CompleteProfile()
        return render(request, 'schedule/enrolled_form.html', {'form': form})

    #Case not logged
    return render(request, 'schedule/enrolled_form.html')
