"""
--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station. 
During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. 
Specifically, two wires are connected to a central port and extend outward on a grid. 
You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. 
To fix the circuit, you need to find the intersection point closest to the central port. 
Because the wires are on a grid, use the Manhattan distance for this measurement. 
While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?

--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; 
choose the intersection where the sum of both wires' steps is lowest. 
If a wire visits a position on the grid multiple times, 
use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, 
including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire
 and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: 
the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
"""

def compute_day():
  print('Finding intersections...')
  problem_input = problem_input_1
  grid = {}
  run_wire(grid, problem_input[0], '1')
  run_wire(grid, problem_input[1], '2')
  result_part_1 = None
  result_part_2 = None
  print('All possible intersections:')
  for coordinate, value in grid.items():
      if value['state'] == 'X' and coordinate != '0,0':
        distance = get_manhattan_distance(coordinate)
        steps = value['steps']
        print('\t', {'coordinate': coordinate, 'distance': distance, 'steps': steps})
        if result_part_1 == None or distance < result_part_1:
          result_part_1 = distance
        if result_part_2 == None or steps < result_part_2:
          result_part_2 = steps
  print('Shortest distance: ', result_part_1)
  print('Shortest steps: ', result_part_2)
  return [result_part_1, result_part_2]

def get_manhattan_distance(coordinate):
  values = coordinate.split(',')
  x = int(values[0])
  y = int(values[1])
  return abs(x) + abs(y)

def run_wire(grid, path, wire_number):
  current_point = (0, 0, 0)
  for path_part in path.split(','):
    parsed_part = parse_path_part(path_part)
    current_point = handle_direction(parsed_part[0], parsed_part[1], grid, current_point, wire_number)

def parse_path_part(path_part):
  return (path_part[0:1], int(path_part[1::]))

def handle_direction(direction, length, grid, current_point, wire_number):
  current_x = current_point[0]
  current_y = current_point[1]
  current_steps = current_point[2]
  x_change = 0
  y_change = 0
  final_x = current_x
  final_y = current_y
  if direction == 'R':
    x_change = 1
    final_x = current_x + length
  if direction == 'L':
    x_change = -1
    final_x = current_x - length
  if direction == 'U':
    y_change = 1
    final_y = current_y + length
  if direction == 'D':
    y_change = -1
    final_y = current_y - length

  while current_x != final_x or current_y != final_y:
    key = str(current_x) + ',' + str(current_y)
    if key in grid:
      if grid[key]['state'] != wire_number:
        grid[key] = { 'state': 'X', 'steps': grid[key]['steps'] + current_steps }
    else: 
      grid[key] = { 'state': wire_number, 'steps': current_steps }
    current_x += x_change
    current_y += y_change
    current_steps += 1

  return (final_x, final_y, current_steps)

example_0 = ('R3,U3', 'U2,R4')
example_1 = ('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83')
example_2 = ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')
example_3 = ('R8,U5,L5,D3', 'U7,R6,D4,L4')
problem_input_1 = (
  'R1003,U756,L776,U308,R718,D577,R902,D776,R760,U638,R289,D70,L885,U161,R807,D842,R175,D955,R643,U380,R329,U573,L944,D2,L807,D886,L549,U592,R152,D884,L761,D915,L726,D677,L417,D651,L108,D377,L699,D938,R555,D222,L689,D196,L454,U309,L470,D234,R198,U689,L996,U117,R208,D310,R572,D562,L207,U244,L769,U186,R153,D756,R97,D625,R686,U244,R348,U586,L385,D466,R483,U718,L892,D39,R692,U756,L724,U148,R70,U224,L837,D370,L309,U235,R382,D579,R404,D146,R6,U584,L840,D863,R942,U646,R146,D618,L12,U210,R126,U163,R931,D661,L710,D883,L686,D688,L148,D19,R703,U530,R889,U186,R779,D503,R417,U272,R541,U21,L562,D10,L349,U998,R69,D65,R560,D585,L949,D372,L110,D865,R212,U56,L936,U957,L88,U612,R927,U642,R416,U348,L541,D416,L808,D759,R449,D6,L517,D4,R494,D143,L536,U341,R394,U179,L22,D680,L138,U249,L285,U879,L717,U756,L313,U222,R823,D208,L134,U984,R282,U635,R207,D63,L416,U511,L179,D582,L651,U932,R646,U378,R263,U138,L920,U523,L859,D556,L277,D518,R489,U561,L457,D297,R72,U920,L583,U23,L395,D844,R776,D552,L55,D500,R111,U409,R685,D427,R275,U739,R181,U333,L215,U808,R341,D537,R336,U230,R247,U748,R846,U404,R850,D493,R891,U176,L744,U585,L987,D849,R271,D848,L555,U801,R316,U753,L390,U97,L128,U45,R706,U35,L928,U913,R537,D512,R152,D410,R76,D209,R183,U941,R289,U632,L923,D190,R488,D934,R442,D303,R178,D250,R204,U247,R707,U77,R428,D701,R386,U110,R641,U925,R703,D387,L946,U415,R461,D123,L214,U236,L959,U517,R957,D524,R812,D668,R369,U340,L606,D503,R755,U390,R142,D921,L976,D36,L965,D450,L722,D224,L303,U705,L584',
  'L993,U810,L931,D139,R114,D77,L75,U715,R540,D994,L866,U461,R340,D179,R314,D423,R629,D8,L692,U446,L88,D132,L128,U934,L465,D58,L696,D883,L955,D565,R424,U286,R403,U57,L627,D930,R887,D941,L306,D951,R918,U587,R939,U821,L65,D18,L987,D707,L360,D54,L932,U366,R625,U609,R173,D637,R661,U888,L68,U962,R270,U369,R780,U845,L813,U481,R66,D182,R420,U605,R880,D276,L6,D529,R883,U189,R380,D472,R30,U35,L510,D844,L146,U875,R152,U545,R274,U920,R432,U814,R583,D559,L820,U135,L353,U975,L103,U615,R401,U692,L676,D781,R551,D985,L317,U836,R115,D216,L967,U286,R681,U144,L354,U678,L893,D487,R664,D185,R787,D909,L582,D283,L519,D893,L56,U768,L345,D992,L248,U439,R573,D98,L390,D43,L470,D435,R176,U468,R688,U388,L377,U800,R187,U641,L268,U857,L716,D179,R212,U196,L342,U731,R261,D92,R183,D623,L589,D215,L966,U878,L784,U740,R823,D99,L167,D992,R414,U22,L27,U390,R286,D744,L360,U554,L756,U715,R939,D806,R279,U292,L960,U633,L428,U949,R90,D321,R749,U395,L392,U348,L33,D757,R289,D367,L562,D668,L79,D193,L991,D705,L562,U25,R146,D34,R325,U203,R403,D714,R607,U72,L444,D76,R267,U924,R289,U962,L159,U726,L57,D540,R299,U343,R936,U90,L311,U243,L415,D426,L936,D570,L539,D731,R367,D374,L56,D251,L265,U65,L14,D882,L956,U88,R688,D34,R866,U777,R342,D270,L344,D953,L438,D855,L587,U320,L953,D945,L473,U559,L487,D602,R255,U871,L854,U45,R705,D247,R955,U885,R657,D664,L360,D764,L549,D676,R85,U189,L951,D922,R511,D429,R37,U11,R821,U984,R825,U874,R753,D524,L537,U618,L919,D597,L364,D231,L258,U818,R406,D208,R214,U530,R261'
)