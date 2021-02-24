import CableColorPairs

def test_number_to_pair(pair_number,expected_major_color, expected_minor_color):
    major_color, minor_color = CableColorPairs.get_color_from_pair_number(pair_number)
    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = CableColorPairs.get_pair_number_from_color(major_color, minor_color)
    assert(pair_number == expected_pair_number)     

if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('Done :)')
