import CableColorPairs

def referenceManualCreation():
    number_start = 1
    number_end = 27     

    for colorPairNumber in range(number_start, number_end):
        major_color, minor_color = CableColorPairs.get_color_from_pair_number(colorPairNumber)
        colorPairCodes = CableColorPairs.color_pair_to_string(major_color, minor_color)
        print ("{:<25} {:<25} {:<25}".format(colorPairCodes, major_color, minor_color))
