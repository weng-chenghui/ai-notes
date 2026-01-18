"""
Discrete 2-to-1 "torus to Klein" map and information-theoretic checks.

This script numerically verifies the finite-alphabet calculations in main.tex,
Section "Information-theoretic analysis (finite discretization)".

Model:
  - Discrete torus:  T_n = Z_{2n} x Z_n
  - Discrete Klein:  K_n = Z_n x Z_n
  - Map p_n:
        if u in {0,...,n-1}:      p_n(u,v) = (u, v)
        if u in {n,...,2n-1}:     p_n(u,v) = (u-n, -v mod n)

Random variables:
  - (U,V) uniform on T_n
  - K = p_n(U,V)
  - Sheet bit B = 0 if U<n else 1
  - Residue T = U mod n
"""

from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass
from typing import Dict, Hashable, Iterable, Tuple


def p_n(u: int, v: int, n: int) -> Tuple[int, int]:
    """Discrete map p_n: Z_{2n} x Z_n -> Z_n x Z_n."""
    if n < 2:
        raise ValueError("n must be >= 2")
    u_mod = u % (2 * n)
    v_mod = v % n
    if u_mod < n:
        return (u_mod, v_mod)
    return (u_mod - n, (-v_mod) % n)


def sheet_bit(u: int, n: int) -> int:
    """B in {0,1} where U = T + nB."""
    return 0 if (u % (2 * n)) < n else 1


def residue_t(u: int, n: int) -> int:
    """T = U mod n."""
    return (u % (2 * n)) % n


def entropy_bits_from_counts(counts: Dict[Hashable, int]) -> float:
    """Shannon entropy H in bits from a count dictionary."""
    total = sum(counts.values())
    if total == 0:
        return 0.0
    h = 0.0
    for c in counts.values():
        if c == 0:
            continue
        p = c / total
        h -= p * math.log2(p)
    return h


def joint_counts(pairs: Iterable[Tuple[Hashable, Hashable]]) -> Counter:
    """Count occurrences of joint outcomes."""
    return Counter(pairs)


def marginalize_first(joint: Counter) -> Counter:
    """From counts of (a,b), return counts of a."""
    out = Counter()
    for (a, _b), c in joint.items():
        out[a] += c
    return out


def marginalize_second(joint: Counter) -> Counter:
    """From counts of (a,b), return counts of b."""
    out = Counter()
    for (_a, b), c in joint.items():
        out[b] += c
    return out


def conditional_entropy_bits(joint_xy: Counter) -> float:
    """
    Compute H(X|Y) in bits from counts of (x,y).
    Uses H(X|Y) = H(X,Y) - H(Y).
    """
    h_xy = entropy_bits_from_counts(joint_xy)
    h_y = entropy_bits_from_counts(marginalize_second(joint_xy))
    return h_xy - h_y


def mutual_information_bits(joint_xy: Counter) -> float:
    """Compute I(X;Y) in bits from counts of (x,y)."""
    h_x = entropy_bits_from_counts(marginalize_first(joint_xy))
    h_y = entropy_bits_from_counts(marginalize_second(joint_xy))
    h_xy = entropy_bits_from_counts(joint_xy)
    return h_x + h_y - h_xy


@dataclass(frozen=True)
class Results:
    n: int
    h_u: float
    h_uv: float
    h_k: float
    h_u_given_k: float
    h_uv_given_k: float
    i_u_k: float
    i_uv_k: float
    i_b_k: float


def compute_results(n: int) -> Results:
    # Enumerate uniform (U,V) on T_n
    uv = [(u, v) for u in range(2 * n) for v in range(n)]

    # Build samples of derived variables
    u_samples = [u for (u, _v) in uv]
    uv_samples = uv
    k_samples = [p_n(u, v, n) for (u, v) in uv]
    b_samples = [sheet_bit(u, n) for (u, _v) in uv]

    # Counts
    u_counts = Counter(u_samples)
    uv_counts = Counter(uv_samples)
    k_counts = Counter(k_samples)

    # Joint counts
    u_k_joint = joint_counts(zip(u_samples, k_samples))
    uv_k_joint = joint_counts(zip(uv_samples, k_samples))
    b_k_joint = joint_counts(zip(b_samples, k_samples))

    # Entropies and mutual informations (bits)
    h_u = entropy_bits_from_counts(u_counts)
    h_uv = entropy_bits_from_counts(uv_counts)
    h_k = entropy_bits_from_counts(k_counts)
    h_u_given_k = conditional_entropy_bits(u_k_joint)
    h_uv_given_k = conditional_entropy_bits(uv_k_joint)
    i_u_k = mutual_information_bits(u_k_joint)
    i_uv_k = mutual_information_bits(uv_k_joint)
    i_b_k = mutual_information_bits(b_k_joint)

    return Results(
        n=n,
        h_u=h_u,
        h_uv=h_uv,
        h_k=h_k,
        h_u_given_k=h_u_given_k,
        h_uv_given_k=h_uv_given_k,
        i_u_k=i_u_k,
        i_uv_k=i_uv_k,
        i_b_k=i_b_k,
    )


def approx_equal(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


if __name__ == "__main__":
    for n in [2, 3, 4, 8, 16]:
        r = compute_results(n)

        # Predicted values from main.tex:
        #   H(U) = log2(2n) = 1 + log2(n)
        #   H(U,V) = log2(2n^2) = 1 + 2log2(n)
        #   H(K) = log2(n^2) = 2log2(n)
        #   H(U|K) = 1
        #   H(U,V|K) = 1
        #   I(U;K) = log2(n)
        #   I((U,V);K) = 2log2(n)
        #   I(B;K) = 0
        pred_h_u = 1.0 + math.log2(n)
        pred_h_uv = 1.0 + 2.0 * math.log2(n)
        pred_h_k = 2.0 * math.log2(n)
        pred_h_u_given_k = 1.0
        pred_h_uv_given_k = 1.0
        pred_i_u_k = math.log2(n)
        pred_i_uv_k = 2.0 * math.log2(n)
        pred_i_b_k = 0.0

        print(f"n={n}")
        print(f"  H(U)          = {r.h_u:.12g}   (pred {pred_h_u:.12g})")
        print(f"  H(U,V)        = {r.h_uv:.12g}  (pred {pred_h_uv:.12g})")
        print(f"  H(K)          = {r.h_k:.12g}   (pred {pred_h_k:.12g})")
        print(f"  H(U|K)        = {r.h_u_given_k:.12g}   (pred {pred_h_u_given_k:.12g})")
        print(f"  H(U,V|K)      = {r.h_uv_given_k:.12g}   (pred {pred_h_uv_given_k:.12g})")
        print(f"  I(U;K)        = {r.i_u_k:.12g}   (pred {pred_i_u_k:.12g})")
        print(f"  I((U,V);K)    = {r.i_uv_k:.12g}  (pred {pred_i_uv_k:.12g})")
        print(f"  I(B;K)        = {r.i_b_k:.12g}   (pred {pred_i_b_k:.12g})")

        ok = (
            approx_equal(r.h_u, pred_h_u)
            and approx_equal(r.h_uv, pred_h_uv)
            and approx_equal(r.h_k, pred_h_k)
            and approx_equal(r.h_u_given_k, pred_h_u_given_k)
            and approx_equal(r.h_uv_given_k, pred_h_uv_given_k)
            and approx_equal(r.i_u_k, pred_i_u_k)
            and approx_equal(r.i_uv_k, pred_i_uv_k)
            and approx_equal(r.i_b_k, pred_i_b_k)
        )
        print(f"  checks: {'OK' if ok else 'FAILED'}\n")

