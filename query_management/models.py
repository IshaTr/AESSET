import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class TimeSlot(models.Model):
    slot_id = models.UUIDField(editable=False, default=uuid.uuid4,
                               primary_key=True)
    date = models.DateField()
    start = models.TimeField()
    finish = models.TimeField()
    count = models.IntegerField()

    def __str__(self):
        return str(self.slot_id)


class Query(models.Model):
    student = models.IntegerField(blank=False, primary_key=True)
    query_type = models.CharField(max_length=240, default='Exam')
    email = models.CharField(max_length=48, db_index=True)
    phone = PhoneNumberField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    modified_at = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return str(self.student)

    class Meta:
        verbose_name_plural = 'Queries'


class Token(models.Model):
    slot = models.OneToOneField(TimeSlot)
    student_id = models.OneToOneField(Query)
    token = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.token)
