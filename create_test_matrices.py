import struct

k = 2
structures = [
    {
        'm': 3,
        'n': 3,
        'matrix1': [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ],
        'matrix2': [
            [10.0],
            [20.0],
            [30.0]
        ]
    },
    {
        'm': 2,
        'n': 2,
        'matrix1': [
            [1.5, 2.5],
            [3.5, 4.5]
        ],
        'matrix2': [
            [5.5],
            [6.5]
        ]
    }
]

with open('input_matrices.bin', 'wb') as f:
    f.write(struct.pack('i', k))

    for s in structures:
        f.write(struct.pack('i', s['m']))
        f.write(struct.pack('i', s['n']))

        for row in s['matrix1']:
            for val in row:
                f.write(struct.pack('f', val))

        for row in s['matrix2']:
            f.write(struct.pack('f', row[0]))

print("Тестовый файл input_matrices.bin создан")