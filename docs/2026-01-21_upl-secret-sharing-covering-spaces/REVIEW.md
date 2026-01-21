# Review: Unique Path Lifting as a Sheet-Keyed Trajectory Scheme

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-21  
**Round:** 1  

## Summary

The note cleanly separates (i) the deterministic covering-space facts (path lifting, disjointness of lifts, endpoint transport/monodromy) from (ii) a genuinely probabilistic statement (the \(1/n\) guessing probability) that requires explicit modeling assumptions. The overall direction is correct and the exposition is close to publication quality.

However, a few points require tightening to match the repository’s rigor standard and to prevent common misreadings of “\(n\)-sheeted” language:

## Issues

### Issue 1: Fiber cardinality \(n\) is used without stating the connectedness assumption
**Severity:** Major  
**Location:** `main.tex`, \cref{sec:introduction,sec:secret-model} (use of “\(n\) sheets” / \(|p^{-1}(b_0)|=n\))  
**Description:** The note assumes the fiber over \(b_0\) has size \(n\), but does not state when this is globally well-defined (i.e., constant fiber cardinality). In general, for a covering map over a disconnected base, different components may have different degrees. The sheet-count intuition is correct once one restricts to the path component of \(b_0\) (or assumes \(B\) path-connected).  
**Suggested Fix:** Add a short proposition: if \(B\) is path-connected, then for any \(b_0,b_1\in B\) the endpoint transport along a path gives a bijection \(p^{-1}(b_0)\cong p^{-1}(b_1)\), hence all fibers have the same finite cardinality. Then clarify that “\(n\)-sheeted” refers to the degree over the component of \(b_0\).
  
**Author Response:** Added a clarification in \cref{sec:introduction} that “\(n\) sheets” is meant over the path component of \(b_0\), and added \cref{cor:fiber-cardinality-constant} (proved using endpoint transport) to formalize the constancy of fiber cardinality on path components.  
**Status:** Resolved

### Issue 2: Regular covering definition is given, but the conceptual equivalences are not recorded
**Severity:** Minor  
**Location:** `main.tex`, \cref{def:regular,prop:regular-deck-relation}  
**Description:** Defining regularity by transitivity of the deck group action is acceptable, but many readers expect the equivalent characterization via normal subgroups of \(\pi_1(B,b_0)\) (under standard hypotheses) or the “all sheets look the same” condition. Without a brief remark, it is easy to misinterpret \cref{rem:nonregular-fail} as claiming “there are no deck transformations,” rather than “there may be too few to connect a given fiber.”  
**Suggested Fix:** Add a short remark enumerating equivalent formulations under standard hypotheses (connected, locally path-connected, semilocally simply connected), while keeping the note self-contained (no external citations required).
  
**Author Response:** Added \cref{rem:regular-equivalences}, explicitly marking the standard hypotheses and giving the normalizer/normal-subgroup equivalence as optional background. The note continues to use only the transitivity definition \cref{def:regular}.  
**Status:** Resolved

### Issue 3: Non-regular case is discussed abstractly but would benefit from one explicit example
**Severity:** Minor  
**Location:** `main.tex`, \cref{rem:nonregular-fail}  
**Description:** The note correctly states that lifts need not be related by deck transformations in non-regular coverings, but it does not provide an example. A small explicit example would prevent readers from falsely believing the deck-translation statement is always true.  
**Suggested Fix:** Add an example of a connected, non-regular finite covering with a non-transitive deck group action (e.g., a degree-3 covering of a wedge of two circles described as a graph covering) and briefly explain why no deck transformation sends a chosen fiber point to another.
  
**Author Response:** Added \cref{sec:nonregular-example}, giving a concrete \(3\)-sheeted covering of \(S^1\vee S^1\) via an explicit labeled graph. Proved that \(\mathrm{Deck}(E/B)\) is trivial in \cref{prop:trivial-deck-group}, hence the covering is non-regular and provides the desired counterexample to “all lifts are deck translates.”  
**Status:** Resolved

## Status
- [ ] Ready to merge  
- [x] Requires changes  

---

# Review: Unique Path Lifting as a Sheet-Keyed Trajectory Scheme

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-21  
**Round:** 4  

## Summary

The reparameterization caveat has been clarified without changing the formal correctness. The new section on constructing paths on the base space is technically accurate, appropriately caveated, and consistent with the rest of the note.

No further issues were found.

## Issues

None.

## Status
- [x] Ready to merge  
- [ ] Requires changes  

---

# Review: Unique Path Lifting as a Sheet-Keyed Trajectory Scheme

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-21  
**Round:** 2  

## Summary

All three issues from Round 1 have been addressed: fiber cardinality is now properly scoped to path components and proved via endpoint transport; regular covering terminology is clarified (with hypotheses clearly marked); and an explicit connected non-regular finite covering with trivial deck group is included.

No further substantive issues were found.

## Issues

None.

## Status
- [x] Ready to merge  
- [ ] Requires changes  

---

# Review: Unique Path Lifting as a Sheet-Keyed Trajectory Scheme

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-21  
**Round:** 3  

## Summary

The note has been extended with a new subsection cataloguing which operations genuinely produce topological paths \(\gamma:[0,1]\to B\) and how to interpret discrete/algorithmic outputs and symbolic ``paths'' with appropriate caveats. The additions are broadly correct and align well with the covering-space interpretation.

One small technical point should be tightened: the reparameterization definition currently allows arbitrary continuous endpoint-fixing maps \(\phi\), which is fine for preserving continuity but can collapse nontrivial subintervals and may not match the intended ``same trace with different speed'' intuition. This is not incorrect, but it is potentially misleading in the context of concatenation and time parameter semantics.

## Issues

### Issue 1: Clarify the intended class of reparameterizations
**Severity:** Minor  
**Location:** `main.tex`, \cref{def:reparameterization,rem:reparameterization}  
**Description:** As written, a reparameterization \(\gamma\circ\phi\) permits \(\phi\) that are constant on intervals. This is topologically valid, but it can introduce ``waiting'' behavior and does not always preserve the geometric trace in the strict sense. Many readers expect reparameterizations to be nondecreasing surjections (or even homeomorphisms) of \([0,1]\).  
**Suggested Fix:** Either (i) strengthen the definition to require \(\phi\) to be continuous, nondecreasing, and surjective, or (ii) keep the current definition but explicitly remark that constant-on-interval reparameterizations correspond to ``pauses'' and are included intentionally.
  
**Author Response:** Kept the broad endpoint-fixing definition but updated \cref{rem:reparameterization} to explicitly note the common restriction to continuous nondecreasing surjections, and to explain that the broader class includes ``pauses'' (constant-on-interval behavior).  
**Status:** Resolved

## Status
- [ ] Ready to merge  
- [x] Requires changes  

