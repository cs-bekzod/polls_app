from django.contrib import admin
from .models import Question,Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Text',               {'fields': ['text']}),
        ('Date information', {'fields': ['created_at']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('text', 'created_at','was_published_recently')
    list_filter = ['created_at']
    search_fields = ['text']
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)