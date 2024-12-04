"""
Python Type Annotations Guide
This file demonstrates various scenarios of Python type hints and annotations.
"""

from typing import (
    List,
    Dict,
    Tuple,
    Set,
    Optional,
    Union,
    Any,
    Callable,
    TypeVar,
    Generic,
)

# 1. Basic Type Annotations
# Integer
age: int = 25

# Float
height: float = 5.11

# String
name: str = "John Doe"

# Boolean
is_active: bool = True

# 2. Complex Data Structures
# Lists
numbers: List[int] = [1, 2, 3, 4, 5]
matrix: List[List[int]] = [[1, 2], [3, 4]]
mixed_list: List[Union[int, str]] = [1, "two", 3, "four"]  # Can be string or int

# Dictionaries
user_info: Dict[str, str] = {"name": "John", "email": "john@example.com"}
nested_dict: Dict[str, Dict[str, int]] = {
    "math": {"score": 90, "rank": 1},
    "science": {"score": 85, "rank": 2},
}

# Tuples
coordinates: Tuple[int, int] = (10, 20)
mixed_tuple: Tuple[str, int, float] = ("test", 42, 3.14)

# Sets
unique_numbers: Set[int] = {1, 2, 3, 4, 5}

# 3. Optional Types
maybe_string: Optional[str] = None  # Can be str or None
maybe_int: Optional[int] = 42  # Can be int or None

# 4. Union Types
id_number: Union[int, str] = "ABC123"  # Can be either int or str


# 5. Function Annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"


def calculate_total(items: List[float], tax_rate: float = 0.1) -> float:
    return sum(items) * (1 + tax_rate)


# 6. Class Type Annotations
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def distance_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


# 7. Generic Types (Type Variables)
"""
Generic types allow you to write flexible, reusable code that works with different types
while maintaining type safety. They're especially useful for containers and data structures.

Benefits of Generics:
1. Type Safety: Catch type-related errors at compile time
2. Code Reusability: Write one class/function that works with multiple types
3. Better Documentation: Clear about what types are expected
Works like STL in Cpp.
"""

# Define type variables
T = TypeVar("T")  # Can be any type
Number = TypeVar("Number", int, float)  # Constrained to int or float
Key = TypeVar("Key")
Value = TypeVar("Value")


# Generic Stack Example
class Stack(Generic[T]):
    """
    A generic stack that can work with any type T.
    Usage:
    - Stack[int]() for integer stack
    - Stack[str]() for string stack
    """

    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> Optional[T]:
        return self.items.pop() if self.items else None

    def peek(self) -> Optional[T]:
        return self.items[-1] if self.items else None


# Generic Dictionary Example
class GenericDict(Generic[Key, Value]):
    """
    A generic dictionary that can work with any key-value type pair.
    Usage:
    - GenericDict[str, int]() for string keys and integer values
    - GenericDict[int, List[str]]() for integer keys and list of strings as values
    """

    def __init__(self) -> None:
        self.data: Dict[Key, Value] = {}

    def set_item(self, key: Key, value: Value) -> None:
        self.data[key] = value

    def get_item(self, key: Key) -> Optional[Value]:
        return self.data.get(key)


# Generic Function Example
def first_element(lst: List[T]) -> Optional[T]:
    """
    A generic function that returns the first element of any type of list
    """
    return lst[0] if lst else None


# Number-specific generic function
def add_numbers(a: Number, b: Number) -> Number:
    """
    A function that works with both int and float
    """
    return a + b


# 8. Callable Types
"""
Callable Types are simply type hints for functions in Python.
Think of them as function pointers in C++ or function references.

Basic Syntax: Callable[[input_types], return_type]
- [input_types]: List of input parameter types
- return_type: What the function returns

Examples:
- Callable[[int], str]     -> Function takes int, returns string
- Callable[[str, str], int] -> Function takes two strings, returns int
- Callable[[], None]       -> Function takes no input, returns nothing
"""

# Example 1: Simple function type
# Type hint for a function that takes two numbers and returns their sum
Calculator = Callable[[int, int], int]


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


# Function that uses a calculator function
def perform_operation(x: int, y: int, operation: Calculator) -> int:
    return operation(x, y)


# Example 2: Function with no parameters
Greeting = Callable[[], str]


def say_hello() -> str:
    return "Hello!"


def say_hi() -> str:
    return "Hi!"


def print_greeting(greeter: Greeting) -> None:
    print(greeter())


# Example 3: Simple callback
# Type hint for a function that processes a string message
MessageHandler = Callable[[str], None]


def log_message(msg: str) -> None:
    print(f"Log: {msg}")


def error_message(msg: str) -> None:
    print(f"Error: {msg}")


def handle_message(message: str, handler: MessageHandler) -> None:
    handler(message)


# 9. Type Aliases
Vector = List[float]
Matrix = List[Vector]


def matrix_multiply(a: Matrix, b: Matrix) -> Matrix:
    # Implementation here
    pass


# Examples of usage
if __name__ == "__main__":
    # Basic types
    print(f"Name: {name}, Age: {age}, Height: {height}")

    # List operations
    numbers.append(6)
    print(f"Numbers: {numbers}")

    # Dictionary operations
    user_info["age"] = "30"
    print(f"User Info: {user_info}")

    # Function with type hints
    total = calculate_total([10.0, 20.0, 30.0])
    print(f"Total with tax: {total}")

    # Class with type hints
    point = Point(3.0, 4.0)
    print(f"Distance: {point.distance_from_origin()}")

    # Generic stack
    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    print(f"Popped: {int_stack.pop()}")

    str_stack: Stack[str] = Stack()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"String from stack: {str_stack.pop()}")

    # Generic Dictionary Usage
    user_data: GenericDict[str, Any] = GenericDict()
    user_data.set_item("name", "John")
    user_data.set_item("scores", [95, 87, 91])
    print(f"User name: {user_data.get_item('name')}")

    # Generic Function Usage
    numbers = [1, 2, 3]
    strings = ["a", "b", "c"]
    print(f"First number: {first_element(numbers)}")
    print(f"First string: {first_element(strings)}")

    # Number Generic Usage
    print(f"Add integers: {add_numbers(5, 3)}")
    print(f"Add floats: {add_numbers(3.14, 2.86)}")

    # Callable Usage
    result1 = perform_operation(10, 5, add)
    print(f"10 + 5 = {result1}")

    result2 = perform_operation(10, 5, subtract)
    print(f"10 - 5 = {result2}")

    print_greeting(say_hello)  # Prints: Hello!
    print_greeting(say_hi)  # Prints: Hi!

    handle_message("Something happened", log_message)  # Normal log
    handle_message("Something went wrong", error_message)  # Error log
