import graphene
from graphene_django import DjangoObjectType
from .models import Person

class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        filter_fields = '__all__'

class Query(graphene.ObjectType):
    allPerson = graphene.List(PersonType)

    def resolve_allPerson(root, info):
        return Person.objects.all()

class updatePersonMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        Name = graphene.String(required=True)
        Phone = graphene.String(required=True)
        Email = graphene.String(required=True)
        Address = graphene.String(required=True)
    person = graphene.Field(PersonType)

    @classmethod
    def mutate(cls, root, info, id, Name, Phone, Email, Address):
        person = Person.objects.get(id=id)
        person.Name=Name
        person.Phone=Phone
        person.Email=Email
        person.Address=Address
        person.save()
        return updatePersonMutation(person=person)

class addPersonMutation(graphene.Mutation):
    class Arguments:
        Name = graphene.String(required=True)
        Phone = graphene.String(required=True)
        Email = graphene.String(required=True)
        Address = graphene.String(required=True)
    person = graphene.Field(PersonType)

    @classmethod
    def mutate(cls, root, info, Name, Phone, Email, Address):
        person = Person(Name=Name, Phone=Phone, Email=Email, Address=Address)
        person.save()
        return addPersonMutation(person=person)

class deletePersonMutation(graphene.Mutation):    
    class Arguments:
        id = graphene.ID()
    person = graphene.Field(PersonType)
    
    @classmethod
    def mutate(cls, root, info, id):
        person = Person.objects.get(id=id)
        person.delete()
        return        

class searchPersonMutation(graphene.Mutation):
    class Arguments:
        Name = graphene.String(required=True)
    person = graphene.Field(PersonType)
    
    @classmethod
    def mutate(cls, root, info, Name):
        person = Person.objects.get(Name__iexact=Name)
        return searchPersonMutation(person=person)

class Mutation(graphene.ObjectType):
    updatePerson = updatePersonMutation.Field()
    addPerson = addPersonMutation.Field()
    deletePerson = deletePersonMutation.Field()
    searchPerson = searchPersonMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

# superuser
# user and password: admin
