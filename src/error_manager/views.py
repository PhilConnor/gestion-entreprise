from django.shortcuts import render
from django.views.generic.list import ListView

from error_manager.models import ErrorCode


class ErrorCodeListView(ListView):

    model = ErrorCode
