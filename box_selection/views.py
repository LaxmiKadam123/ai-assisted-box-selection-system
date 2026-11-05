from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order, OrderItem
from .serializers import OrderInputSerializer
from .services import recommend_box, calculate_total_weight


class BoxRecommendationView(APIView):

    def post(self, request):
        serializer = OrderInputSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create a new order.
        order = Order.objects.create()

        # Add products to the order.
        for item in serializer.validated_data["items"]:
            OrderItem.objects.create(
                order=order,
                product_id=item["product_id"],
                quantity=item["quantity"]
            )

        # Calculate weight and recommend a box.
        total_weight = calculate_total_weight(order)
        box = recommend_box(order)

        if box:
            recommendation = {
                "id": box.id,
                "name": box.name,
                "cost": str(box.cost),
                "max_weight": str(box.max_weight)
            }
        else:
            recommendation = None

        return Response(
            {
                "order_id": order.id,
                "total_weight": str(total_weight),
                "recommended_box": recommendation,
                "message": (
                    "Suitable box found."
                    if box
                    else "No suitable shipping box available."
                )
            },
            status=status.HTTP_200_OK
        )