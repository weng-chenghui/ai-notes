# Review: A Bayesian Semantics for MPC: Priors, Views, and Posterior Privacy

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-13  
**Round:** 1

## Summary
The note proposes an explicitly Bayesian semantics: a protocol plus adversary strategy induces a transcript channel \(Q_{\mathcal{A}}(\tau\mid\sigma)\); a prior on global states yields posteriors; privacy is formulated as conditional independence of the target secret and transcript given an intended leakage function \(\ell\). Shamir is treated fully information-theoretically. DSDP is treated at the functionality level and, for transcript-level privacy, via an explicit idealized channel model with an open question about computational encryption.

## Issues

### Issue 1: Clarify measurability/finite-space assumptions
**Severity:** Minor  
**Location:** `main.tex`, \cref{sec:bayes-prelim}  
**Description:** The text alternates between sums (finite case) and integrals (general case). This is fine, but a short explicit statement “finite spaces assumed unless otherwise stated” would make the measure-theoretic level unambiguous.  
**Suggested Fix:** Add one sentence near the start of \cref{sec:bayes-prelim} declaring that the development is presented in the finite setting for simplicity.

### Issue 2: DSDP idealization should be clearly labeled as such
**Severity:** Minor  
**Location:** `main.tex`, \cref{def:dsdp-ideal-channel}  
**Description:** The idealized transcript model is appropriate for validating the Bayesian definition, but it should be highlighted that it is a modeling assumption (perfect secrecy of ciphertexts) that does not hold for public-key encryption.  
**Suggested Fix:** Emphasize “idealized” in the surrounding text (already mostly done), and optionally add a remark that computational encryption typically yields indistinguishability rather than exact conditional independence.

## Status
- [x] Ready to merge
- [ ] Requires changes

