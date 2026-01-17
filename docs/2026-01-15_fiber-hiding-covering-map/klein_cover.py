import math
from typing import Tuple


def frac(t: float) -> float:
    """Return the fractional part of t in [0, 1)."""
    return t - math.floor(t)


def torus_to_klein(u: float, v: float) -> Tuple[float, float]:
    """
    A computable 2-to-1 covering map p: T^2 -> K, presented on fundamental domains.

    Representation:
      - Torus T^2 is represented by (u, v) with u, v taken mod 1 (so u, v in [0, 1)).
      - Klein bottle K is represented by (x, y) in [0, 1) x [0, 1) with identifications:
            (x, 0) ~ (x, 1)
            (0, y) ~ (1, 1 - y)

    Definition (fold then double):
      - Normalize (u, v) by the involution (u, v) ~ (u + 1/2, 1 - v)
        so that u is folded into [0, 1/2).
      - Output (x, y) = (2u, v) in [0, 1) x [0, 1).
    """
    u = frac(u)
    v = frac(v)

    # Fold along u = 1/2
    if u >= 0.5:
        u -= 0.5
        v = frac(1.0 - v)

    x = 2.0 * u
    y = v
    return (x, y)


def klein_preimages(x: float, y: float) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    """
    Return two torus-coordinate preimages of a Klein point (x, y) in the fundamental square.
    These satisfy:
        torus_to_klein(u1, v1) == (x mod 1, y mod 1)
        torus_to_klein(u2, v2) == (x mod 1, y mod 1)
    """
    x = frac(x)
    y = frac(y)
    u1, v1 = (0.5 * x, y)
    u2, v2 = (0.5 * x + 0.5, frac(1.0 - y))
    return (u1, v1), (u2, v2)


if __name__ == "__main__":
    # Quick sanity check: both preimages map to the same Klein coordinates
    test_points = [(0.1, 0.2), (0.7, 0.9), (0.0, 0.3), (0.999, 0.001)]
    for x, y in test_points:
        (u1, v1), (u2, v2) = klein_preimages(x, y)
        out1 = torus_to_klein(u1, v1)
        out2 = torus_to_klein(u2, v2)
        print(f"K=({x:.3f},{y:.3f})  pre1=({u1:.3f},{v1:.3f}) -> {out1}  pre2=({u2:.3f},{v2:.3f}) -> {out2}")

