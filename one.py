""" Pallendrome Checker 
    For this first problem fix the function
    so that if the input text is a pallendrome, it returns True.
    And if not, it returns false.

    Try running it on some samples to make sure it works
"""

def reverse(text): 
    return text[::-1] 
  
def lower(text):
    return text.lower()

def replace(text):
    return text.replace(" ", "")
    
def checkisPallendrome(text):
    rev = replace(text)
    rev = lower(text)
    rev = reverse(text) 
  
    if (text == rev): 
        return True
    return False



def tester(text, expected_result):
    actual_result = checkisPallendrome(text)

    print_text = "The text was: " + str(text) + " | "
    if expected_result == actual_result:
        print_text += "Correct: " + str(expected_result) + " == " + str(actual_result)
    else:
        print_text += "Incorrect: " + str(expected_result) + " != " + str(actual_result)
    return print_text


if __name__ == "__main__":
    # Try it on these to see if it works?
    text0 = "My foot is a hamburger"
    text1 = "Go hang a salami Im a lasagna hog"
    text2 = "She sells sea shells by the sea shore"
    text3 = "race car"
    text4 = "My school"

    # Test it like this
    print(tester(text0, False))
    print(tester(text1, True))
    print(tester(text4, False))
