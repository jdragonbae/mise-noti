from rest_framework import serializers

from schedule.models import Schedule


class ScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'summary', 'location', 'timezone', 'micro_dust')
