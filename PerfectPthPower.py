def main():
    x = int(input())
    while x != 0:
        k = 31
        done = False
        while k>1 and not done:
            l = int(abs(x)**(1/k)-1)
            m = int(abs(x)**(1/k))
            u = int(abs(x)**(1/k)+1)
            if l**k == abs(x) or m**k == abs(x) or u**k == abs(x):
                done = True
            else:
                if x < 0:
                    k -= 1
                k -= 1
        print(k)
        x = int(input())
main()