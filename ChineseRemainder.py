def main():
    specs = int(input())
    for i in range(specs):
        prob = input().split()
        for n in range(4):
            prob[n] = int(prob[n])
            
        k = prob[1]*prob[3]
        x = (prob[0]*prob[3]*()+prob[2]*prob[1]*())%k
        
        print(x,k)
main()
