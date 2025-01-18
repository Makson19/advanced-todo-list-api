from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, pagination
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task
from tasks.serializers import TaskSerializer


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'per'


class TaskCreateListView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completed']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['-id']
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
    

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

