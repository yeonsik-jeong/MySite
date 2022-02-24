from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from pyboard.forms import QuestionForm
from pyboard.models import Question

# Create your views here.
@login_required(login_url='pyauth:login')
def createQuestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.create_date = timezone.now()
            instance.save()
            return redirect('pyboard:index')
    else:
        form = QuestionForm()

    context = {'form': form}
    
    return render(request, 'pyboard/question_form.html', context)

@login_required(login_url='pyauth:login')
def modifyQuestion(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    
    if request.user != question.author:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect('pyboard:detailQuestion', questionId=question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)   # if not instance, it shows error that NOT NULL constraint failed: create_date
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.modify_date = timezone.now()
            instance.save()
            return redirect('pyboard:detailQuestion', questionId=question.id)
    else:
        form = QuestionForm(instance=question)

    context = {'form': form}
    print("subject: " + str(form.fields['subject']))

    return render(request, 'pyboard/question_form.html', context)

@login_required(login_url='pyauth:login')
def deleteQuestion(request, questionId):
    question = get_object_or_404(Question, pk=questionId)

    if request.user != question.author:
        messages.error(request, "삭제 권한이 없습니다.")
        return redirect('pyboard:detailQuestion', questionId=question.id)
   
    question.delete()
    return redirect('pyboard:index')

@login_required(login_url='pyauth:login')
def recommendQuestion(request, questionId):
    question = get_object_or_404(Question, pk=questionId)

    if request.user == question.author:
        messages.error(request, "본인은 추천 권한이 없습니다.")
    else:        
        question.recommenders.add(request.user)

    return redirect('pyboard:detailQuestion', questionId=question.id)