from django.urls import path
from api import views

urlpatterns = [
    path('branches/autocomplete/', views.Branches.as_view()),

    path('branches/', views.BranchAutocomplete.as_view())
]