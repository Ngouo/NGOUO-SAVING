from django.shortcuts import render, redirect
from .models import Saving, SoldeGlobal
from .form import SavingForm
from .utils import notification
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    solde = SoldeGlobal.objects.first()
    savings = Saving.objects.all().order_by('-date_ajout')
    context = {
        'montant_total': solde.montant_total,
        'savings': savings,
    }
    return render(request, 'Saving/home.html', context)

@login_required(login_url='login')
def operation(request):
    if request.method == 'POST':
        form = SavingForm(request.POST)
        if form.is_valid():
            saving = form.save()            

            solde, _ = SoldeGlobal.objects.get_or_create(id=1)

            if saving.type_operation == 'DEPOT':
                solde.montant_total += saving.montant

            if saving.type_operation == 'RETRAIT':
                solde.montant_total -= saving.montant
            if saving.type_operation == 'RETRAIT' and solde.montant_total < saving.montant:
                form.add_error('montant', 'Solde insuffisant pour effectuer ce retrait.')
                return render(request, 'Saving/depot.html', {'form': form})


            solde.save()
            try:
                notification(
                    subject="Nouvelle opération enregistrée",
                    message=f"Une nouvelle opération a été enregistrée. Veuillez consulter la plateforme pour plus d'informations."
                )
            except Exception as e:
                messages.warning(request, f"Opération enregistrée, mais l'envoi du mail a échoué : {str(e)}")

            messages.success(request, "Opération enregistrée avec succès.")


            return redirect('home')
        
    else :
        form = SavingForm()

    return render(request, 'Saving/depot.html', {"form": form})
