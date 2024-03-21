from django.shortcuts import render
from rest_framework.decorators import api_view
import openai
import requests
from .models import Openai
import random
from .serializers import OpenaiSerializer 
from rest_framework.response import Response
api_key='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'
openai.api_key=api_key
# Create your views here.
@api_view(['POST'])
def get_image_from_text(request):
    data = request.data 
    if request.method == 'POST' and 'user_input' in data:
        user_input = data['user_input']
        response = openai.Image.create(
            prompt=user_input,
            size='256x256'
        )
        img_url = response['data'][0]['url']
        
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            unique_numbers = random.sample(range(1, 1001), 1000)
            count = random.choice(unique_numbers)
            fname = f"image-{count}.jpg"

            openai_obj = Openai.objects.create(
                user_input=user_input,
                image=img_url
            )
            serializer = OpenaiSerializer(openai_obj, many=False)
            return Response(serializer.data)
        else:
            return Response({"message": "Failed to fetch image from URL."}, status=img_response.status_code)
    else:
        return Response({"message": "Invalid request method or missing 'user_input' parameter."}, status=400)

@api_view(['GET'])
def getdata(request):
    openai=Openai.objects.all()
    serializer=OpenaiSerializer(openai, many=True)
    return Response(serializer.data)

