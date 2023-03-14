import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from machine_learning.manager import TapasBaseClass

tapas_instance = TapasBaseClass()

# Create your views here.
@csrf_exempt
def get_result(request):
    if request.method == "POST":
        query = json.loads(request.body)
        result = tapas_instance.ask(query['query'])
        print(result)
        return HttpResponse(
             content=json.dumps({"status": 200, "result": result[0]['answer']})
        )

