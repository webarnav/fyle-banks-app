import csv
from api import models as api_models


def populate_data(csv_file_path):

    fields = ['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name']

    with open(csv_file_path, 'r')as f:

      data = csv.reader(f)

      for row in data:
            row_data = {fields[index]: val for index, val in enumerate(row)}
            api_models.Bank.objects.create(row_data)

