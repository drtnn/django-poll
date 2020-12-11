from django.contrib import admin
from .models import Question, QueAnswer, UserAnswer, Poll, UserTextAnswer


class PollAdmin(admin.ModelAdmin):
	list_display = ('poll_id', 'poll_title', 'created_at', 'answered_at',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('que_id', 'que_type', 'que_title', 'poll',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class QueAnswerAdmin(admin.ModelAdmin):
	list_display = ('que', 'que_answer',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class UserAnswerAdmin(admin.ModelAdmin):
	list_display = ('user', 'que_answer',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class UserTextAnswerAdmin(admin.ModelAdmin):
	list_display = ('user', 'que', 'que_textanswer',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Question, QuestionAdmin)
admin.site.register(QueAnswer, QueAnswerAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
admin.site.register(UserTextAnswer, UserTextAnswerAdmin)
admin.site.register(Poll, PollAdmin)
