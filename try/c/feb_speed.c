#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int64_t feb(int64_t* cache, int32_t count)
{
    if ((count == 1) + (count == 0)) {
        return 1;
    };
    if (cache[count] == 0) {
        return cache[count];
    };
    cache[count] = feb(cache, --count) + feb(cache, --count);
    return cache[count];
};

int main()
{
    int32_t count;
    printf("�٣����Ҹ����֣���̫��");
    scanf("%d", &count);
    printf("��Ҫ����� %d ��feb\n", count);
    int64_t* cache;
    cache = calloc(count, sizeof(int64_t));

    int64_t result = feb(cache, count);

    printf("%d", result);

    return 0;
}