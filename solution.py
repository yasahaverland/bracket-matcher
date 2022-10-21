'''
  python
 bracket_matcher('abc(123)')
  returns true

 bracket_matcher('a[b]c(123')
  returns false -- missing closing parens

 bracket_matcher('a[bc(123)]')
  returns true

 bracket_matcher('a[bc(12]3)')
  returns false -- improperly nested

 bracket_matcher('a{b}{c(1[2]3)}')
  returns true

 bracket_matcher('a{b}{c(1}[2]3)')
returns false -- improperly nested

 bracket_matcher('()')
 returns true

 bracket_matcher('[]]')
returns false - no opening bracket to correspond with last character

 bracket_matcher('abc123yay')
returns true -- no brackets = correctly matched
'''


# Write a Python function that takes a string input. This string represents code. It may have any number of characters in it, and the characters may be anything. For our purposes, we'll ignore anything that isn't one of the following: `[`, `]`, `{`, `}`, `(`, `)`. Your function definition looks like this:


def bracket_matcher(input):
  # string = 'abc(123)'
  # get rif of letters and numbers -- be left with an "array" of just brackets
  open_list = ["[","{","("]
  close_list = ["]","}",")"]
  # stack the open brackets
  stack = []
  # somehow compare the pattern through iteration over the stack to check if each type of bracket is opening and closing
  # loop through all the input
  for i in input:
    # if its opening braket, stack it!
    if i in open_list:
        stack.append(i)
    # if its a closing braket, go to close_list and give me the coresponding index for that bracket i
    elif i in close_list:
        pos = close_list.index(i)
        # comparing: with the indexes from closing_list, go to open_list and get the corresponding BRAKETS of those indexes
        # pop the brakets as they match
        if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
              stack.pop()
        else:
            return False
  # if the length of stack is 0 - that neans they were all pairs in the right order, return true!
  if len(stack) == 0:
      return True
  # if len has a value, it means it did't find a matching braket to be popped. 
  else:
      return False

print(bracket_matcher('a{b}{c(1[2]3)}'))

 
  

  