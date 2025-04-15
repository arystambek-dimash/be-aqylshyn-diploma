from django.db import models

from apps.common.models import BaseModel
from apps.ielts.entity_models.attempts.ielts_test_attempt import IeltsTestAttempt
from apps.ielts.entity_models.readings.reading_options import IeltsReadingOption
from apps.ielts.entity_models.readings.reading_question import IeltsReadingQuestion


class IeltsReadingSubmission(BaseModel):
    attempt = models.ForeignKey(
        IeltsTestAttempt,
        on_delete=models.CASCADE,
        related_name='reading_submissions',
        verbose_name='Test Attempt'
    )
    question = models.ForeignKey(
        IeltsReadingQuestion,
        on_delete=models.CASCADE,
        related_name='submissions',
        verbose_name='Reading Question'
    )
    selected_option = models.ForeignKey(
        IeltsReadingOption,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        verbose_name='Selected Option'
    )
    fill_blank_answer = models.JSONField(
        null=True,
        blank=True,
        verbose_name='Fill-in-the-blanks Answer',
        help_text="Array of candidate answers if the question is fill in the blanks"
    )
    select_insert_answer = models.JSONField(
        null=True,
        blank=True,
        verbose_name='Select Insert Answer',
        help_text="Candidate selected words or phrases as a JSON array"
    )

    def __str__(self):
        return f"Reading Submission for Q#{self.question.id} by {self.attempt.user}"

    class Meta:
        verbose_name = "IELTS Reading Submission"
        verbose_name_plural = "IELTS Reading Submissions"
