from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # Will use CKEditor for WYSIWYG support
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_hi = models.TextField(blank=True, null=True)  # Hindi translation
    answer_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['id']  

    def save(self, *args, **kwargs):
        if not self.question_hi or not self.answer_hi:
            translator = Translator()
            try:
                if not self.question_hi:
                    self.question_hi = translator.translate(
                        self.question, dest='hi').text
                if not self.question_bn:
                    self.question_bn = translator.translate(
                        self.question, dest='bn').text
                if not self.answer_hi:
                    self.answer_hi = translator.translate(
                        self.answer, dest='hi').text
                if not self.answer_bn:
                    self.answer_bn = translator.translate(
                        self.answer, dest='bn').text
            except Exception as e:
                print(f"Error during translation: {e}")
                self.question_hi = self.question_hi or self.question
                self.question_bn = self.question_bn or self.question
                self.answer_hi = self.answer_hi or self.answer
                self.answer_bn = self.answer_bn or self.answer
        super().save(*args, **kwargs)
