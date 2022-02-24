from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from pyboard.forms import CommentForm
from pyboard.models import Question, Answer, Comment

# Create your views here.
@login_required(login_url='pyauth:login')
def createCommentForQuestion(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.question = question
            instance.author = request.user
            instance.create_date = timezone.now()
            instance.save()
            # return redirect('pyboard:detailQuestion', questionId=question.id)
            return redirect('{}#comment_{}'.format(resolve_url('pyboard:detailQuestion', questionId=question.id), instance.id))
    else:
        form = CommentForm()

    context = {'form': form}

    return render(request, 'pyboard/comment_form.html', context)

@login_required(login_url='pyauth:login')
def modifyCommentForQuestion(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)
    
    if request.user != comment.author:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect('pyboard:detailQuestion', questionId=comment.question.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.modify_date = timezone.now()
            instance.save()
            # return redirect('pyboard:detailQuestion', questionId=comment.question.id)
            return redirect('{}#comment_{}'.format(resolve_url('pyboard:detailQuestion', questionId=comment.question.id), instance.id))
    else:
        form = CommentForm(instance=comment)

    context = {'form': form}

    return render(request, 'pyboard/comment_form.html', context)

@login_required(login_url='pyauth:login')
def deleteCommentForQuestion(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)

    if request.user != comment.author:
        messages.error(request, "삭제 권한이 없습니다.")
    else:
        comment.delete()        

    return redirect('pyboard:detailQuestion', questionId=comment.question.id)

@login_required(login_url='pyauth:login')
def createCommentForAnswer(request, answerId):
    answer = get_object_or_404(Answer, pk=answerId)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.answer = answer
            instance.author = request.user
            instance.create_date = timezone.now()
            instance.save()
            # return redirect('pyboard:detailQuestion', questionId=answer.question.id)
            return redirect('{}#comment_{}'.format(resolve_url('pyboard:detailQuestion', questionId=answer.question.id), instance.id))
    else:
        form = CommentForm()

    context = {'form': form}

    return render(request, 'pyboard/comment_form.html', context)

@login_required(login_url='pyauth:login')
def modifyCommentForAnswer(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)
    
    if request.user != comment.author:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect('pyboard:detailQuestion', questionId=comment.answer.question.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.modify_date = timezone.now()
            instance.save()
            # return redirect('pyboard:detailQuestion', questionId=comment.answer.question.id)
            return redirect('{}#comment_{}'.format(resolve_url('pyboard:detailQuestion', questionId=comment.answer.question.id), instance.id))
    else:
        form = CommentForm(instance=comment)

    context = {'form': form}

    return render(request, 'pyboard/comment_form.html', context)

@login_required(login_url='pyauth:login')
def deleteCommentForAnswer(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)

    if request.user != comment.author:
        messages.error(request, "삭제 권한이 없습니다.")
    else:
        comment.delete()        

    return redirect('pyboard:detailQuestion', questionId=comment.answer.question.id)