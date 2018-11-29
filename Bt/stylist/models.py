from django.db import models
from enum import Enum
from django.urls import reverse


class Price(models.Model):
    day_session = models.CharField(max_length=250)
    evening_session = models.CharField(max_length=250)
    morning_session = models.CharField(max_length=250)

    def __str__(self):
        return self.day_session


class Timeslot(models.Model):
    SessionStatus = (
        ('FREE', 'free'),
        ('BUSY', 'busy'),
    )

    day = models.CharField(max_length=250, choices=SessionStatus, default='FREE')
    evening = models.CharField(max_length=250, choices=SessionStatus, default='FREE')
    morning = models.CharField(max_length=250, choices=SessionStatus, default='FREE')

    def __str__(self):
        return self.evening


class Freelancer(models.Model):
    StatusType = (
        ('Stylist', 'Stylist'),
        ('Educator', 'Educator'),
    )

    freelancer_name = models.CharField(max_length=250)
    age = models.IntegerField()
    value = models.IntegerField()
    type = models.CharField(max_length=250, choices=StatusType, default='Stylist')
    time_slot_id = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('stylist:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.freelancer_name
