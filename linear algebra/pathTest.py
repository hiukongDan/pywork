# path test
from pathlib import Path

if __name__ == "__main__":
    print(Path(__file__).resolve().parent)