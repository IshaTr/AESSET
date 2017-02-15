from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from seating_manager.models import Student
from .serializers import QuerySerializer


@api_view(['POST'])
def RequestQuery(request):
    if request.method == 'POST':
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            query_obj = serializer.save()
            SendEmail(query_obj.email)
            return HttpResponse("Email has been sent")

        else:
            return Response(serializer.errors)


# python -m smtpd -n -c DebuggingServer localhost:1025
# To test please run the smtp server
def SendEmail(email):
    message = ("Hello there")
    send_mail("hello", message, "hey@sharda.ac.in", [email])


# class RequestQueryView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'index.html'

#     def post(self, request):
#         serializer = QuerySerializer(data=request.data)
#         if serializer.is_valid():
#             query_obj = serializer.save()
