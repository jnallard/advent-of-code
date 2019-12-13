"""
--- Day 1: The Tyranny of the Rocket Equation ---
Santa has become stranded at the edge of the Solar System while delivering presents to other planets! 
To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas,
he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. 
  To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""

def compute_day():
  print('Calculating fuel needed...')
  module_fuel = 0
  total_fuel = 0

  for mass in module_masses:
    # calculate fuel needed for module
    fuel = fuel_for_mass(mass)
    module_fuel += fuel

    #calculate fuel needed for fuel
    fuel_added_last_round = fuel
    while fuel_added_last_round > 0:
      total_fuel += fuel_added_last_round
      fuel_added_last_round = fuel_for_mass(fuel_added_last_round)

  print(module_fuel, 'units of fuel needed for modules.')
  print(total_fuel, 'units of fuel needed in total.')
  return [module_fuel, total_fuel]

def fuel_for_mass(mass):
  """Calculates the fuel needed to launch a module"""
  return int((mass / 3)) - 2

module_masses = [
  83453,
  89672,
  81336,
  74923,
  71474,
  117060,
  55483,
  116329,
  123515,
  99383,
  80314,
  108221,
  128335,
  72860,
  139235,
  127843,
  140120,
  63561,
  68854,
  109062,
  146211,
  59096,
  123085,
  105763,
  127657,
  142212,
  111007,
  100166,
  63641,
  59010,
  108575,
  93619,
  144095,
  74561,
  95059,
  145318,
  81404,
  96567,
  91799,
  92987,
  107137,
  87678,
  126842,
  85594,
  116330,
  104714,
  128117,
  132641,
  75602,
  90747,
  69038,
  67322,
  146147,
  147535,
  83266,
  85908,
  124634,
  51681,
  104430,
  56202,
  68631,
  69970,
  116985,
  140878,
  125357,
  126229,
  66379,
  103213,
  108210,
  73855,
  130992,
  113363,
  82298,
  111468,
  110751,
  52272,
  103661,
  122262,
  114363,
  80881,
  65183,
  125291,
  100119,
  56995,
  101634,
  55467,
  136284,
  107433,
  95647,
  71462,
  133265,
  104554,
  62499,
  61347,
  68675,
  123501,
  113954,
  135798,
  80825,
  128235,
]