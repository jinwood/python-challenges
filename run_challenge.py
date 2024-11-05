import os
import sys
import pytest
import importlib
from typing import Optional


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

    #  Import test module to display the challenge description
    try:
        module = importlib.import_module(
            f"challenges.{challenge_path}.test_{challenge_path.split('/')[-1]}")
        print("\nChallenge Description:")
        print("=" * 50)
        print(module.__doc__)
        print("=" * 50 + "\n")
    except ImportError:
        return f"Could not load tests for '{challenge_path}!"

    # Run pytest for the challenge
    pytest.main(['-v', full_path])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_challenge.py <challenge_path>")
        print("Example: python run_challenge.py easy/sum")
        sys.exit(1)

    result = run_challenge(sys.argv[1])
    if (result):
        print(result)

# pytest==7.4.0
