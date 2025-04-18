from django.contrib import admin

from .entity_models.ielts_speaking import IeltsSpeakingQuestion
from .models import (
    IeltsModule,
    IeltsSubModule,
    IeltsTest,
    IeltsReading,
    IeltsReadingQuestion,
    IeltsReadingOption,
    IeltsReadingFillBlank,
    IeltsReadingSelectInsert,
    IeltsWriting,
    WritingImage,
    IeltsListening,
    IeltsListeningQuestion,
    IeltsListeningOption,
    IeltsListeningFillBlank,
)


# ───────────── Module, SubModule & Test Admins ─────────────

class IeltsSubModuleInline(admin.TabularInline):
    model = IeltsSubModule
    extra = 1


@admin.register(IeltsModule)
class IeltsModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    inlines = [IeltsSubModuleInline]


class IeltsTestInline(admin.TabularInline):
    model = IeltsTest
    extra = 1


@admin.register(IeltsSubModule)
class IeltsSubModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'module')
    inlines = [IeltsTestInline]


# ───────────── Reading Admins ─────────────

class IeltsReadingQuestionInline(admin.TabularInline):
    model = IeltsReadingQuestion
    extra = 1


@admin.register(IeltsReading)
class IeltsReadingAdmin(admin.ModelAdmin):
    list_display = ('title', 'test')
    inlines = [IeltsReadingQuestionInline]
    fields = ('title', 'content', 'test')


# In the Reading Question admin, we add inlines for its details
class IeltsReadingOptionInline(admin.TabularInline):
    model = IeltsReadingOption
    extra = 1


class IeltsReadingFillBlankInline(admin.StackedInline):
    model = IeltsReadingFillBlank
    extra = 0
    max_num = 1


class IeltsReadingSelectInsertInline(admin.StackedInline):
    model = IeltsReadingSelectInsert
    extra = 0
    max_num = 1


@admin.register(IeltsReadingQuestion)
class IeltsReadingQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_content', 'question_type', 'reading')
    fields = ('reading', 'question_content', 'question_type')
    inlines = [
        IeltsReadingOptionInline,
        IeltsReadingFillBlankInline,
        IeltsReadingSelectInsertInline,
    ]


# ───────────── Listening Admins ─────────────

class IeltsListeningQuestionInline(admin.TabularInline):
    model = IeltsListeningQuestion
    extra = 1


@admin.register(IeltsListening)
class IeltsListeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'test')
    fields = ('title', 'audio_file', 'test')
    inlines = [IeltsListeningQuestionInline]


class IeltsListeningOptionInline(admin.TabularInline):
    model = IeltsListeningOption
    extra = 1


class IeltsListeningFillBlankInline(admin.StackedInline):
    model = IeltsListeningFillBlank
    extra = 0
    max_num = 1


@admin.register(IeltsListeningQuestion)
class IeltsListeningQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_content', 'question_type', 'listening')
    fields = ('listening', 'question_content', 'question_type')
    inlines = [
        IeltsListeningOptionInline,
        IeltsListeningFillBlankInline,
    ]


# ───────────── Writing Admins ─────────────

class WritingImageInline(admin.TabularInline):
    model = WritingImage
    extra = 1


@admin.register(IeltsWriting)
class IeltsWritingAdmin(admin.ModelAdmin):
    list_display = ('title', 'test')
    inlines = [WritingImageInline]
    fields = ('title', 'description', 'context', 'test')


# ───────────── Speaking Admins ─────────────
@admin.register(IeltsSpeakingQuestion)
class IeltsSpeakingQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'test')
    fields = ('question', 'additional_information', "test")


# ───────────── IeltsTest Admin (Combining Reading, Writing, & Listening) ─────────────

class IeltsReadingInline(admin.TabularInline):
    model = IeltsReading
    extra = 1


class IeltsWritingInline(admin.TabularInline):
    model = IeltsWriting
    extra = 1


class IeltsListeningInline(admin.TabularInline):
    model = IeltsListening
    extra = 1


class IeltsSpeakingInline(admin.TabularInline):
    model = IeltsSpeakingQuestion
    extra = 1


@admin.register(IeltsTest)
class IeltsTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_model')
    inlines = [IeltsReadingInline, IeltsWritingInline, IeltsListeningInline, IeltsSpeakingInline]
