# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* repr functions to classes so that debugging is easier
* delete old config files
* fixed jupyter notebooks
* `micasense.mp_config.spawn_pool()` using a per-pool spawn context (rawpy/OpenMP safe on Linux)
* `micasense.warp_io` — `save_warp_matrices` / `load_warp_matrices` for `.npy` warp matrix I/O
* Alignment v2, Batch Processing v2 notebooks and `batch_processing_script.py` use `warp_io`

### Fixed

* `SIFT_align_capture`: assign reference SIFT image when reference and target bands share shape (fixes `NameError` when `ref` is a multispectral band)
* `SIFT_align_capture`: fall back to calibrated warp matrices when SIFT match count is low (e.g. LWIR) instead of raising
* `ImageSet.save_stacks` and `imageutils` alignment pools use spawn context (not global `set_start_method`)
* declare `rawpy` as a runtime dependency
* remove unused `Capture.__sift_warp_matrices`

## [0.1.1] - 2025-12-28

### Added

* Added Classifiers and readme links

## [0.1.1] - 2025-12-27

### Added

* CI pipeline
* Community-Disclaimer
* SCM based versioning
* add file_paths to nested_lists output of imageset (741e443a)
* add functions to save tiffs separately (cf2bbdee)


### Fixed

* fixed warning in tests (8acef086)
* fixed numpy error (f25e07a1)
* fixed rng parameter for skimage ransac (a6ee4340)

## [0.0.1] - 2024-03-27

The last commit on the upstream micasense repository.
