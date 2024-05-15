from django.shortcuts import render
from .forms import ContactForm
# Header and footer view 

def index(request):
    return render(request,'index.html')
def ao(request):
    return render(request,'ao.html')
def contact(request):
    return render(request,'contact.html')
def reglements(request):
    return render(request,'reglements.html')
def false(request):
    return render(request,'false.html')
def marches(request):
    return render(request,'marches.html')
def demarches(request):
    return render(request,'demarches.html')
def investissement(request):
    return render(request,'investissement.html')
def doc(request):
    return render(request,'doc.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data here
            type_of_request = form.cleaned_data['type_of_request']
            company_name = form.cleaned_data['company_name']
            industry = form.cleaned_data['industry']
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            observations = form.cleaned_data['observations']
            # Add your processing logic here
            # For example, you can print the data to the console:
            print(f"Type of Request: {type_of_request}, Company Name: {company_name}, Industry: {industry}, Full Name: {full_name}, Phone Number: {phone_number}, Email: {email}, Observations: {observations}")
            # You can also redirect to a success page or render a thank you message
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})