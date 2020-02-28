import graphene
from graphene_django.types import DjangoObjectType
from .models import Child, Sports, English, Test
from django.contrib.auth import models


class ChildType(DjangoObjectType):
    class Meta:
        model = Child


class UserType(DjangoObjectType):
    class Meta:
        model = models.User


class TestType(DjangoObjectType):
    class Meta:
        model = Test


class EnglishType(DjangoObjectType):
    class Meta:
        model = English


class SportsType(DjangoObjectType):
    class Meta:
        model = Sports


class GroupType(DjangoObjectType):
    class Meta:
        model = models.Group


class CreateUser(graphene.Mutation):
    class Input:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
    user = graphene.Field(UserType)
    @staticmethod
    def mutate(self, info, username, email, password):
        print(self)
        models.UserManager.create_user(username, email, password)


class Mutation(graphene.AbstractType):
    create_user = CreateUser.Field()


class Query(graphene.AbstractType):
    childrens = graphene.List(ChildType)
    users = graphene.List(UserType)
    groups = graphene.List(GroupType)
    sports = graphene.List(SportsType)
    tests = graphene.List(TestType)
    english = graphene.List(EnglishType)

    def resolve_childrens(self, context, **kwargs):
        return Child.objects.all()

    def resolve_users(self, context, **kwargs):
        return models.User.objects.all()

    def resolve_groups(self, context, **kwargs):
        return models.Group.objects.all()

    def resolve_sports(self, context, **kwargs):
        return Sports.objects.all()

    def resolve_english(self, context, **kwargs):
        return English.objects.all()

    def resolve_tests(self, context, **kwargs):
        return Test.objects.all()
