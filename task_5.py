def compare_versions(a: str, b: str) -> int:
    a, b = a.split()[-1].split('.'), b.split()[-1].split('.')
    while a and b:
        element_a = a.pop(0)
        element_b = b.pop(0)
        if element_a > element_b:
            return 1
        elif element_b > element_a:
            return -1
    else:
        if a:
            return 1
        elif b:
            return -1
        return 0
