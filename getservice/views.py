from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


#
# Client views
#
class ClientRetrieveView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


#
# Company views
#
class CompanyRetrieveView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdateView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CreateCompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


#
# Office views
#
class OfficeRetrieveView(generics.RetrieveAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class OfficeUpdateView(generics.UpdateAPIView):
    queryset = Office.objects.all()
    serializer_class = CreateOfficeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class OfficeCreateView(generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class = CreateOfficeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class OfficeListView(generics.ListAPIView):
    serializer_class = OfficeSerializer

    def get_queryset(self):
        queryset = Office.objects.all()

        params = self.request.query_params

        company = params.get('company', None)

        if company:
            queryset = queryset.filter(company=company)

        return queryset


#
# Position views
#
class PositionRetrieveView(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionUpdateView(generics.UpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = CreatePositionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class PositionCreateView(generics.CreateAPIView):
    queryset = Position.objects.all()
    serializer_class = CreatePositionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class PositionListView(generics.ListAPIView):
    serializer_class = PositionSerializer

    def get_queryset(self):
        queryset = Position.objects.all()

        params = self.request.query_params

        company = params.get('company', None)

        if company:
            queryset = queryset.filter(company=company)

        return queryset


#
# Employee views
#
class EmployeeRetrieveView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()

        params = self.request.query_params

        office = params.get('office', None)
        position = params.get('position', None)

        if office:
            queryset = queryset.filter(office=office)

        if position:
            queryset = queryset.filter(position__in=position.split(','))

        return queryset


#
# Service views
#
class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()

        params = self.request.query_params

        office = params.get('office', None)

        if office:
            queryset = queryset.filter(office__in=office.split(','))

        return queryset


#
# Price views
#
class PriceRetrieveView(generics.RetrieveAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceUpdateView(generics.UpdateAPIView):
    queryset = Price.objects.all()
    serializer_class = CreatePriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class PriceCreateView(generics.CreateAPIView):
    queryset = Price.objects.all()
    serializer_class = CreatePriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class PriceListView(generics.ListAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        queryset = Price.objects.all()

        params = self.request.query_params

        position = params.get('position', None)
        service = params.get('service', None)

        if position:
            queryset = queryset.filter(position=position)

        if service:
            queryset = queryset.filter(service=service)

        return queryset


#
# Entry views
#
class EntryRetrieveView(generics.RetrieveAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryUpdateView(generics.UpdateAPIView):
    queryset = Entry.objects.all()
    serializer_class = CreateEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class EntryCreateView(generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = CreateEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class EntryListView(generics.ListAPIView):
    serializer_class = EntrySerializer

    def get_queryset(self):
        queryset = Entry.objects.all()

        params = self.request.query_params

        client = params.get('client', None)
        employee = params.get('employee', None)
        service = params.get('service', None)
        office = params.get('office', None)

        if client:
            queryset = queryset.filter(client=client)

        if employee:
            queryset = queryset.filter(employee=employee)

        if service:
            queryset = queryset.filter(service=service)

        if office:
            queryset = queryset.filter(office=office)

        return queryset
