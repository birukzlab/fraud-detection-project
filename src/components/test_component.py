# src/components/test_component.py

from src.utils import get_greeting


def sample_function():
    greeting = get_greeting("Fraud Detection Project")
    print(greeting)

if __name__ == "__main__":
    print("test_component.py is running...")
    sample_function()
