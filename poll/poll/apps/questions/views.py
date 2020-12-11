from django.http import Http404, HttpResponseRedirect
import datetime
from django.shortcuts import render
from .models import Poll, Question, QueAnswer, UserAnswer, UserTextAnswer
from django.contrib.auth.models import User


def index(request):
	now = datetime.datetime.now()
	actual_polls = Poll.objects.filter(answered_at__gte=now)
	return render(request, 'questions/base.html', {'actual_polls' : actual_polls})
	
def poll(request, poll_id):
	try:
		now = datetime.datetime.now()
		poll = Poll.objects.filter(answered_at__gte=now).get(poll_id=poll_id)
		ques = Question.objects.filter(poll__poll_id=poll_id)
		answers = QueAnswer.objects.filter(que__poll__poll_id=poll_id)
	except:
		raise Http404('Опрос не найден!')

	dictionary = {
		'poll' : poll,
		'questions' : ques,
		'queanswers' : answers,
	}
	return render(request, "questions/poll.html", dictionary)

def leave_poll(request, poll_id):
	try:
		now = datetime.datetime.now()
		poll = Poll.objects.filter(answered_at__gte=now).get(poll_id=poll_id)
	except:
		raise Http404('Опрос не найден!')

	try:
		user = User.objects.get(username=request.POST['user'])
	except:
		user = User(is_superuser=False, username=request.POST['user'])
		user.save()

	for i in request.POST:
		print(i)
		print(request.POST[i])
		if i == 'user' or i == 'csrfmiddlewaretoken':
			continue
		if '-' in i:
			que = Question.objects.get(que_id=i.split('-')[0])
			answer = UserAnswer(user=user, que_answer=QueAnswer.objects.get(answer_id=request.POST[i]))
			answer.save()
			continue

		que = Question.objects.get(que_id=i)
		if que.que_type == 'text':
			answer = UserTextAnswer(user=user, que=que, que_textanswer=request.POST[i])
			answer.save()
		elif que.que_type == 'one':
			answer = UserAnswer(user=user, que_answer=QueAnswer.objects.get(answer_id=request.POST[i]))
			answer.save()
	now = datetime.datetime.now()
	actual_polls = Poll.objects.filter(answered_at__gte=now)
	return render(request, 'questions/base.html', {'actual_polls' : actual_polls})
