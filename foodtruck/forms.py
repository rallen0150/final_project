import os
from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    sender = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        sender = self.cleaned_data["sender"]
        message = self.cleaned_data["message"]
        subject = "Food Truck Finder"
        body = """Hey you got an email regarding your website!
               From: {}
               Message: {}
               """.format(sender, message)
        recipient_list = [os.environ.get("EMAIL_HOST_USER")]
        # print(recipient_list)
        send_mail(subject, body, sender, recipient_list)
