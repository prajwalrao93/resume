from django import forms
from django.core.validators import EmailValidator, MinLengthValidator
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    name = forms.CharField(max_length=250, required=True, validators=[MinLengthValidator(2)],
                           widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(validators=[EmailValidator(message="Enter a valid email address.")],
                             widget=forms.TextInput(attrs={'placeholder': 'Enter your Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Subject"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Your message"}), validators=[MinLengthValidator(10)]
    )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def clean_message(self):
        data = self.cleaned_data['message']
        unwanted_words = ['spam', 'money', 'subscribe']
        if any(word in data.lower() for word in unwanted_words):
            raise forms.ValidationError("Please do not include spam words in your message.")
        return data

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')
        if 'help' in subject.lower() and 'urgent' not in message.lower():
            raise forms.ValidationError("Urgent help requests should include 'urgent' in the message.")
