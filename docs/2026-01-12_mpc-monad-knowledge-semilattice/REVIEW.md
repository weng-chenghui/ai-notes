# Review: MPC as a Monadic Interface with Knowledge-Semilattice Semantics

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-12  
**Round:** 1

## Summary
The note presents a clean separation between (i) a monadic interface for compositional shared computation and (ii) an indexed adversary-view semantics whose induced knowledge sets form a meet-semilattice under intersection. Both Shamir secret sharing and the DSDP dot-product protocol are expressed within the same framework, and the strongest claims are accompanied by self-contained arguments.

## Issues

### Issue 1: Clarify what is and is not claimed for DSDP security
**Severity:** Minor  
**Location:** `main.tex`, \cref{prop:dsdp-sim-alice}  
**Description:** The simulation argument is intentionally a proof sketch. It is important that the text does not over-interpret the sketch as a complete, formally quantified theorem over all corruption patterns and all scheme subtleties (e.g., message space constraints, details of homomorphic evaluation distribution).  
**Suggested Fix:** Add a brief sentence emphasizing scope: corrupted Alice only (as stated), semi-honest only, and security relative to leakage \(\ell(u,v)=s\). Optionally note that other corruption patterns require separate simulators.
**Author Response:** Added an explicit ``three-part privacy checklist'' in \cref{sec:privacy-checklist} that separates functionality-level identifiability from protocol-level leakage, and points to \cref{def:leakage-security} as the precise scope (semi-honest, corrupted set \(S\), relative to a stated leakage function). The DSDP statement remains explicitly scoped to corrupted Alice only.
**Status:** Resolved

### Issue 2: Meet-semilattice semantics could be tied more explicitly to transcript accumulation
**Severity:** Minor  
**Location:** `main.tex`, \cref{sec:meet-semilattice} and \cref{sec:composition}  
**Description:** The note introduces constraint intersection as the meet operation. A short explicit mapping “each observed message adds a constraint” would help connect the formalism to protocol transcripts in both examples.  
**Suggested Fix:** Add one short remark that identifies \(C(\tau)\) as the set of global states consistent with a concrete transcript prefix, and that sequential messages correspond to iterated meets.
**Author Response:** Added a dedicated remark “Transcripts as iterated constraints” in \cref{sec:meet-semilattice}, and connected it to the privacy checklist in \cref{sec:privacy-checklist}.
**Status:** Resolved

## Status
- [x] Ready to merge
- [ ] Requires changes

