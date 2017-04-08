from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User

import json

class StatusView(APIView):

	def get(self, request, format=None):
		try:
			user = User.objects.filter(is_superuser=True)
			return Response(json.dumps(True))
		except Exception as e:
			user = User.objects.filter(is_superuser=True)
			return Response(json.dumps(False))
		

	def post(self, request, format=None):
		try:
			listaIter = []
			listaStr = request.data.split(',')
			for i in listaStr:listaIter.append(int(i))
			listaIter.sort()
			print(listaIter)
			return Response(listaIter, status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)
