from django.db import models
from django.db.models import ManyToManyField
from django.utils import timezone
#from .widgets import ContactSelectMultiple

class Company(models.Model):
    name = models.TextField()
    address = models.TextField(null=True, blank=True)
    description = models.TextField(max_length=25, null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    mapurl = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.address}'

class Role(models.Model):
    name = models.TextField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, default=None)  # Provide a default value here
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.company}'
        
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=25, null=True, blank=True)
    lname = models.CharField(max_length=25, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    role = ManyToManyField(Role,related_name='contacts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["lname","fname"]

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.lname}, {self.fname} - {self.role}'

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        super(Note, self).save(*args, **kwargs)

class Job(models.Model):
    STATUS_CHOICES = [
        ("0", "Expressed Interest"),
        ("1", "Applied"),
        ("2", "Interviewing"),
        ("3", "Pending Offer"),
        ("4", "Rejection Received"),
        ("5", "Withdrawn"),
    ]
    LOCATION_CHOICES = [
        ("0", "Unknown"),
        ("1", "Office"),
        ("2", "Hybrid"),
        ("3", "Remote"),
    ]
    TRAVEL_CHOICES = [
        ("0", "Unknown"),
        ("1", "None"),
        ("2", "Low"),
        ("3", "Medium"),
        ("4", "High"),
    ]
    PRIORITY_CHOICES = [
        ("0", "Unknown"),
        ("1", "Low"),
        ("2", "Medium"),
        ("3", "High"),
        ("4", "Critical"),
    ]
    COMP_CHOICES = [
        ("0", "Unknown"),
        ("1", "Low"),
        ("2", "Medium"),
        ("3", "High"),
    ]
    QUAL_CHOICES = [
        ("0", "Unknown"),
        ("1", "Comfortable"),
        ("2", "Challenged"),
        ("3", "Stretching"),
    ]
    
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    url = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    contacts = ManyToManyField(Contact, related_name='jobs') #, widget=ContactSelectMultiple)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='0')
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='0')
    travel = models.CharField(max_length=50, choices=TRAVEL_CHOICES, default='0')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='0')
    compensation = models.CharField(max_length=50, choices=COMP_CHOICES, default='0')
    qualifications = models.CharField(max_length=50, choices=QUAL_CHOICES, default='0')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(Job, self).save(*args, **kwargs)

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        super(Log, self).save(*args, **kwargs)

