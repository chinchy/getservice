from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('clients/<int:pk>', ClientRetrieveView.as_view()),
    path('clients/update/<int:pk>', ClientUpdateView.as_view()),
    path('clients/new', ClientCreateView.as_view()),
    path('clients/all', ClientListView.as_view()),

    path('companies/<int:pk>', CompanyRetrieveView.as_view()),
    path('companies/update/<int:pk>', CompanyUpdateView.as_view()),

    path('offices/<int:pk>', OfficeRetrieveView.as_view()),
    path('offices/update/<int:pk>', OfficeUpdateView.as_view()),
    path('offices/new', OfficeCreateView.as_view()),
    path('offices/all', OfficeListView.as_view()),

    path('positions/<int:pk>', PositionRetrieveView.as_view()),
    path('positions/update/<int:pk>', PositionUpdateView.as_view()),
    path('positions/new', PositionCreateView.as_view()),
    path('positions/all', PositionListView.as_view()),

    path('employees/<int:pk>', EmployeeRetrieveView.as_view()),
    path('employees/update/<int:pk>', EmployeeUpdateView.as_view()),
    path('employees/new', EmployeeCreateView.as_view()),
    path('employees/all', EmployeeListView.as_view()),

    path('services/<int:pk>', ServiceRetrieveView.as_view()),
    path('services/update/<int:pk>', ServiceUpdateView.as_view()),
    path('services/new', ServiceCreateView.as_view()),
    path('services/all', ServiceListView.as_view()),

    path('prices/<int:pk>', PriceRetrieveView.as_view()),
    path('prices/update/<int:pk>', PriceUpdateView.as_view()),
    path('prices/new', PriceCreateView.as_view()),
    path('prices/all', PriceListView.as_view()),

    path('entries/<int:pk>', EntryRetrieveView.as_view()),
    path('entries/update/<int:pk>', EntryUpdateView.as_view()),
    path('entries/new', EntryCreateView.as_view()),
    path('entries/all', EntryListView.as_view()),
]
