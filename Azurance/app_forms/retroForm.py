from django import forms
import datetime as DtT

cities = (
    ("paris", "Paris"),
    ("nantes", "Nantes"),
    ("nice", "Nice"),
    ("monaco", "Monaco"),
    ("strasbourg", "Strasbourg"),
    ("brest", "Brest"),
    ("ajaccio", "Ajaccio"),
    ("laon", "Laon"),
    ("calais", "Calais"),
    ("aubusson", "Aubusson")
)


class RetroForm(forms.Form):
    clientName = forms.CharField(label="Nom de l'entreprise", max_length=100)
    clientName.widget.attrs.update({'class': 'form-control'})

    dailyMaxTurnover = forms.FloatField(label="Chiffre d'affaire journalier maximum")
    dailyMaxTurnover.widget.attrs.update({'class': 'form-control'})

    fixedCosts = forms.FloatField(label="Coûts fixes journalier")
    fixedCosts.widget.attrs.update({'class': 'form-control'})

    rainfall = forms.FloatField(label="Niveau de pluie journalier pivot. (mm)")
    rainfall.widget.attrs.update({'class': 'form-control'})

    subscriptionDate = forms.CharField(label="Année rétrospective", max_length=4)
    subscriptionDate.widget.attrs.update({'class': 'form-control'})

    location = forms.ChoiceField(label="Ville", choices=cities)
    location.widget.attrs.update({'class': 'form-control'})

    printPDF = forms.ChoiceField(label="Obtenir devies en pdf", choices=(("Non", "Non"), ("Oui", "Oui")))
    printPDF.widget.attrs.update({'class': 'form-control'})
