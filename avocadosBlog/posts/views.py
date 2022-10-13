from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse

class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Pablo Cabrera Castrejon',
            'years': 24,
            'codes': ['Javascript', 'Typescript', 'Python']
        }
        return render(request, 'hello_world.html', context=data)
