from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from wsb_python.settings import BASE_DIR
# Create your views here.

def info(request):
    data = {
            'info': 'Poniżej przedsatawione są endpointy do różnyuch zadań',
            'algorytm z wykorzystaniem stosu': 'https://michaldev.pythonanywhere.com/stos',
            'algorytm z wykorzystaniem kolejki': 'https://michaldev.pythonanywhere.com/kolejka',
            'program z tablicą hasującą': 'https://michaldev.pythonanywhere.com/tablica',
            'algorytm grafowy': 'https://michaldev.pythonanywhere.com/graf',
            'dziel i zwyciężaj': 'https://michaldev.pythonanywhere.com/dziel-zwyciezaj',
            'palindrom': 'https://michaldev.pythonanywhere.com/pali',
            'rekurencja': 'https://michaldev.pythonanywhere.com/reku',
            'singleton': 'https://michaldev.pythonanywhere.com/singleton',
            'adapter': 'https://michaldev.pythonanywhere.com/adapter',

            }
    return JsonResponse(data)

def stos(request):
    json_path = BASE_DIR / 'wsb_python_app' / 'json_files' / 'stos.json'
    with open(json_path, 'r') as file:
        data = json.load(file)

    return JsonResponse(data)

def kolejka(request):
    json_path = BASE_DIR / 'wsb_python_app' / 'json_files' / 'kolejka.json'
    with open(json_path, 'r') as file:
        data = json.load(file)

    return JsonResponse(data)

def tablica(request):
    json_path = BASE_DIR / 'wsb_python_app' / 'json_files' / 'tablica.json'
    with open(json_path, 'r') as file:
        data = json.load(file)

    return JsonResponse(data)

def graf(request):
    json_path = BASE_DIR / 'wsb_python_app' / 'json_files' / 'graf.json'
    with open(json_path, 'r') as file:
        data = json.load(file)

    return JsonResponse(data)

def dziel_zwyciezaj(request):
    json_path = BASE_DIR / 'wsb_python_app' / 'json_files' / 'dziel_zwyciezaj.json'
    with open(json_path, 'r') as file:
        data = json.load(file)

    return JsonResponse(data)

def pali(request):
    json_path = BASE_DIR / 'wsb_python_app' / 'json_files' / 'pali.json'
    with open(json_path, 'r') as file:
        data = json.load(file)

    return JsonResponse(data)

def reku(request):
    json_path = BASE_DIR / 'wsb_python_app' / 'json_files' / 'reku.json'
    with open(json_path, 'r') as file:
        data = json.load(file)

    return JsonResponse(data)

def singleton(request):
    json_path = BASE_DIR / 'wsb_python_app' / 'json_files' / 'singleton.json'
    with open(json_path, 'r') as file:
        data = json.load(file)

    return JsonResponse(data)

def adapter(request):
    json_path = BASE_DIR / 'wsb_python_app' / 'json_files' / 'adapter.json'
    with open(json_path, 'r') as file:
        data = json.load(file)

    return JsonResponse(data)