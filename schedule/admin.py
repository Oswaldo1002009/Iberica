from django.contrib import admin
from .models import Program, Level, Weeks, Teacher, Classes


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
