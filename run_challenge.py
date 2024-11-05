import os
import sys
import pytest
import importlib
from typing import Optional

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)


def run_challenge(challenge_path: str) -> Optional[str]:
    """
    Run tests for a specific challenge.
    Args:
        challenge_path: Path to the challenge (e.g. 'easy/sum')
    """
    # Construct the full path
    full_path = os.path.join('challenges', challenge_path)

    if not os.path.exists(full_path):
        return f"Challenge '{challenge_path}' not found!"

    try:
        # Convert filesystem path to import path
        module_path = challenge_path.replace('/', '.')
        import_path = f"challenges.{module_path}.test_{challenge_path.split('/')[-1]}"
        print(f"Trying to import: {import_path}")

        module = importlib.import_module(import_path)

        print("\nChallenge Description:")
        print("=" * 50)
        print(module.__doc__)
        print("=" * 50 + "\n")
    except ImportError as e:
        print(f"Import error details: {e}")
        return f"Could not load tests for '{challenge_path}'"
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
        return f"Error running challenge '{challenge_path}'"

    # Run pytest for the challenge
    pytest.main(['-v', full_path])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_challenge.py <challenge_path>")
        print("Example: python run_challenge.py easy/sum")
        sys.exit(1)

    result = run_challenge(sys.argv[1])
    if result:
        print(result)
