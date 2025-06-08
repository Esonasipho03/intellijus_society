from django.contrib import admin
from .models import TeamMember, NewsletterSubscriber
import csv
from django.http import HttpResponse
from .models import Event

admin.site.register(Event)


@admin.action(description="Export selected emails to CSV")
def export_emails(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="newsletter_subscribers.csv"'
    writer = csv.writer(response)
    writer.writerow(['Email', 'Subscribed On'])
    for subscriber in queryset:
        writer.writerow([subscriber.email, subscriber.subscribed_on])
    return response

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on')
    actions = [export_emails]

admin.site.register(TeamMember)
admin.site.register(NewsletterSubscriber, NewsletterAdmin)