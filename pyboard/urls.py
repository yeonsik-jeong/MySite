from django.urls import path
# from pyboard import views   # Not "import views"
from pyboard.views import views_base, views_question, views_answer, views_comment

app_name = 'pyboard'

urlpatterns = [
    # views_base.py
    path('', views_base.index, name='index'),
    path('question/<int:questionId>/', views_base.detailQuestion, name='detailQuestion'),
    
    # views_question.py
    path('question/create/', views_question.createQuestion, name='createQuestion'),
    path('question/modify/<int:questionId>/', views_question.modifyQuestion, name='modifyQuestion'),
    path('question/delete/<int:questionId>/', views_question.deleteQuestion, name='deleteQuestion'),
    path('question/recommend/<int:questionId>/', views_question.recommendQuestion, name='recommendQuestion'),
    
    # views_answer.py
    path('answer/create/question/<int:questionId>/', views_answer.createAnswer, name='createAnswer'),
    path('answer/modify/<int:answerId>/', views_answer.modifyAnswer, name='modifyAnswer'),
    path('answer/delete/<int:answerId>/', views_answer.deleteAnswer, name='deleteAnswer'),
    path('answer/recommend/<int:answerId>/', views_answer.recommendAnswer, name='recommendAnswer'),

    # views_comment.py
    path('comment/create/question/<int:questionId>/', views_comment.createCommentForQuestion, name='createCommentForQuestion'),
    path('comment/modify/question/<int:commentId>/', views_comment.modifyCommentForQuestion, name='modifyCommentForQuestion'),
    path('comment/delete/question/<int:commentId>/', views_comment.deleteCommentForQuestion, name='deleteCommentForQuestion'),
    path('comment/create/answer/<int:answerId>/', views_comment.createCommentForAnswer, name='createCommentForAnswer'),
    path('comment/modify/answer/<int:commentId>/', views_comment.modifyCommentForAnswer, name='modifyCommentForAnswer'),
    path('comment/delete/answer/<int:commentId>/', views_comment.deleteCommentForAnswer, name='deleteCommentForAnswer'),
]