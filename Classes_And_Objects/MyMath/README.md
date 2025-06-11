# MyMath Python Project

A practice project to learn OOP concepts in Python By Bharavi Sadineni

## Project Overview

- MyMath is a simple Python class project built to practice Object-Oriented Programming concepts.
- Demonstrates use of classes, objects, and methods
- Uses *args to handle variable number of inputs
- Implements basic arithmetic and factorial logic
- Includes input validation and result formatting

  ### Constructor:
  ```bash
  def __init__(self, *details):
    Accepts variable number of arguments.
  ```

  ### Instance variable:
  ```bash
  self.my_details: stores the numbers for operations.
  ```

## Methods in MyMath

- [Add()](): Returns the sum of all inputs.
- [Sup()](): Returns result after subtracting all inputs sequentially.
- [Mul()](): Returns the product of all inputs.
- [Dev()](): Divides inputs sequentially, avoiding divide-by-zero.
- [Modules()](): Returns remainder sequentially, with error check.
- [factoriel()](): Prints and returns factorial of first input if valid.

## Examples:
  ### Example-1:
  Performing Addition operation for "n" number of values

    i = MyMath(2, 3)
    print(i.Add())

  #### Output:
      5

  ### Example-2:
  Performing Addition operation for "n" number of values

    i = MyMath(2, 3)
    print(i.Sup())

  #### Output:
      5
