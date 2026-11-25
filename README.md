# Python OOP Practice

A reusable skill for generating beginner-friendly Python 3 object-oriented programming exercises at easy, medium, and hard difficulty levels.

## What it does

- Creates one exercise at the requested difficulty (easy by default).
- Provides the problem first, without a solution unless one is requested.
- Keeps exercises, hints, starter code, solutions, and explanations consistent in style.
- Progresses from single-class exercises to cooperating classes, composition, and inheritance without adding unnecessary complexity.

## Style guidelines

Generated code uses PascalCase class names, snake_case names for other identifiers, public instance attributes, explicit constructors, four-space indentation, double-quoted strings, and no type annotations. Complete runnable examples use a `main()` function and the standard `if __name__ == "__main__":` entry point.

See [SKILL.md](SKILL.md) for the full behavior and style rules. The example in [references/style-example.py](references/style-example.py) demonstrates the intended code structure.

## Use

Ask for a Python OOP exercise, for example:

- “Give me an easy OOP problem.”
- “Give me a medium OOP problem.”
- “Give me a hard OOP problem.”

You can then request hints, starter code, a complete solution, or an explanation. The skill keeps those follow-ups aligned with the original exercise and its style.

## Repository contents

- `SKILL.md` — skill instructions and exercise-generation guidelines.
- `references/style-example.py` — a compact example of the preferred Python style.
