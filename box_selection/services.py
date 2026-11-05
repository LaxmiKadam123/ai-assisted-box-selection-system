from itertools import permutations
from decimal import Decimal

from .models import Product, ShippingBox, Order, OrderItem

def can_product_fit(product, box):
    product_dimensions = [
        product.length,
        product.width,
        product.height
    ]

    box_dimensions = [
        box.length,
        box.width,
        box.height
    ]

    # Check all possible product rotations
    for dimensions in permutations(product_dimensions):
        if all(
            dimensions[i] <= box_dimensions[i]
            for i in range(3)
        ):
            return True

    return False



def calculate_total_weight(order):
    total_weight = Decimal("0.00")

    for item in order.items.all():
        total_weight += item.product.weight * item.quantity

    return total_weight



def can_pack_order(order, box):
    # Create a list containing every individual product.
    products = []

    for item in order.items.all():
        for _ in range(item.quantity):
            products.append(item.product)

    # Try to place larger products first.
    products.sort(
        key=lambda p: p.length * p.width * p.height,
        reverse=True
    )

    # Initially, the entire box is empty.
    free_spaces = [
        (box.length, box.width, box.height)
    ]

    for product in products:
        product_dimensions = (
            product.length,
            product.width,
            product.height
        )

        best_choice = None

        # Check every available empty space and product rotation.
        for space_index, space in enumerate(free_spaces):
            for dimensions in permutations(product_dimensions):
                if all(
                    dimensions[i] <= space[i]
                    for i in range(3)
                ):
                    unused_volume = (
                        space[0] * space[1] * space[2]
                        - dimensions[0] * dimensions[1] * dimensions[2]
                    )

                    if best_choice is None or unused_volume < best_choice[0]:
                        best_choice = (
                            unused_volume,
                            space_index,
                            dimensions
                        )

        # If no empty space can accommodate this product, packing fails.
        if best_choice is None:
            return False

        _, space_index, dimensions = best_choice
        space = free_spaces.pop(space_index)

        # Divide the remaining empty area into three non-overlapping spaces.
        dx, dy, dz = dimensions
        sx, sy, sz = space

        remaining_spaces = [
            (sx - dx, sy, sz),
            (dx, sy - dy, sz),
            (dx, dy, sz - dz)
        ]

        for remaining_space in remaining_spaces:
            if all(value > 0 for value in remaining_space):
                free_spaces.append(remaining_space)

    return True



def recommend_box(order):
    total_weight = calculate_total_weight(order)

    suitable_boxes = []

    for box in ShippingBox.objects.all():

        # Check weight capacity first.
        if total_weight > box.max_weight:
            continue

        # Check whether all products fit inside the box.
        if can_pack_order(order, box):
            suitable_boxes.append(box)

    # Sort suitable boxes by cost (lowest first).
    suitable_boxes.sort(key=lambda box: box.cost)

    if suitable_boxes:
        return suitable_boxes[0]

    return None