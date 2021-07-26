from django.shortcuts import render
from .models import Account, Cookies

from django.views.decorators.csrf import csrf_exempt
from .serializers import AccountSerializer, CookiesSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from deepturn.login import Login
from instagram.models import Cookies
from django.http import JsonResponse

@csrf_exempt
def account(request):
    """
    """
    data = JSONParser().parse(request)
    if request.method == 'GET':
        id = data['id']
        query = Account.objects.get(pk=id)
        serializer = AccountSerializer(query, many=False)
        return JsonResponse(serializer.data, safe=False)
        
    if request.method == 'POST':
        username = data['username']
        password = data['password']
        exists = Account.objects.filter(username=username).exists()
        if exists:
            id = Account.objects.get(username=username)
            cookies = dict(Cookies.objects.filter(pk=id).values()[0])
            cookies.pop('account_id')
            Login().login(username, password, cookies=cookies)
        else:
            ig_auth = Login().first_login(username, password)
            serializer = AccountSerializer(data=ig_auth)
            if serializer.is_valid():
                serializer.save() 
                cserializer = CookiesSerializer(data=ig_auth['cookies'])
                if cserializer.is_valid():
                    cserializer.save()
                    serializer.data.update(cserializer.data)
                    return JsonResponse(serializer.data, status=201)
                serializer.errors.update(cserializer.errors) 
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def cookies(request):
    """
    """
    data = JSONParser().parse(request)
    if request.method == 'GET':
        try:
            cookies = Cookies.objects.get(id=data['id'])
            return JsonResponse(cookies, safe=False)
        except Cookies.DoesNotExist:
            return JsonResponse(False, safe=False)

    elif request.method == 'POST':
        print(f"IN COOKIE FUNC: {data}")
        serializer = CookiesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        print(f"SERUAL ERRS: {serializer.errors}")
        return JsonResponse(serializer.errors, status=400)

