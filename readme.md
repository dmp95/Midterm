# Calculator App Development Documentation

## Introduction

This project involved developing a Calculator app from scratch, including repository setup, application development, and documentation. The development process leveraged techniques from lectures and utilized tools such as WSL, VS Code, and GitHub.

## Design Patterns

The calculator app incorporates several design patterns to ensure a modular, maintainable, and scalable architecture. These patterns facilitate easy extension and modification of the app’s functionality:

### I. Factory Method Pattern
- **Purpose**: To create plugin instances dynamically.
- **Implementation**: The `PluginManager` is responsible for loading and instantiating plugins based on the available files in plugin directories.

### II. Singleton Pattern
- **Purpose**: To manage a single shared state for calculation history.
- **Implementation**: Although not a strict singleton, the design ensures a unified state for calculation history across the application.

### III. Command Pattern
- **Purpose**: To encapsulate commands as objects, allowing for parameterization, logging, and support for undoable operations.
- **Implementation**: Arithmetic operations such as `add`, `subtract`, `multiply`, `divide`, and `exponent` are encapsulated as command objects.

### IV. Strategy Pattern
- **Purpose**: To provide interchangeable arithmetic operations.
- **Implementation**: The `Calculation` class utilizes different strategies for operations including `add`, `subtract`, `multiply`, `divide`, and `exponent`.

### V. Facade Pattern
- **Purpose**: To simplify the interface to the complex calculation subsystem.
- **Implementation**: The `Calculator` class abstracts the complexities involved in creating `Calculation` objects and managing history.

### VI. Decorator Pattern
- **Purpose**: To suppress output during test execution.
- **Implementation**: The `suppress_output_decorator` in `test_utils.py` temporarily redirects `stdout` and `stderr` to facilitate testing.

## Environment Variables

### Overview

Environment variables are utilized to manage logging configurations and API keys, enhancing security and flexibility by keeping sensitive information out of the codebase.

### I. Logging Configuration
- **Location**: Configured in the `calculator/__init__.py` file.
- **Purpose**: To set up logging settings dynamically using environment variables.

### II. API Key Management
- **Location**: Managed in the `main.py` file.
- **Purpose**: To securely handle API key configurations using the `API_KEY` environment variable.

### Implementation Details
- **.env File**: Contains necessary environment variables and is located in the project root.
- **Security**: The `.env` file is excluded from version control by Git to protect sensitive information.

## Logging Functions

### I. Basic Configuration
- **Purpose**: To establish the logging setup.
- **Implementation**: Configured with `basicConfig`, allowing dynamic log level and format based on environment variables.

### II. Arithmetic Operations Logging
- **Purpose**: To record details of each arithmetic operation.
- **Implementation**: Logs operands and results of operations, along with errors such as division by zero.

### III. Command Handling Logging
- **Purpose**: To log user commands and execution results.
- **Implementation**: Records commands executed by users, including command names and any encountered errors.

### IV. Plugin Management Logging
- **Purpose**: To track the loading of plugins.
- **Implementation**: Logs plugin loading activities and any errors that occur during this process.

## Error Handling Strategies

### I. Look Before You Leap (LBYL)
- **Example**: Preventing division by zero.
- **Implementation**: Ensures the divisor is not zero before performing division operations.

### II. Easier to Ask for Forgiveness than Permission (EAFP)
- **Example**: Handling command execution errors.
- **Implementation**: Executes commands within a try block and handles exceptions if they arise.

## Conclusion

The application of these design patterns, effective use of environment variables, thorough logging, and strategic error handling ensures that the calculator app is robust, modular, and scalable. This design facilitates easy updates and extensions to the application's functionality.
