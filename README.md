# PLP Python Week 5: Modules Assignment

## Overview of Files

* `password_generator.py` - Uses standard library modules `random` and `string` to generate customizable, secure random alphanumeric passwords.
* `helpers.py` - Custom helper module containing math rounding utility functions (`tables_needed`) and greeting utilities (`welcome`).
* `main.py` - Imports the custom `helpers` module to execute and display formatted results.
* `screenshots/` - Screenshots showing independent executions of `password_generator.py`, `helpers.py`, and `main.py`.

## Reflection

Understanding the `if __name__ == "__main__":` guard in `helpers.py` was key. It ensures that test code runs when executing the module file directly, but remains hidden when the module is imported into `main.py`.
