from django import forms
from testapp.models import Website
class WebsiteForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    mobile_number = forms.CharField()
    message = forms.CharField()
    class Meta():
        model = Website
        fields = '__all__'