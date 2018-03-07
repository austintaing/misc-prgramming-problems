# ProblemID: guessinggame


def main():
    low = 0
    high = 11
    guess = int(input())
    while guess != 0:
        result = input()
        if result == "too high":
            if guess < high:
                high = guess
        elif result == "too low":
            if guess > low:
                low = guess
        else:
            if guess >= high or guess <= low:
                print("Stan is dishonest")
            else:
                print("Stan may be honest")    
            low = 0
            high = 11
        guess = int(input())
    
main()