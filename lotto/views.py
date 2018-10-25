from django.shortcuts import render
from .models import GuessNumbers,Location



# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    location = Location.objects.get(id=1)
    return render(request, 'lotto/index.html', {'lottos': lottos,'location':location})
