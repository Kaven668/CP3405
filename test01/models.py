from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    age = models.IntegerField()


class QuestionCategory(models.Model):
    # Question category table
    question_category_id = models.IntegerField(primary_key=True)
    question_category = models.CharField(max_length=45, null=False)


class QuestionType(models.Model):
    # Question type table
    question_type_id = models.IntegerField(primary_key=True)
    question_type = models.CharField(max_length=45, null=True)


class Survey(models.Model):
    # Servery ID table
    survey_id = models.IntegerField(primary_key=True)


class MediaType(models.Model):
    # Media type table
    media_type_id = models.IntegerField(primary_key=True)


class Question(models.Model):
    # Question table
    question_id = models.IntegerField(primary_key=True)
    question_title = models.CharField(max_length=45, null=False)
    question_type = models.ForeignKey(QuestionType, on_delete=models.SET_NULL, null=True)


class QuestionHasSurvey(models.Model):
    # Question has survey tables
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)


class Option(models.Model):
    # Option table
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    option_id = models.IntegerField(primary_key=True)
    option_description = models.CharField(max_length=45, null=True)
    media_type = models.ForeignKey(MediaType, on_delete=models.SET_NULL, null=True)
    option_correct = models.BooleanField()


class QuestionHasQuestionCategory(models.Model):
    # Question has question category
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    question_category = models.ForeignKey(QuestionCategory, on_delete=models.SET_NULL, null=True)


