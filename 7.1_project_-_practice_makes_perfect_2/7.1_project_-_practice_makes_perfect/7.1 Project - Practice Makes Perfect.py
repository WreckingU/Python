# Paste your code from CodeCademy project "Practice Makes Perfect"
# pages 2-15 above the code below.

#2
loop_condition = True

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

#3
def is_int(x):
    if x - int(x) == 0:
        return True
    else:
        return False


#4
def digit_sum(n):
    num = 0
    while n != 0:
        num += n%10
        n //= 10
    return num

#5
def factorial(x):
    newlist = range(+1,x)
    for i in newlist:
        x *= i
    return x


#6
def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True



#7
def reverse(text):
    s = ''
    for i in range(-1,-len(text)-1,-1):
        s = s+text[i]
    return s


#8
def anti_vowel(text):
    t = ""
    for c in text:
        if c not in "aeiouAEIOU":
            t += c
    return t


#9
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    new = word.lower()
    for i in new:
        for s in score:
            if i == s:
                total += score[s]
    return total

print scrabble_score("marigold")


#10
def censor(text,word):
    astericks = "*" * len(word)
    thing = text.replace(word, astericks)
    return thing


#11
def count(sequence, item):
  count = 0
  for c in sequence:
      if c == item:
          count += 1
  return count


#12
def purify(num):
    odd=[]
    for i in num:
        if i%2 == 0:
            odd.append(i)
    return odd


#13
def product(list_integers):
    total = 1
    for i in (list_integers):
        total *= i
    return total


#14
def remove_duplicates(full_list):
    new_list = []
    for item in full_list:
        if item not in new_list:
            new_list.append(item)
    return new_list



#15
def median(numbers):
    num = sorted(numbers)
    if len(numbers)%2 == 0:
        return (num[len(num)/2-1] + num[len(num)/2])/2.0
    else:
        return num[len(num)/2]




#Don't delete this print statement!
print

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    print key, d[key]

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item


print "Part 2 - is_even"
print "6 is even is " + str(is_even(6))
print "5 is even is " + str(is_even(5))
print

print "Part 3 - is_int"
print "-1 is an integer is " + str(is_int(-1))
print "7.5 is an integer is " + str(is_int(7.5))
print

print "Part 4 - digit_sum"
print "The sum of 1234 is " + str(digit_sum(1234))
print

print "Part 5 - factorial"
print "The factorial of 1 is " + str(factorial(1))
print "The factorial of 4 is " + str(factorial(4))
print

print "Part 6 - is_prime"
print "11 is prime is " + str(is_prime(11))
print "18 is prime is " + str(is_prime(18))
print

print "Part 7 - reverse"
print "abcd reversed is " + reverse("abcd")
print

print "Part 8 - anti_vowel"
print "Hey You! without vowels is " + anti_vowel("Hey You!")
print

print "Part 9 - scrabble_score"
print "In scabble the word Helix would score " + str(scrabble_score("Helix")) + " points."
print

print "Part 10 - censor"
print "'this hack is wack hack' censored with 'hack' is '" + censor("this hack is wack hack", "hack") + "'"
print

print "Part 11 - count"
print "How many times does the number 1 appear in the list [1,2,1,1]? " + str(count([1,2,1,1],1))
print

print "Part 12 - purify"
print "The list [1,2,3] purified wihtout odds is " + str(purify([1,2,3]))
print

print "Part 13 - product"
print "The product of product [4, 5, 5] is " + str(product([4, 5, 5]))
print

print "Part 14 - remove_duplicates"
print "[1,1,2,2] without duplicates is " + str(remove_duplicates([1,1,2,2]))
print

print "Part 15 - median"
print "The median of [7,12,3,1,6] is " + str(median([7,12,3,1,6]))
print "The median of [7,3,1,4] is " + str(median([7,3,1,4]))

