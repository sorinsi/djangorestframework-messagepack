import array
import datetime
import decimal
import uuid

from django.db.models import QuerySet
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.functional import Promise


class MessagePackEncoder:

    @staticmethod
    def encode(obj):
        # Copied from rest_framework.encoders.JSONEncoder
        if isinstance(obj, Promise):
            return force_str(obj)
        elif isinstance(obj, datetime.datetime):
            representation = obj.isoformat()
            if representation.endswith("+00:00"):
                representation = representation[:-6] + "Z"
            return representation
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, datetime.time):
            if timezone and timezone.is_aware(obj):
                raise ValueError("Can't represent timezone-aware times.")
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return str(obj.total_seconds())
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        elif isinstance(obj, QuerySet):
            return tuple(obj)
        elif isinstance(obj, array.array):
            return obj.tolist()
        elif hasattr(obj, "__iter__"):
            return tuple(item for item in obj)
        return obj
