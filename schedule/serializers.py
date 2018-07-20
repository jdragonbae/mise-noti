from rest_framework import serializers

from schedule.models import Schedule


class ScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('scheTitle', 'location', 'date', 'micro_dust')
