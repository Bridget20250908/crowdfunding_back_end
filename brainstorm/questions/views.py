from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer, QuestionDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly
from .permissions import IsProviderOrReadOnly


class QuestionList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            question = Question.objects.get(pk=pk)
            self.check_object_permissions(self.request, question)
            return question
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionDetailSerializer(
            instance=question,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsProviderOrReadOnly
    ]

    def get_object(self, pk):
        try:
            answer = Answer.objects.get(pk=pk)
            self.check_object_permissions(self.request, answer)
            return answer
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def put(self, request, pk):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(
            instance=answer,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        answer = self.get_object(pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
