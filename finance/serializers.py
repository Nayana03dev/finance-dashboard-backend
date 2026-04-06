from rest_framework import serializers
from .models import FinancialRecord

class FinancialRecordSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = FinancialRecord
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than 0")
        return value

    def validate_type(self, value):
        if value not in ['income', 'expense']:
            raise serializers.ValidationError("Type must be 'income' or 'expense'")
        return value
