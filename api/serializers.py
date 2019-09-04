from rest_framework import serializers


class BranchInfoSerializer(serializers.Serializer):
    ifsc = serializers.CharField()
    bank_id = serializers.IntegerField()
    branch = serializers.CharField(required=True)
    address = serializers.CharField()
    city = serializers.CharField()
    district = serializers.CharField()
    state = serializers.CharField()
