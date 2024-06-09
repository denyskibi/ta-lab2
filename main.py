# Standard Libraries
import sys

# Custom Modules
from core.inversion_calculator import InversionCalculator
from utils import numpy_utils


def stop():
    sys.exit(1)


def main():
    # Create necessary class objects
    inversion_calculator = InversionCalculator()

    try:
        # Step #1: Завантажуємо матрицю з файлу
        loaded_matrix = numpy_utils.load_matrix_from_file(file_path="files/test_10_5.txt")

        ...
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed due to error: {e}")
    else:
        print(f"[SUCCESS] Finish without any errors!")


if __name__ == '__main__':
    main()
