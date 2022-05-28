# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#   print_hi('PyCharm')

# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(elbow,below):
      print(elbow,below)
    # Convert string into lists
      list1 = list(elbow)
      list2 = list(below)
    # Sort the list value
      list1.sort()
      list2.sort()

      position = 0
      matches = True

      while position < len(elbow) and matches:
            if list1[position]==list2[position]:
                position = position + 1
            else:
                matches = False

      return matches

print(find_anagram('elbow','below'))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
