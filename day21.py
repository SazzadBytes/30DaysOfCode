'''Generic 
There is no option for submitting in python 
may be we can implement generic like this '''

from typing import List, TypeVar

T = TypeVar('T')  # Define a type variable

def printArray(a: List[T]) -> None:
    """Print each element of the generic list on a new line."""
    for element in a:
        print(element)

def main():
    n = int(input())
    int_list = [int(input()) for _ in range(n)]

    n = int(input())
    string_list = [input() for _ in range(n)]
    
    print("Item Printed")
    printArray(int_list)
    printArray(string_list)

if __name__ == "__main__":
    main()
