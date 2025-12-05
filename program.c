#include <stdio.h>
#include <stdlib.h>

int main() {
    int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int sum = 0;

    for (int i = 0; i < 10; i++) {
        sum += array[i];
        printf("Element[%d] = %d\n", i, array[i]);
    }

    if (sum > 50) {
        printf("Sum is greater than 50: %d\n", sum);
    } else {
        printf("Sum is less or equal to 50: %d\n", sum);
    }

    return 0;
}