"""
Main calculator interface.
"""
import operations

def calculate(operation: str, a: float, b: float) -> float:
    """
    Routes the requested operation to the correct math function.
    """
    if operation == "add":
        return operations.add(a, b)
    elif operation == "subtract":
        return operations.subtract(a, b)
    else:
        raise ValueError(f"Operation '{operation}' is not supported yet.")

if __name__ == "__main__":
    # Quick manual test
    print(f"10 + 5 = {calculate('add', 10, 5)}")
