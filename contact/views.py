# contact/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construction du message complet
            full_message = (
                f"📬 Nouveau message de {nom}\n\n"
                f"📧 Adresse email : {email}\n\n"
                f"💬 Message :\n{message}"
            )

            send_mail(
                subject=f"📩 Message de contact depuis le site de Bangoulap",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['ketchadjiguymartial@gmail.com'],
                fail_silently=False,
            )
            sent = True
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form, 'sent': sent})
