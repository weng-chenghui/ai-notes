# Review: Fiber Ambiguity as a Hiding Heuristic (Linear Maps vs.\ a 2-to-1 Covering \(T^2\to K\))
  
**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-17  
**Round:** 11  
  
## Summary
This round reviews the two additions made during the current session:
1. A worked \(n=5\) example table (\cref{ex:table-t-b-u-v}) illustrating the decomposition \(U=T+nB\) and the map \(p_5\).
2. A new subsection (\cref{sec:biased-u}) analyzing when the sheet bit \(B\) remains hidden under non-uniform distributions of \((U,V)\).

Both additions are mathematically correct and enhance the document's pedagogical value. The information-theoretic analysis in the biased-input subsection correctly identifies the two failure modes and provides a clean sufficient condition for perfect hiding of \(B\).
  
## Issues

### Issue 1: Minor terminology—"symmetric under negation"
**Severity:** Minor  
**Location:** `main.tex`, \cref{prop:biased-u-sufficient} (around line 375)  
**Description:** The phrase "symmetric under negation, i.e.\ \(V\overset{d}{=}-V\)" is understandable but slightly non-standard. A more common phrasing would be "negation-invariant in distribution" or simply "has a distribution invariant under \(v\mapsto -v\)."
  
**Suggested Fix:** Consider rephrasing to: "and that \(V\) is negation-invariant in distribution, i.e.\ \(V\overset{d}{=}-V\)." Alternatively, keep as-is if the current phrasing is deemed sufficiently clear.

### Issue 2: The table could note the fiber-pairing more explicitly
**Severity:** Minor  
**Location:** `main.tex`, \cref{ex:table-t-b-u-v} (around lines 321–343)  
**Description:** The table shows individual rows, and the text afterward notes that \(p_5(0,1)=p_5(5,4)=(0,1)\). It would be slightly clearer if the table explicitly grouped or annotated fiber-pairs (rows that map to the same \(K\)) to visually reinforce the two-preimage structure.
  
**Suggested Fix:** Either (a) reorder rows so that fiber-pairs are adjacent (e.g., \((0,1)\) and \((5,4)\) next to each other), or (b) add a column or annotation indicating which rows share the same output \(K\). This is optional and a matter of presentation preference.

### Issue 3: Proof of \cref{prop:biased-u-sufficient} could be slightly expanded
**Severity:** Minor  
**Location:** `main.tex`, proof of \cref{prop:biased-u-sufficient} (around lines 382–388)  
**Description:** The proof correctly uses the chain rule and the fact that \(I(B;W\mid T)=0\) under the stated assumptions. A one-sentence clarification of why \(W\) given \(T\) does not depend on \(B\) (because \(V\perp(B,T)\) and \(V\overset{d}{=}-V\)) would make the argument slightly more self-contained.
  
**Suggested Fix:** Add a brief sentence such as: "Since \(V\) is independent of \((B,T)\) and has the same distribution as \(-V\), the conditional distribution of \(W\) given \(T\) is identical whether \(B=0\) or \(B=1\)."

### Issue 4: Verify table entries for completeness
**Severity:** Verification  
**Location:** `main.tex`, \cref{ex:table-t-b-u-v}  
**Description:** Spot-checked several rows; all appear correct:
- \(U=0,V=1,B=0\): \(K=(0,1)\) ✓
- \(U=5,V=1,B=1\): \(K=(0,-1)=(0,4)\) ✓
- \(U=7,V=2,B=1\): \(T=2\), \(K=(2,-2)=(2,3)\) ✓
- \(U=9,V=4,B=1\): \(T=4\), \(K=(4,-4)=(4,1)\) ✓

No errors found.
  
## Status
- [x] Ready to merge
- [ ] Requires changes

