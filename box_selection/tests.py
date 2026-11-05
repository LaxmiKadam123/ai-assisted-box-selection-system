from decimal import Decimal

from django.test import TestCase

from .models import Product, ShippingBox, Order, OrderItem
from .services import (
    can_product_fit,
    calculate_total_weight,
    recommend_box
)


class BoxSelectionTests(TestCase):

    def setUp(self):
        # Create sample products.
        self.laptop = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=3,
            weight=2
        )

        self.mouse = Product.objects.create(
            name="Mouse",
            length=10,
            width=6,
            height=4,
            weight=0.2
        )

        # Create sample shipping boxes.
        self.small_box = ShippingBox.objects.create(
            name="Small",
            length=35,
            width=25,
            height=10,
            max_weight=3,
            cost=20
        )

        ShippingBox.objects.create(
            name="Medium",
            length=45,
            width=35,
            height=20,
            max_weight=10,
            cost=35
        )

        ShippingBox.objects.create(
            name="Large",
            length=60,
            width=45,
            height=30,
            max_weight=20,
            cost=60
        )

    def test_product_fits_after_rotation(self):
        self.assertTrue(
            can_product_fit(self.laptop, self.small_box)
        )

    def test_calculate_total_order_weight(self):
        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.laptop,
            quantity=1
        )

        OrderItem.objects.create(
            order=order,
            product=self.mouse,
            quantity=1
        )

        total = calculate_total_weight(order)

        self.assertEqual(total, Decimal("2.20"))

    def test_recommend_cheapest_suitable_box(self):
        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.laptop,
            quantity=1
        )

        OrderItem.objects.create(
            order=order,
            product=self.mouse,
            quantity=1
        )

        recommended = recommend_box(order)

        self.assertEqual(recommended, self.small_box)

    def test_no_box_available_for_heavy_order(self):
        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=self.laptop,
            quantity=20
        )

        recommended = recommend_box(order)

        self.assertIsNone(recommended)