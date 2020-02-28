from django.db import models

# Create your models here.


class Child(models.Model):
    name = models.CharField(max_length=50)
    std = models.IntegerField()
    school = models.TextField()


class English(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    communication = models.IntegerField()
    Comprehensive = models.IntegerField()
    Grammar = models.IntegerField()
    Vocabulary = models.IntegerField()
    Writing = models.IntegerField()
    Aptitude = models.IntegerField()
    LogicalReasoning = models.IntegerField()
    GeneralMentalAbility = models.IntegerField()
    MathSkills = models.IntegerField()
    GeneralKnowledge = models.IntegerField()


class Test(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    Language1 = models.IntegerField()
    Language2 = models.IntegerField()
    Language3 = models.IntegerField()
    Maths = models.IntegerField()
    Science = models.IntegerField()
    Social = models.IntegerField()
    Test_Date = models.DateField()


class Sports(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    running = models.IntegerField()
    basketball = models.IntegerField()
    cycling = models.IntegerField()
    chess = models.IntegerField()
    swimming = models.IntegerField()
