from django.shortcuts import render
from django.http import Http404
from members.models import Members
from .models import Accumulator
from .serializer import AccumulatorSerializer, MemberAccumulatorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


# Create your views here.
class AccumulatorListCreate(generics.ListCreateAPIView):
    queryset = Accumulator.objects.all()
    serializer_class = AccumulatorSerializer


class MemberAccumulatorList(generics.ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberAccumulatorSerializer


class AccumulatorDetails(APIView):
    """
    Retrieve, update or delete a instance.
    """
    def get_object(self, pk):
        try:
            return Accumulator.objects.get(pk=pk)
        except Accumulator.DoesNotExist:
            raise Http404("Member ID not found")

    def get(self, request, pk, format=None):
        accumulator = self.get_object(pk)
        serializer = AccumulatorSerializer(accumulator)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        accumulator = self.get_object(pk)
        serializer = AccumulatorSerializer(accumulator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        accumulator = self.get_object(pk)
        accumulator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
