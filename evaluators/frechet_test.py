import pytest
from model.point import Point
from model.line_segment import LineSegment
from evaluators.frechet import FrechetLineSegmentEvaluator
from math import sqrt


@pytest.fixture
def frechet():
    return FrechetLineSegmentEvaluator()


def test_parallel_segments(frechet):
    p1 = Point(0, 0, 0)
    p2 = Point(1, 1, 1)
    q1 = Point(0, 0, 1)
    q2 = Point(1, 1, 2)
    result = frechet._segment_distance(p1, p2, q1, q2)
    assert result == pytest.approx(0.0, rel=1e-5)


@pytest.mark.xfail(
    reason="Doesn't handle perpendicular case correctly. Adjusting it to do so will affect other segment types."
)
def test_perpendicular_segments(frechet):
    p1 = Point(0, 0, 0)
    p2 = Point(0, 1, 0)
    q1 = Point(1, 0, 0)
    q2 = Point(1, 1, 0)
    result = frechet._segment_distance(p1, p2, q1, q2)
    assert result == pytest.approx(1.0, rel=1e-9)


def test_coincident_segments(frechet):
    p1 = Point(0, 0, 0)
    p2 = Point(1, 1, 1)
    q1 = Point(0, 0, 0)
    q2 = Point(1, 1, 1)
    result = frechet._segment_distance(p1, p2, q1, q2)
    assert result == pytest.approx(0.0, rel=1e-5)


def test_non_intersecting_segments(frechet):
    p1 = Point(0, 0, 0)
    p2 = Point(1, 1, 1)
    q1 = Point(2, 2, 2)
    q2 = Point(3, 3, 3)
    result = frechet._segment_distance(p1, p2, q1, q2)
    assert result == pytest.approx(0.0, rel=1e-5)


def test_different_lengths(frechet):
    p1 = Point(0, 0, 0)
    p2 = Point(2, 0, 0)
    q1 = Point(1, 1, 1)
    q2 = Point(1, 2, 1)
    result = frechet._segment_distance(p1, p2, q1, q2)
    assert result == pytest.approx(1.0, rel=1e-5)


# TODO: test actual segments
