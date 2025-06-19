from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def validate_isbn(value):
    if len(value) != 13:
        raise ValidationError('ISBN must be exactly 13 characters')

def validate_not_future(value):
    if value > date.today():
        raise ValidationError('Published date cannot be in the future')

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(validators=[validate_not_future])
    isbn = models.CharField(max_length=13, validators=[validate_isbn])
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
