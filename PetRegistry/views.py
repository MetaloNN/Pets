from django.shortcuts import render
from PetRegistry.models import Pet

# Create your views here.


def index(request):

    pepes = vars(Pet.objects.all()[1])
    

    return render(request, 'base.html', {'pepes' : pepes})
    #return render(request, 'base.html', print(pepes))


