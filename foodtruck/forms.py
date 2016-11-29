import os
from django import forms
from django.core.mail import send_mail
from foodtruck.models import Foodtruck, Profile

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

class MultipleEmailForm(forms.Form):
    sender = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # recipient_list = []
        # for x in Profile.objects.all():
        #     recipient_list.append(x.email)
        # print(recipient_list)
        sender = self.cleaned_data["sender"]
        message = self.cleaned_data["message"]
        subject = "Now On Site at a New Location"
        body = """Thanks for favoriting my Food Truck! You guys are awesome!
               From: {}
               Message: {}
               """.format(sender, message)
        recipient_list = ["rallen0150@gmail.com", "fsciety1@gmail.com"]
        send_mail(subject, body, sender, recipient_list)
        # while len(recipient_list) > 0:
        #     recipient_list.pop()
