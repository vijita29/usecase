from django.shortcuts import render
from django.http import Http404
from .models import Members
from .serializer import MemberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


# Create your views here.
# class MemberList(APIView):
#     """
#     List all member, or create a new member.
#     """
#     def get(self, request, format=None):
#         members = Members.objects.all()
#         serializer = MemberSerializer(members, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = MemberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberListCreate(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(APIView):
    """
    Retrieve, update or delete a member instance.
    """
    def get_object(self, pk):
        try:
            return Members.objects.get(pk=pk)
        except Members.DoesNotExist:
            raise Http404("Member ID not found")

    def get(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
