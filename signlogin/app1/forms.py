from django import forms
from .models import Bin
class Binform(forms.ModelForm):
    class Meta:
        model = Bin
        fields = [
            "Bin_id",
            "Bin_location",
            "Bin_capacity",
        ]