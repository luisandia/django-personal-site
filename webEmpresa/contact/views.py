from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # senf email and redirect
            email = EmailMessage(
                "Nuevo mensaje de contacto",  # asunto,
                "De {} <{}\n\nEscribio:\n\n{}>".format(name, email, content),  # cuerpo,
                "no-contestar@inbox.mailtrap.io",  # origen,
                ['anonimo_destino@gmail.com'],  # destino,
                reply_to=[email],  # reply_to
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')

    return render(request, "contact/contact.html", {'form': contact_form})
