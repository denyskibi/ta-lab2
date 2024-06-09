# Third-party Libraries
from numpy.typing import NDArray


def count_inversions(matrix: NDArray[int], user1: int, user2: int) -> int:
    inversions_count = 0

    favourite_films_user1 = matrix[user1 - 1]
    favourite_films_user2 = matrix[user2 - 1]

    films_count = len(favourite_films_user1)

    for i in range(films_count):
        if favourite_films_user1[i] > favourite_films_user2[i]:
            inversions_count += 1

    return inversions_count
