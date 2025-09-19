from .models import Saving
from django import forms



class SavingForm(forms.ModelForm):
    class Meta:
        model = Saving
        fields = ['type_operation', 'montant', 'motif']