from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def create_car(requests, *args, **kwargs):
    return JsonResponse({'success': True})
