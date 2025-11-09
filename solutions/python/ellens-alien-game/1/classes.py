"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class) total_aliens_created : int
        Tracks the total number of Alien instances created.
    x_coordinate : int
        Position on the x-axis.
    y_coordinate : int
        Position on the y-axis.
    health : int
        Number of health points, starts at 3.

    Methods
    -------
    hit() :
        Decrement Alien health by one point.
    is_alive() -> bool :
        Return True if Alien health > 0, else False.
    teleport(new_x_coordinate, new_y_coordinate) :
        Move Alien object to new coordinates.
    collision_detection(other) :
        Implementation TBD.
    """

    total_aliens_created = 0  # Class attribute to track total aliens

    def __init__(self, x_coordinate: int, y_coordinate: int):
        """Initialize an Alien with given coordinates and default health."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Decrement Alien health by one point, not below zero."""
        if self.health > 0:
            self.health -= 1

    def is_alive(self) -> bool:
        """Return True if Alien health is greater than zero."""
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        """Move Alien to new (x, y) coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other) -> None:
        """Placeholder for future collision detection implementation."""
        pass


def new_aliens_collection(coordinates: list[tuple[int, int]]) -> list[Alien]:
    """Create a list of Alien instances from a list of (x, y) coordinate pairs.

    Parameters
    ----------
    coordinates : list[tuple[int, int]]
        List of coordinate pairs for Alien placement.

    Returns
    -------
    list[Alien]
        List of created Alien instances.
    """
    return [Alien(x, y) for x, y in coordinates]
