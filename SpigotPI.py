from time import time
from threading import Thread
import concurrent.futures

def fix_predigits(pi_digits, curr_index=-1):
    if pi_digits[curr_index] + 1 == 10:
        pi_digits[curr_index] = 0
        fix_predigits(pi_digits, curr_index - 1)
    else:
        pi_digits[curr_index] += 1
        pi_digits.append(0)

DIGITS = 1000
array_len = int(10 * DIGITS / 3) + 1
array = [2] * array_len
carry = 0
curr_sum = 0
pi_digits = []
def spigot():
    global array_len
    global array
    global carry
    global curr_sum
    for j in reversed(range(array_len)):
        num = j
        denom = num * 2 + 1

        curr_sum = array[j] * 10 + carry  # multiply by 10 and sum
        array[j] = curr_sum % denom if j > 0 else curr_sum % 10  # remainder
        carry = int(curr_sum / denom) * num

def getPI(digits):
    global array_len
    global array
    global carry
    global curr_sum
    for _ in range(digits):
        with concurrent.futures.ThreadPoolExecutor() as executer:
            executer.submit(spigot)
        predigit = int(curr_sum / 10)
        if predigit > 9:
            fix_predigits(pi_digits)
        else:
            pi_digits.append(int(curr_sum / 10))

    return pi_digits

start = time()
pi_digits = getPI(DIGITS)
time_stop = time()-start
digits = [str(n) for n in list(pi_digits)]

print("PI = %s.%s\n" % (digits.pop(0), "".join(digits)))
print (f"Time: {time_stop}")
print (f"Max numbers: {DIGITS}")