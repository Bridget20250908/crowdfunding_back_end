from rest_framework import serializers
from django.apps import apps


class AnswerSerializer(serializers.ModelSerializer):
    # add provider line to answer"
    provider = serializers.ReadOnlyField(source='provider.id')

    class Meta:
        model = apps.get_model('questions.Answer')
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = apps.get_model('questions.Question')
        fields = '__all__'


class QuestionDetailSerializer(QuestionSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get(
            'date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
