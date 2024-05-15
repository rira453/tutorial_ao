from django import forms

class ContactForm(forms.Form):
    TYPE_CHOICES = (
        ('info', 'Demande d\'info'),
        ('other', 'Autre demande'),
    )
    type_of_request = forms.ChoiceField(label='Type de demande', choices=TYPE_CHOICES, required=True)
    company_name = forms.CharField(label='Nom de la société', max_length=100, required=True)
    industry = forms.CharField(label='Secteur d\'activité', max_length=100, required=True)
    full_name = forms.CharField(label='Nom/Prénom', max_length=100, required=True)
    phone_number = forms.CharField(label='N° de Téléphone', max_length=20, required=True)
    email = forms.EmailField(label='E-mail', max_length=100, required=True)
    observations = forms.CharField(label='Observations', widget=forms.Textarea, required=True)
