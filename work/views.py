from django.shortcuts import render

from rest_framework import generics, viewsets
from .serializers import BranchSerializer, EmployeesSerializer
from .models import Branch, Employees


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer



class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer




