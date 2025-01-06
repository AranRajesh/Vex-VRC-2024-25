#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("This is ADDITION: %f + %f = %f. \n", 19.843, 10.349, 19.843 + 10.349);
    printf("This is SUBTRACTION: %f - %f = %f. \n", 1904.32, 1023.13, 1904.32 - 1023.13);
    printf("This is MULTIPLICATION: %f * %f = %f. \n", 10.3, 15.4, 10.3 * 15.4);
    printf("This is DIVISION: %f / %f = %f. \n", 100.6, 10.2, 100.6 / 10.2);
    printf("This is POWER: 2 ^ 3 = %f. \n", pow(2,3));
    printf("This is SQUARE ROOT: The square root of 36 is %f. \n", sqrt(36));
    printf("This is SQUARE ROOT: The square root of 36 is %f. \n", sqrt(36));
    printf("3.5 rounded up is %f, and 3.5 rounded down is %f. \n", ceil(3.5), floor(3.5));

    printf("Things to remember: \n  - WHEN AN INTEGER DOES ANY OPERATION WITH ANOTHER INTEGER, THE RETURNED ANSWER WILL BE A INTEGER. \n  - IF IT IS AN INTEGER WITH A FLOATING POINT NUMBER, IT WILL BE A DECIMAL.");
    return 0;
}
