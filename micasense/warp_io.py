"""Load and save band alignment warp matrices (.npy)."""

from pathlib import Path
from typing import List, Union

import numpy as np
from skimage.transform import ProjectiveTransform

MatrixLike = Union[np.ndarray, ProjectiveTransform]


def _matrix_to_array(matrix: MatrixLike) -> np.ndarray:
    if isinstance(matrix, ProjectiveTransform):
        return np.asarray(matrix.params, dtype=np.float64)
    return np.asarray(matrix, dtype=np.float64)


def warp_matrices_to_arrays(matrices: List[MatrixLike]) -> np.ndarray:
    """Convert warp matrices to an object array of 3×3 float64 (on-disk format)."""
    return np.array([_matrix_to_array(m) for m in matrices], dtype=object)


def arrays_to_warp_matrices(
    arrays: np.ndarray, *, as_projective: bool = True
) -> list:
    """
    Convert a loaded object array back to warp matrices.

    :param as_projective: If True, return ``ProjectiveTransform`` (SIFT / skimage).
        If False, return ``ndarray`` (OpenCV alignment path).
    """
    result = []
    for item in arrays:
        arr = np.asarray(item)
        if as_projective:
            result.append(ProjectiveTransform(matrix=arr.astype(np.float64)))
        else:
            result.append(arr.astype(np.float32))
    return result


def save_warp_matrices(path: Union[Path, str], matrices: List[MatrixLike]) -> None:
    """Save warp matrices in the standard ``.npy`` format (object array, pickle)."""
    np.save(Path(path), warp_matrices_to_arrays(matrices), allow_pickle=True)


def load_warp_matrices(
    path: Union[Path, str], *, as_projective: bool = True
) -> list:
    """Load warp matrices written by :func:`save_warp_matrices`."""
    arrays = np.load(Path(path), allow_pickle=True)
    return arrays_to_warp_matrices(arrays, as_projective=as_projective)
