# ProblemID: cargame


def main():
    specs = input().split()
    specs[0] = int(specs[0])
    specs[1] = int(specs[1])
    
    dictionary = []
    for i in range(specs[0]):
        dictionary.append(input())
    dictionary.sort()
    
    for i in range(specs[1]):
        prefix = input().lower()
        i = 0
        done = False
        word = "No valid word"
        while i<len(dictionary) and not done:
            if prefix[0] in dictionary[i]:
                j = dictionary[i].find(prefix[0])
                if prefix[1] in dictionary[i][j+1:]:
                    k = dictionary[i][j+1:].find(prefix[1])
                    if prefix[2] in dictionary[i][j+k+2:]:
                        word = dictionary[i]
                        done = True
            i += 1
        print(word)
            
main()