import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("first_name",'last_name','email','username')

class Query(graphene.ObjectType):
    allUsers = graphene.List(UserType)

    def resolve_allUsers(root, info):
        return User.objects.all()

schema = graphene.Schema(query=Query)

# superuser
# user and password: admin
