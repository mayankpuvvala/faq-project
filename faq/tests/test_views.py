import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ


@pytest.mark.django_db
def test_faq_list_view():
    client = APIClient()
    FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework."
    )
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert response.data['count'] == 1  # Check the total count of FAQs
    assert len(response.data['results']) == 1  # Check the number of FAQs in the results list


@pytest.mark.django_db
def test_faq_create_view():
    client = APIClient()
    data = {
        "question": "What is Python?",
        "answer": "Python is a programming language."
    }
    response = client.post(reverse('faq-list'), data, format='json')
    assert response.status_code == 201
    assert FAQ.objects.count() == 1