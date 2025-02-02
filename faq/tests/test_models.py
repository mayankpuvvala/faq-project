import pytest
from django.core.exceptions import ValidationError
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework."
    )
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a web framework."
    assert faq.question_hi is not None
    assert faq.question_bn is not None
    assert faq.answer_hi is not None
    assert faq.answer_bn is not None