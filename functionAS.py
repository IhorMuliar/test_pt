def functionAS(n):
    commonDifference = 3
    # print("Common Difference in the arithmetic sequence is: ", commonDifference)
    firstTerm = 4
    # print("First term in the arithmetic sequence is: ", firstTerm)
    sumOfTerms = 0
    for i in range(1, n + 1):
        ithTerm = firstTerm + (i - 1) * commonDifference
        sumOfTerms = sumOfTerms + ithTerm
    return sumOfTerms

if __name__ == '__main__':
    while True:
        n = int(input('Enter number: '))
        print("N = ", n, 'Sum = ', functionAS(n))