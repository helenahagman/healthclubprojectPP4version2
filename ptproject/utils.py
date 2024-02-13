import random
from django.utils import timezone
from django.core.exceptions import ValidationError
from django import forms


def num_validation(num):
    if not num. isdigit():
        raise ValidationError('Only numbers are allowed in this field')


def alpha_only(value):
    if not value.isalpha():
        raise ValidationError('Only alphabetic characters are allowed in this field')


def date_validation(date):
    if date < timezone.now().date():
        raise forms.ValidationError('You can only choose dates in the future')