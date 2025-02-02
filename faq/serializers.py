from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = [
            'id',
            'question',
            'answer',
            'question_hi',
            'question_bn',
            'answer_hi',
            'answer_bn']

    def validate(self, data):
        if not data.get('question') or not data.get('answer'):
            raise serializers.ValidationError(
                "Question and Answer fields are required.")
        return data
