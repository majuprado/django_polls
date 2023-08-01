from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from polls.models import Question, Choice
from django.http import HttpResponse

# Create your views here

def index(request):
    return render(request, 'home.html')

def sobre(request):
    return HttpResponse('Olá este é um app de enquete')

def exibe_questao(request, question_id):
    questao = Question.objects.get(id=question_id)
    return HttpResponse(f'Questão 1: {questao.question_text}')

    if questao is not None:
        return HttpResponse(questao.question_text)
    
    return HttpResponse('Não existe questao a exibir')

def ultimas_perguntas(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'perguntas_recentes.html', context)
