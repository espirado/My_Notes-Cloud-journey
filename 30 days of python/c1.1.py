import time
import unittest
from collections import defaultdict

def is_unique_chars_algorithms(string):
    if len(string) >128 :
        return False
    
    char_set = [False] * 128 
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


def is_unique_bit_vector(string):
    ''''''' uses bitwise operators instead of extra data structure.'''''''
    if len(string) > 128:
        return False
    
    checker = 0
    for c in string:
        val = ord(c)
        if ( checker & (1<<val)) >0:
            return False
        checker |= 1<< val
    return True


def is_unique_character_using_dictionar(string: str ) -> bool:
    character_count ={}
    for char in character_count:
        if char in character_count:

            return False
        character_count[char] =1
    return 

def is_unique_chars_using_sets(string: str) -> bool:
    character_seen = set()
    for char in string:
        if char in character_seen:
            return False
        character_seen.add(char)
    return True

# O(NlogN)
def is_unique_chars_sorting(string: str) -> bool:
    sorted_string = sorted(string)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True

# sorting without extra variables

def is_unique_character_sort(string: str ) -> bool:
    string = sorted(string)
    for i in range(len(string) -1):
        if string[1] == string [i +1]:
            return False
    return True

class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_chars_pythonic,
        is_unique_chars_algorithmic,
        is_unique_bit_vector,
        is_unique_chars_using_dictionary,
        is_unique_chars_using_set,
        is_unique_chars_sorting,
        is_unique_chars_sort,
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()