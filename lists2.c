#include <stdio.h>
#include <math.h>

void reverse(int *numbers, int list_size);

int main() {
    int test[] = {1, 7, 3, 6, 11, 67, 23, 5, 2};
    int i;
    for (i = 0; i < 9; i++) {
        printf("%d ", test[i]);
    }
    printf("\n");
    reverse(&test[0], 9);
    for (i = 0; i < 9; i++) {
        printf("%d ", test[i]);
    }
    printf("\n");
    return 0;
}

void reverse(int *numbers, int list_size) {
    // Write function that reverses a list, preferably in place.
    int i;
    for (i = 0; i < ceil(list_size / 2); i++) {
        numbers[i] = numbers[i] ^ numbers[list_size - i - 1];
        numbers[list_size - i - 1] = numbers[i] ^ numbers[list_size - i - 1];
        numbers[i] = numbers[i] ^ numbers[list_size - i - 1];
    }
}
