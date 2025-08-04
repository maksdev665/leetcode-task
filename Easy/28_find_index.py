def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    
    haystack_len = len(haystack)
    needle_len = len(needle)

    for i in range(haystack_len - needle_len + 1):
        if haystack[i:i + needle_len] == needle:
            return i
    
    return -1
    


print(str_str("hello", "ll"))     # 2
print(str_str("aaaaa", "bba"))    # -1
print(str_str("abc", ""))         # 0