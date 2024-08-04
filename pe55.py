# This is the solution to ProjectEuler 55.

# https://projecteuler.net/problem=55

count = 0

# loop theu all the numbers from 1 to 9999.
for n in range(1, 10000):
    isPalindrome = False
    # we know that it's not going to be more then 50 iterations required
    for a in range(50):
        # add the integer of the reversed string of n to n
        n += int(str(n)[::-1])
        # if the string of n is the same as the reversed string of n
        if str(n) == str(n)[::-1]:
            # if it is, we have found out that it is a palindrome number set the test to true and break out so we don't
            # do any unnecessary iterations
            isPalindrome = True
            break
    # if it never formed a palindrome number add one to number of lychrel numbers
    if not isPalindrome:
        count += 1

# print how many lychrel numbers we found
print (count)
