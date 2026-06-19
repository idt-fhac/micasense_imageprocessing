#!/usr/bin/env python
"""Tests for SIFT_align_capture and multiprocessing spawn configuration."""

import numpy as np

from micasense.mp_config import spawn_pool


def test_sift_align_smoke(non_panel_rededge_capture):
    matrices = non_panel_rededge_capture.SIFT_align_capture(ref=0, min_matches=10)
    assert len(matrices) == len(non_panel_rededge_capture.images)
    assert np.allclose(matrices[0], np.eye(3))


def test_sift_align_same_shape_ref(non_panel_rededge_capture):
    """MS band as ref when all bands share resolution must not raise NameError."""
    matrices = non_panel_rededge_capture.SIFT_align_capture(ref=2, min_matches=10)
    assert len(matrices) == len(non_panel_rededge_capture.images)
    assert np.allclose(matrices[2], np.eye(3))


def test_sift_align_lwir_fallback(non_panel_altum_capture):
    """Altum LWIR should fall back to calibrated warp instead of aborting."""
    matrices = non_panel_altum_capture.SIFT_align_capture(ref=0, min_matches=10)
    assert len(matrices) == len(non_panel_altum_capture.images)
    assert np.allclose(matrices[0], np.eye(3))


def test_spawn_pool_uses_spawn_context():
    with spawn_pool(1) as pool:
        assert pool._ctx.get_start_method() == "spawn"
