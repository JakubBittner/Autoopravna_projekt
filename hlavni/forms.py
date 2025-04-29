# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Repair
from .models import RepairReservation

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Pokud se hesla neshodují
        if password != confirm_password:
            raise forms.ValidationError('Hesla se neshodují!')
        
        return cleaned_data

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['customer', 'title', 'description', 'status']

    def __init__(self, *args, **kwargs):
        super(RepairForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class RepairReservationForm(forms.ModelForm):
    class Meta:
        model = RepairReservation
        fields = ['date', 'time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }