import pytest
from django.urls import reverse
from .models import FAQ


@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.")
    assert faq.get_translated_question('hi') != faq.question
    assert faq.get_translated_answer('hi') != faq.answer


@pytest.mark.django_db
def test_faq_api(client):
    FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.")
    response = client.get(reverse('faq-list') + '?lang=hi')
    assert response.status_code == 200
