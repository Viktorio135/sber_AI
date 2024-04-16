import requests
import json

from django import template
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

register = template.Library()


@register.simple_tag()
def generate_answer(text):
    chat = GigaChat(credentials='YmFhOTAzMGMtNTg1ZS00N2Q5LWE1MDEtNzU3MjA4ZjQzZDQzOmFlOTIxOGMyLWJiOGEtNGI2Yy04YmE5LWU2YWQ2YzgzNDRjNA==', verify_ssl_certs=False)

    messages = [
        SystemMessage(
            content=""
        )
    ]

    messages.append(HumanMessage(content=text))
    res = chat(messages)
    messages.append(res)
    return res.content
        