from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    inquiry = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        """
        method returns formatted information
        return: subject, msg
        """
        #cleaned data
        clean_data = super().clean()

        name = clean_data.get('name').strip()
        from_email = clean_data.get('email')
        subject = clean_data.get('inquiry')

        msg = f'{name} from {from_email} said:\n{subject}\n\n'
        msg += clean_data.get('message')

        return subject, msg

    def send(self):
        #method sends email using info from get_info method
        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECEIPIENT_ADDRESS]
            )