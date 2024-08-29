from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerilizer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerilizer
    return Response(person)
