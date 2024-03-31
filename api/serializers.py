from rest_framework import serializers

class TalabaSerilazers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    first_name = serializers.CharField(max_length = 124)
    last_name = serializers.CharField(max_length = 124)
    age = serializers.IntegerField()
    country = serializers.CharField(max_length = 124)

