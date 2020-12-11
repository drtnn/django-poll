from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
	poll_id = models.AutoField(primary_key=True)
	poll_title = models.CharField('Название опроса', max_length=128)
	poll_desc = models.TextField('Описание опроса')
	created_at = models.DateTimeField(verbose_name='Дата старта', auto_now=True, editable=False)
	answered_at = models.DateTimeField("Дата окончания", null=True, blank=True)
	
	def __str__(self):
		return f'{self.poll_id}. {self.poll_title}'
	
	class Meta:
		verbose_name = "Опрос"
		verbose_name_plural = "Опросы"

class Question(models.Model):
	que_id = models.AutoField(primary_key=True)
	que_type = models.CharField(
		"Тип вопроса",
		max_length=4,
		choices=[
			('text', 'Ответ текстом'),
			('one', 'Ответ с выбором одного варианта'),
			('many', 'Ответ с выбором нескольких вариантов'),
	])
	que_title = models.CharField('Вопрос', max_length=128)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name='Опрос')
		
	def __str__(self):
		return f'{self.poll.poll_title}: {self.que_title}'

	class Meta:
		verbose_name = "Вопрос"
		verbose_name_plural = "Вопросы"

class QueAnswer(models.Model):
	answer_id = models.AutoField(primary_key=True)
	que = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
	que_answer = models.CharField('Ответ на вопрос', max_length=128)

	def __str__(self):
		return f'{self.que.que_title} {self.que_answer}'
	
	class Meta:
		verbose_name = "Ответ на вопрос"
		verbose_name_plural = "Ответы на вопросы"

class UserAnswer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
	que_answer = models.ForeignKey(QueAnswer, on_delete=models.CASCADE, verbose_name='Ответ на вопрос')
	
	def __str__(self):
		return f'{self.user.username} {self.que_answer.que_answer}'
	
	class Meta:
		verbose_name = "Ответ пользователя"
		verbose_name_plural = "Ответы пользователей"

class UserTextAnswer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
	que = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
	que_textanswer = models.CharField('Текстовый ответ на вопрос', max_length=128)

	def __str__(self):
		return f'{self.user.username} {self.que_textanswer}'

	class Meta:
		verbose_name = "Тестовый ответ пользователя"
		verbose_name_plural = "Текстовые ответы пользователей"

