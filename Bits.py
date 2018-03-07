# ProblemID: bits


def main():
    num = int(input())
    
    for i in range(num):
        val = input()
        max1 = 0
        for j in range(1,len(val)+1):
            bs = bin(int(val[:j]))
            num1 = 0
            for b in bs:
                if b == '1':
                    num1 += 1
                    
            if num1 > max1:
                max1 = num1
        print(max1)

main()