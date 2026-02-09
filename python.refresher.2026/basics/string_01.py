def demo_string_01(input):
    test_string = input
    NOT_EMPTY = False
    if test_string != "" and len(test_string)>1:
        NOT_EMPTY = True
    if NOT_EMPTY:
        print(f"TEST STRING: {test_string}")
        print(f" string length: {len(test_string)}")
        # left strip
        stripped_string1 = test_string.lstrip()
        print(f"Leftmost spaces stripped\n {stripped_string1}")
        print(f" string length: {len(stripped_string1)}")

        # right strip
        stripped_string2 = test_string.lstrip()
        print(f"Leftmost spaces stripped\n {stripped_string2}")
        print(f" string length: {len(stripped_string2)}")

        # strip
        stripped_string_3 = test_string.strip()
        print(f"Leftmost spaces stripped\n {stripped_string_3}")
        print(f" string length: {len(stripped_string_3)}")

        string_upper_cased = stripped_string_3.upper()
        print(f"UPPERCASED: \n {string_upper_cased}")

        string_reversed = stripped_string_3[::-1]
        print(f"Reverese {string_reversed}")
    else :
        print("WARNING: COULDN'T PROCESS THE REQUEST")


def demo_loop_and_print(n):
    for i in range(n+1):
        print(f"[{i}]: This is being printed from a loop.")

demo_string_01(" Newcastle ")
demo_loop_and_print(5)
demo_string_01("")




