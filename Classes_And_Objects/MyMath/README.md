# MyMath Python Project

A practice project to learn OOP concepts in Python By Bharavi Sadineni
___

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Complete-brightgreen)

___

## Project Overview

*  MyMath is a simple Python class project built to practice Object-Oriented Programming concepts.
* Demonstrates use of classes, objects, and methods
* Use *args to handle variable number of inputs
* Implements basic arithmetic and factorial logic
* Includes input validation and result formatting

---

  ### Constructor:
  ```bash
  def __init__(self, *details):
    Accepts variable number of arguments.
  ```

  ### Instance variable:
  ```bash
  self.my_details: stores the numbers for operations.
  ```

---

## Methods in MyMath

- [Add()](#add): Returns the sum of all inputs.
- [Sup()](#sup): Returns result after subtracting all inputs sequentially.
- [Mul()](#mul): Returns the product of all inputs.
- [Dev()](#dev): Divides inputs sequentially, avoiding divide-by-zero.
- [Modules()](#modules): Returns remainder sequentially, with error check.
- [factoriel()](#factoriel): Prints and returns factorial of first input if valid.

---

## Examples:
  ### Example-1:
  Performing Addition operation for "n" number of values by using
  #### Add()
    i = MyMath(2, 3)
    print(f"output: {i.Add()}")

  #### Output:
      output: 5
___
  ### Example-2:
  Performing Subtraction operation for "n" number of values by using
  #### Sup()

    i = MyMath(2, 3)
    print(f"output: {i.Sup()}")

  #### Output:
      output: -1
___
  ### Example-3:
  Performing multiplication operation for "n" number of values by using
  #### Mul()
    i = MyMath(2, 3)
    print(f"output: {i.Mul()}")

  #### Output:
      output: 6
___
  ### Example-4:
  Performing division operation for "n" number of values by using
  #### Dev()

    i = MyMath(2, 3)
    print(f"output: {i.Dev()}")

  #### Output:
      output: 0.667
___
  ### Example-4:
  Performing to get reminder "n" number of values by using
  #### Modules()

    i = MyMath(2, 3)
    print(f"output: {i.Modules()}")

  #### Output:
      output: 2
___
  ### Example-4:
  Performing division operation for single values by using
  #### factoriel()

    i = MyMath(5)
    print(f"output:\n{i.factoriel()}")

  #### Output:
      output:
      1! = 1
      2! = 2
      3! = 6
      4! = 24
      5! = 120
      120

___

## What I Learned
  - Key concepts practiced through MyMath project:
  - Using *args to accept flexible input
  - Basic OOP structure: class, __init__, methods
  - Control structures like loops and conditionals
  - Simple validation and error handling
  - Designing reusable components
  - 
---

## 🤝 Contributing

Contributions are welcome!

- Fork the repo
- Make your changes in a new branch
- Submit a Pull Request
- 
---

## 👨‍💻 Author

**Bharavi Sadineni**  
_Aspiring Python Developer | Focused on building OOP and real-time projects_  
📫 *Feel free to connect for feedback or collaboration!*