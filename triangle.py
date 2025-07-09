class Triangle:
    """Simple representation of a geometric triangle defined by the length of its three sides."""

    def __init__(self, side1: float, side2: float, side3: float) -> None:
        """Initialize a Triangle with three side lengths.
        Args:
            side1: Length of the first side.
            side2: Length of the second side.
            side3: Length of the third side.
        Raises:
            ValueError: If any side length is not positive.
        """
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All side lengths must be positive numbers.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        """Calculate and return the perimeter of the triangle."""
        return self.side1 + self.side2 + self.side3


def calculate_perimeter(triangle: Triangle) -> float:
    """Return the perimeter of the given Triangle instance.

    Args:
        triangle: An instance of the Triangle class.

    Returns:
        The perimeter of the triangle.
    """
    return triangle.perimeter()