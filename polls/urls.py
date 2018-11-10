from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	# путь /polls/
	path('', views.index, name='index'),
	# путь /polls/5/
	path('<int:question_id>/', views.detail, name='detail'),
	# путь /polls/5/results/
	path('<int:question_id/results/', views.results, name='results'),
	# путь /polls/5/vote/
	path('<int:question_id/vote/', views.vote, name='vote'),
]