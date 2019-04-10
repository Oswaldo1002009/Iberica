from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'program'
        verbose_name_plural = 'programs'

    def __str__(self):
        return self.name


class Level(models.Model):
    level = models.IntegerField(db_index=True)
    name = models.CharField(max_length=200)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    description = models.CharField(max_length=300, blank=True)
    program_id = models.ForeignKey(Program, related_name='level', on_delete=models.CASCADE)
    cost1 = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    cost2 = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    class Meta:
        ordering = ('level',)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    birth_date = models.DateTimeField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Weeks(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    ini_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = 'week'
        verbose_name_plural = 'weeks'

    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=200)
    time_ini = models.TimeField()
    time_end = models.TimeField()
    max_places = models.IntegerField()
    rem_places = models.IntegerField()
    ocu_places = models.IntegerField()
    teacher_id = models.ForeignKey(Teacher, related_name='classes', on_delete=models.CASCADE)
    date_id = models.ForeignKey(Weeks, related_name='classes', on_delete=models.CASCADE)

    class Meta:
        ordering = ('date_id',)
        verbose_name = 'class'
        verbose_name_plural = 'classes'

    def __str__(self):
        return self.name
