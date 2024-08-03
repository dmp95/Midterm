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



## Environment Variables

### Overview

Environment variables play a crucial role in configuring the application, particularly for logging settings and API key management. This approach enhances security by keeping sensitive information out of the codebase and provides flexibility for configuration changes.

### I. Logging Configuration

- **Location**: Defined in the `calculator/__init__.py` file.
- **Purpose**: Environment variables are utilized to set up logging configurations dynamically.

### II. API Key Management

- **Location**: Managed in the `main.py` file.
- **Purpose**: The `API_KEY` environment variable is used to handle API key configurations securely.

### Implementation Details

- **.env File**: A `.env` file is included at the project root, containing the required environment variables.
- **Security**: The `.env` file is excluded from version control by Git to protect sensitive information.

### Conclusion

By leveraging environment variables, the application maintains modularity, security, and ease of maintenance. This design pattern facilitates straightforward updates and extensions to the application’s functionality.






use of logging
