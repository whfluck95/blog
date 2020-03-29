import json
import html
from django.shortcuts import render
from django.http import JsonResponse
from tools.logging_check import logging_check
from .models import Topic
from user.models import UserProfile


# Create your views here.
@logging_check('POST','DELETE')
def topics(request,author_id):

    if request.method == 'POST':
        #发表博客
        author = request.user
        if author.username != author_id:
            result = {'code':30101,'error':'The author is error'}
            return JsonResponse(result)
        json_str = request.body
        json_obj = json.loads(json_str)
        title = json_obj.get('title')
        #注意xxs攻击，将用户输入进行转义
        title = html.escape(title)

        category = json_obj.get('category')
        if category not in ['tec','no-tec']:
            result = {'code':30102,'error':'Thanks,your category is error'}
            return JsonResponse(result)
        limit = json_obj.get('limit')
        if limit not in ['private','public']:
            result = {'code':30103,'error':'Thanks,your limit is error'}
            return JsonResponse(result)
        #带样式的 文章内容
        content = json_obj.get('content')
        #纯文本的 文章内容 -用于做文章简介的切片
        content_text = json_obj.get('content_text')
        introduce = content_text[:30]
        # 创建topic
        Topic.objects.create(
            title=title,
            limit=limit,
            category=category,
            content=content,
            introduce=introduce,
            author=author,

        )
        result = {'code':200,'username':author.username}
        return JsonResponse(result)

    if request.method == 'GET':
        #获取用户文章数据

    if request.method == 'DELETE':
        pass


