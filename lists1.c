#include <stdio.h>

int max(int numbers[], int list_size);

int main() {
    int test[] = {1, 7, 3, 6, 11, 67, 23, 5, 2};
    int result = max(test, 9);
    printf("%d\n", result);
}

int max(int numbers[], int list_size) {
    // Write a function that returns the largest element in a list.
    int i;
    int largest = 0;
    for (i = 0; i < list_size; i++) {
        if (numbers[i] > largest) {
            largest = numbers[i];
        }
    }
    return largest;
}
