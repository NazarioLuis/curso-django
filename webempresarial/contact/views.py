from django.shortcuts import render,redirect
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
            #Envio de correo
            email = EmailMessage(
                "La cafeteria: Nuevo mensaje de contacto",
                "De {} <{}>\n\n{}".format(name,email,content),
                "noreply@inbox.mailtrap.io",
                ["test@mail.com"],
                reply_to=[email]
            )
            try:
                email.send()
            except:
                return redirect(reverse('contact')+"?fail")
            

            return redirect(reverse('contact')+"?ok")

    return render(request,'contact/contact.html',{'form':contact_form})