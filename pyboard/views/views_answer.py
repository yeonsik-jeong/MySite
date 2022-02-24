from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from pyboard.forms import AnswerForm
from pyboard.models import Question, Answer

# Create your views here.
@login_required(login_url='pyauth:login')
def createAnswer(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.question = question
            instance.author = request.user
            instance.create_date = timezone.now()
            instance.save()
            # return redirect('pyboard:detailQuestion', questionId=question.id)
            return redirect('{}#answer_{}'.format(resolve_url('pyboard:detailQuestion', questionId=question.id), instance.id))
    else:
        form = AnswerForm()

    context = {'question': question, 'form': form}

    return render(request, 'pyboard/question_detail.html', context)

@login_required(login_url='pyauth:login')
def modifyAnswer(request, answerId):
    answer = get_object_or_404(Answer, pk=answerId)
    
    if request.user != answer.author:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect('pyboard:detailQuestion', questionId=answer.question.id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.modify_date = timezone.now()
            instance.save()
            # return redirect('pyboard:detailQuestion', questionId=answer.question.id)
            return redirect('{}#answer_{}'.format(resolve_url('pyboard:detailQuestion', questionId=answer.question.id), instance.id))
    else:
        form = AnswerForm(instance=answer)

    # context = {'answer': answer, 'form': form}
    context = {'form': form}
    # print("form.content: " + str(form.fields['content']))

    return render(request, 'pyboard/answer_modify.html', context)        

@login_required(login_url='pyauth:login')
def deleteAnswer(request, answerId):
    answer = get_object_or_404(Answer, pk=answerId)

    if request.user != answer.author:
        messages.error(request, "삭제 권한이 없습니다.")
    else:
        answer.delete()        

    return redirect('pyboard:detailQuestion', questionId=answer.question.id)

@login_required(login_url='pyauth:login')
def recommendAnswer(request, answerId):
    answer = get_object_or_404(Answer, pk=answerId)

    if request.user == answer.author:
        messages.error(request, "본인은 추천 권한이 없습니다.")
    else:        
        answer.recommenders.add(request.user)

    return redirect('pyboard:detailQuestion', questionId=answer.question.id)