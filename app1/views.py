from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView




# Create your views here.
def v_add_numbers(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        result = num1 + num2
    else:
        result = None

    return render(request, 'index.html', {'result': result})


from .models import CalculatedResult


def v_add_numbers2(request):
    result = None  # Définir la variable result en dehors de la logique de POST

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

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Etudiant
from .forms import EtudiantForm

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'liste_etudiants.html', {'etudiants': etudiants})




def ajouter_etudiant(request):
    if request.method == 'POST':
        # hna declarina form li drtha f forms.py 
        form = EtudiantForm(request.POST)
        # hna condition ida dkhl les information s7a7 
        if form.is_valid():
            #ida kan kolch swaswa ndiro save donc django howa ydir test 
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    
    # Modification : Récupérer les erreurs du formulaire
    #hna nbrtto error ida ghlt l html 
    errors = form.errors.as_data()

    return render(request, 'ajouter_etudiant.html', {'form': form, 'errors': errors})








def modifier_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'modifier_etudiant.html', {'form': form})


def supprimer_etudiant(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'confirmer_suppression.html', {'etudiant': etudiant})
