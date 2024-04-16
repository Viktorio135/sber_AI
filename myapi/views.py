from django.shortcuts import render
from django.http import JsonResponse
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

import json

def get_answer(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
        
    text = body_data.get('message')
    if text != None:
        chat = GigaChat(credentials='YmFhOTAzMGMtNTg1ZS00N2Q5LWE1MDEtNzU3MjA4ZjQzZDQzOmFlOTIxOGMyLWJiOGEtNGI2Yy04YmE5LWU2YWQ2YzgzNDRjNA==', verify_ssl_certs=False)
        messages = [
            SystemMessage(
                content="Ты обычный ИИ чат"
            )
        ]
        messages.append(HumanMessage(content=text))
        res = chat(messages)
        messages.append(res)
        return JsonResponse({'answer': res.content})
    else:
         return JsonResponse({'answer': 'Пост запрос говно'})
        