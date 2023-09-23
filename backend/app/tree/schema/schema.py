import graphene
import logging

from graphql_jwt.decorators import login_required, permission_required
from graphene_django import DjangoObjectType
from ..models import *

# TODO It is much better to use Relay, if the DB is big


class TreeTypeType(DjangoObjectType):
    class Meta:
        model = TreeType
        fields = "__all__"

class Query(graphene.ObjectType):
   
    all_tree_types = graphene.List(
        TreeTypeType, 
        tree_type_ids =  graphene.List(of_type=graphene.ID)
    )

    def resolve_all_tree_types(root, info, tree_type_ids = None):

        
        if tree_type_ids:
            return TreeType.objects.filter(id__in=tree_type_ids)
        return TreeType.objects.all()
        
        



schema = graphene.Schema(query=Query)