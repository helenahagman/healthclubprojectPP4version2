from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Contact, Booking, Profile, MemberComment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name_contact', 'email', 'contact_message']
            

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['session', 'name', 'phonenumber', 'email', 'age', 'gender', 'message', 'time']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number']
    
    # def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required information')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class MemberCommentForm(forms.ModelForm):
    class Meta:
        model = MemberComment
        fields = ['comment', 'photo']