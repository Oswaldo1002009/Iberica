from django.contrib import admin
from .models import Program, Level, Weeks, Teacher, Classes, Blood_type, Enrolled, Em_contact, Groups,\
    ClassEnrolled, TallerGuitarra, Observador


admin.site.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'available']


admin.site.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['program_id', 'level', 'name', 'min_age', 'max_age', 'description', 'cost1', 'cost2']

admin.site.register(Weeks)

admin.site.register(Teacher)

admin.site.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'rem_places': ('max_places',)}

admin.site.register(Blood_type)

admin.site.register(Groups)

admin.site.register(Enrolled)

admin.site.register(Em_contact)

admin.site.register(ClassEnrolled)

admin.site.register(TallerGuitarra)

admin.site.register(Observador)