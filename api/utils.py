from api import models as api_models
from django.db.models import Q


def get_start_stop_indexes(limit, offset):

    return offset*limit + limit, offset*limit + 2*limit

def get_search_results_for_search_query(search_field_value, limit=10, offset=0):

    start, stop = get_start_stop_indexes(limit, offset)

    if not search_field_value:
        return api_models.Bank.objects.all()[start:stop]

    q_obj = Q()
    for field, value in search_field_value.items():

        q_obj |= Q(**{'{}__icontains'.format(field): value})

    return api_models.Bank.objects.filter(q_obj)[start:stop]
