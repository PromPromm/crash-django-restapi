from rest_framework.serializers import ModelSerializer
from myapp.models import ItemModel

class ItemSerializer(ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
