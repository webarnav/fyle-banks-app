from django.db import models


class Bank(models.Model):

    ifsc = models.CharField(unique=True, max_length=255)
    bank_id = models.IntegerField(primary_key=True)
    branch = models.CharField(max_length=255)
    address =  models.TextField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ifsc']

    def __str__(self):
        return '{] {}'.format(self.ifsc, self.branch)

    def get_searchable_fields(self):
        return ['ifsc', 'branch', 'city', 'district', 'state', 'address']

