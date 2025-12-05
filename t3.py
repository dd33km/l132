def check_brackets(filename):
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    opening = set(brackets.keys())
    closing = set(brackets.values())

    stack = []
    bracket_counts = {'(': 0, '{': 0, '[': 0}

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"Проверка файла: {filename}")
        print("Содержимое файла:")
        print(content)
        print()

        line_num = 1
        col_num = 1

        for char in content:
            if char == '\n':
                line_num += 1
                col_num = 1
                continue

            if char in opening:
                stack.append((char, line_num, col_num))
                bracket_counts[char] += 1

            elif char in closing:
                if not stack:
                    print(f"ОШИБКА: Закрывающая скобка '{char}' без соответствующей открывающей")
                    print(f"Позиция: строка {line_num}, столбец {col_num}")
                    return False

                last_opening, open_line, open_col = stack.pop()

                if brackets[last_opening] != char:
                    print(f"ОШИБКА: Несоответствие скобок")
                    print(f"Открывающая '{last_opening}' на строке {open_line}, столбце {open_col}")
                    print(f"Закрывающая '{char}' на строке {line_num}, столбце {col_num}")
                    return False

            col_num += 1

        if stack:
            print("ОШИБКА: Есть незакрытые скобки:")
            for bracket, line, col in stack:
                print(f"'{bracket}' на строке {line}, столбце {col}")
            return False

        print("ПРОВЕРКА ПРОЙДЕНА УСПЕШНО")
        print()
        print("Статистика скобок:")
        print(f"Круглые скобки (): {bracket_counts['(']}")
        print(f"Фигурные скобки: {bracket_counts['{']}")
        print(f"Квадратные скобки []: {bracket_counts['[']}")
        print()
        print("Все скобки правильно открыты и закрыты")

        return True

    except FileNotFoundError:
        print(f"ОШИБКА: Файл '{filename}' не найден")
        return False
    except Exception as e:
        print(f"ОШИБКА при чтении файла: {e}")
        return False


def task3():
    check_brackets('program.c')


if __name__ == "__main__":
    task3()