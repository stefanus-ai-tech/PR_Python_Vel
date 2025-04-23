def primeNumbers(size):
    #if size < 10: size = 10
    arr = [True]*size
    arr[0] = arr[1] = False
    for i in range(2, int(size**.5) + 1):
        if arr[i]:
            for j in range(i*i, size, i):
                arr[j] = False
    for i in range(size):
        if arr[i]: p.append(i)
    
def main():
    primeNumbers(3)
    print(p)
    print("Jumlah bilangan prima = ", len(p))
    
if __name__ == "__main__":
    p = []
    main()
