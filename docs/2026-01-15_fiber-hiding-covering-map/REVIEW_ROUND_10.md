# Review: Fiber Ambiguity as a Hiding Heuristic (Linear Maps vs.\ a 2-to-1 Covering \(T^2\to K\))
  
**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-17  
**Round:** 10  
  
## Summary
This round reviews the document for mathematical correctness. The information-theoretic discretization and the \(\pi_1(K)\) presentation are broadly correct as stated, but the Möbius-band construction in the topology interlude is not correct as written, and a few other places need clarification or additional justification to meet the repository's rigor standards.
  
## Issues
### Issue 1: Möbius band quotient model is not correct as written
**Severity:** Critical  
**Location:** `main.tex`, \cref{sec:mobius-to-circle} (around lines 324--336)  
**Description:** The definition
\[
M := (S^1\times I)/\!\sim,\qquad (\theta,0)\sim(\theta,0),\quad (\theta,1)\sim(-\theta,1)
\]
only imposes an identification on the boundary circle \(S^1\times\{1\}\) and does not implement the mapping-torus identification needed for the Möbius band. As a quotient, it does not yield the standard Möbius band and is unlikely to be a manifold at the identified boundary points (the identification does not extend to a neighborhood of the boundary). The sentence "Equivalently, \(M\) is the mapping torus of the reflection \(r:I\to I\), \(r(t)=1-t\)" is therefore inconsistent with the displayed quotient.
  
**Suggested Fix:** Replace the construction with a standard correct model, e.g.
- **Mapping torus model:** \(M := (I\times[0,1])/\bigl((t,0)\sim(1-t,1)\bigr)\), with projection to \(S^1\) induced by \([t,s]\mapsto e^{2\pi i s}\).
- **Square-with-twist model:** \(M := ([0,1]\times[0,1])/\bigl((0,t)\sim(1,1-t)\bigr)\), with the second coordinate giving the base circle.
Then update \(\pi_M\) accordingly and keep the monodromy discussion.

**Author Response:** Fixed. Replaced the incorrect quotient with the standard mapping-torus model \(M := (I\times[0,1])/((t,0)\sim(1-t,1))\) and updated the projection \(\pi_M([t,s])=e^{2\pi i s}\). Added concrete description of the gluing.  
**Status:** Resolved
  
### Issue 2: The explicit map \(p:T^2\to K\) is presented as a covering without proof/justification
**Severity:** Major  
**Location:** `main.tex`, \cref{sec:explicit-map,ex:covering-torus-klein}  
**Description:** The note defines a piecewise "fold then double" formula for \(p\), and later refers to the "standard quotient map \(p:T^2\to K\)" as a \(2\)-sheeted covering map. However, the document does not verify that the formula descends to a continuous map on the torus quotient, nor that it satisfies the local-triviality condition in \cref{def:covering-map}. As written, \cref{prop:two-preimages} establishes a 2-point preimage construction but does not prove the covering-map property.
  
**Suggested Fix:** Add a short justification such as:
- identify the involution \(\tau(u,v)=(u+\tfrac12,\,1-v)\) on \(T^2\), note it is free, and state that \(K\cong T^2/\langle\tau\rangle\) so the quotient projection is a 2-sheeted covering; or
- explicitly verify local neighborhoods in \(K\) lift to two disjoint copies in \(T^2\) for the given formula (at least sketch).
If treated as "standard," add an external citation with a precise pointer.

**Author Response:** Fixed. Added explicit definition of the involution \(\tau(u,v)=(u+\tfrac12,1-v)\), proved it is fixed-point free (hence a free \(\mathbb{Z}_2\)-action), and stated that \(p:T^2\to K\) is the quotient by this free involution, making it a 2-sheeted covering map.  
**Status:** Resolved
  
### Issue 3: Endpoint convention in the normalization step creates coordinate representatives outside \([0,1)\)
**Severity:** Minor  
**Location:** `main.tex`, \cref{sec:explicit-map} (lines 115--127)  
**Description:** For \(u\in[\tfrac12,1)\) and \(v=0\), the normalization sets \(v' = 1-v = 1\), which lies outside \([0,1)\). This is harmless if the intent is to work in \([0,1]\) and immediately pass to the \(y\sim y+1\) identification in \(K\), but the text simultaneously presents representatives in \([0,1)\times[0,1)\).
  
**Suggested Fix:** Either change the representative convention to \([0,1]\times[0,1]\) (with appropriate boundary identifications), or explicitly reduce \(v'\) modulo \(1\) before forming \((x,y)\).

**Author Response:** Fixed. Changed the normalization formula to explicitly apply \((1-v)\bmod 1\).  
**Status:** Resolved
  
### Issue 4: \(\pi_0(F)=0\) is not the correct statement in the LES argument
**Severity:** Minor  
**Location:** `main.tex`, proof of \cref{prop:pi1-short-exact} (around lines 441--447)  
**Description:** The proof states "\(\pi_0(F)=0\) since \(F\cong S^1\) is path-connected." Here \(\pi_0(F)\) is a pointed set (or set of components), not a group, and it is not "\(0\)" in the usual sense; rather, it is a singleton.
  
**Suggested Fix:** Replace with: "\(\pi_0(F)\) is a singleton since \(F\) is path-connected," and phrase the exactness conclusion accordingly (or cite the standard exact-sequence-of-groups refinement for connected fiber).

**Author Response:** Fixed. Replaced with: "The right term \(\pi_0(F)\) is a singleton (equivalently, the trivial pointed set) since \(F\cong S^1\) is path-connected."  
**Status:** Resolved
  
### Issue 5: Several "standard facts" are stated as propositions without proof or citation
**Severity:** Minor  
**Location:** `main.tex`, \cref{prop:covering-uplp,prop:bundle-fibration}  
**Description:** The statements "covering maps lift paths uniquely" and "bundles are fibrations (HLP)" are standard, but within this repository's stated rigor rules they should be accompanied by at least a proof sketch or an external reference with theorem/section pointer.
  
**Suggested Fix:** Add short proof sketches (e.g., via evenly covered neighborhoods for UPLP; via local trivializations and the homotopy lifting construction for bundles), or add precise citations to a standard algebraic topology text.

**Author Response:** Fixed. Added proof sketches for both propositions: (1) for UPLP, via evenly covered neighborhoods and compactness; (2) for bundles-are-fibrations, via local trivializations, compactness, and the gluing lemma.  
**Status:** Resolved
  
## Status
- [x] Ready to merge
- [ ] Requires changes

