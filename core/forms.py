from django import forms
from django.core.mail.message import EmailMessage
from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='E-mail')
    subject = forms.CharField(label='Subject')
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {name}\nE-mail: {email}\nSubject: {subject}\nMessage: {message}'
        mail = EmailMessage(
            subject='Email sent by the django system',
            body=content,
            from_email=email,
            to=['lucas.takiya@gmail.com'],
            headers={'Reply-to': email}
        )
        mail.send()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'storage', 'image']
