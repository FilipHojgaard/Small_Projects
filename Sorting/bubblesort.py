import random

def randomArray(*args):
    if len(args) > 0:
        # Len argument given
        arr_len = int(args[0])
        arr = []
        for i in range(0,arr_len):
            arr.append(random.randint(0,100))
    else:
        # No len argument given. Make a random length
        arr_len = random.randint(10,50)
        arr = []
        for i in range(0, arr_len):
            arr.append(random.randint(0,100))
    return arr


def bubblesort(arr):
    print(arr)
    swaps = 0
    worst_case = len(arr)**2
    for i in range(len(arr), 0, -1):
        for j in range(0, i-1):
            if (arr[j] > arr[j+1]):
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
    print(f"worst case: {worst_case}")
    print(f"Actual swaps: {swaps}")
    return arr


def main():
    randomArray()
    bubblesort(randomArray())

if __name__ == "__main__":
    main()
