"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 172930-683082.

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
"""

def compute_day():
  print('Getting possible passwords...')
  part_1_result = None
  possible_passwords = []
  i = problem_input_1['min']
  while i <= problem_input_1['max']:
    if is_possible_password(i, problem_input_1['exact_adjacent_match']):
      possible_passwords.append(i)
    i += 1
  part_1_result = len(possible_passwords)
  print('Possible password count: ', part_1_result)

  part_2_result = None
  possible_passwords = []
  i = problem_input_2['min']
  while i <= problem_input_2['max']:
    if is_possible_password(i, problem_input_2['exact_adjacent_match']):
      possible_passwords.append(i)
    i += 1
  part_2_result = len(possible_passwords)
  print('Possible password count (with exact_adjacent_match): ', part_2_result)
  return [part_1_result, part_2_result]

def is_possible_password(password, exact_adjacent_match):
  password = str(password)
  previous_num_char = None
  adjacent_matches = {}
  for num_char in password:
    num_char = int(num_char)
    if(previous_num_char != None):
      if num_char < previous_num_char:
        return False
      if num_char == previous_num_char:
        if num_char not in adjacent_matches:
          adjacent_matches[num_char] = 1
        adjacent_matches[num_char] += 1
    previous_num_char = num_char
  for _, count in adjacent_matches.items():
    if exact_adjacent_match and count == 2:
      return True
    elif not exact_adjacent_match:
      return True
  return False

example_1 = {'min': 111111, 'max': 111111, 'exact_adjacent_match': False}
example_2 = {'min': 223450, 'max': 223450, 'exact_adjacent_match': False}
example_3 = {'min': 123789, 'max': 123789, 'exact_adjacent_match': False}
example_4 = {'min': 112233, 'max': 112233, 'exact_adjacent_match': True}
example_5 = {'min': 123444, 'max': 123444, 'exact_adjacent_match': True}
example_6 = {'min': 111122, 'max': 111122, 'exact_adjacent_match': True}
problem_input_1 = {'min': 172930, 'max': 683082, 'exact_adjacent_match': False}
problem_input_2 = {'min': 172930, 'max': 683082, 'exact_adjacent_match': True}