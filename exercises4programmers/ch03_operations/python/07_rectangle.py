'''
pseudocode

get_length_and_width
    length: int = int(input("What is the length of the room in feet? "))
    width: int = int(input("What is the width of the room in feet? "))
end

calculate_feet_to_meter
    squre_meter: float = round(square_feet * 0.09290304, 3)
end

calculate_squre_feet
    squre_feet = length * width
end

main
    length, width = get_length_and_width()
    squre_feet = calculate_squre_feet(length, width)
    squre_meter = calculate_feet_to_meter(squre_feet)
    print_out result
end
'''
SQUARE_METER = 0


def get_length_and_width() -> tuple:
    '''get length and width from std input'''
    length: int = int(input("What is the length of the room in feet? "))
    width: int = int(input("What is the width of the room in feet? "))
    return length, width


def calculate_feet_to_meter(square_feet: int) -> float:
    square_meter: float = round(square_feet * 0.09290304, 3)
    return square_meter


def calculate_square(length: int, width: int) -> int:
    return length * width


def rectangle_squre():
    '''calculate rectangle square from feet into meter'''
    length, width = get_length_and_width()
    square_feet = calculate_square(length, width)
    global SQUARE_METER
    SQUARE_METER = calculate_feet_to_meter(square_feet)

    print(f'''You entered dimensions of {length} feet by {width} feet
The area is
{square_feet} square feet
{SQUARE_METER} square meters''')


if __name__ == '__main__':
    rectangle_squre()
