def roman_to_int(user_roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(user_roman) == 0:
        return None

    prev_symbol = user_roman[-1]
    if prev_symbol not in roman_numerals:
        return None

    result = roman_numerals[prev_symbol]

    for current_symbol in user_roman[-2::-1]:
        result_prev = roman_numerals[prev_symbol]

        if current_symbol not in roman_numerals:
            return None
        result_curr = roman_numerals[current_symbol]

        if result_curr >= result_prev:
            result += result_curr
        else:
            result -= result_curr
        prev_symbol = current_symbol
    return result


def main():
    full_str = input()

    for word in full_str.split(' '):
        dec_number = roman_to_int(word)
        if dec_number is None:
            print(word, end=' ')
        else:
            print(dec_number, end=' ')


if __name__ == "__main__":
    main()
