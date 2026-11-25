---
name: python-oop-practice
description: Generates easy, medium, and hard Python 3 OOP practice problems using a consistent beginner-friendly coding style. Applies the same style to their hints, starter code, solutions, and explanations, and to requests for Python OOP practice code.
---

# Python OOP Practice

Increase problem difficulty while keeping naming, syntax choices, and code organization familiar. Apply these conventions to every class, snippet, demonstration, and follow-up solution in this practice workflow. Explicit user requests can change a convention; difficulty alone must never change it.

## Requests and default behavior

Support these requests and equivalent wording:

- "Give me an easy OOP problem"
- "Give me a medium OOP problem"
- "Give me a hard OOP problem"

Generate one problem at the requested level. If difficulty is unspecified, use easy and state the choice briefly. Continue using the same style when the user asks for hints, starter code, a solution, or an explanation.

By default, provide the problem without its solution or implementation code. Show sample behavior and expected results in plain text. Give hints, starter code, or a complete solution only when requested, and match the amount of help requested.

## Fixed Python 3 style

- Use PascalCase for class names, such as BankAccount.
- Use snake_case for variables, instance attributes, parameters, functions, and methods, such as account_balance.
- Use descriptive names and self as the instance parameter.
- Use public instance attributes: self.balance, never self._balance or self.__balance. Do not introduce leading underscores on ordinary attributes or methods at higher difficulty levels.
- Keep underscores between words. Preserve Python special names such as __init__, __name__, and __main__; the rule against leading underscores does not prohibit required Python special names.
- Define an explicit __init__ constructor and assign instance attributes explicitly with self.attribute = parameter. Initialize per-object mutable collections in the constructor.
- Use four spaces for indentation and double quotes for string literals. Keep ordinary Python spacing and clear blank lines between methods and definitions.
- Omit type annotations consistently, including parameter, return, and variable annotations.
- Favor straightforward loops, explicit conditions, and readable intermediate variables over compressed expressions or clever shortcuts.
- Avoid properties, dataclasses, decorators, and similar alternative class-definition patterns unless the user specifically requests them. Use ordinary methods for inheritance and method overriding; hard problems do not require abstract-class decorators.
- Do not add getters and setters merely to wrap every public attribute. Use methods for meaningful object behavior.
- Keep comments and explanations simple and consistent with the code's terminology. Call values stored on self instance attributes.

## Predictable code organization

When code is requested:

1. Put any necessary standard-library imports first; use standard-library-only examples by default.
2. Put class definitions next. Define a dependency or base class before the class that uses or inherits from it.
3. In each class, place __init__ first, followed by other methods in a clear, stable order. Preserve that order when extending an existing example.
4. Put a main() function after the classes to demonstrate object creation and method calls.
5. End complete runnable examples with the standard if __name__ == "__main__": entry point calling main().

Methods should generally return results or update object state; handle demonstration output with print() in main(). If an exercise specifically requires a display method, state that exception in the requirements and follow it consistently.

For a requested small snippet or hint, supply only the relevant portion while preserving these conventions. Do not add a full solution just to include main(). When explaining or repairing user code, preserve its problem requirements and use the fixed style for newly generated practice code.

Before generating implementation code, read [the reference example](references/style-example.py). Reuse its naming, constructor, method, return, and demonstration patterns rather than copying its subject matter or forcing its methods onto unrelated problems.

## Difficulty progression

- Easy: One class, a small set of attributes, an explicit constructor, and a few simple methods. Focus on creating objects, reading attributes, and changing object state.
- Medium: Multiple cooperating classes, composition, collections of objects, and basic validation. Keep the same public attributes and explicit methods used at easy level.
- Hard: More involved object relationships and business rules, with inheritance and method overriding where appropriate. Increase reasoning and coordination demands while retaining the same syntax and layout. Do not add patterns or abstractions solely to make the exercise look advanced.

Choose a coherent scenario. Class counts beyond easy are guided by the scenario, not a quota. Keep required concepts achievable with the fixed style; do not require a feature the style excludes unless the user asks to practice it.

## Exercise format

Use this order for every problem:

1. Title and difficulty.
2. A short scenario.
3. Required classes, including each class's constructor inputs, public attributes, and method names with their intended behavior and results.
4. Rules and constraints, including relevant validation and edge cases. State required failure behavior clearly.
5. Example behavior and expected results that agree with those requirements.

Keep requirements proportional to the requested difficulty. Avoid prescribing output formatting that distracts from practicing OOP. A requested solution must solve the stated exercise, use the same class and method names, and reproduce its expected behavior.

## Final consistency check

Before responding, check that:

- The problem fits the requested difficulty; harder levels changed concepts rather than coding style.
- All ordinary instance attributes are public, with no leading underscore names.
- Naming, four-space indentation, double quotes, and absence of type annotations are consistent wherever code appears.
- Constructors and complete-program layout match the reference; snippets remain appropriately scoped.
- No unrequested properties, dataclasses, decorators, or alternative styles were introduced.
- Requirements and expected results agree, and requested solutions cover the stated behavior and relevant edge cases.
- A problem-only request does not reveal its implementation or full solution.
