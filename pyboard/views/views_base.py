from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count
from pyboard.models import Question

# Create your views here.
QUESTION_NUMBERS_PER_PAGE = 10

def index(request):
    # questionList = Question.objects.order_by('-create_date')

    pageNumber = request.GET.get('pageNumber', '1')       
    keyword = request.GET.get('keyword', '')
    sortOrder = request.GET.get('sortOrder', 'recent')

    if sortOrder == 'recent':
        questionList = Question.objects.order_by('-create_date')
    elif sortOrder == 'recommendatory':
        questionList = Question.objects.annotate(num_recommenders=Count('recommenders')).order_by('-num_recommenders', '-create_date')
    else:    
        questionList = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    
    if keyword:
        questionList = questionList.filter(
            Q(subject__icontains=keyword) |
            Q(content__icontains=keyword) |
            Q(author__username__icontains=keyword) |
            Q(answer__author__username__icontains=keyword)
        ).distinct()
    
    paginator = Paginator(questionList, QUESTION_NUMBERS_PER_PAGE)
    # pageNumber = request.GET.get('page', '1')
    pageQuestionList = paginator.get_page(pageNumber)
    lastPageNumber = paginator.num_pages

    # context = {'questionList': questionList}
    # context = {'questionList': pageQuestionList}
    # context = {'questionList': pageQuestionList, 'pageNumber': pageNumber, 'keyword': keyword, 'sortOrder': sortOrder}
    context = {'questionList': pageQuestionList, 'lastPageNumber': lastPageNumber, 'keyword': keyword, 'sortOrder': sortOrder}  # Yeonsik

    # return HttpResponse("Hello, Welcome to the pyboard. pyboard는 파이썬으로 구현한 게시판입니다.")
    return render(request, 'pyboard/question_list.html', context)

def detailQuestion(request, questionId):
    # print("questionId in %s:  %d"  % (detail.__name__, questionId))
    # question = Question.objects.get(id=questionId)
    question = get_object_or_404(Question, pk=questionId)
    context = {'question': question}

    return render(request, 'pyboard/question_detail.html', context)