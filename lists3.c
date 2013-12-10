#include<stdio.h>
#include<stdbool.h>

bool in_list(int number, int list[], int list_size);

int main() {
    int test[] = {1, 7, 3, 6, 11, 67, 23, 5, 2};
    bool result = in_list(8, test, 9);
    printf("%d\n", result); // false
    result = in_list(5, test, 9);
    printf("%d\n", result); // true
    return 0;
}

bool in_list(int number, int list[], int list_size) {
    int i;
    bool found = false;
    for (i = 0; i < list_size; i++) {
        if (list[i] == number) {
            found = true;
            break;
        }
    }
    return found;
}
