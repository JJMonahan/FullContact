from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Contact, NoteAssoc, Note, Role, RoleAssoc, Company, Job, Log
from django.contrib.auth.models import User, Group
from .serializers import (
    ContactSerializer, NoteAssocSerializer, NoteSerializer, RoleSerializer,
    RoleAssocSerializer, CompanySerializer, JobSerializer, LogSerializer,
    UserSerializer, GroupSerializer
)

class ContactModelTest(TestCase):
    def test_create_contact(self):
        role = Role.objects.create(name='Manager')
        contact = Contact.objects.create(
            fname='John',
            lname='Doe',
            email='john@example.com',
            phone=123456789,
            role=role,
        )
        self.assertEqual(contact.fname, 'John')

class ContactSerializerTest(APITestCase):
    def test_contact_serializer(self):
        role = Role.objects.create(name='Manager')
        data = {
            'fname': 'John',
            'lname': 'Doe',
            'email': 'john@example.com',
            'phone': 123456789,
            'role': role.id,
        }
        serializer = ContactSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class NoteModelTest(TestCase):
    def test_create_note(self):
        note = Note.objects.create(content='This is a test note')
        self.assertEqual(note.content, 'This is a test note')

class NoteSerializerTest(APITestCase):
    def test_note_serializer(self):
        data = {
            'content': 'This is a test note',
        }
        serializer = NoteSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class RoleModelTest(TestCase):
    def test_create_role(self):
        role = Role.objects.create(name='Manager')
        self.assertEqual(role.name, 'Manager')

class RoleSerializerTest(APITestCase):
    def test_role_serializer(self):
        data = {
            'name': 'Manager',
        }
        serializer = RoleSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class RoleAssocModelTest(TestCase):
    def test_create_role_assoc(self):
        role = Role.objects.create(name='Manager')
        role_assoc = RoleAssoc.objects.create(role=role)
        self.assertEqual(role_assoc.role, role)

class RoleAssocSerializerTest(APITestCase):
    def test_role_assoc_serializer(self):
        role = Role.objects.create(name='Manager')
        data = {
            'role': role.id,
        }
        serializer = RoleAssocSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class CompanyModelTest(TestCase):
    def test_create_company(self):
        company = Company.objects.create(name='Company Inc.', address='123 Main St.', description='Test company')
        self.assertEqual(company.name, 'Company Inc.')

class CompanySerializerTest(APITestCase):
    def test_company_serializer(self):
        data = {
            'name': 'Company Inc.',
            'address': '123 Main St.',
            'description': 'Test company',
        }
        serializer = CompanySerializer(data=data)
        self.assertTrue(serializer.is_valid())

class JobModelTest(TestCase):
    def test_create_job(self):
        job = Job.objects.create(title='Software Developer', description='Test job', url='https://example.com')
        self.assertEqual(job.title, 'Software Developer')

class JobSerializerTest(APITestCase):
    def test_job_serializer(self):
        data = {
            'title': 'Software Developer',
            'description': 'Test job',
            'url': 'https://example.com',
        }
        serializer = JobSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class LogModelTest(TestCase):
    def test_create_log(self):
        log = Log.objects.create(content='This is a test log')
        self.assertEqual(log.content, 'This is a test log')

class LogSerializerTest(APITestCase):
    def test_log_serializer(self):
        data = {
            'content': 'This is a test log',
        }
        serializer = LogSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')

class UserSerializerTest(APITestCase):
    def test_user_serializer(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class GroupModelTest(TestCase):
    def test_create_group(self):
        group = Group.objects.create(name='Test Group')
        self.assertEqual(group.name, 'Test Group')

class GroupSerializerTest(APITestCase):
    def test_group_serializer(self):
        data = {
            'name': 'Test Group',
        }
        serializer = GroupSerializer(data=data)
        self.assertTrue(serializer.is_valid())

# Run your tests using 'python manage.py test your_app_name'
