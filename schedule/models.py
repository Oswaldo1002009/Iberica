from django.db import models
from django.contrib.auth.models import User

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
    level = models.CharField(max_length=200)
    name = models.CharField(max_length=200, db_index=True)
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
    name = models.CharField(max_length=200, db_index=True)
    level_id = models.ForeignKey(Level, related_name="classes", on_delete=models.CASCADE)
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


class Blood_type(models.Model):
    type = models.CharField(max_length=50, db_index=True, default='')

    class Meta:
        verbose_name = 'Blood_type'
        verbose_name_plural = 'Blood_types'

    def __str__(self):
        return self.type


class Groups(models.Model):
    code = models.CharField(max_length=100, db_index=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    enrolled = models.IntegerField()
    total_payed = models.BooleanField(default=False)

    class Meta:
        ordering = ('code', )
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.code


class Enrolled(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=200)
    birth_date = models.DateTimeField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    academy = models.CharField(max_length=100)
    disease = models.CharField(max_length=200)
    blood_type = models.ForeignKey(Blood_type, related_name='blood_type', on_delete=models.CASCADE)
    enrolled = models.BooleanField(default=False)
    amount_en = models.IntegerField()
    payed_courses = models.IntegerField()
    total_payed = models.BooleanField(default=False)
    group = models.ForeignKey(Groups, related_name='group_enrolled', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Enrolled'
        verbose_name_plural = 'Enrolled'

    def __str__(self):
        return self.name


class Em_contact(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    relation = models.CharField(max_length=50)
    phone = models.IntegerField()
    enrolled = models.ForeignKey(Enrolled, related_name='Enrolled_contact', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Emergency_contact'
        verbose_name_plural = 'Emergency_contacts'

    def __str__(self):
        return self.name


class ClassEnrolled(models.Model):
    id_program = models.ForeignKey(Program, related_name="Program", on_delete=models.CASCADE)
    id_level = models.ForeignKey(Level, related_name="Level", on_delete=models.CASCADE)
    id_class = models.ForeignKey(Classes, related_name='Class', on_delete=models.CASCADE, db_index=True)
    id_enrolled = models.ForeignKey(User, related_name='Student', on_delete=models.CASCADE, db_index=True)

    class Meta:
        index_together = (('id_class', 'id_enrolled'),)
        verbose_name = 'Class Enrolled'
        verbose_name_plural = 'Classes Enrolled'

    def __str__(self):
        return "%s %s" % (self.id_class, self.id_enrolled)
