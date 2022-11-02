from rest_framework import serializers
from apps.translator.utils.constants import MAX_VALUE


class NumberSerializer(serializers.Serializer):
    """The number field must be a positive integer lesser than a
    quadrillion"""

    number = serializers.IntegerField(min_value=1, max_value=MAX_VALUE)
