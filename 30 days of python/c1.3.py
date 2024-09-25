# Write a method to replace all spaces in a string with "%20" You may assume that the string has sufficient space at the end to hold the additional charcaters and that you are given the "trye lenth of the string. "
"""Example " Mr John Smith ", 13 
 output: "Mr%20John%smith%20",%13      
"""
import unittest

def urlify_algo(string, length):
     """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
     char_list = list(string)
     new_index = len(char_list)

     for i in reversed(range(length)):
          if char_list[1]==" ":
               #replace spaces
               char_list[new_index -3 : new_index] = "%20"
               new_index-= 3

          else:
        #move characters
               char_list[new_index -1 ] = char_list[1]
               new_index -= 1

               # convert back to strings
               return "".join(char_list[new_index:])
          

def urlify_pythonic(text, length):
    #using standard library
    return text[:length].replace(" ", "%20")

class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    testable_functions = [urlify_algo, urlify_pythonic]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = urlify(*args)
                assert actual == expected, f"Failed {urlify.__name__} for: {[*args]}"


if __name__ == "__main__":
    unittest.main()
