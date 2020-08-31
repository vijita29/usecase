from rest_framework import serializers
from .models import Claims
from members.models import Members


class ClaimSerializer(serializers.ModelSerializer):
    claim_id = serializers.CharField(source='id', read_only=True)

    class Meta:
        model = Claims
        fields = ['claim_id', 'member_id', 'claim_date', 'billed_amount', 'paid_amount', 'provider_name',
                  'claim_type']
