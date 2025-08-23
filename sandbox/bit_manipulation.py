'''    
1. Bitwise AND (&)
    - performs logical AND operation on each pair of corresponding bits
    - the result bit is 1 only if both input bits are 1

    Use cases:
    - checking if a specific bit is set
    - clearing (setting to 0) specific bits

NOTE:
To represent a negative number -n in two's complement:
1. the fomula: -n = ~n + 1 (~n is bitwise NOT of n, n is the number), OR
2. the math: -x = 2^n - x  (where n is the bit width, x is the number)
'''
def is_bit_set(n, pos):
    mask = 1 << pos # a mask is a bit patttern used to selectively show, hide, or modify specific bits
    return n & mask

def clear_bit(n, pos):
    mask = ~(1 << pos)
    return n & mask

'''
2. Bitwise OR (|)
    - performs logical OR operation on each pair of corresponding bits
    - the result bit is 1 if any input bit is 1

    Use case:
    - setting (turning to 1) specific bits
'''
def set_bit(n, pos):
    mask = 1 << pos
    return n | mask

'''
3. Bitwise XOR (^) - Exclusive OR
    - performs logical XOR operation on each of corresponding bits
    - the result bit is 1 only if both bits are different

    Use case:
    - toggling (flipping) specific bits
    - finding the unique element in an array where all others appear twice
    - swapping two numbers without a temporary variable
'''
def flip_bit(n, pos):
    mask = 1 << pos
    return n ^ pos

def find_unique(arr):
    res = 0
    for n in arr:
        res ^= n
    return res

def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

'''
4. Bitwise NOT (~) – Complement
    - flips all the bits of its operand, also known as the one's complement
    -  0s become 1s, and 1s become 0s.

    Use cases:
    - cre4ating mask for clearing bits (often used with AND)

    NOTE:
    In Java (and lots of other language), integers are stored using two's complement representation for negative numbers.
    So, ~x is equivalent to -x - 1.

    Here's a breakdown:
    -x = ~x + 1
    ~x = -x - 1

    These are two different operations:
    a. (1 << bit_width) - 1 : creates a bit mask (all bits are set) with exactly bit_width bits
    b. ~(1 << bit_width)    : creates a bit mask >= bit_width bits, because it flips all bits in the integer
'''
# see clear_bit func

'''
5. Left Shift (<<)
    - shifts all bits of left operand to the left by the number of positions specified by right operand
    - fills new rightmost bits with 0s

    NOTE:
    x << n is equal to multiplying x by 2^n (where n is bit width, as long as no significant bits are lost)
'''

'''
6. SIGNED Right Shift (>>)
    - shifts all bits of left operand to the right by the number of positions specified by right operand
    - sign preservation: fills new leftmost bits with copies of the original sign bit
    - this preserves the sign of the number

    NOTE:
    x >> n is equal to dividing x by 2^n (where n is bit width, integer division, rounding towards -inf for negative numbers)
'''

'''
7. UNSIGNED Right Shift (>>>)
    - shifts all bits of the left operand to the right by the number of positions specified by the right operand
    - zero fill: fills new leftmost bits with 0s, regardless of the original sign bit

    Use cases:
    - when you need to treat number purely as bit pattern
    - to use in hashing algorithms / dealing with color values packed into integer
    
    NOTE:
    a. for positive numbers, >>> behaves like >>
    b. for negative numbers, result bits will always be positive (or 0)
'''

# PRACTICE

def test_bit_manipulation():
    # Checking if the k-th Bit is Set (is 1)
    def is_bit_set(num, k):
        return (1 << k) & num != 0

    # Setting the k-th Bit (to 1)
    def set_bit(num, k): # 100, 
        return (1 << k) | num
    
    # Clearing (Unsetting) the k-th Bit (to 0)
    def clear_bit(num, k):
        return ((1 << k) - 1) & num

    # Toggling (Flipping) the k-th Bit
    def toggle_bit(num, k):
        return (1 << k) ^ num

    # Checking if a Number is Even or Odd
    def is_even(num):
        return num & 1 == 0

    def is_odd(num):
        return num & 1 != 0

    # Multiplying/Dividing by Powers of 2
    def multi_pow2(a, b):
        # import math
        # return a << math.log2(b)
        if b > 0 and b & (b-1) == 0:
            return a << (b.bit_length() - 1)
        return a*b

    def div_pow2(a, b):
        if b > 0 and b & (b-1) == 0:
            return a >> (b.bit_length() - 1)
        return a//b

    # Swapping Two Numbers Without a Temporary Variable
    def swap(a, b):
        a ^= b # a = a ^ b
        b ^= a # b = b ^ (a ^ b) = a
        a ^= b # a = (a ^ b) ^ a = b
    
    # Counting Set Bits (Hamming Weight / Population Count) NOTE: Java Built-in: Integer.bitCount(n)
    # a. Technique 1 (Iterate and Check): Loop through each bit and check if it's set.
    def count_bit_iterative(num):
        # return bin(num).count('1')
        # return num.bit_count()
        # return sum(num & (1 << i) != 0 for i in range(num.bit_length()))
        c = 0
        while num > 0:
            if num & 1 == 1: # check if LSB is set
                c += 1
            num >>= 1
        return c

    # b. Technique 2 (Brian Kernighan's Algorithm): 
    #       - In each step, n & (n-1) clears the rightmost set bit of n. 
    #       - Loop until n becomes 0. The number of iterations is the number of set bits. 
    #       - This is often more efficient    
    def count_bit_kernighan(num):
        c = 0
        while num > 0:
            num &= num - 1 # clears the rightmodt set bit
            c += 1
        return c


    # Checking if a Number is a Power of 2
    def is_power_2(num):
        return num > 0 and num & (num - 1) == 0

    # Finding the Position of the Rightmost Set Bit (Least Significant Bit - LSB)
    def get_lsb_pos(num):
        return (num & -num).bit_length() - 1
    
    # def get_lsb_pos(num, c=0):
    #     if num & 1:
    #         return c
    #     get_lsb_pos(num >> 1, c + 1)

    # Finding the Position of the Most Significant Bit (MSB)
    def get_msb_pos(num):
        return num.bit_length() - 1

    # Clearing All Bits from MSB to k-th Bit
    def clear_bits_from_msb(num, end=0):
        if end <= 0:
            return 0 
        mask = (1 << end) - 1 # exclusive
        # mask = (1 << (end + 1)) - 1 # exclusive
        return num & mask

    # Clearing All Bits from LSB to k-th Bit
    def clear_bits_from_lsb(num, end=0):
        if end <= 0:
            return num 
        mask = ~((1 << end) - 1) # exclusive
        # mask = ~((1 << (end + 1)) - 1) # inclusive
        return num & mask


    # Representing Sets (Bitmasks)
    '''
    An integer can represent a set of up to 32 (or 64 for long) distinct items. The k-th bit being set means the k-th item is in the set.
    - Union: set1 | set2
    - Intersection: set1 & set2
    - Difference (set1 - set2): set1 & (~set2)
    - Add item k: set | (1 << k)
    - Remove item k: set & (~(1 << k))
    - Check if item k is present: (set & (1 << k)) != 0
    '''
    # Iterate through all subsets of a set (bitmasks) represented by n:
    def get_all_subsets(arr):
        n = len(arr)
        subsets, subset = [], []
        for i in range(1 << n):  # 1 << n is 2^n
            subset = []
            for j in range(n):
                # If j-th bit is set in i, include items[j]. 
                # i.e., 
                # if i = 110 and j = 100 (j is pointing to c, because c index is 2),
                # then intesection results in non-zero/non-falsy. Thus, include b
                if i & (1 << j): 
                    subset.append(arr[j])
            subsets.append(subset)
        
        return subsets
        
        # n = len(arr)
        # return [
        #     [arr[j] for j in range(n) if i & (1 << j)]
        #     for i in range(1 << n)
        # ]


    # Working with Negative Numbers (Two's Complement)
    '''
    Java uses two's complement to represent negative integers. To get the two's complement of a positive number x:
    1. Invert all bits of x (one's complement: ~x).
    2. Add 1 to the result: ~x + 1.
        This is why ~x is (-x) - 1, and -x is (~x) + 1.
        Bitwise operations generally work as expected with two's complement numbers, 
        but you need to be mindful of the sign bit, especially with right shifts.
    '''

    # Set, clear, and toggle a bit
    def set_but(num, k):
        return num | (1 << k)

    def clear_bit(num, k):
        return num & ~(1 << k)
    
    def toggle_bit(num, k):
        return num ^ (1 << k)

    # Find the rightmost set bit
    def find_lsb(num):
        return num & -num

    # Detect if two integers have opposite signs
    def is_opposite_sign(a, b):
        return a ^ b < 0

    
    # Inverting All Bits
    def invert_bits(num):
        return ~num


if __name__ == "__main__" :
    pass