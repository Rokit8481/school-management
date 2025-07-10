import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_project.settings')
django.setup()

from school.models import Subject, Teacher, Class, Student, Schedule, Grade
import random

#Предмети
subject1 = Subject.objects.create(
    name="Математика",
    description="Поглиблене вивчення математики"
)
subject2 = Subject.objects.create(
    name="Українська мова",
    description="Граматика, лексика, синтаксис"
)
subject3 = Subject.objects.create(
    name="Історія",
    description="Історія України та світу"
)
subject4 = Subject.objects.create(
    name="Біологія",
    description="Жива природа, організми та екосистеми"
)
subject5 = Subject.objects.create(
    name="Хімія",
    description="Речовини та їхні перетворення"
)
subject6 = Subject.objects.create(
    name="Фізика",
    description="Закони природи та експериментальні дослідження"
)
subject7 = Subject.objects.create(
    name="Інформатика",
    description="Компʼютери, алгоритми та програмування"
)
subject8 = Subject.objects.create(
    name="Географія",
    description="Країни, материки, географічні процеси"
)


#Вчителі
teacher1 = Teacher.objects.create(
    first_name="Іван",
    last_name="Петренко",
    email="ivan.petrenko@example.com",
    subject=subject1
)
teacher2 = Teacher.objects.create(
    first_name="Ольга",
    last_name="Шевченко",
    email="olha.shevchenko@example.com",
    subject=subject2
)
teacher3 = Teacher.objects.create(
    first_name="Андрій",
    last_name="Коваль",
    email="andriy.koval@example.com",
    subject=subject3
)
teacher4 = Teacher.objects.create(
    first_name="Наталія",
    last_name="Сидоренко",
    email="natalia.sydorenko@example.com",
    subject=subject4
)
teacher5 = Teacher.objects.create(
    first_name="Юрій",
    last_name="Мельник",
    email="yuriy.melnyk@example.com",
    subject=subject5
)
teacher6 = Teacher.objects.create(
    first_name="Людмила",
    last_name="Бондар",
    email="lyudmyla.bondar@example.com",
    subject=subject6
)
teacher7 = Teacher.objects.create(
    first_name="Сергій",
    last_name="Ткаченко",
    email="serhiy.tkachenko@example.com",
    subject=subject7
)
teacher8 = Teacher.objects.create(
    first_name="Ірина",
    last_name="Демченко",
    email="iryna.demchenko@example.com",
    subject=subject8
)
teacher9 = Teacher.objects.create(
    first_name="Марина",
    last_name="Литвиненко",
    email="marina.lytvynenko@example.com",
    subject=subject1
)
teacher10 = Teacher.objects.create(
    first_name="Олександр",
    last_name="Гончар",
    email="oleksandr.honchar@example.com",
    subject=subject1
)
teacher11 = Teacher.objects.create(
    first_name="Тетяна",
    last_name="Романенко",
    email="tetiana.romanenko@example.com",
    subject=subject2 
)
teacher12 = Teacher.objects.create(
    first_name="Валентин",
    last_name="Захарченко",
    email="valentyn.zakharchenko@example.com",
    subject=subject2 
)
teacher13 = Teacher.objects.create(
    first_name="Світлана",
    last_name="Кравчук",
    email="svitlana.kravchuk@example.com",
    subject=subject6
)
teacher14 = Teacher.objects.create(
    first_name="Борис",
    last_name="Ющенко",
    email="borys.yushchenko@example.com",
    subject=subject6
)
teacher15 = Teacher.objects.create(
    first_name="Леся",
    last_name="Гриценко",
    email="lesia.hrytsenko@example.com",
    subject=subject3 
)
teacher16 = Teacher.objects.create(
    first_name="Микола",
    last_name="Овчаренко",
    email="mykola.ovcharenko@example.com",
    subject=subject8 
)


#Класи
class1 = Class.objects.create(
    name="5-А",
    class_teacher=teacher9
)
class2 = Class.objects.create(
    name="5-Б",
    class_teacher=teacher12
)
class3 = Class.objects.create(
    name="6-А",
    class_teacher=teacher10
)
class4 = Class.objects.create(
    name="6-Б",
    class_teacher=teacher7
)
class5 = Class.objects.create(
    name="7-А",
    class_teacher=teacher11
)
class6 = Class.objects.create(
    name="7-Б",
    class_teacher=teacher8
)
class7 = Class.objects.create(
    name="8-А",
    class_teacher=teacher5
)
class8 = Class.objects.create(
    name="8-Б",
    class_teacher=teacher13
)
class9 = Class.objects.create(
    name="9-А",
    class_teacher=teacher6
)
class10 = Class.objects.create(
    name="9-Б",
    class_teacher=teacher15
)
class11 = Class.objects.create(
    name="10-А",
    class_teacher=teacher4
)
class12 = Class.objects.create(
    name="10-Б",
    class_teacher=teacher3
)
class13 = Class.objects.create(
    name="11-А",
    class_teacher=teacher1
)
class14 = Class.objects.create(
    name="11-Б",
    class_teacher=teacher2
)


#Учні
#Клас 5-А
student1_5a = Student.objects.create(
    first_name="Олена",
    last_name="Іваненко",
    birth_date="2008-05-15",
    email="olena.ivanenko@example.com",
    class_group=class1
)
student2_5a = Student.objects.create(
    first_name="Максим",
    last_name="Петренко",
    birth_date="2008-06-20",
    email="maksym.petrenko@example.com",
    class_group=class1
)
student3_5a = Student.objects.create(
    first_name="Катерина",
    last_name="Сидоренко",
    birth_date="2008-04-10",
    email="kateryna.sydorenko@example.com",
    class_group=class1
)

#Клас 5-Б
student1_5b = Student.objects.create(
    first_name="Ігор",
    last_name="Коваленко",
    birth_date="2008-07-12",
    email="igor.kovalenko@example.com",
    class_group=class2
)
student2_5b = Student.objects.create(
    first_name="Наталя",
    last_name="Литвин",
    birth_date="2008-03-30",
    email="nataliya.lytvyn@example.com",
    class_group=class2
)
student3_5b = Student.objects.create(
    first_name="Дмитро",
    last_name="Гончаренко",
    birth_date="2008-08-05",
    email="dmytro.honcharenko@example.com",
    class_group=class2
)

#Клас 6-А
student1_6a = Student.objects.create(
    first_name="Вікторія",
    last_name="Мельник",
    birth_date="2007-05-22",
    email="viktoriya.melnyk@example.com",
    class_group=class3
)
student2_6a = Student.objects.create(
    first_name="Сергій",
    last_name="Романенко",
    birth_date="2007-06-15",
    email="serhiy.romanenko@example.com",
    class_group=class3
)
student3_6a = Student.objects.create(
    first_name="Оксана",
    last_name="Кравчук",
    birth_date="2007-04-18",
    email="oksana.kravchuk@example.com",
    class_group=class3
)

#Клас 6-Б
student1_6b = Student.objects.create(
    first_name="Тарас",
    last_name="Шевченко",
    birth_date="2007-09-01",
    email="taras.shevchenko@example.com",
    class_group=class4
)
student2_6b = Student.objects.create(
    first_name="Лариса",
    last_name="Бондаренко",
    birth_date="2007-03-10",
    email="larysa.bondarenko@example.com",
    class_group=class4
)
student3_6b = Student.objects.create(
    first_name="Андрій",
    last_name="Олійник",
    birth_date="2007-05-05",
    email="andriy.oliynyk@example.com",
    class_group=class4
)

#Клас 7-А
student1_7a = Student.objects.create(
    first_name="Ірина",
    last_name="Демченко",
    birth_date="2006-06-17",
    email="iryna.demchenko@example.com",
    class_group=class5
)
student2_7a = Student.objects.create(
    first_name="Михайло",
    last_name="Захарченко",
    birth_date="2006-07-29",
    email="mykhailo.zakharchenko@example.com",
    class_group=class5
)
student3_7a = Student.objects.create(
    first_name="Ольга",
    last_name="Ковальчук",
    birth_date="2006-08-03",
    email="olha.kovalchuk@example.com",
    class_group=class5
)

#Клас 7-Б
student1_7b = Student.objects.create(
    first_name="Володимир",
    last_name="Гнатенко",
    birth_date="2006-04-23",
    email="volodymyr.hnatenko@example.com",
    class_group=class6
)
student2_7b = Student.objects.create(
    first_name="Світлана",
    last_name="Павленко",
    birth_date="2006-09-11",
    email="svitlana.pavlenko@example.com",
    class_group=class6
)
student3_7b = Student.objects.create(
    first_name="Юрій",
    last_name="Ткаченко",
    birth_date="2006-05-30",
    email="yuriy.tkachenko@example.com",
    class_group=class6
)

#Клас 8-А
student1_8a = Student.objects.create(
    first_name="Анастасія",
    last_name="Мороз",
    birth_date="2005-04-12",
    email="anastasiya.moroz@example.com",
    class_group=class7
)
student2_8a = Student.objects.create(
    first_name="Павло",
    last_name="Козак",
    birth_date="2005-08-25",
    email="pavlo.kozak@example.com",
    class_group=class7
)
student3_8a = Student.objects.create(
    first_name="Інна",
    last_name="Дорошенко",
    birth_date="2005-06-30",
    email="inna.doroshenko@example.com",
    class_group=class7
)

#Клас 8-Б
student1_8b = Student.objects.create(
    first_name="Віктор",
    last_name="Романюк",
    birth_date="2005-05-17",
    email="viktor.romanyuk@example.com",
    class_group=class8
)
student2_8b = Student.objects.create(
    first_name="Оксана",
    last_name="Гришина",
    birth_date="2005-07-19",
    email="oksana.hryshyna@example.com",
    class_group=class8
)
student3_8b = Student.objects.create(
    first_name="Євген",
    last_name="Терещенко",
    birth_date="2005-03-28",
    email="yevhen.tereshchenko@example.com",
    class_group=class8
)

#Клас 9-А
student1_9a = Student.objects.create(
    first_name="Марина",
    last_name="Лебедєва",
    birth_date="2004-02-10",
    email="maryna.lebedieva@example.com",
    class_group=class9
)
student2_9a = Student.objects.create(
    first_name="Ілля",
    last_name="Кравченко",
    birth_date="2004-11-05",
    email="illya.kravchenko@example.com",
    class_group=class9
)
student3_9a = Student.objects.create(
    first_name="Світлана",
    last_name="Петренко",
    birth_date="2004-07-22",
    email="svitlana.petrenko@example.com",
    class_group=class9
)

#Клас 9-Б
student1_9b = Student.objects.create(
    first_name="Андрій",
    last_name="Соколов",
    birth_date="2004-09-14",
    email="andriy.sokolov@example.com",
    class_group=class10
)
student2_9b = Student.objects.create(
    first_name="Юлія",
    last_name="Демченко",
    birth_date="2004-06-18",
    email="yuliya.demchenko@example.com",
    class_group=class10
)
student3_9b = Student.objects.create(
    first_name="Олег",
    last_name="Мельник",
    birth_date="2004-12-02",
    email="oleh.melnyk@example.com",
    class_group=class10
)

#Клас 10-А
student1_10a = Student.objects.create(
    first_name="Наталія",
    last_name="Ткачук",
    birth_date="2003-01-25",
    email="nataliya.tkachuk@example.com",
    class_group=class11
)
student2_10a = Student.objects.create(
    first_name="Володимир",
    last_name="Ковальчук",
    birth_date="2003-03-17",
    email="volodymyr.kovalchuk@example.com",
    class_group=class11
)
student3_10a = Student.objects.create(
    first_name="Оксана",
    last_name="Шевченко",
    birth_date="2003-05-05",
    email="oksana.shevchenko@example.com",
    class_group=class11
)

#Клас 10-Б
student1_10b = Student.objects.create(
    first_name="Тетяна",
    last_name="Романенко",
    birth_date="2003-02-12",
    email="tetiana.romanenko@example.com",
    class_group=class12
)
student2_10b = Student.objects.create(
    first_name="Микола",
    last_name="Захарченко",
    birth_date="2003-04-28",
    email="mykola.zakharchenko@example.com",
    class_group=class12
)
student3_10b = Student.objects.create(
    first_name="Світлана",
    last_name="Бондаренко",
    birth_date="2003-06-19",
    email="svitlana.bondarenko@example.com",
    class_group=class12
)

#Клас 11-А
student1_11a = Student.objects.create(
    first_name="Іван",
    last_name="Петренко",
    birth_date="2002-03-03",
    email="ivan.petrenko@example.com",
    class_group=class13
)
student2_11a = Student.objects.create(
    first_name="Олена",
    last_name="Ковальчук",
    birth_date="2002-07-14",
    email="olena.kovalchuk@example.com",
    class_group=class13
)
student3_11a = Student.objects.create(
    first_name="Дмитро",
    last_name="Сидоренко",
    birth_date="2002-05-21",
    email="dmytro.sydorenko@example.com",
    class_group=class13
)

#Клас 11-Б
student1_11b = Student.objects.create(
    first_name="Оксана",
    last_name="Шевченко",
    birth_date="2002-01-15",
    email="oksana.shevchenko@example.com",
    class_group=class14
)
student2_11b = Student.objects.create(
    first_name="Юрій",
    last_name="Ткаченко",
    birth_date="2002-09-30",
    email="yuriy.tkachenko@example.com",
    class_group=class14
)
student3_11b = Student.objects.create(
    first_name="Марина",
    last_name="Гончар",
    birth_date="2002-06-12",
    email="marina.honchar@example.com",
    class_group=class14
)

#Генерація розкладу уроків
weekdays = ["mon", "tue", "wed", "thu", "fri"]

times = [
    ("08:30", "09:15"),
    ("09:25", "10:10"),
    ("10:20", "11:05"),
    ("11:15", "12:00"),
    ("12:10", "12:55"),
    ("13:05", "13:50"),
    ("14:00", "14:45"),
    ("14:55", "15:40"),
]

class_pairs = [
    (class1, class2), 
    (class3, class4),
    (class5, class6),
    (class7, class8),
    (class9, class10),
    (class11, class12),
    (class13, class14),
]

subject_teachers = {}
all_teachers = Teacher.objects.all()
for teacher in all_teachers:
    subject_teachers.setdefault(teacher.subject.id, []).append(teacher)

for class_a, class_b in class_pairs:
    used_slots = set() 

    for _ in range(8):
        subject = random.choice(Subject.objects.all())
        teacher = random.choice(subject_teachers[subject.id])
        weekday = random.choice(weekdays)
        time_slot = random.choice(times)

        while (weekday, time_slot[0]) in used_slots:
            weekday = random.choice(weekdays)
            time_slot = random.choice(times)

        used_slots.add((weekday, time_slot[0]))

        for class_group in [class_a, class_b]:
            Schedule.objects.create(
                class_group=class_group,
                subject=subject,
                teacher=teacher,
                weekday=weekday,
                start_time=time_slot[0],
                end_time=time_slot[1]
            )



#Геренація оцінок
weekdays = ["mon", "tue", "wed", "thu", "fri"]

subject_teachers = {}
for teacher in Teacher.objects.all():
    subject_teachers.setdefault(teacher.subject.id, []).append(teacher)

all_subjects = list(Subject.objects.all())

all_students = Student.objects.all()

for student in all_students:
    random_subjects = random.sample(all_subjects, 3)

    for subject in random_subjects:
        teacher = random.choice(subject_teachers[subject.id])
        weekday = random.choice(weekdays)
        grade_value = random.randint(8, 12)

        Grade.objects.create(
            student=student,
            teacher=teacher,
            subject=subject,
            weekday=weekday,
            grade=grade_value
        )