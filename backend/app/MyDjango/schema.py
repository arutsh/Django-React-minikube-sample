import graphene
import graphql_jwt
from graphene_django import  DjangoObjectType
from user.schema import schema as user_schema


class Query(user_schema.Query,
            graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation,
                graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)