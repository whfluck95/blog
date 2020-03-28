import json
import hashlib

from django.http import JsonResponse
from django.shortcuts import render
from .models import UserProfile
from wtoken.views import make_token
# Create your views here.
def users(request):

    if request.method == 'GET':
        #拿取数据
        pass
    elif request.method == 'POST':
        #创建用户
        json_str = request.body
        if not json_str:
            result = {'code':10101,'error':'Please give me data~'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        username = json_obj.get('username')
        email = json_obj.get('email')
        if not username:
            result = {'code':10102,'error':'Please give me username~'}
            return JsonResponse(result)
        #TODO 检查 json dict 中的key 是否存在
        password1 = json_obj.get('password1')
        password2 = json_obj.get('password2')
        if password1 != password2 :
            result = {'code':10103,'error':'The password is error !'}
            return JsonResponse(result)
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code':10104,'error':'The username is already existed'}
            return JsonResponse(result)

        #生成散列密码
        pm = hashlib.md5()
        pm.update(password1.encode())

        #创建用户
        try:
            UserProfile.objects.create(
                username=username,
                password=pm.hexdigest(),
                nickname=username,
                email=email
            )
        except Exception as e:
            print('-----create error-----')
            print(e)
            result= {'code':10105,'error':'The username is already existed !!'}
            return JsonResponse(result)

        #生成token
        token = make_taken(username,3600*24)
        result = {'code':200,'data':{'token':token.decode()},'username':username}
        return JsonResponse(result)

    elif:
        pass