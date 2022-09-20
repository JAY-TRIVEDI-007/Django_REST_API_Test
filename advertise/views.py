from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def create_ad(request, *args, **kwargs):
    return JsonResponse({'success': True})
