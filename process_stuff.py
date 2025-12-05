def process_numbers():
    try:
        with open('number1.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        numbers = []
        for line in lines:
            row = list(map(float, line.strip().split()))
            numbers.append(row)

        differences = []
        for i in range(len(numbers) - 1):
            diff_row = []
            max_len = max(len(numbers[i]), len(numbers[i + 1]))
            for j in range(max_len):
                val1 = numbers[i][j] if j < len(numbers[i]) else 0
                val2 = numbers[i + 1][j] if j < len(numbers[i + 1]) else 0
                diff_row.append(val1 - val2)
            differences.append(diff_row)

        with open('number3.txt', 'w', encoding='utf-8') as f:
            for row in differences:
                f.write(' '.join(map(str, row)) + '\n')
                print(' '.join(map(str, row)))

        all_nums = [num for row in differences for num in row]
        count_div5 = sum(1 for num in all_nums if num % 5 == 0)

        with open('number2.txt', 'a', encoding='utf-8') as f:
            f.write(f"\nResult = {count_div5}\n")

        print(f"Result = {count_div5}")

    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")


def process_text():
    try:
        with open('text1.txt', 'r', encoding='utf-8') as f:
            content = f.read()

        words = content.split()
        reversed_words = [word[::-1] for word in words]

        with open('text2.txt', 'w', encoding='utf-8') as f:
            f.write(' '.join(reversed_words))

        print("Текст обработан и записан в text2.txt")

    except FileNotFoundError:
        print("Файл text1.txt не найден")


if __name__ == "__main__":
    process_numbers()
    process_text()