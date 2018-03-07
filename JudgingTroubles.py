def main():
    num = int(input())
    dom = {}
    kat = {}
    for i in range(num):
        result = input()
        if result in dom:
            dom[result] += 1
        else:
            dom[result] = 1
            
    for i in range(num):
        result = input()
        if result in kat:
            kat[result] += 1
        else:
            kat[result] = 1
        
    agree = 0    
    for result in dom:
        if result in kat:
            if dom[result] >= kat[result]:
                agree += kat[result]
            else:
                agree += dom[result]
                
    print(agree)
    
main()