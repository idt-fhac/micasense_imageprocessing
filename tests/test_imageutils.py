#!/usr/bin/env python
# coding: utf-8
"""
Test imageutils functionality

Copyright 2017 MicaSense, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import pytest
from numpy import array


truth_warp_matrices = [
    array(
        [
            [1.00970826e00, 1.77994467e-03, -1.56924379e01],
            [-8.81481370e-04, 1.00902183e00, -2.00348790e01],
            [9.37048882e-07, 1.81088623e-07, 1.00000000e00],
        ]
    ),
    array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]),
    array(
        [
            [1.00178888e00, 5.20346163e-03, 3.69187005e01],
            [-3.96537869e-03, 1.00147557e00, 1.30881661e01],
            [9.43072540e-07, 4.60918812e-07, 1.00000000e00],
        ]
    ),
    array(
        [
            [1.00392234e00, 3.71917056e-04, 5.63565776e-01],
            [-1.01700706e-03, 1.00376351e00, -1.93992179e01],
            [7.62785884e-08, -6.79246435e-07, 1.00000000e00],
        ]
    ),
    array(
        [
            [1.00017929e00, -1.68397918e-03, -6.94129471e00],
            [-4.79481808e-04, 9.99392449e-01, -1.86069216e01],
            [-7.16703525e-07, -1.58956796e-06, 1.00000000e00],
        ]
    ),
    array(
        [
            [6.40923927e-02, -9.44614560e-04, 1.44295833e01],
            [1.15806613e-03, 6.36425220e-02, 7.48762382e00],
            [2.72813889e-06, 7.70422215e-07, 1.00000000e00],
        ]
    ),
]

truth_image_sizes = [
    (2064, 1544),
    (2064, 1544),
    (2064, 1544),
    (2064, 1544),
    (2064, 1544),
    (160, 120),
]

truth_lens_distortions = [
    array([-1.229523e-01, 2.344970e-01, 1.695486e-05, -4.560869e-04, -1.624159e-01]),
    array([-0.1279964, 0.2289589, 0.00027409, -0.00074023, -0.1536382]),
    array([-0.1281345, 0.2031752, 0.00043306, -0.00098965, -0.09603056]),
    array([-1.309457e-01, 2.203982e-01, -1.260115e-05, -4.066518e-04, -1.594542e-01]),
    array([-0.128634, 0.2207445, 0.0003157, -0.00077475, -0.1538338]),
    array([-0.3571166, 0.2329389, 0.00148511, -0.00306555, -0.02952669]),
]

truth_camera_matrices_old = [
    array(
        [
            [2.24343510e03, 0.00000000e00, 1.01295942e03],
            [0.00000000e00, 2.24343510e03, 7.67547825e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [2.23882015e03, 0.00000000e00, 1.01802029e03],
            [0.00000000e00, 2.23882015e03, 7.30214492e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [2.23464845e03, 0.00000000e00, 1.01673333e03],
            [0.00000000e00, 2.23464845e03, 7.58373912e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [2.24700170e03, 0.00000000e00, 1.01524638e03],
            [0.00000000e00, 2.24700170e03, 7.80426086e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [2.24418040e03, 0.00000000e00, 1.01343188e03],
            [0.00000000e00, 2.24418040e03, 7.45014492e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [162.63769993, 0.0, 78.2788333],
            [0.0, 162.63769993, 56.92766664],
            [0.0, 0.0, 1.0],
        ]
    ),
]

truth_camera_matrices = [
    array(
        [
            [2.26561955e03, 0.00000000e00, 1.03073913e03],
            [0.00000000e00, 2.26561955e03, 7.59208694e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [2.25366650e03, 0.00000000e00, 1.03212464e03],
            [0.00000000e00, 2.25366650e03, 7.72739129e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [2.25435270e03, 0.00000000e00, 1.07806666e03],
            [0.00000000e00, 2.25435270e03, 7.83782607e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [2.26837520e03, 0.00000000e00, 1.03717681e03],
            [0.00000000e00, 2.26837520e03, 7.52794202e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [2.26240075e03, 0.00000000e00, 1.02280000e03],
            [0.00000000e00, 2.26240075e03, 7.47063767e02],
            [0.00000000e00, 0.00000000e00, 1.00000000e00],
        ]
    ),
    array(
        [
            [160.98314994, 0.0, 81.30491663],
            [0.0, 160.98314994, 58.28508331],
            [0.0, 0.0, 1.0],
        ]
    ),
]

expected_dimensions = (20.0, 32.0, 1995.0, 1491.0)


def test_image_properties(non_panel_altum_capture):
    for i, image in enumerate(non_panel_altum_capture.images):
        assert image.size() == pytest.approx(truth_image_sizes[i])
        assert image.cv2_distortion_coeff() == pytest.approx(
            truth_lens_distortions[i], abs=0.001
        )
        assert image.cv2_camera_matrix() == pytest.approx(
            truth_camera_matrices[i], abs=0.001
        )


# def test_warp_matrices(non_panel_altum_capture):
#     warp_matrices = non_panel_altum_capture.get_warp_matrices()
#     print(warp_matrices)
#     for index, warp_matrix in enumerate(warp_matrices):
#         assert (warp_matrix == pytest.approx(truth_warp_matrices[index], rel=1e-2))
#
#
# def test_cropping(non_panel_altum_capture):
#     warp_matrices = non_panel_altum_capture.get_warp_matrices()
#     cropped_dimensions, _ = imageutils.find_crop_bounds(non_panel_altum_capture, warp_matrices)
#     assert (cropped_dimensions == pytest.approx(expected_dimensions, abs=1))
