import csv
from django.shortcuts import render, redirect
from .forms import CSVUploadForm
from .models import Lead, Opportunity

def import_leads(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_reader = csv.reader(decoded_file)
            for row in csv_reader:
                name, email = row
                Lead.objects.create(name=name, email=email)
            return redirect('leads:list')
    else:
        form = CSVUploadForm()
    return render(request, 'leads/import_leads.html', {'form': form})

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {'leads': leads})

def mark_contact(request, lead_id):
    lead = Lead.objects.get(pk=lead_id)
    lead.is_contact = True
    lead.save()
    return redirect('leads:list')

def contact_list(request):
    contacts = Lead.objects.filter(is_contact=True)
    return render(request, 'leads/contact_list.html', {'contacts': contacts})

def mark_opportunity(request, lead_id):
    lead = Lead.objects.get(pk=lead_id)
    lead.is_opportunity = True
    lead.save()
    return redirect('leads:list')

def opportunity_list(request):
    opportunities = Opportunity.objects.all()
    return render(request, 'leads/opportunity_list.html', {'opportunities': opportunities})

def create_opportunity(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        # Render form
        pass

