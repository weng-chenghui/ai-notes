# Review: Integers from the Universal Cover of the Circle

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-18  
**Round:** 1

## Summary
The note captures the intended intuition well and uses appropriate terminology (covering map, fibers, deck transformations). However, several statements currently rely on ``standard facts'' without proof or citation, and one general classification claim is stronger than needed for the stated goals. Tightening these points would improve rigor and keep the document self-contained.

## Issues

### Issue 1: Covering/universal-cover claim is not justified
**Severity:** Major  
**Location:** `main.tex`, Abstract; \cref{sec:universal-cover}  
**Description:** The text states that \(p(t)=e^{2\pi i t}\) is ``the universal covering map'' and later says ``(indeed, the universal cover)'' but does not provide a proof that \(p\) is a covering map, nor does it justify the universal property.  
**Suggested Fix:** Add a proposition proving that \(p\) is a covering map using explicit evenly covered arcs and the exponential/log correspondence on such arcs. Either (a) remove ``universal'' claims, or (b) state them as standard and add a precise citation (with theorem number/page), or (c) add an explicit argument for simply-connectedness of \(\mathbb{R}\) and the universal covering property.
  
**Author Response:** Added \cref{prop:p-is-covering} with an explicit evenly-covered-arc proof, and removed the unproved ``universal cover'' phrasing from the abstract and main text.  
**Status:** Resolved

### Issue 2: General classification statement via \(\pi_1\)-actions is too strong without citation
**Severity:** Major  
**Location:** `main.tex`, \cref{sec:discrete-fiber}  
**Description:** The statement ``connected coverings with fiber \(F\) are governed by a \(\pi_1(B)\)-action on \(F\)'' is essentially a classification theorem. As written it is not proved and not cited with the required precision.  
**Suggested Fix:** Avoid the general claim and instead give a concrete construction over \(S^1\): for a discrete set \(F\) and bijection \(T:F\to F\), define \(E=(\mathbb{R}\times F)/\!\sim\) with \((t+1,f)\sim (t,T(f))\) and map \([t,f]\mapsto e^{2\pi i t}\). Prove directly that this map is a covering (when \(T\) is bijective). This achieves the desired intuition (``state update per full turn'') without invoking the full classification theorem.
  
**Author Response:** Replaced the general \(\pi_1\)-classification claim with the explicit construction in \cref{prop:mapping-torus-cover} and a direct proof that the resulting map \(q:E\to S^1\) is a covering.  
**Status:** Resolved

### Issue 3: ``Canonical identification of fibers with \(\mathbb{Z}\)'' needs a clearer qualifier
**Severity:** Minor  
**Location:** `main.tex`, Abstract  
**Description:** The statement ``fibers are ... canonically identified with \(\mathbb{Z}\) once a basepoint lift is chosen'' is correct but could be sharpened: the identification depends on the choice of lift and is canonical only relative to that choice (equivalently, canonical as a torsor under deck transformations).  
**Suggested Fix:** Rephrase to emphasize ``canonical relative to a chosen lift'' or mention that the fiber is a \(\mathbb{Z}\)-torsor.
  
**Author Response:** Rephrased the abstract to state choice-relative canonicity and explicitly mention the \(\mathbb{Z}\)-torsor viewpoint.  
**Status:** Resolved

## Status
- [x] Ready to merge
- [ ] Requires changes

---

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-18  
**Round:** 2

## Summary (Round 2)
All previously identified issues have been addressed: the covering-map claim is now proved explicitly, the universal-cover wording is justified via a clear definition plus contractibility of \(\mathbb{R}\), and the over-strong general \(\pi_1\)-classification statement has been replaced by a concrete construction over \(S^1\) with a direct proof.

## Status (Round 2)
- [x] Ready to merge
- [ ] Requires changes

