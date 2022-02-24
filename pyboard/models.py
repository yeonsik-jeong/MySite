from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def getDefaultUser():
    # result, _ = User.objects.get_or_create(id=1)  
    result = 1  # default should be an id (number)
    return result

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default=lambda: User.objects.get(id=1))  # Django can't serialize lambda
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=getDefaultUser, related_name="questionAuthor")
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    recommenders = models.ManyToManyField(User, related_name="questionRecommenders")

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default=lambda: User.objects.get(id=1))
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=getDefaultUser)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    recommenders = models.ManyToManyField(User, related_name="answerRecommenders")

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=getDefaultUser)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
