# Review: Fiber Ambiguity as a Hiding Heuristic (Linear Maps vs.\ a 2-to-1 Covering \(T^2\to K\))
  
**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-15  
**Round:** 1  
  
## Summary
The note cleanly separates geometric non-injectivity (fiber structure) from distributional hiding, and provides an explicit fundamental-domain description of a 2-to-1 map \(T^2\to K\) plus runnable Python code. However, it currently lacks a parallel, finite-alphabet information-theoretic analysis for the covering-map example, which is essential given the intended ``hiding via fibers'' motivation.
  
## Issues
  
### Issue 1: Covering-map claim vs.\ heuristic statement
**Severity:** Minor  
**Location:** `main.tex`, \cref{sec:explicit-map}--\cref{sec:hiding-heuristic}  
**Description:** The note informally calls the map a ``2-to-1 covering'' while \cref{prop:two-preimages} only proves two explicit preimages; a full covering-map proof would require an ``evenly covered neighborhood'' argument.
**Suggested Fix:** Either (i) add a short lemma proving the covering property via local rectangles, or (ii) consistently describe it as a ``standard 2-to-1 map'' and leave the covering proof as future work.

### Issue 2: Missing finite-alphabet mutual-information analysis for \(T^2\to K\)
**Severity:** Major  
**Location:** `main.tex`, \cref{sec:cover}  
**Description:** The note motivates ``hiding'' but does not provide a concrete Shannon-entropy analysis for the torus-to-Klein example analogous to \cref{prop:perfect-hiding}. In particular, an explicit statement of what is (and is not) hidden (e.g.\ the \(\mathbb{Z}_2\) sheet) would clarify the security intuition.
**Suggested Fix:** Add a discrete model (e.g.\ \(\mathbb{Z}_{2n}\times\mathbb{Z}_n \to \mathbb{Z}_n\times\mathbb{Z}_n\)) with exact 2-point fibers, and compute \(H(U\mid K)\), \(I(U;K)\), and (optionally) \(I(B;K)\) for a chosen ``secret bit'' \(B\).
  
## Status
- [ ] Ready to merge
- [x] Requires changes

---

## Author Responses (after revisions)

### Issue 1: Covering-map claim vs.\ heuristic statement
**Author Response:** The note already treated the smooth covering claim cautiously in \cref{prop:two-preimages} and \cref{rem:covering-vs-dimension-drop}. In the current revision, the information-theoretic section is developed via an explicit \emph{finite} model \(p_n\) with exact two-point fibers (no need for a smooth covering proof). The smooth-map discussion remains explicitly heuristic.
**Status:** Resolved

### Issue 2: Missing finite-alphabet mutual-information analysis for \(T^2\to K\)
**Author Response:** Added \cref{sec:info-theory}, including a discrete torus \(\mathbb{T}_n\), a discrete Klein model \(\mathbb{K}_n\), an explicit 2-to-1 map \(p_n\) (\cref{def:discrete-cover}), and entropy/mutual-information computations (\cref{prop:hide-bit,prop:leakage-u}) showing precisely what is hidden (the sheet bit) and what leaks (\(U\bmod n\)).
**Status:** Resolved


