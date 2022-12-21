class Department(models.Model):

    title = models.CharField(max_length=255)
    photo = VersatileImageField("Image", upload_to="department/", blank=True, null=True)

    def __str__(self):
        return self.title


class DepartmentDivision(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
        
class DepartmentDivisionTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.department1 = Department.objects.create(title="Mechanical Engineering")
        self.department2 = Department.objects.create(title="Computer Science")
        self.department3 = Department.objects.create(
            title="Applied Electronics and Instrumentation",
        )
        self.division1 = DepartmentDivision.objects.create(
            title="A", department=self.department1
        )
        self.division2 = DepartmentDivision.objects.create(
            title="B", department=self.department2
        )
        self.division3 = DepartmentDivision.objects.create(
            title="A", department=self.department3
        )

    def test_str(self):
        """Test the string representation of the model."""
        self.assertEqual(str(self.division1), self.division1.title)
        self.assertEqual(str(self.division2), self.division2.title)
        self.assertEqual(str(self.division3), self.division3.title)


# -------<<< Test Case Related :---->

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Test Views <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from academic.models import Department, DepartmentDivision, Semester
from core.models import TimeSlot
from faculty.models import Faculty, Message, Timetable
from users.models import User

class FacultyTests(APITestCase):

    list_url = reverse("faculty-list")

    def setUp(self):
        self.admin_credentials = {"username": "admin", "password": "admin"}
        self.user_credentials = {"username": "user", "password": "user"}

        self.admin = User.objects.create_superuser(**self.admin_credentials)
        self.user = User.objects.create_user(**self.user_credentials)

        user = User(username="test", mailto:email="test@gmail.com")
        user.save()
        self.first_post = Faculty.objects.create(
            user_id=user.id,
            name="tester",
            faculty_id="unk",
            joined_year="1111-11-11",
            blood_group="B+",
            gender="male",
            date_of_birth="1111-11-11",
            address="text",
        )

        self.valid_post = {
            "user": user.id,
            "name": "tester",
            "faculty_id": "testern",
            "joined_year": "1111-11-11",
            "blood_group": "B+",
            "gender": "male",
            "date_of_birth": "1111-11-11",
            "address": "text",
        }

    def test_admin_faculty_get(self):
        self.client.login(**self.user_credentials)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_faculty_get(self):
        self.client.login(**self.admin_credentials)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_faculty_post(self):
        self.client.login(**self.admin_credentials)

        a = Faculty.objects.get(user_id=self.valid_post["user"])
        a.delete()
        response = self.client.post(self.list_url, data=self.valid_post, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_faculty_update_put(self):
        self.client.login(**self.admin_credentials)

        response = self.client.put(
            reverse("faculty-detail", kwargs={"pk": self.first_post.pk}),
            data=json.dumps(self.valid_post),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_faculty_delete(self):
        self.client.login(**self.admin_credentials)

        response = self.client.delete(
            reverse("faculty-detail", kwargs={"pk": self.first_post.pk}),
            data=json.dumps(self.valid_post),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        
        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Test Models <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<       


from django.test import TestCase

from academic.models import Department, DepartmentDivision, Semester
from core.models import TimeSlot
from faculty.models import Faculty, Message, Timetable
from users.models import User

class Faculty_Test(TestCase):
    def test_faculty_model(self):
        user = User(username="unknow", mailto:email="unknow@gmail.com")
        user.set_password("password12!")
        user.save()
        faculty = Faculty()
        faculty = Faculty(
            user=user,
            name="unknow",
            faculty_id="tester",
            joined_year="1111-11-11",
            blood_group="B+",
            gender="male",
            date_of_birth="1111-11-11",
            address="text",
        )
        faculty.save()
        self.assertEqual(str(faculty), "unknow")

class Message_Test(TestCase):
    def setUp(self):
        self.admin_credentials = {"username": "admin", "password": "admin"}
        self.user_credentials = {"username": "user", "password": "user"}

        self.admin = User.objects.create_superuser(**self.admin_credentials)
        self.user = User.objects.create_user(**self.user_credentials)

        self.faculty = Faculty.objects.create(
            user_id=self.admin.id,
            name="tester",
            faculty_id="tester",
            joined_year="1111-11-11",
            blood_group="B+",
            gender="male",
            date_of_birth="1111-11-11",
            address="text",
        )
        self.message = Message.objects.create(
            faculty_id=self.faculty.id,
            message="hello",
        )

    def test_str(self):
        self.assertEqual(str(self.message), self.message.message)

class TimetableTestCase(TestCase):
    def setUp(self):

        self.admin_credentials = {"username": "admin", "password": "admin"}
        self.user_credentials = {"username": "user", "password": "user"}

        self.admin = User.objects.create_superuser(**self.admin_credentials)
        self.user = User.objects.create_user(**self.user_credentials)

        self.semester = Semester.objects.create(
            title="I", start_date="2010-2-8", end_date="2015-3-3"
        )
        self.department = Department.objects.create(title="Mechanical Engineering")
        self.department_division = DepartmentDivision.objects.create(
            title="A", department=self.department
        )
        self.faculty = Faculty.objects.create(
            user_id=self.admin.id,
            name="tester",
            faculty_id="tester",
            joined_year="1111-11-11",
            blood_group="B+",
            gender="male",
            date_of_birth="1111-11-11",
            address="text",
        )
        self.timeslot = TimeSlot.objects.create(
            start_time="19:24:39", end_time="19:24:40"
        )

        self.timetable = Timetable.objects.create(
            year="2022-12-02",
            day="monday",
            subject="medical",
            semester_id=self.semester.id,
            department_id=self.department.id,
            department_division_id=self.department_division.id,
            faculty_id=self.faculty.id,
            timeslot_id=self.timeslot.id,
        )

    def test_str(self):

        self.assertEqual(str(self.timetable), self.timetable.subject)
        
        
        
        
        
        
        
        
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    role = get_role(user)
    return {
        'refresh': str(refresh)
,
        'access': str(refresh.access_token),
        'user_type': str(role),
    }


def get_role(user):
    if user.is_staff:
        return "admin"
    elif user.is_vendor:
        return "vendor"
