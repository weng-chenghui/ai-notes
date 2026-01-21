# Review: Discretizing the \(2\)-Sheeted Covering \(T^2\to K\)

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-18  
**Round:** 1

## Summary
The note clearly separates (i) the continuous covering \(T^2\to K\) described in \(E,B,\pi\) language, (ii) a property checklist, and (iii) a discrete analogue with an explicit comparison table. The overall direction is sound, but a few claims and definitions require tightening to avoid overstatement and to keep the discrete ``graph covering'' construction fully explicit.

## Issues

### Issue 1: Identification \(E/\langle\tau\rangle\cong K\) is asserted without construction
**Severity:** Major  
**Location:** `main.tex`, \cref{rem:quotient-is-klein}  
**Description:** The remark states that the orbit space is homeomorphic to the Klein bottle but does not provide a map or a citation.  
**Suggested Fix:** Either (a) provide a short explicit fundamental-domain argument (enough to justify the identification for this note), or (b) downgrade to ``is standard'' and mark as an external reference (then add a BibTeX entry).

**Author Response:** Added \cref{prop:quotient-is-klein-explicit}, defining an explicit map \(p:T^2\to K\) via a normalization/fold and showing it induces a homeomorphism \(\bar p:E/\langle\tau\rangle\cong K\) (compact-to-Hausdorff continuous bijection argument).  
**Status:** Resolved

### Issue 2: Graph quotient \(G(B_n)=G(E_n)/\langle\tau_n\rangle\) is underspecified
**Severity:** Major  
**Location:** `main.tex`, \cref{sec:graph-structure}  
**Description:** The quotient graph is invoked informally; the definition of adjacency downstairs should be explicit to avoid ambiguity (especially regarding multiple edges / loops).  
**Suggested Fix:** Define \(G(B_n)\) with vertices as orbits and adjacency declared when representatives are adjacent in \(G(E_n)\); state whether the resulting graph is simple (and if multiple edges are collapsed).

**Author Response:** Made the orbit-graph construction explicit: vertices are orbits in \(B_n\); adjacency is defined by existence of adjacent representatives in \(G(E_n)\); clarified that the simple graph is used (multiplicities forgotten).  
**Status:** Resolved

### Issue 3: Proof sketches should state the precise hypotheses used
**Severity:** Minor  
**Location:** `main.tex`, \cref{prop:free-z2-cover,prop:cover-upl,prop:graph-covering}  
**Description:** The proof sketches are correct in spirit but should explicitly mention the key ingredients (Hausdorffness for separating \(e\) and \(\tau(e)\); compactness of \(I\) for the finite subcover in path lifting; local neighbor bijection for graph coverings).  
**Suggested Fix:** Add one sentence per proof sketch clarifying the used fact.

**Author Response:** Strengthened the path-lifting sketch to explicitly invoke compactness of \(I\). The covering-by-quotient sketch already stated Hausdorffness and finiteness; the graph-covering sketch now explicitly states the neighbor-bijection mechanism.  
**Status:** Resolved

## Status
- [x] Ready to merge
- [ ] Requires changes

---

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-18  
**Round:** 2

## Summary
All previously raised issues are resolved. The identification \(E/\langle\tau\rangle\cong K\) is now supported by an explicit construction, the quotient-graph definition is unambiguous, and proof sketches state the needed hypotheses. The document meets the intended structure (continuous/topological part, property checklist, discretization and comparison).

---

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-18  
**Round:** 3

## Summary
Added \cref{sec:richer-cell-complex} explaining how a \(2\)-dimensional square complex refines the set-level and graph-level discretizations via skeleta, and why \(2\)-cells are needed to approximate surface topology (e.g.\ \(\pi_1(T^2)\cong\mathbb{Z}^2\) rather than a free group). The added material is consistent with prior claims and improves conceptual completeness; no further issues found.

## Status
- [x] Ready to merge

---

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-18  
**Round:** 4

## Summary
Added \cref{sec:skeleton-choices-mpc}, a protocol-oriented summary section with three subsections (\(0\)-, \(1\)-, and \(2\)-skeleton) that (i) specifies the construction, (ii) enumerates which properties P1--P5 are preserved (with names), and (iii) motivates each level in MPC terms (including IID vs stateful evolution, and \(2\)-skeleton use cases). No new technical issues identified.

## Status
- [x] Ready to merge

---

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-18  
**Round:** 5

## Summary
Expanded the \(2\)-skeleton motivation to include an explicit ``diamond'' commutation diagram for two update operations \(A\) and \(B\), and added \cref{sec:refinement-to-continuum} explaining that continuum approximation is achieved by refining \(2\)-dimensional cell decompositions (increasing resolution) rather than increasing skeleton dimension beyond \(2\). No issues found.

## Status
- [x] Ready to merge

---

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-18  
**Round:** 6

## Summary
Added Appendix A (\cref{app:mathcomp-survey}), a survey of formalizing the \(T^2\to K\) covering in the MathComp-Analysis Coq library. The survey covers four settings (continuous, \(0\)-skeleton, \(1\)-skeleton, \(2\)-skeleton with parametric cell density), listing for each: (i) what infrastructure is already present, (ii) what is lacking (with task lists and status), and (iii) effort estimates. Key findings: the \(0\)-skeleton model is immediately formalizable; the \(1\)-skeleton requires a lightweight graph library; continuous and \(2\)-skeleton settings require substantial new development (covering theory, cell complexes, fundamental groups). The appendix concludes with an overall assessment table and a practical recommendation. No issues found.

## Status
- [x] Ready to merge
