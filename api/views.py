from django.http import response as django_response
from rest_framework import views as rest_views
from rest_framework import status as rf_status
from api import utils as api_utils
from api import serializers as api_serializers

# Endpoint: /api/branches/autocomplete?q=<>
# Example: /api/branches/autocomplete?q=RTGS&limit=3&offset=0
# Sample response:

# class PaginationMixin(object):
#     pagination_class = None
#     _paginator = None
#
#     def paginate(self, records, request):
#         self._paginator = self.pagination_class()
#         result_page = self._paginator.paginate_queryset(records, request)
#         return result_page
#
#     def get_paginated_response(self, data):
#         return self._paginator.get_paginated_response(data)
#
#
# class StandardPaginatedView(PaginationMixin):
#     pagination_class = api_paginators.StandardResultsSetPagination
#

class SerializationMixin(object):
    serializer_class = None

    def get_serialized_data(self, records, request):
        return self.serializer_class(records, many=True, context={'request': request})


class BaseSearchAPI(rest_views.APIView, SerializationMixin):

    def get(self, request, *args, **kwargs):

        submitted_data = request.GET

        search_term = submitted_data.get('q')
        limit = submitted_data.get('limit', 10)
        offset = submitted_data.get('offset', 0)

        records = self.get_results(search_term, limit, offset)

        serializer = self.serializer_class(records, many=True, context={'request': request})
        return django_response.JsonResponse(serializer.data, status=rf_status.HTTP_200_OK)

    def get_results(self, *args, **kwargs):
        raise NotImplementedError


class Branches(BaseSearchAPI):
    serializer_class = api_serializers.BranchInfoSerializer

    @property
    def searchable_fields(self):
        return ['ifsc', 'branch', 'city', 'district', 'state', 'address']

    def get_results(self, search_term, limit, offset, **kwargs):
        query = {i: search_term for i in self.searchable_fields}
        return api_utils.get_search_results_for_search_query(query, limit=limit, offset=offset)

class BranchAutocomplete(BaseSearchAPI):

    def get_results(self, search_term, limit, offset, **kwargs):
        query = {'branch': search_term}

        return api_utils.get_search_results_for_search_query(query, limit=limit, offset=offset)
