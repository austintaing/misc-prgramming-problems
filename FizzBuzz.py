# ProblemID: fizzbuzz


def main():
    params = input()
    params = params.split()
    for i in range(len(params)):
        params[i] = int(params[i])
        
    for i in range(1, params[2]+1):
        out = ''
        if i % params[0] == 0:
            out += "Fizz"
        if i % params[1] == 0:
            out += "Buzz"
        if out == '':
            out = i
            
        print(out)
        
main()