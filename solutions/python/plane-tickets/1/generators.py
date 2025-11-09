"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    row_letters = ("A", "B", "C", "D")

    current = 0
    while current < number:
        yield row_letters[current % len(row_letters)]
        current += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats_in_row = 4
    current_seat = 1
    current_row = 1
    row_idx = 1
    seat_letters = generate_seat_letters(number)

    while current_seat <= number:
        if current_row == 13:
            current_row += 1

        yield f'{current_row}{seat_letters.__next__()}'

        if row_idx == seats_in_row:
            row_idx = 1
            current_row += 1
            current_seat += 1
        else:
            row_idx += 1
            current_seat += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = generate_seats(len(passengers))
    return {name: next(seats) for name in passengers}


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        yield f'{seat}{flight_id}'.ljust(12, '0')