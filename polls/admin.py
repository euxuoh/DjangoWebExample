from django.contrib import admin
from polls.models import Poll, Choice

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [('Poll', {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    date_hierarchy = 'pub_date'
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)