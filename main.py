import sys
import operator
import time


def updateSignupList(signup, final_library, days_passed, num_signups, final_books):
    try:
        if num_signups <= len(signup) and days_passed == signup[num_signups][1]:
            days_passed = 0
            final_library.append(signup[num_signups][0])
            print("Library Signedup-", len(final_library))
            final_books.append([])
            num_signups += 1
    except IndexError:
        print(num_signups)
        print(signup)
    return days_passed, num_signups


def getShippingDays(shipping, final_library):
    num_shipping = 0
    for ship in shipping:
        if ship[0] in final_library:
            num_shipping = ship[1]
            break
    return num_shipping


def main():
    file = open(sys.argv[1], "r")
    b, l, d = list(map(int, file.readline().rstrip().split()))

    s = list(map(int, file.readline().rstrip().split()))
    scores = {i: 0 for i in range(len(s))}
    for i in range(len(s)):
        scores[i] = s[i]

    scores=sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    print("Scores:", scores)

    libraries = []
    books = []
    signup = {i: 0 for i in range(l)}
    shipping = {i: 0 for i in range(l)}

    for i in range(l):
        libraries.append(list(map(int, file.readline().rstrip().split())))
        books.append(list(map(int, file.readline().rstrip().split())))
        signup[i] = libraries[i][1]
        shipping[i] = libraries[i][2]

    signup = sorted(signup.items(), key=operator.itemgetter(1))
    shipping = sorted(shipping.items(), key=operator.itemgetter(1))

    print("Books:", books)
    print("Signup: ", signup)
    print("Shipping", shipping)

    final_books = []
    final_library = []


    num_signups = 0
    print("Max Days: ", d)
    
    days = 0

    final_library.append(signup[0][0])
    days += signup[0][1] +1
    days_passed = 1
    num_signups += 1
    final_books.append([])


    start = time.time()

    while days <= d:
        for parallel in range(num_signups):
            num_shipping = getShippingDays(shipping, final_library)
            tmp_books = []

            for score in scores:
                try:
                    if score[0] in books[signup[parallel][0]] and score[0] not in tmp_books and num_shipping > 0 and score[0] not in final_books[parallel] and days <= d:
                        tmp_books.append(score[0])
                        num_shipping -= 1
                    elif num_shipping == 0:
                        break
                except IndexError:
                    print(books[signup[parallel][0]])
                    print(parallel)
                    print("final book ", final_books)
                    print[final_books[parallel]]
            final_books[parallel] = final_books[parallel] + tmp_books
        days += 1
        days_passed += 1
        print("Day-", days, " of ", d)
        end = time.time()
        if (end-start) >= 1000:
            break
        print("Time Elapsed: ", (end-start))
        if num_signups != len(signup):
            days_passed, num_signups = updateSignupList(signup, final_library, days_passed, num_signups, final_books)

    print("Final Library: ",final_library)
    print("Final Books: ", final_books)


    file = open("output.txt", "w")
    file.write(str(len(final_library))+"\n")
    for i in range(len(final_library)):
        file.write(str(final_library[i])+" "+str(len(final_books[i]))+"\n")
        file.write(" ".join(list(map(str, final_books[i])))+"\n")

    print("Done")

main()