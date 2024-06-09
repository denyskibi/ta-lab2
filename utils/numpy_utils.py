# Third-party Libraries
import numpy as np
from numpy.typing import NDArray


def load_matrix_from_file(file_path: str) -> NDArray[int]:
    loaded_matrix = np.loadtxt(file_path, dtype=int)
    return loaded_matrix
