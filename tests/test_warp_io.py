#!/usr/bin/env python
"""Tests for warp matrix save/load."""

import numpy as np
from skimage.transform import ProjectiveTransform

from micasense.warp_io import (
    arrays_to_warp_matrices,
    load_warp_matrices,
    save_warp_matrices,
    warp_matrices_to_arrays,
)


def test_warp_matrices_round_trip_ndarray(panel_altum_capture, tmp_path):
    matrices = panel_altum_capture.get_warp_matrices()
    path = tmp_path / "warp.npy"
    save_warp_matrices(path, matrices)
    loaded = load_warp_matrices(path)
    for orig, transform in zip(matrices, loaded):
        np.testing.assert_allclose(orig, transform.params, atol=1e-6)


def test_warp_matrices_round_trip_projective(tmp_path):
    matrices = [
        ProjectiveTransform(matrix=np.eye(3)),
        ProjectiveTransform(matrix=np.diag([1.0, 1.0, 1.0])),
    ]
    path = tmp_path / "warp_sift.npy"
    save_warp_matrices(path, matrices)
    loaded = load_warp_matrices(path)
    for orig, loaded_t in zip(matrices, loaded):
        np.testing.assert_allclose(orig.params, loaded_t.params, atol=1e-6)


def test_load_as_arrays(tmp_path):
    arrays = warp_matrices_to_arrays([np.eye(3), np.eye(3) * 2])
    path = tmp_path / "warp_cv.npy"
    np.save(path, arrays, allow_pickle=True)
    loaded = load_warp_matrices(path, as_projective=False)
    assert len(loaded) == 2
    assert all(isinstance(m, np.ndarray) for m in loaded)
    np.testing.assert_allclose(loaded[0], np.eye(3), atol=1e-6)
