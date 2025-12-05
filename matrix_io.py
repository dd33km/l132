import struct


def read_matrices(filename):
    structures = []
    try:
        with open(filename, 'rb') as f:
            k = struct.unpack('i', f.read(4))[0]

            for _ in range(k):
                m = struct.unpack('i', f.read(4))[0]
                n = struct.unpack('i', f.read(4))[0]

                matrix1 = []
                for i in range(m):
                    row = []
                    for j in range(n):
                        val = struct.unpack('f', f.read(4))[0]
                        row.append(val)
                    matrix1.append(row)

                matrix2 = []
                for i in range(m):
                    val = struct.unpack('f', f.read(4))[0]
                    matrix2.append([val])

                structures.append((matrix1, matrix2, m, n))

        return structures
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return []


def write_matrices(filename, results):
    with open(filename, 'wb') as f:
        f.write(struct.pack('i', len(results)))

        for result, m, n in results:
            f.write(struct.pack('i', m))
            f.write(struct.pack('i', n + 1))

            for row in result:
                for val in row:
                    f.write(struct.pack('f', val))


def print_structure(structures, title):
    print(f"\n{title}")
    for idx, (mat1, mat2, m, n) in enumerate(structures):
        print(f"\nСтруктура {idx + 1}:")
        print("Матрица 1:")
        for row in mat1:
            print(' '.join(f"{val:8.2f}" for val in row))
        print("Матрица 2:")
        for row in mat2:
            print(f"{row[0]:8.2f}")


def print_results(results, title):
    print(f"\n{title}")
    for idx, (result, m, n) in enumerate(results):
        print(f"\nРезультат {idx + 1}:")
        for row in result:
            print(' '.join(f"{val:8.2f}" for val in row))


if __name__ == "__main__":
    structures = read_matrices("input_matrices.bin")

    if structures:
        print_structure(structures, "Содержимое первого файла:")

        results = []
        for mat1, mat2, m, n in structures:
            result = []
            for i in range(m):
                row = mat1[i] + mat2[i]
                result.append(row)
            results.append((result, m, n))

        write_matrices("output_matrices.bin", results)

        print_results(results, "Содержимое второго файла:")
