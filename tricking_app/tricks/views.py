from django.shortcuts import render
from tricks.models import Trick
import requests

# Create your views here.

def index(request):
    get_tricks()
    tricks = Trick.objects.all()
    
    context = {
        'tricks': tricks
    }
    return render(request, 'index.html', context)

def get_tricks():
    """
    data : [statusCode, flash, 
            {data : [classes, origins, tricks]}
                    {tricks: }
    """
    response = requests.get('http://club540.com/api/tricks')
    data = response.json()
    data = data["data"]["tricks"]
    val = 0
    dset = set()
    for trick in data:
        if trick["name"] not in dset:

            val+=1
            name = trick["name"]
            description = trick["description"]
            canPerform = (val % 2 == 0)
            
            dset.add(name)
            #print(name)
        
            curr_trick = Trick(name=name,description=description,canPerform=canPerform)
            curr_trick.save()

def practice(request):
  
    return render(request, 'practice.html')

    



def detail(request, pk):
    trick = Trick.objects.get(pk=pk)
    context = {
        'trick': trick
    }
    return render(request, 'detail.html', context)


