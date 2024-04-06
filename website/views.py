from django.shortcuts import render ,HttpResponseRedirect , redirect
from website.forms import newslettr , ContactForms
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def index_view(request):
    return render(request, 'web/index.html')

def about_view(request):
    return render(request, 'web/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.name = "ananymous"
            contact.save()
            messages.add_message(request,messages.SUCCESS,'your tikct submited successfuly')
        else:
            messages.add_message(request,messages.ERROR,'your tikct didnt submited')
    else:
        form = ContactForms()
    return render(request, 'web/contact.html', {'form': form})

def newsletter(request):
    if request.method == 'POST':
        form = newslettr(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Welcome to Our Website'
            message = 'Dear User,\n\nWelcome to our website. We are glad to have you with us!'
            from_email = 'project@project-askari.ir'
            to_email = form.cleaned_data.get('email')
            recipient_list = [to_email]
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Your ticket submitted successfully')
            return redirect('/')
        else:
            messages.error(request, 'Your ticket did not submit')
