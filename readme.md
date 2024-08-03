# Calculator App Development Documentation

## Introduction

This midterm project required the creation of a new repository from scratch, development, and documentation of a functional Calculator app that meets specific requirements. The development process utilized techniques learned from lectures, employing WSL, VS Code, and GitHub.

## Design Patterns

The following design patterns were implemented to ensure a modular, maintainable, and scalable design for the calculator app, enabling easy extension and modification of its functionality:

### I. Factory Method Pattern
- **Purpose**: Dynamically create instances of plugins.
- **Implementation**: The `PluginManager` loads and creates instances of various plugins based on the files available in the plugin directories.

### II. Singleton Pattern
- **Purpose**: Ensure that only one instance of the `Calculations` history exists and is used throughout the application.
- **Implementation**: While not a strict singleton, the design ensures a single shared state for the calculation history.

### III. Command Pattern
- **Purpose**: Encapsulate commands as objects, allowing the application to parameterize clients with different requests, queue or log requests, and support undoable operations.
- **Implementation**: Commands such as `add`, `subtract`, `multiply`, `divide`, and `exponent` are defined and encapsulated as objects.

### IV. Strategy Pattern
- **Purpose**: Encapsulate arithmetic operations within separate functions and make them interchangeable.
- **Implementation**: The `Calculation` class uses these strategies to perform operations like `add`, `subtract`, `multiply`, `divide`, and `exponent`.

### V. Facade Pattern
- **Purpose**: Provide a simplified interface to the complex subsystem of calculations and operations.
- **Implementation**: The `Calculator` class hides the complexities of creating `Calculation` objects and managing calculation history.

### VI. Decorator Pattern
- **Purpose**: Suppress output during test execution.
- **Implementation**: The `suppress_output_decorator` in `test_utils.py` wraps functions to temporarily redirect `stdout` and `stderr`.

## Conclusion

The implementation of these design patterns ensures that the calculator app is modular, maintainable, and scalable, allowing for easy extension and modification of its functionality.







use of environment variables



use of logging
