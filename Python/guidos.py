EXPECTED_BAKE_TIME=40

def bake_time_remaining(bake):
    
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    remaining=EXPECTED_BAKE_TIME-bake
    return remaining


def preparation_time_in_minutes(number_of_layers):
    
    """Calculate the preparation itme.

    :param total2: number_of_layers * int.
    :return: number_of_layers * int (in minutes) derived from preparation_time_in_minutes.

    Function that takes the number of layers in the lasagna and the time of each layer.
    """
    
    total2=number_of_layers*2
    return total2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    
    """Calculate the preparation itme.

    :param total3: (number_of_layers*int)+elapsed_bake_time
    :return: (number_of_layers*int)+elapsed_bake_time derived from elapsed_time_in_minutes.

    Function that takes the number of layers in the lasagna and the time of each layer, and add to the elapsed bake time.
    """
    
    total3=(number_of_layers*2)+elapsed_bake_time
    return total3