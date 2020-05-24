from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES  = (
    ('S','Stripe'),
    ('P','Paypal'),
)

class CheckoutForms(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Laugarvegur 62'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder':'303'
    }))
    country = CountryField(blank_label = '(select country)').formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100'
    }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'101'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices = PAYMENT_CHOICES)
