from django.shortcuts import render
from enquetes.models import Enquete

def bemvindo(request):
    return render(request, 'bemvindo.html')

def enquete(request, enquete_id):
<<<<<<< HEAD
    enquete = Enquete.objects.get(id=enquete_id)
    return render(request, 'enquete.html', {"enquete" : enquete,})
=======
    enquete = Enquete()

    if enquete_id == 1:
        enquete = Enquete(1, 'É preciso realmente aprender lógica de programação?', '28/08/2020')
    if enquete_id == 2:
        enquete = Enquete(2, 'Quais áreas de TI tem retorno financeiro mais rápido?', '29/08/2020')
    if enquete_id == 3:
        enquete = Enquete(3, 'Qual linguagem é mais fácil: JAVA, PHP ou C#?', '30/08/2020')

    return render(request, 'enquete.html', {"enquete" : enquete})
>>>>>>> cd6b625126045f08e37d2286676344a497cc9ab1
