## Stack

See the execution of a simple C program and how functions would be pushed onto the stack:

| The Stack      |
| -------------- |
| printMessage() |
| init()         |
| main()         |

```c

void printMessage()
{
  printf("Hello!");
}

void init()
{
  printMessage();
}

int main()
{
  init();

  return 0;
}

```

First, main() is pushed to the stack as it is the entry-point to every program. Then init() is pushed to the stack. Next, printMessage() is added. After the `printf()` completes, `printMessage()` can be popped from the stack, and subsequently `init()` can be popped too. To finish off, there are no more functions to be called in `main()`, so this is popped from the stack, marking the completion of this program.
