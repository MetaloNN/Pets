from django.shortcuts import render
from PetRegistry.models import Pet

# Create your views here.


def index(request):
    #en el [x] por ahora asignamos el objeto que necesitamos traer
    #pepes = vars(Pet.objects.all()[1])

    pepes = Pet.objects.all()
    
    

    return render(request, 'base.html', {'pepes' : pepes})
   


