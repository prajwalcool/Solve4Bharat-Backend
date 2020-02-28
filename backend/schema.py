import graphene
from simple_app.schema import Query,Mutation as Mut

class Query(Query,graphene.ObjectType):
    pass
class Mutation(Mut,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)