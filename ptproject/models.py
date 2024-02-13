from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from ptproject.utils import num_validation, alpha_only


STATUS = ((0, "Draft"), (1, "Published"))

def get_default_session():
    session = Session.objects.first()
    if not session:
        pass
    return session


class Session(models.Model):
    trainer_name = models.CharField(max_length=100)
    session_type = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    booked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.session_type} with {self.trainer_name} on {self.date} from {self.start_time} to {self.end_time}"


class Booking(models.Model):
    """
    Create a booking request form
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=get_default_session, null=True)
    name = models.CharField(max_length=100, default='State your name')
    phonenumber = models.CharField(max_length=15, default='1234567890')
    email = models.EmailField(max_length=70, default='your@mail.com')
    age = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    gender = models.CharField(
        choices=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        default='male'
    )
    message = models.TextField(max_length=300, default='')
    date = models.DateField()
    time = models.TimeField()
    approved = models.BooleanField(default=False)

    TIME_CHOICES = [
        ('AM', 'Before Noon'),
        ('PM', 'After Noon'),
    ]
    time = models.CharField(max_length=2, choices=TIME_CHOICES, default='AM')

    
    def __str__(self):
        return f'Booking by {self.user.username} for session {self.session.session_type} on {self.session.date}'


class Contact(models.Model):
    """
    Model for contact messages.

    """

    name_contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, default='default@example.com')
    contact_message = models.TextField(max_length=400, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'Contact message submitted by {self.name_contact} on {self.created_on}'


class Profile(models.Model):
    """
    User profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=70, default='default@example.com')
    phone_number = models.CharField(max_length=20, null=True, blank=True, validators=[num_validation])
    first_name = models.CharField(max_length=50, null=True, blank=True, validators=[alpha_only])
    last_name = models.CharField(max_length=50, null=True, blank=True, validators=[alpha_only])
    password = models.CharField(max_length=128, null=True, blank=True)


    def __str__(self):
        return f'{self.user} profile'


class MemberComment(models.Model):
    """
    Member comments
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    photo = models.ImageField(upload_to='member_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
