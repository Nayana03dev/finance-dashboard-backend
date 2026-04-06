from rest_framework import viewsets
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsAnalystOrAdmin


class FinancialRecordViewSet(viewsets.ModelViewSet):
    serializer_class = FinancialRecordSerializer

    def get_queryset(self):
        user = self.request.user

        # Role-based access
        if user.role in ['admin', 'analyst']:
            queryset = FinancialRecord.objects.all()
        else:
            #  Viewer → no access
            queryset = FinancialRecord.objects.none()

        #  Filtering
        record_type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        date = self.request.query_params.get('date')
        user_id = self.request.query_params.get('user_id')  # for analyst/admin

        if record_type:
            queryset = queryset.filter(type=record_type)

        if category:
            queryset = queryset.filter(category__icontains=category)

        if date:
            queryset = queryset.filter(date=date)

        # Analyst/Admin can filter by user
        if user.role in ['admin', 'analyst'] and user_id:
            queryset = queryset.filter(user__id=user_id)

        return queryset

    #  Analyst should NOT create records
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        # Only analyst + admin can view records
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated(), IsAnalystOrAdmin()]

        return [IsAuthenticated(), IsAdmin()] # Only admin can create/update/delete