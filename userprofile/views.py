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
            validation = UserProfileInfo.objects.get(user=user)
        except UserProfileInfo.DoesNotExist:
            validation = None
        if validation is not None:
            enrolled = Enrolled.objects.get(user=user)
            return render(request, 'schedule/already_enrolled.html', {'validation': validation, 'enrolled': enrolled})

        #Case logged user completing enrolled form
        if request.method == 'POST':
            form = CompleteProfile(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                profile = UserProfileInfo.objects.create(user=obj.user, form_validate=True)
                return HttpResponseRedirect(reverse_lazy('profileform'))

        #Case logged user but enrolled form has not been completed
        form = CompleteProfile()
        return render(request, 'schedule/enrolled_form.html', {'form': form})

    #Case not logged
    return render(request, 'schedule/enrolled_form.html')
