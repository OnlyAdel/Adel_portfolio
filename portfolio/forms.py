from django.forms import ModelForm
from .models import Contact

#class ContactForm(forms.Form):
#	name = forms.CharField(max_length=100)
#	email = forms.EmailField(label="tape your email here")
#	subject = forms.CharField(max_length=200)
#	message = forms.CharField(widget=forms.Textarea)


class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		def __str__(self):
			return self.subject	
