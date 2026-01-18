# Review: Fiber Ambiguity as a Hiding Heuristic (Linear Maps vs.\ a 2-to-1 Covering \(T^2\to K\))
  
**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-17  
**Round:** 13  
  
## Summary
This round reviews a new appendix section (\cref{sec:appendix-examples}) that collects additional topology examples of maps with multiple preimages and formalizes the ``finite fiber via quotient'' mechanism through free finite group actions (\cref{sec:appendix-finite-group-quotients}). The statements are mathematically correct, use existing definitions, and reinforce the note's theme that topological non-injectivity is distinct from information-theoretic hiding. The document recompiles cleanly.
  
## Issues
### Issue 1: Mild topological hypothesis in \cref{prop:finite-free-quotient-cover}
**Severity:** Minor  
**Location:** `main.tex`, \cref{prop:finite-free-quotient-cover}  
**Description:** The proposition states a sufficient condition (finite group, free action, Hausdorff \(E\)) for the quotient map \(E\to E/G\) to be a \(|G|\)-sheeted covering. While correct in standard settings (e.g.\ manifolds and CW complexes), some texts additionally assume mild regularity (e.g.\ \(E\) is locally path-connected / locally compact) to streamline the evenly-covered neighborhood argument and avoid pathological quotients.
  
**Suggested Fix:** Optionally strengthen hypotheses to ``\(E\) Hausdorff and locally path-connected'' (or ``\(E\) a manifold''), or add a short remark clarifying that the intended use is in manifold-like examples (such as \(T^2\), \(S^n\)).
  
## Status
- [x] Ready to merge
- [ ] Requires changes

