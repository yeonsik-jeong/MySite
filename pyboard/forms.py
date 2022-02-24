from django import forms
from pyboard.models import Answer, Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        """
        labels = {
            'subject': "제목",
            'content': "내용",
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer  
        fields = ['content']
        labels = {
            'content': "답변 내용",
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': "댓글 내용",
        }