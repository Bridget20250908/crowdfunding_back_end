from rest_framework_import serializers
from django.apps import apps


class FundraiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'