from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User

import json

class StatusView(APIView):
	'''
	O método get dessa Class Based View retorna o status do servidor.
	'''

	def get(self, request, format=None):
		try:
			user = User.objects.filter(is_superuser=True)
			return Response(json.dumps(True))
		except Exception as e:
			user = User.objects.filter(is_superuser=True)
			return Response(json.dumps(False))


class OrderView(APIView):
	'''
	O método post dessa Class Based View retorna o uma lista ordenada dada uma lista de entrada.
	'''

	def post(self, request, format=None):
		try:
			print(request.data)
			listaIter = []
			listaStr = request.data['data'].split(',')
			for i in listaStr:listaIter.append(int(i))
			listaIter.sort()
			print(listaIter)
			return Response(listaIter, status=status.HTTP_201_CREATED)
		except Exception as e:
			print(e)
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

class SumView(APIView):
	'''
	O método post dessa Class Based View retorna a soma dada uma lista de entrada.
	'''

	def post(self, request, format=None):
		try:
			print(request.data['data'])
			listaIter = []
			listaStr = request.data['data'].split(',')
			for i in listaStr:listaIter.append(int(i))
			print(sum(listaIter))
			return Response(sum(listaIter), status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

class MaxView(APIView):
	'''
	O método post dessa Class Based View retorna o maior número dada uma lista de entrada.
	'''
	def post(self, request, format=None):
		try:
			print(request.data['data'])
			listaIter = []
			listaStr = request.data['data'].split(',')
			for i in listaStr:listaIter.append(int(i))
			print(max(listaIter))
			return Response(max(listaIter), status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

class MinView(APIView):
	'''
	O método post dessa Class Based View retorna o menor número dada uma lista de entrada.
	'''

	def post(self, request, format=None):
		try:
			print(request.data['data'])
			listaIter = []
			listaStr = request.data['data'].split(',')
			for i in listaStr:listaIter.append(int(i))
			print(min(listaIter))
			return Response(min(listaIter), status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)