from django.shortcuts import render

# Create your views here.
def add_numbers(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        result = num1 + num2
    else:
        result = None

    return render(request, 'index.html', {'result': result})



def add_name(request):
    if request.method == 'POST':
        nom = request.POST.get('nom', '')
        prenom = request.POST.get('prenom', '')
        data = {'nom': nom, 'prenom': prenom}
    else:
        data = None

    return render(request, 'add_name.html', {'data': data})


from .models import CalculatedResult

def add_numbers2(request):

    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        result = num1 + num2

        # Enregistrer les valeurs dans la base de données
        CalculatedResult.objects.create(
            num1=num1,
            num2=num2,
            result=result
        )

    # Récupérer l'historique des calculs depuis la base de données
    history = CalculatedResult.objects.all().order_by('-id')

    return render(request, 'index2.html', {'history': history, 'result': result})

