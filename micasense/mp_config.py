"""Multiprocessing helpers for rawpy/OpenMP safety."""

import multiprocessing as mp
from multiprocessing.pool import Pool
from typing import Optional


def spawn_pool(processes: Optional[int] = None) -> Pool:
    """Process pool using spawn (safe with rawpy/libraw OpenMP on Linux)."""
    return mp.get_context("spawn").Pool(processes=processes or mp.cpu_count())
