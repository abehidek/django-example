from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def getData(request):
    person = { "name": "Igor", "age": 19 },
    return Response(person)

@api_view(["GET"])
def getBalta(request):
    person = { "name": "Balta", "age": 20 },
    return Response(person)
