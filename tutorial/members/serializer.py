from rest_framework import serializers
from .models import Members


class MemberSerializer(serializers.ModelSerializer):
    member_id = serializers.CharField(source='id', read_only=True)

    class Meta:
        model = Members
        fields = ['member_id', 'member_name']
