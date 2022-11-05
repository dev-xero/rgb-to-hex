def rgb_to_hex(rgb: str, out_format: str = 'native'):
    # Convert an rgb string sequence to a hex value
    # The format for the data is r,g,b so these will be in an array latter

    # Convert the string into an array
    rgb_arr = rgb.replace(' ', '').split(',')

    # Check if it's length is not anything else but three
    if len(rgb_arr) == 3 and not rgb_arr.__contains__(''):  # Check for empty strings too
        # Construct a HEX code from the loop

        # Is the string valid?
        is_valid_string: bool = False

        # Check the format for the output defaults to 'native'
        if out_format == 'native':
            hex_value = '0x'
        elif out_format == 'color':
            hex_value = '#'
        else:
            hex_value = ''

        # Loop through the items
        for value in rgb_arr:
            # Convert the str into an int value
            int_value = int(value)

            if 0 <= int_value <= 255:
                hex_value += '%x' % int_value
                is_valid_string = True
            else:
                print('That\'s not a valid RGB color')
                is_valid_string = False
                break

        # Print no answer if the string is not valid
        if is_valid_string:
            if out_format == 'color':
                print(f'Your Input: {rgb} -> HEX Code: {str(hex_value).upper()} (color mode)')
            else:
                print(f'Your Input: {rgb} -> HEX Code: {hex_value} (native mode)')

    else:
        print('That isn\'t a valid input')


# Try it out -> '255, 255, 255', 'color'
rgb_to_hex(str(input('Enter a valid RGB string (comma separated): ')), str(input('Formatting Mode (color/ native): ')))
