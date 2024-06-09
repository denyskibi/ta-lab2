# Third-party Libraries
from numpy.typing import NDArray


def count_inversions(matrix: NDArray[int], user1: int, user2: int) -> int:
    matrix_without_user_numbers = matrix[:, 1:]  # cut the first column with users
    inversions_count = 0

    favourite_films_user1 = matrix_without_user_numbers[user1 - 1]
    favourite_films_user2 = matrix_without_user_numbers[user2 - 1]

    films_count = len(favourite_films_user1)

    for i in range(films_count):
        if favourite_films_user1[i] > favourite_films_user2[i]:
            inversions_count += 1

    return inversions_count
