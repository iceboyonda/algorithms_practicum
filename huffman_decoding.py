def huffman_decode(encoded_text, huffman_codes):
    # Создаем обратное отображение кодов
    reverse_codes = {code: char for char, code in huffman_codes.items()}

    decoded_text = []
    current_code = ""

    # Проходим по закодированной строке
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text.append(reverse_codes[current_code])
            current_code = ""

    return ''.join(decoded_text)


def main():
    # Ввод данных
    input_data = [
        "12 60",
        "' ': 1011",
        "'.': 1110",
        "'D': 1000",
        "'c': 000",
        "'d': 001",
        "'e': 1001",
        "'i': 010",
        "'m': 1100",
        "'n': 1010",
        "'o': 1111",
        "'s': 011",
        "'u': 1101",
        "100011110001001101000111111011001010011000010110011010111110"
    ]

    # Чтение количества уникальных символов и размера закодированной строки
    first_line = input_data[0].split()
    unique_chars_count = int(first_line[0])

    # Чтение кодов символов
    huffman_codes = {}
    for line in input_data[1:unique_chars_count + 1]:
        char_code = line.split(': ')
        char = char_code[0].strip("'")
        code = char_code[1]
        huffman_codes[char] = code

    # Чтение закодированной строки
    encoded_text = input_data[unique_chars_count + 1]

    # Декодирование строки
    decoded_string = huffman_decode(encoded_text, huffman_codes)

    # Вывод результата
    print(decoded_string)


# Запуск основной функции
if __name__ == "__main__":
    main()
