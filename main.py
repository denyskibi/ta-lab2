# Standard Libraries
import sys

# Custom Modules
from core import favourite_films_inversions
from utils import numpy_utils


def stop():
    sys.exit(1)


def main():
    try:
        # Step #1: Load matrix from the file
        loaded_matrix = numpy_utils.load_matrix_from_file(file_path="files/test_10_5.txt")

        # Step #2: Count inversions for random users
        inversions_1_2 = favourite_films_inversions.count_inversions(matrix=loaded_matrix, user1=1, user2=2)
        inversions_1_5 = favourite_films_inversions.count_inversions(matrix=loaded_matrix, user1=1, user2=5)

        # Step #3: Print the result
        print(f"[INFO] Inversions between users 1 and 2: {inversions_1_2}")
        print(f"[INFO] Inversions between users 1 and 5: {inversions_1_5}")
    except KeyboardInterrupt:
        print("[ERROR] Failed: script interrupted by user (CTRL + C)")
        stop()
    except Exception as e:
        print(f"[ERROR] Failed due to error: {e}")
        stop()


if __name__ == '__main__':
    main()
