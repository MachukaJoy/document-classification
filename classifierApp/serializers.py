from rest_framework import serializers
from .models import Result

class DocumentClassifySerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
    fields = ('imagepath','image','predicted','confidence','saved')