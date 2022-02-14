# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import re

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = "2021-01-01"
    b = "2021/01/01"
    pattern1 = r"(\d{4}-\d{1,2}-\d{1,2})"
    pattern2 = r"(\d{4}/\d{1,2}-\d{1,2})"
    pattern3 = r"(\d{4}\d{1,2}\d{1,2})"
    match = re.search(pattern1,a)
    print(match == None)
    #print(len(match.group()))
    #print(match.group(0))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
