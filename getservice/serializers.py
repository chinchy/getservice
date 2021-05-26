from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

__all__ = (
    'ClientSerializer',
    'CreateClientSerializer',
    'CompanySerializer',
    'CreateCompanySerializer',
    'OfficeSerializer',
    'CreateOfficeSerializer',
    'PositionSerializer',
    'CreatePositionSerializer',
    'EmployeeSerializer',
    'CreateEmployeeSerializer',
    'ServiceSerializer',
    'CreateServiceSerializer',
    'PriceSerializer',
    'CreatePriceSerializer',
    'EntrySerializer',
    'CreateEntrySerializer'
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = '__all__'


class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = Company
        fields = '__all__'


class CreateCompanySerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = Company
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Office
        fields = '__all__'


class CreateOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Position
        fields = '__all__'


class CreatePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    office = OfficeSerializer()
    position = PositionSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = '__all__'


class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only=True, many=True)

    class Meta:
        model = Service
        fields = '__all__'


class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    service = ServiceSerializer()

    class Meta:
        model = Price
        fields = '__all__'


class CreatePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    employee = EmployeeSerializer()
    service = ServiceSerializer()
    office = OfficeSerializer()

    class Meta:
        model = Entry
        fields = '__all__'


class CreateEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
