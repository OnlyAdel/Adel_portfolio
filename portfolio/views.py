from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Certificate
from .forms import ContactForm


def home(request):
	certificates = Certificate.objects.all()[:6]
	return render(request, 'portfolio/home.html', {'certificates': certificates })


def adelprojects(request):
	projects = Project.objects.all()
	return render(request, 'portfolio/projects.html', {'projects': projects })


def adelcertificates(request):
	certificates = Certificate.objects.all()
	return render(request, 'portfolio/certificates.html', {'certificates': certificates})

def django(request):
	certificates = Certificate.objects.filter(title__contains="Django")
	return render(request, 'portfolio/certificates.html', {'certificates': certificates})

def python(request):
	certificates = Certificate.objects.filter(title__contains="Python")
	return render(request, 'portfolio/certificates.html', {'certificates': certificates})
	
def digitalmarketing(request):
	certificates = Certificate.objects.filter(title__contains="Digital")
	return render(request, 'portfolio/certificates.html', {'certificates': certificates})
	
def ai(request):
	certificates = Certificate.objects.filter(title__contains="Artificial")
	return render(request, 'portfolio/certificates.html', {'certificates': certificates})
	
def api(request):
	certificates = Certificate.objects.filter(title__contains="API")
	return render(request, 'portfolio/certificates.html', {'certificates': certificates})

def contact(request):
	if request.method == 'GET':
		form = ContactForm()
		return render(request, 'portfolio/contact.html', {'form': form})
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			
			form.save()
			
			return redirect('thanks')

def thanks(request):

	return render(request, 'portfolio/thanks.html')	
			
	
def detail(request, certificate_id):
	certificate = get_object_or_404(Certificate, pk=certificate_id)
	return render(request, 'portfolio/detail.html', {'certificate':certificate})
