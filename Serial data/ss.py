import time

def main():
    mls1 = 0
    for i in range(5):
        print(i)
        time.sleep(1)
        L = i
    mls = L/60
    # al[9] = mlsㄜ
    mls1 = mls1 + mls
    print(mls1)
    time.sleep(1)


if __name__ == "__main__":
    main()
    