from django.shortcuts import render, redirect
from .models import TeamMember, NewsletterSubscriber
from .forms import ContactForm, NewsletterForm
from django.http import FileResponse
from django.core.mail import send_mail
import os
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from datetime import date
from .models import Event

def home(request):
    newsletter_form = NewsletterForm()
    total_subscribers = NewsletterSubscriber.objects.count()
    context = {
        'newsletter_form': newsletter_form,
        'subscriber_count': total_subscribers
    }
    if request.method == 'POST' and 'newsletter_email' in request.POST:
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data['email']
            NewsletterSubscriber.objects.get_or_create(email=email)
            context.update({
                'newsletter_success': True,
                'newsletter_form': NewsletterForm(),
                'subscriber_count': NewsletterSubscriber.objects.count()
            })
    return render(request, 'home.html', context)

def about(request):
    team = TeamMember.objects.all()  # Replace TeamMember with your actual model
    return render(request, 'about.html', {'team': team})


def team(request):
    members = TeamMember.objects.all()
    return render(request, 'team.html', {'team': members})

def membership(request):
    return render(request, 'membership.html')

def download_form(request):
    filepath = os.path.join(settings.MEDIA_ROOT, 'ILS_Membership_Form.pdf')
    return FileResponse(open(filepath, 'rb'), as_attachment=True, filename='ILS_Membership_Form.pdf')

def download_constitution(request):
    filepath = os.path.join(settings.MEDIA_ROOT, 'ILS_Constitution.pdf')
    return FileResponse(open(filepath, 'rb'), as_attachment=True, filename='ILS_Constitution.pdf')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_mail(
                    subject=f"Contact from {form.cleaned_data['name']}",
                    message=form.cleaned_data['message'],
                    from_email=form.cleaned_data['email'],
                    recipient_list=['intellijuslawsociety@gmail.com']
                )
                return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def terms(request):
    return render(request, 'terms.html')
def gallery(request):
    return render(request, 'gallery.html')

def gallery(request):
    events = Event.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, 'gallery.html', {'events': events})

from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "Sitemap: https://intellijus-society.onrender.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")



def sitemap_xml(request):
    content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://intellijus-society.onrender.com/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>'''
    return HttpResponse(content, content_type='application/xml')

from django.views.static import serve
import os
from django.conf import settings

def google_verification_file(request):
    file_path = os.path.join(settings.BASE_DIR, 'core', 'static', 'google3c1cb1b5cdd53735.html')
    return serve(request, os.path.basename(file_path), os.path.dirname(file_path))
