from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import ItemModel
from .serializer import ItemSerializer

@api_view(['GET'])
def getmethod(request):
    items = ItemModel.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postmethod(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
