from apps.ielts.entity_models.ielts_writing import IeltsWriting
from apps.ielts.entity_models.ielts_writing import WritingImage
from .entity_models.ielts_module import IeltsModule
from .entity_models.ielts_sub_module import IeltsSubModule
from .entity_models.ielts_test import IeltsTest
from .entity_models.ielts_test_submit import IeltsTestSubmit
from .entity_models.listenings.listening import IeltsListening
from .entity_models.listenings.listening_options import IeltsListeningFillBlank
from .entity_models.listenings.listening_options import IeltsListeningOption
from .entity_models.listenings.listening_parts import IeltsListeningPart
from .entity_models.listenings.listening_question import IeltsListeningQuestion
from .entity_models.readings.reading import IeltsReading
from .entity_models.readings.reading_options import IeltsReadingFillBlank
from .entity_models.readings.reading_options import IeltsReadingOption
from .entity_models.readings.reading_options import IeltsReadingSelectInsert
from .entity_models.readings.reading_question import IeltsReadingQuestion
from .entity_models.speakings.speaking_parts import IeltsSpeakingPart
from .entity_models.speakings.speaking_questions import IeltsSpeakingQuestion

admin_models = [
    IeltsModule,
    IeltsReading,
    IeltsReadingQuestion,
    IeltsReadingFillBlank,
    IeltsListening,
    IeltsListeningPart,
    IeltsListeningQuestion,
    IeltsListeningOption,
    IeltsListeningFillBlank,
    IeltsSubModule,
    IeltsReadingOption,
    IeltsReadingSelectInsert,
    IeltsWriting,
    WritingImage,
    IeltsTest,
    IeltsTestSubmit,
    IeltsSpeakingQuestion,
    IeltsSpeakingPart
]
