from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from finance.models import FinancialRecord
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.db.models.functions import TruncMonth

User = get_user_model()


class DashboardSummary(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # 🔐 Analyst/Admin → see ALL users separately
        if user.role in ['admin', 'analyst']:

            users = User.objects.all()
            result = []

            for u in users:
                queryset = FinancialRecord.objects.filter(user=u)

                income = queryset.filter(type='income').aggregate(
                    total=Sum('amount')
                )['total'] or 0

                expense = queryset.filter(type='expense').aggregate(
                    total=Sum('amount')
                )['total'] or 0

                category_totals = queryset.values('category').annotate(
                    total=Sum('amount')
                )

                recent_activity = queryset.order_by('-date')[:5]

                recent_data = [
                    {
                        "id": r.id,
                        "amount": r.amount,
                        "type": r.type,
                        "category": r.category,
                        "date": r.date,
                        "notes": r.notes
                    }
                    for r in recent_activity
                ]

                monthly_trend = queryset.annotate(
                    month=TruncMonth('date')
                ).values('month').annotate(
                    total=Sum('amount')
                ).order_by('month')

                result.append({
                    "user": u.username,
                    "total_income": income,
                    "total_expense": expense,
                    "net_balance": income - expense,
                    "category_totals": list(category_totals),
                    "recent_activity": recent_data,
                    "monthly_trend": list(monthly_trend)
                })

            return Response({
                "scope": "all_users",
                "data": result
            })

        # 👁️ Viewer → only own dashboard
        else:
            queryset = FinancialRecord.objects.filter(user=user)

            income = queryset.filter(type='income').aggregate(
                total=Sum('amount')
            )['total'] or 0

            expense = queryset.filter(type='expense').aggregate(
                total=Sum('amount')
            )['total'] or 0

            category_totals = queryset.values('category').annotate(
                total=Sum('amount')
            )

            recent_activity = queryset.order_by('-date')[:5]

            recent_data = [
                {
                    "id": r.id,
                    "amount": r.amount,
                    "type": r.type,
                    "category": r.category,
                    "date": r.date,
                    "notes": r.notes
                }
                for r in recent_activity
            ]

            monthly_trend = queryset.annotate(
                month=TruncMonth('date')
            ).values('month').annotate(
                total=Sum('amount')
            ).order_by('month')

            return Response({
                "scope": "single_user",
                "user": user.username,
                "total_income": income,
                "total_expense": expense,
                "net_balance": income - expense,
                "category_totals": list(category_totals),
                "recent_activity": recent_data,
                "monthly_trend": list(monthly_trend)
            })