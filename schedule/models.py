# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Program(models.Model):
    name = models.CharField(max_length=50, db_index=True)
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
    week1 = models.CharField(max_length=50, db_index=True)
    ini1 = models.DateTimeField()
    end1 = models.DateTimeField()

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
    code = models.ForeignKey(User, related_name='code', on_delete=models.CASCADE, db_index=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    enrolled = models.IntegerField(default=0, blank=True)
    total_payed = models.BooleanField(default=False)

    class Meta:
        ordering = ('code', )
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.code


class Enrolled(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    GENDER = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    birth_date = models.DateTimeField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    academy = models.CharField(max_length=100)
    disease = models.TextField(blank=True)
    BLOOD_TYPES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPES)
    #enrolled = models.BooleanField(default=False, blank=True, null=True)
    #amount_en = models.IntegerField(blank=True, null=True)
    #payed_courses = models.IntegerField(blank=True, null=True)
    #total_payed = models.BooleanField(default=False, blank=True, null=True)
    #group = models.ForeignKey(Groups, related_name='group_enrolled', on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = [['user']]
        ordering = ('name',)
        verbose_name = 'Enrolled'
        verbose_name_plural = 'Enrolled'

    def __str__(self):
        return "%s: %s %s" % (self.user, self.name, self.lastname)


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


class TallerGuitarra(models.Model):
    id_enrolled = models.ForeignKey(User, related_name='Guitar_Enrolled', on_delete=models.CASCADE, db_index=True)
    classes = models.CharField(max_length=1, blank=True)
    CLASSES1 = (
        ('8-12 julio, 9:00 am - 12:00 pm: Román Vicenti', '8-12 julio, 9:00 am - 12:00 pm: Román Vicenti'),
    )
    CLASSES2 = (
        ('15-17 julio, 9:00 am - 12:00 pm: Oscar Lagos', '15-17 julio, 9:00 am - 12:00 pm: Oscar Lagos'),
    )
    CLASSES3 = (
        ('18-20 julio, 9:00 am - 12:00 pm: Antonio Campos y Jose Luis Medina',
         '18-20 julio, 9:00 am - 12:00 pm: Antonio Campos y Jose Luis Medina'),
    )
    s1 = models.CharField(max_length=100, choices=CLASSES1, blank=True)
    s2 = models.CharField(max_length=100, choices=CLASSES2, blank=True)
    s3 = models.CharField(max_length=100, choices=CLASSES3, blank=True)

    class Meta:
        verbose_name = 'Taller de Guitarra'
        verbose_name_plural = 'Talleres de Guitarra'

    def __str__(self):
        return "%s %s" % (self.id_class, self.id_enrolled)
    
class Observador(models.Model):
    id_enrolled = models.ForeignKey(User, related_name='Observer_Enrolled', on_delete=models.CASCADE, db_index=True)
    CHOICES = (
        ('8-12 julio (Semana 1)', '8-19 julio (Semana 1)'),
        ('15-19 julio (Semana 2)', '15-19 julio (Semana 2)'),
        ('8-19 julio (Dos semanas)', '8-19 julio (Dos semanas)'),
        ('1 día', '1 día'),
    )
    id_class = models.CharField(max_length=30, choices=CHOICES)

    class Meta:
        verbose_name = 'Observador'
        verbose_name_plural = 'Observadores'

    def __str__(self):
        return "%s %s" % (self.id_class, self.id_enrolled)

class Inter(models.Model):
    id_enrolled = models.ForeignKey(User, related_name='Inter_Enrolled', on_delete=models.CASCADE, db_index=True)
    WEEK1_12 = (
        ('Cristóbal Reyes "Valoración del Flamenco"',
         'Cristóbal Reyes "Valoración del Flamenco"'),
        ('Eduardo Alves "Técnica de Danza Clásica" Nivel Intermedio',
         'Eduardo Alves "Técnica de Danza Clásica" Nivel Intermedio'),
        ('Nuria Balbaneda "Técnica de Danza Clásica" Nivel Avanzado',
         'Nuria Balbaneda "Técnica de Danza Clásica" Nivel Avanzado'),
        ('La Truco "Certificaciones de la EFA para Nivel Básico" Solo Avanzados (NUEVO)',
         'La Truco "Certificaciones de la EFA para Nivel Básico" Solo Avanzados (NUEVO)'),
        ('Juan Paredes "Siente el Flamenco"',
         'Juan Paredes "Siente el Flamenco"'),
        ('Carlos López Aragón "Danza Flamenca Urbana"',
         'Carlos López Aragón "Danza Flamenca Urbana"'),
        ('Maribel Gallardo "Técnica de Danza Española" Castañuelas, Vueltas y Braceos',
         'Maribel Gallardo "Técnica de Danza Española" Castañuelas, Vueltas y Braceos'),
        ('José Galán "Flamenco Inclusivo" Dirigido a Niveles Intermedio y Avanzado (NUEVO)',
         'José Galán "Flamenco Inclusivo" Dirigido a Niveles Intermedio y Avanzado (NUEVO)'),
    )
    WEEK1_13 = (
        ('Cristóbal Reyes "Valoración del Flamenco"',
         'Cristóbal Reyes "Valoración del Flamenco"'),
        ('Eduardo Alves "Técnica de Danza Clásica" Nivel Básico',
         'Eduardo Alves "Técnica de Danza Clásica" Nivel Básico'),
        ('Nuria Balbaneda "Coreografía de Danza Clásica" Nivel Intermedio y Avanzado',
         'Nuria Balbaneda "Coreografía de Danza Clásica" Nivel Intermedio y Avanzado'),
        ('Ana López "Estilización y Escuela Bolera"',
         'Ana López "Estilización y Escuela Bolera"'),
        ('María Juncal "Técnica de Brazos y Cuerpo"',
         'María Juncal "Técnica de Brazos y Cuerpo"'),
        ('Carlos López Aragón "Acrodanza"',
         'Carlos López Aragón "Acrodanza"'),
        ('Maribel Gallardo "Repertorio de la Danza Española" Goyescas (Abanico) y La Vida Breve (Castañuelas)',
         'Maribel Gallardo "Repertorio de la Danza Española" Goyescas (Abanico) y La Vida Breve (Castañuelas)'),
    )
    WEEK2_12 = (
        ('Eduardo Alves "Técnica de Danza Clásica" Nivel Intermedio',
         'Eduardo Alves "Técnica de Danza Clásica" Nivel Intermedio'),
        ('Nuria Balbaneda "Técnica de Danza Clásica" Nivel Avanzado',
         'Nuria Balbaneda "Técnica de Danza Clásica" Nivel Avanzado'),
        ('Cristóbal Reyes "Valoración del Flamenco"',
         'Cristóbal Reyes "Valoración del Flamenco"'),
        ('María Juncal "Técnica de Pies"',
         'María Juncal "Técnica de Pies"'),
        ('José Galán "Flamenco Inclusivo" Dirigido a Niveles Intermedio y Avanzado (NUEVO)',
         'José Galán "Flamenco Inclusivo" Dirigido a Niveles Intermedio y Avanzado (NUEVO)'),
        ('Maribel Gallardo "Técnica de Danza Española" Castañuelas, Vueltas y Braceos',
         'Maribel Gallardo "Técnica de Danza Española" Castañuelas, Vueltas y Braceos'),
        ('Raquel Ruiz "Neo Folk"',
         'Raquel Ruiz "Neo Folk"'),
        ('Ana López "Estilización y Escuela Bolera"',
         'Ana López "Estilización y Escuela Bolera"'),
    )
    WEEK2_13 = (
        ('Cristóbal Reyes "Valoración del Flamenco"',
         'Cristóbal Reyes "Valoración del Flamenco"'),
        ('Eduardo Alves "Técnica de Danza Clásica" Nivel Básico',
         'Eduardo Alves "Técnica de Danza Clásica" Nivel Básico'),
        ('Nuria Balbaneda "Coreografía de Danza Clásica" Nivel Intermedio y Avanzado',
         'Nuria Balbaneda "Coreografía de Danza Clásica" Nivel Intermedio y Avanzado'),
        ('Juan Paredes "Siente el Flamenco"',
         'Juan Paredes "Siente el Flamenco"'),
        ('La Truco "Certificaciones de la EFA para Nivel Intermedio" Solo Avanzados (NUEVO)',
         'La Truco "Certificaciones de la EFA para Nivel Intermedio" Solo Avanzados (NUEVO)'),
        ('Maribel Gallardo "Repertorio de la Danza Española" Goyescas (Abanico) y La Vida Breve (Castañuelas)',
         'Maribel Gallardo "Repertorio de la Danza Española" Goyescas (Abanico) y La Vida Breve (Castañuelas)'),
        ('Raquel Ruiz "Neo Folk"',
         'Raquel Ruiz "Neo Folk"'),
    )
    week1_12 = models.CharField(max_length=150, choices=WEEK1_12, blank=True)
    week1_13 = models.CharField(max_length=150, choices=WEEK1_13, blank=True)
    week2_12 = models.CharField(max_length=150, choices=WEEK2_12, blank=True)
    week2_13 = models.CharField(max_length=150, choices=WEEK2_13, blank=True)
    weeks = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Interdisciplinario'
        verbose_name_plural = 'Interdisciplinarios'

    def __str__(self):
        return "%s %s" % (self.weeks, self.id_enrolled)


class Intensivo(models.Model):
    id_enrolled = models.ForeignKey(User, related_name='Intensivo_Enrolled', on_delete=models.CASCADE, db_index=True)
    level = models.CharField(max_length=20, blank=True)
    weeks = models.CharField(max_length=50, blank=True)
    turn = models.CharField(max_length=50, blank=True)

    NIWEEK1_9 = (('José Galán', 'José Galán'),)
    NIWEEK1_10 = (('Manuel Fernández "El carpeta" (Seguiriyas)', 'Manuel Fernández "El carpeta" (Seguiriyas)'),)
    NIWEEK2_9 = (('Nazaret Reyes (Alegrías)', 'Nazaret Reyes (Alegrías)'),)
    NIWEEK2_10 = (('María Juncal (Tientos)', 'María Juncal (Tientos)'),)
    n1m1 = models.CharField(max_length=150, choices=NIWEEK1_9, blank=True)
    n1m2 = models.CharField(max_length=150, choices=NIWEEK1_10, blank=True)
    n2m1 = models.CharField(max_length=150, choices=NIWEEK2_9, blank=True)
    n2m2 = models.CharField(max_length=150, choices=NIWEEK2_10, blank=True)

    BWEEK1_9 = (('Juan Paredes (Bailes festeros por tangos)', 'Juan Paredes (Bailes festeros por tangos)'),)
    BWEEK1_10 = (('Valeriano Paños (Farruca)', 'Valeriano Paños (Farruca)'),)
    BWEEK2_9 = (('Pablo Egea', 'Pablo Egea'),)
    BWEEK2_10 = (('Nazaret Reyes (Tangos)', 'Nazaret Reyes (Tangos)'),)
    b1m1 = models.CharField(max_length=150, choices=BWEEK1_9, blank=True)
    b1m2 = models.CharField(max_length=150, choices=BWEEK1_10, blank=True)
    b2m1 = models.CharField(max_length=150, choices=BWEEK2_9, blank=True)
    b2m2 = models.CharField(max_length=150, choices=BWEEK2_10, blank=True)

    IWEEK1_9 = (('El Carpeta (Bulerías)', 'El Carpeta (Bulerías)'),
                ('Nazaret Reyes (Alegrías)','Nazaret Reyes (Alegrías)'),)
    IWEEK1_10 = (('Rafael Estévez (Tangos)', 'Rafael Estévez (Tangos)'),
                 ('Nazaret Reyes (Caña)', 'Nazaret Reyes (Caña)',),)
    IWEEK1_3 = (('María Juncal (Fandangos)', 'María Juncal (Fandangos)'),)
    IWEEK1_5 = (('Ana Morales (Alegrías de Córdoba)', 'Ana Morales (Alegrías de Córdoba)'),)
    IWEEK2_9 = (('Eduardo Guerrero (Bulerías)', 'Eduardo Guerrero (Bulerías)'),
                ('El Carpeta (Seguiriyas)', 'El Carpeta (Seguiriyas)'),)
    IWEEK2_10 = (('María Moreno (Romance)', 'María Moreno (Romance)'),
                 ('Ana Morales (Guajira)','Ana Morales (Guajira)'),)
    IWEEK2_3 = (('Karen Lugo (Bambera)', 'Karen Lugo (Bambera)'),)
    IWEEK2_5 = (('Juan Paredes (Bailes festeros por bulerías)', 'Juan Paredes (Bailes festeros por bulerías)'),)
    i1m1 = models.CharField(max_length=150, choices=IWEEK1_9, blank=True)
    i1m2 = models.CharField(max_length=150, choices=IWEEK1_10, blank=True)
    i1v1 = models.CharField(max_length=150, choices=IWEEK1_3, blank=True)
    i1v2 = models.CharField(max_length=150, choices=IWEEK1_5, blank=True)
    i2m1 = models.CharField(max_length=150, choices=IWEEK2_9, blank=True)
    i2m2 = models.CharField(max_length=150, choices=IWEEK2_10, blank=True)
    i2v1 = models.CharField(max_length=150, choices=IWEEK2_3, blank=True)
    i2v2 = models.CharField(max_length=150, choices=IWEEK2_5, blank=True)

    AWEEK1_9 = (('Valeriano Paños (Martinete)', 'Valeriano Paños (Martinete)'),
                ('Rafael Estevez (Cantiña del amarano)', 'Rafael Estevez (Cantiña del amarano)'),
                ('Javier LaTorre (Guajira) -Grupo exclusivo para maestros y/o bailarines profesionales-',
                 'Javier LaTorre (Guajira) -Grupo exclusivo para maestros y/o bailarines profesionales-'),)
    AWEEK1_10 = (('Javier LaTorre (Taranto)', 'Javier LaTorre (Taranto)'),
                 ('La Truco (Soleá)', 'La Truco (Soleá)'),)
    AWEEK1_3 = (('Ana Morales (Soleá)', 'Ana Morales (Soleá)'),
                ('Pedro Córdoba (Soleá por bulería)', 'Pedro Córdoba (Soleá por bulería)'),)
    AWEEK1_5 = (('Pedro Córdoba (Soleá por bulería)', 'Pedro Córdoba (Soleá por bulería)'),
                ('María Juncal (Guajira)', 'María Juncal (Guajira)'),)
    AWEEK2_9 = (('Ana Morales (Seguiriya)', 'Ana Morales (Seguiriya)'),
                ('María Moreno (Soleá por bulería)', 'María Moreno (Soleá por bulería)'),
                ('Pedro Córdoba (Jaleos) -Grupo exclusivo para maestros y/o bailarines profesionales-',
                 'Pedro Córdoba (Jaleos) -Grupo exclusivo para maestros y/o bailarines profesionales-'),)
    AWEEK2_10 = (('Eduardo Guerrero (Fandango)', 'Eduardo Guerrero (Fandango)'),
                 ('Pedro Córdoba (Soleá por Bulería)', 'Pedro Córdoba (Soleá por Bulería)'),)
    AWEEK2_3 = (('Javier LaTorre (Alegrías)', 'Javier LaTorre (Alegrías)'),
                ('La Truco (Seguiriya)', 'La Truco (Seguiriya)'),)
    AWEEK2_5 = (('Karen Lugo (Martinete)', 'Karen Lugo (Martinete)'),
                ('Javier LaTorre (Farruca)', 'Javier LaTorre (Farruca)'),)

    a1m1 = models.CharField(max_length=150, choices=AWEEK1_9, blank=True)
    a1m2 = models.CharField(max_length=150, choices=AWEEK1_10, blank=True)
    a1v1 = models.CharField(max_length=150, choices=AWEEK1_3, blank=True)
    a1v2 = models.CharField(max_length=150, choices=AWEEK1_5, blank=True)
    a2m1 = models.CharField(max_length=150, choices=AWEEK2_9, blank=True)
    a2m2 = models.CharField(max_length=150, choices=AWEEK2_10, blank=True)
    a2v1 = models.CharField(max_length=150, choices=AWEEK2_3, blank=True)
    a2v2 = models.CharField(max_length=150, choices=AWEEK2_5, blank=True)

    class Meta:
        verbose_name = 'Intensivo'
        verbose_name_plural = 'Intensivos'

    def __str__(self):
        return "%s %s %s %s" % (self.level, self.weeks, self.turn, self.id_enrolled)


class Elemental(models.Model):
    id_enrolled = models.ForeignKey(User, related_name='Elemental_Enrolled', on_delete=models.CASCADE, db_index=True)
    level = models.CharField(max_length=20, blank=True)
    weeks = models.CharField(max_length=50, blank=True)

    NBWEEK1 = (('Pablo Egea', 'Pablo Egea'),)
    NBWEEK2 = (('El Carpeta (Alegría)', 'El Carpeta (Alegría)'),)
    JABWEEK1 = (('9:00 am 10:30 am | Juan Paredes (Bailes festeros por tangos)',
                 '9:00 am 10:30 am | Juan Paredes (Bailes festeros por tangos)'),
                ('10:35 am - 12:05 pm | Valeriano Paños (Farruca)', '10:35 am - 12:05 pm | Valeriano Paños (Farruca)'),)
    JABWEEK2 = (('9:00 am - 10:30 am | José Galán', '9:00 am - 10:30 am | José Galán'),
                ('10:35 am - 12:05 pm | Nazaret Reyes (Tangos)', '10:35 am - 12:05 pm | Nazaret Reyes (Tangos)'),)

    n1 = models.CharField(max_length=150, choices=NBWEEK1, blank=True)
    n2 = models.CharField(max_length=150, choices=NBWEEK2, blank=True)
    j1 = models.CharField(max_length=150, choices=JABWEEK1, blank=True)
    j2 = models.CharField(max_length=150, choices=JABWEEK2, blank=True)

    class Meta:
        verbose_name = 'Elemental'
        verbose_name_plural = 'Elementales'

    def __str__(self):
        return "%s %s %s" % (self.level, self.weeks, self.id_enrolled)

class Independiente(models.Model):
    id_enrolled = models.ForeignKey(User, related_name='Independiente_Enrolled', on_delete=models.CASCADE, db_index=True)
    weeks = models.CharField(max_length=50, blank=True)
    classes = models.CharField(max_length=1, blank=True)

    P900 = (
        ('NIÑOS INTERMEDIO - José Galán', 'NIÑOS INTERMEDIO - José Galán'),
        ('NIVEL BÁSICO - Juan Paredes (Bailes festeros por tangos)',
         'NIVEL BÁSICO - Juan Paredes (Bailes festeros por tangos)'),
        ('NIVEL INTERMEDIO - Nazaret Reyes (Alegrías)',
         'NIVEL INTERMEDIO - Nazaret Reyes (Alegrías)'),
        ('NIVEL INTERMEDIO - El Carpeta (Bulerías)', 'NIVEL INTERMEDIO - El Carpeta (Bulerías)'),
        ('NIVEL AVANZADO - Rafael Estévez (Cantiña del amarano)',
         'NIVEL AVANZADO - Rafael Estévez (Cantiña del amarano)'),
        ('NIVEL AVANZADO - Valeriano Paños (Martinete)',
         'NIVEL AVANZADO - Valeriano Paños (Martinete)'),
        ('NIVEL PROFESIONAL - Javier LaTorre', 'NIVEL PROFESIONAL - Javier LaTorre'),
    )
    P1035 = (
        ('NIÑOS BÁSICO - Pablo Egea', 'NIÑOS BÁSICO - Pablo Egea'),
        ('NIÑOS INTERMEDIO - El Carpeta (Seguiriyas)', 'NIÑOS INTERMEDIO - El Carpeta (Seguiriyas)'),
        ('NIVEL BÁSICO - Valeriano Paños (Farruca)', 'NIVEL BÁSICO - Valeriano Paños (Farruca)'),
        ('NIVEL INTERMEDIO - Rafael Estévez (Tangos)', 'NIVEL INTERMEDIO - Rafael Estévez (Tangos)'),
        ('NIVEL INTERMEDIO - Nazaret Reyes (Caña)', 'NIVEL INTERMEDIO - Nazaret Reyes (Caña)'),
        ('NIVEL AVANZADO - La Truco (Soleá)', 'NIVEL AVANZADO - La Truco (Soleá)'),
        ('NIVEL AVANZADO - Javier LaTorre (Taranto)', 'NIVEL AVANZADO - Javier LaTorre (Taranto)'),
    )
    P1530 = (
        ('NIVEL INTERMEDIO - María Juncal (Fandangos)', 'NIVEL INTERMEDIO - María Juncal (Fandangos)'),
        ('NIVEL AVANZADO - Pedro Córdoba (Soleá por bulería)', 'NIVEL AVANZADO - Pedro Córdoba (Soleá por bulería)'),
        ('NIVEL AVANZADO - Ana Morales (Soleá)', 'NIVEL AVANZADO - Ana Morales (Soleá)'),
    )
    P1705 = (
        ('NIVEL INTERMEDIO - Ana Morales (Alegrías de Córdoba)', 'NIVEL INTERMEDIO - Ana Morales (Alegrías de Córdoba)'),
        ('NIVEL AVANZADO - María Juncal (Guajira)', 'NIVEL AVANZADO - María Juncal (Guajira)'),
        ('NIVEL AVANZADO - Pedro Córdoba (Martinete)', 'NIVEL AVANZADO - Pedro Córdoba (Martinete)'),
    )
    S900 = (
        ('NIÑOS INTERMEDIO - Nazaret Reyes (Alegrías)', 'NIÑOS INTERMEDIO - Nazaret Reyes (Alegrías)'),
        ('NIVEL BÁSICO - José Galán', 'NIVEL BÁSICO - José Galán'),
        ('NIVEL INTERMEDIO - El Carpeta (Seguiriyas)', 'NIVEL INTERMEDIO - El Carpeta (Seguiriyas)'),
        ('NIVEL INTERMEDIO - Eduardo Guerrero (Bulerías)', 'NIVEL INTERMEDIO - Eduardo Guerrero (Bulerías)'),
        ('NIVEL AVANZADO - María Moreno (Bata de Cola por Alegrías)',
         'NIVEL AVANZADO - María Moreno (Bata de Cola por Alegrías)'),
        ('NIVEL AVANZADO - Ana Morales (Seguiriya)', 'NIVEL AVANZADO - Ana Morales (Seguiriya)'),
        ('NIVEL PROFESIONAL - Pedro Córdoba', 'NIVEL PROFESIONAL - Pedro Córdoba'),
    )
    S1035 = (
        ('NIÑOS BÁSICO - El Carpeta (Alegría)', 'NIÑOS BÁSICO - El Carpeta (Alegría)'),
        ('NIÑOS INTERMEDIO - María Juncal (Tientos)', 'NIÑOS INTERMEDIO - María Juncal (Tientos)'),
        ('NIVEL BÁSICO - Nazaret Reyes (Tangos)', 'NIVEL BÁSICO - Nazaret Reyes (Tangos)'),
        ('NIVEL INTERMEDIO - Ana Morales (Guajira)', 'NIVEL INTERMEDIO - Ana Morales (Guajira)'),
        ('NIVEL INTERMEDIO - María Moreno (Romance)', 'NIVEL INTERMEDIO - María Moreno (Romance)'),
        ('NIVEL AVANZADO - Pedro Córdoba (Soleá por bulería)', 'NIVEL AVANZADO - Pedro Córdoba (Soleá por bulería)'),
        ('NIVEL AVANZADO - Eduardo Guerrero (Fandango)', 'NIVEL AVANZADO - Eduardo Guerrero (Fandango)'),
    )
    S1530 = (
        ('NIVEL INTERMEDIO - Karen Lugo (Bambera)', 'NIVEL INTERMEDIO - Karen Lugo (Bambera)'),
        ('NIVEL AVANZADO - La Truco (Seguiriya)', 'NIVEL AVANZADO - La Truco (Seguiriya)'),
        ('NIVEL AVANZADO - Javier LaTorre (Alegrías)', 'NIVEL AVANZADO - Javier LaTorre (Alegrías)'),
    )
    S1705 = S1530 = (
        ('NIVEL INTERMEDIO - Juan Paredes (Bailes festeros, bulerías)',
         'NIVEL INTERMEDIO - Juan Paredes (Bailes festeros, bulerías)'),
        ('NIVEL AVANZADO - Javier LaTorre (Farruca)', 'NIVEL AVANZADO - Javier LaTorre (Farruca)'),
        ('NIVEL AVANZADO - Karen Lugo (Martinete)', 'NIVEL AVANZADO - Karen Lugo (Martinete)'),
    )

    p9 = models.CharField(max_length=150, choices=P900, blank=True)
    p10 = models.CharField(max_length=150, choices=P1035, blank=True)
    p3 = models.CharField(max_length=150, choices=P1530, blank=True)
    p5 = models.CharField(max_length=150, choices=P1705, blank=True)
    s9 = models.CharField(max_length=150, choices=S900, blank=True)
    s10 = models.CharField(max_length=150, choices=S1035, blank=True)
    s3 = models.CharField(max_length=150, choices=S1530, blank=True)
    s5 = models.CharField(max_length=150, choices=S1705, blank=True)

    class Meta:
        verbose_name = 'Independiente'
        verbose_name_plural = 'Independientes'

    def __str__(self):
        return "%s %s" % (self.weeks, self.id_enrolled)
