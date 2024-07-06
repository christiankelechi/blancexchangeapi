from rest_framework import viewsets

from core_app_root.security.auth.serializer.promptmessage import MessagePrompt
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework import status 
from core_app_root.security.auth import base_url
import requests
from rest_framework.permissions import AllowAny

class MessagePromptViewset(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    http_method_names=['post']
    serializer_class=MessagePrompt
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            print(serializer.data)
            if 'chair' in str(serializer.validated_data['message_body']):
                response=requests.get(f"{base_url.url}complexshapes/chair/")
                
                response=response.json()
                
                return Response({"status":True,"message":"Text Recieved Successfully ready for processing",'data':response},status=status.HTTP_200_OK)
            
            elif 'gear' in str(serializer.validated_data['message_body']):
                response=requests.get(f"{base_url.url}complexshapes/gear/")
                
                response=response.json()
                
                return Response({"status":True,"message":"Text Recieved Successfully ready for processing",'data':response},status=status.HTTP_200_OK)
            
            elif 'hammer' in str(serializer.validated_data['message_body']):
                response=requests.get(f"{base_url.url}complexshapes/hammer/")
                
                response=response.json()
                
                return Response({"status":True,"message":"Text Recieved Successfully ready for processing",'data':response},status=status.HTTP_200_OK)
            elif 'feeder' in str(serializer.validated_data['message_body']) and not ('hole' in str(serializer.validated_data['message_body'])):
                response=requests.get(f"{base_url.url}complexshapes/feeder/")
                
                response=response.json()
                
                return Response({"status":True,"message":"Text Recieved Successfully ready for processing",'data':response},status=status.HTTP_200_OK)
            elif 'savingbox' in str(serializer.validated_data['message_body']):
                response=requests.get(f"{base_url.url}complexshapes/savingbox/")
                
                response=response.json()
                
                return Response({"status":True,"message":"Text Recieved Successfully ready for processing",'data':response},status=status.HTTP_200_OK)
            elif 'bottle' in str(serializer.validated_data['message_body']) and not 'hole' in str(serializer.validated_data['message_body']):
                response=requests.get(f"{base_url.url}complexshapes/bottle/")
                
                response=response.json()
                
                return Response({"status":True,"message":"Text Recieved Successfully ready for processing",'data':response},status=status.HTTP_200_OK)
            elif 'beam' in str(serializer.validated_data['message_body']) and not 'hole' in str(serializer.validated_data['message_body']):
                response=requests.get(f"{base_url.url}complexshapes/beam/")
                
                response=response.json()
                
                return Response({"status":True,"message":"Text Recieved Successfully ready for processing",'data':response},status=status.HTTP_200_OK)
            elif 'bottle' in str(serializer.validated_data['message_body']) and 'hole' in str(serializer.validated_data['message_body']):
                response=requests.get(f"{base_url.url}edit/holow/complexshapes/bottle/")
                
                response=response.json()
                
                return Response({"status":True,"message":"Text Recieved Successfully ready for processing",'data':response},status=status.HTTP_200_OK)
            
            elif 'feeder' in str(serializer.validated_data['message_body']) and  'hole' in str(serializer.validated_data['message_body']):
                response=requests.get(f"{base_url.url}edit/hollow/complexshapes/feeder/")
                
                response=response.json()
                
                return Response({"status":True,"message":"Text Recieved Successfully ready for processing",'data':response},status=status.HTTP_200_OK)
            
            else:
                response=requests.get(f"{base_url.url}edit/hollow/complexshapes/feeder/")
                response=response.json()
                return Response({"status":True,"message":"The asssets cant be generated ,try another one",'data':response},status=status.HTTP_200_OK)
            
        return Response({"status":True,"message":"Text Recieved Successfully ready for processing"},status=status.HTTP_200_OK)