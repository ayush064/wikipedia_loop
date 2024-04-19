from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import wikipedia_loop

class WikipediaLoopView(APIView):
    def post(self, request):
        start_url = request.data.get('url')
        if not start_url:
            return Response({'error': 'URL is required'}, status=400)

        count, visited = wikipedia_loop(start_url)

        return Response({
            'count': count,
            'visited': visited
        })