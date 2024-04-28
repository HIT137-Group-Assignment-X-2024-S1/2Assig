def separate_and_convert(input_string):
    # Define translation tables to map digits to none and non-digits to empty string
    digit_translation = str.maketrans('', '', '02468')
    non_digit_translation = str.maketrans('', '', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # Separate digits and letters from the input string
    number_string = input_string.translate(non_digit_translation)
    letter_string = input_string.translate(digit_translation)

    # Filter odd numbers and collect lowercase and uppercase letters
    odd_numbers_ascii = ''.join(str(ord(char)) for char in number_string if char.isdigit() and int(char) % 2 != 0)
    all_letters = ''.join(char for char in letter_string if char.isalpha())

    return odd_numbers_ascii, all_letters

input_string = 'aaa89Sergei95104Mar626835Santos456Software100Now80aaa'
number_result, letter_result = separate_and_convert(input_string)

print("Odd Number String:", number_result)
print("All Letters String:", letter_result)