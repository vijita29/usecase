from rest_framework import serializers
from .models import Accumulator
from members.models import Members


class AccumulatorSerializer(serializers.ModelSerializer):
    accumulator_id = serializers.CharField(source='id', read_only=True)

    class Meta:
        model = Accumulator
        fields = ['accumulator_id', 'member_id', 'ind_deduct_limit', 'ind_deduct_used', 'ind_ofp_limit', 'ind_ofp_used',
                  'family_deduct_limit', 'family_deduct_used', 'family_ofp_limit', 'family_ofp_used']


class MemberAccumulatorSerializer(serializers.ModelSerializer):
    member_id = serializers.CharField(source='id')
    accumulator_list = AccumulatorSerializer(many=True, source='accumulator')

    class Meta:
        model = Members
        fields = ['member_id', 'member_name', 'accumulator_list']