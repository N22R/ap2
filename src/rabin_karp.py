def rabin_karp(haystack: str, needle: str):
    if not needle or not haystack or len(needle) > len(haystack):
        return []

    base = 256
    prime = 101
    n, m = len(haystack), len(needle)
    needle_hash = haystack_hash = 0
    highest_base = pow(base, m - 1, prime)

    for i in range(m):
        needle_hash = (needle_hash * base + ord(needle[i])) % prime
        haystack_hash = (haystack_hash * base + ord(haystack[i])) % prime

    result = []
    for i in range(n - m + 1):
        if needle_hash == haystack_hash and haystack[i:i + m] == needle:
            result.append(i)

        if i < n - m:
            haystack_hash = ((haystack_hash - ord(haystack[i]) * highest_base) * base + ord(haystack[i + m])) % prime
            if haystack_hash < 0:
                haystack_hash += prime

    return result
