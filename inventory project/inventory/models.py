from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify

# Create your models here.


class Inventories (models.Model):
    STATUS_CHOICES = (
        ('', 'Select Equipment Status'),
        ('Inactive','Inactive'),
        ('Active','Active'),        
        ('Faulty','Faulty'),
    )
    manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,)
    seq_number = models.CharField(max_length=10)
    equipment_name = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=30)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    entry = models.DateTimeField(default=timezone.now)
    tag_number = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Select Equipment Status')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-entry',)
    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.equipment_name, self.id)

    def get_absolute_url(self):
        return reverse('details',
                        args=[
                              self.entry.year,
                              self.entry.month,
                              self.entry.day, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.equipment_name)
        super(Inventories, self).save(*args, **kwargs)
