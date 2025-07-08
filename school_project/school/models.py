from django.db import models


# Модель предмету
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Модель вчителя
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Модель класу
class Class(models.Model):
    name = models.CharField(max_length=20)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='class_teacher')

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(blank=True, null=True)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Schedule(models.Model):
    WEEKDAYS = [
        ('mon', 'Понеділок'),
        ('tue', 'Вівторок'),
        ('wed', 'Середа'),
        ('thu', 'Четвер'),
        ('fri', 'Пʼятниця'),
        ('sat', 'Субота'),
        ('sun', 'Неділя'),
    ]

    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='schedules')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    weekday = models.CharField(max_length=3, choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_group} - {self.subject} ({self.get_weekday_display()})"
