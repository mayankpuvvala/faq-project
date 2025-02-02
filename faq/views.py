from django.shortcuts import render
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

class FAQList(generics.ListCreateAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.GET.get('lang', 'en')  # Default language is 'en'
        faqs = FAQ.objects.all()

        # Translate questions and answers based on selected language
        for faq in faqs:
            faq.question = faq.get_translated_question(lang) or faq.question
            faq.answer = faq.get_translated_answer(lang) or faq.answer

        return faqs

    def get(self, request, *args, **kwargs):
        # Pass the language parameter and FAQs to the template
        faqs = self.get_queryset()
        return render(request, 'faq_list.html', {'faqs': faqs})
