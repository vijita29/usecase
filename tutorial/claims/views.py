from django.shortcuts import render
from django.http import Http404
from .models import Claims
from .serializer import ClaimSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import datetime
from django.db.models import Sum


# Create your views here.
class ClaimListCreate(generics.ListCreateAPIView):
    queryset = Claims.objects.all()
    serializer_class = ClaimSerializer


class ClaimDetail(APIView):
    """
    Retrieve, update or delete a claim instance.
    """
    def get_object(self, pk):
        try:
            return Claims.objects.get(pk=pk)
        except Claims.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        claim = self.get_object(pk)
        serializer = ClaimSerializer(claim)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        claim = self.get_object(pk)
        serializer = ClaimSerializer(claim, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        claim = self.get_object(pk)
        claim.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClaimFilterList(generics.GenericAPIView):
    def get_queryset(self):
        claim_start_date = self.request.query_params.get('claim_start_date', None)
        claim_end_date = self.request.query_params.get('claim_end_date', None)
        claim_periods_in_months = self.request.query_params.get('claim_periods_in_months', None)
        claim_type = self.request.query_params.get('claim_type', None)
        if claim_type:
            if claim_start_date and claim_end_date:
                query = Claims.objects.filter(claim_type=claim_type, claim_date__range=[claim_start_date, claim_end_date])
            elif claim_periods_in_months:
                enddate = datetime.date.today()
                startdate = enddate - datetime.timedelta(days=int(claim_periods_in_months)*30)
                query = Claims.objects.filter(claim_type=claim_type,
                                              claim_date__range=[startdate, enddate])
            else:
                query = Claims.objects.filter(claim_type=claim_type)
        else:
            if claim_start_date and claim_end_date:
                query = Claims.objects.filter(claim_type=claim_type,
                                              claim_date__range=[claim_start_date, claim_end_date])
            elif claim_periods_in_months:
                enddate = datetime.date.today()
                startdate = enddate - datetime.timedelta(days=int(claim_periods_in_months) * 30)
                query = Claims.objects.filter(claim_type=claim_type,
                                              claim_date__range=[startdate, enddate])
            else:
                query = Claims.objects.all()
        return query

    def get(self, request):
        claims = self.get_queryset()
        serializer = ClaimSerializer(claims, many=True)
        summary = {
            "total_billed_amount": claims.aggregate(Sum('billed_amount'))['billed_amount__sum'],
            "total_paid_amount": claims.aggregate(Sum('paid_amount'))['paid_amount__sum']
        }
        return_data = {"summary": summary, "claims_set": serializer.data}
        return Response(return_data)

