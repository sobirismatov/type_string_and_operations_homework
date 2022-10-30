from re import A


def main(s,n):
    """
    s string is given. repeat it n times and return the resulting string.
    Args:
        s: str
        n: int
    Returns:
        str: return answer.
    """
    a=s*n
    return a
print(main("salom",3))