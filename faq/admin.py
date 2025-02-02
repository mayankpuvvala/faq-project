from django import forms
from django.contrib import admin
from .models import FAQ


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3}),
            'answer': forms.Textarea(attrs={'rows': 5}),
        }


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQForm
    list_display = (
        'question',
        'answer',
        'question_hi',
        'question_bn',
        'answer_hi',
        'answer_bn')
    search_fields = ('question', 'answer')
    list_filter = ('question_hi', 'question_bn', 'answer_hi', 'answer_bn')
