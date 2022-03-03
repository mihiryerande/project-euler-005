# Problem 005:
#     Smallest Multiple
#
# Description:
#     2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#     What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

def main(n):
    """
    Return the smallest number divisible by all factors 1 through `n`.

    Args:
        n (int): Natural number

    Returns:
        Smallest multiple of 1 through `n`.

    Raises:
        AssertError: if incorrect params are given
    """
    assert type(n) == int and n > 0

    # Create a 'sieve' of all desired factors.
    # 'Reduce' all the desired factors to only the essential factors.
    # Smallest multiple will be the product of those alone.
    s = list(range(1, n+1))
    m = 1
    i = 1
    while len(s) > 0:
        f = s.pop(0)
        if f != 1:
            m *= f  # Include in final multiple
            for j in range(i-1, len(s), i):
                s[j] //= f  # Reduce remaining factors
        i += 1
    return m


if __name__ == '__main__':
    num = int(input('Enter a natural number: '))
    mult = main(num)
    print('Smallest number divisible by all numbers 1 to {}:\n{}'.format(num, mult))
