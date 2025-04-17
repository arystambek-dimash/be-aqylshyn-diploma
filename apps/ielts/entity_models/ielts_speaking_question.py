from django.db import models

from apps.ielts.entity_models.ielts_test import IeltsTest


class IeltsSpeakingQuestion(models.Model):
    question = models.TextField()
    additional_information = models.TextField()

    test = models.ForeignKey(IeltsTest, on_delete=models.CASCADE, related_name='speaking_questions')

    def __str__(self):
        return self.test

    class Meta:
        verbose_name_plural = "Speaking | Tasks"
