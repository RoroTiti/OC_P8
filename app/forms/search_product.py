from django import forms


class SearchProductForm(forms.Form):
    search_term = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Rechercher un produit...",
            "class": "input is-rounded"
        })
    )
