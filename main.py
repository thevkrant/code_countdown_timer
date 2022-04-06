import time

def timer():
    list1 = []
    start = time.perf_counter()
    for i in range(10000000):
        list1.append(i**2)
    end = time.perf_counter()
    return f'Code Run time is {end - start:0.2f} seconds'

if __name__ == "__main__":
    print(timer())
