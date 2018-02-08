from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    EmailField,
    ValidationError,
    HyperlinkedIdentityField,
    SerializerMethodField,
    )

from django.contrib.auth import get_user_model
from django.db.models import Q

from products.models import Product
from accounts.api.serializers import ProfileSerializer

User = get_user_model()


class ProductsSerializer(ModelSerializer):
    user = SerializerMethodField(read_only=True)
    category = SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'user',
            'category',
            'name',
            'price',
            'discount',
            'quantity',
            'number_of_sales',
            'number_of_views',
            'avg_rate',
            'description',
            'image',
            'avg_rate',
            'slug',
            'slider',
            'publish',
            'block_review',
            'added',
            'updated',
        ]

    def get_user(self, obj):
        return str(obj.user)

    def get_category(self, obj):
        return str(obj.category)