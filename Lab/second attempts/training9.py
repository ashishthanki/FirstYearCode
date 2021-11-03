"""Some support functions"""


def code0():
    """A trivial code - no change."""
    return {}


def code1():
    """A very simple example (symmetric)."""
    return {'e': 'x', 'x': 'e'}


def code2():
    """A simple example i->s, s->g and g->i."""
    return {'i': 's', 's': 'g', 'g': 'i'}


def code3():
    """A more complicated code."""
    dic = {}
    #lower case letters
    dic['z'] = 'a'
    for i in range(ord('a'), ord('z')):
        dic[chr(i)] = chr(i + 1)
    #upper case letters
    dic['Z'] = 'A'
    for i in range(ord('A'), ord('Z')):
        dic[chr(i)] = chr(i + 1)
    #space, stop and some other special characters
    dic[' '] = '$'
    dic['.'] = '#'
    dic['#'] = '.'
    dic['$'] = ' '
    dic['?'] = '!'
    dic['!'] = '?'
    return dic


def check_code_is_reversible(dic):
    """Given a dictionary used as a code mapping, this function checks
    whether the set of keys is the same set of values: if the elements
    in the keys are the same unique set as those in the values, then
    this mapping is bijective (the set of values is then actually a
    permutation of the set of input values) and can be inverted.

    If this is not the case, some debug information is printed, and a
    ValueError exception raised.
    """

    unique_keys = set()
    unique_vals = set()
    for key, val in dic.items():
        unique_keys.add(key)
        unique_vals.add(val)
    if unique_vals != unique_keys:
        print "Code is not reversible:"
        print "keys are   %s", sorted(unique_keys)
        print "values are %s", sorted(unique_vals)
        raise ValueError("Code is not reversible - stopping here")
    return True


def test_codes():
    """Check that codes defined above are reversible."""
    for c in (code0(), code1(), code2(), code3()):
        assert check_code_is_reversible(c)


secretmessage = "Zpv$ibwf$tvddfttgvmmz$efdpefe$uijt$tfdsfu$nfttbhf#$Dpohsbuvmbujpot?"


#if this file is executed on it's own, check codes given
if __name__ == "__main__":
    test_codes()


def trapez(f, a, b, n):
    """computes and returns the trapezoidal integration rule"""
    h = float((b - a)) / n
    p = sum(map(lambda i: f(a + i * h), range(1, n)))
    return (h * 0.5) * (f(a) + f(b) + 2 * p)


def encode(code, msg):
    """The function should apply thex mapping to each character of the string
    described above and return the encoded output string."""
    s = ''
    length = len(msg)
    for i in range(length):
        if True == code.__contains__(msg[i]):
            s = s.__add__(code[msg[i]])
        else:
            s = s.__add__(msg[i])
    return s


def reverse_dic(s):
    """" takes a dictionary d as the input argument and
    returns a dictionary r."""
    result = {}
    for i in s:
        result[s[i]] = i
    return result


def decode(code, msg):
    """The function decode should return the decoded message"""
    rev = reverse_dic(code)
    s = ''
    length = len(msg)
    for i in range(length):
        if True == rev.__contains__(msg[i]):
            s = s.__add__(rev[msg[i]])
        else:
            s = s.__add__(msg[i])
    return s
