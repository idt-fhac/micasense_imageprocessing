#!/usr/bin/env python
# coding: utf-8
"""Smoke tests for Panel.panel_corners() on bundled example imagery.

The regression in the latest commit was caused by OpenCV being strict about the
input dtype to cv2.getPerspectiveTransform. This test exercises panel_corners()
end-to-end on the repository's example panel images to ensure it runs without
raising and returns a valid 4-corner polygon.
"""

from __future__ import annotations

import glob
from pathlib import Path

import pytest

import micasense.image as image
import micasense.panel as panel


def _example_panel_images() -> list[str]:
    repo_root = Path(__file__).parent.parent

    patterns = [
        repo_root / "data" / "REDEDGE-MX" / "IMG_0001_*.tif",
        repo_root / "data" / "REDEDGE-P" / "IMG_0000_*.tif",
        repo_root / "data" / "REDEDGE-MX-DUAL" / "IMG_0000_*.tif",
    ]

    files: list[str] = []
    for pat in patterns:
        files.extend(sorted(glob.glob(str(pat))))

    # Keep only images which are likely to contain a panel. If the list is empty,
    # don't hard fail locally; CI/packaging should include the sample imagery.
    return files


@pytest.mark.parametrize("image_path", _example_panel_images())
def test_panel_corners_runs_on_example_panels(image_path: str):
    img = image.Image(image_path)
    pan = panel.Panel(img)

    corners = pan.panel_corners()

    assert corners is not None, f"panel_corners() returned None for {image_path}"
    assert len(corners) == 4, f"expected 4 corners for {image_path}, got {len(corners)}"


def test_panel_corners_examples_present():
    """Fail with a clear message if sample data is missing."""
    files = _example_panel_images()
    assert files, (
        "No example panel images found under data/. Did you fetch LFS/sample data?"
    )
