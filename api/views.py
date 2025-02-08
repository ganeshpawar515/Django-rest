from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item,Joke
from .serializers import ItemSerializer, JokeSerializer
@api_view(['GET'])
def getData(request):
    items=Item.objects.all()
    serializer=ItemSerializer(items, many=True)
    return Response(serializer.data)
    # return Response({"dev-name":"Ganesh","age":25})

@api_view(['POST'])
def addData(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["PUT","PATCH"])
def updateData(request, pk):
    item=Item.objects.get(pk=pk)
    serializer=ItemSerializer(item,data=request.data, partial=(request.method=="PATCH"))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data,status=404)

import requests
@api_view(["GET"])
def getJoke(request):
    # jokes=Joke.objects.all()
    # serializer = JokeSerializer(jokes,many=True)
    joke=requests.get("https://api.chucknorris.io/jokes/random")
    joke=joke.json()
    print("recieved: ",joke["value"])
    return Response({"joke":joke["value"]})


    
    