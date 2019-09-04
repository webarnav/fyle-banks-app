from django.db import models


class Bank(models.Model):

    ifsc = models.CharField(unique=True)
    bank_id = models.IntegerField(primary_key=True)
    branch = models.CharField(required=True)
    address =  models.TextField()
    city = models.CharField()
    district = models.CharField()
    state = models.CharField()

    created_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ifsc']

    def __str__(self):
        return '{] {}'.format(self.ifsc, self.branch)

    def get_searchable_fields(self):
        return ['ifsc', 'branch', 'city', 'district', 'state', 'address']

