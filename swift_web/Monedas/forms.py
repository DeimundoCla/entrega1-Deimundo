from django import forms


class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Nombre")
    apellido= forms.CharField(max_length=500, label="Apellido")
    email= forms.EmailField(max_length=500, label="Email")
    fecha= forms.DateField(label="Fecha")
    comment= forms.CharField(label='',widget=forms.Textarea(
        attrs={'placeholder': 'Enter your comment here'}))