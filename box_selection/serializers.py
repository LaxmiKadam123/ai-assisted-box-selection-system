from rest_framework import serializers
from .models import Order, OrderItem, Product


class OrderItemInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class OrderInputSerializer(serializers.Serializer):
    items = OrderItemInputSerializer(many=True)

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError(
                "An order must contain at least one product."
            )

        for item in value:
            if not Product.objects.filter(id=item["product_id"]).exists():
                raise serializers.ValidationError(
                    f"Product with ID {item['product_id']} does not exist."
                )

        return value