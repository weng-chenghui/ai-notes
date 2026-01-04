# Review: Fix BibTeX builds and preserve acronym casing

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-04  
**Round:** 1

## Summary

This PR addresses two user-visible issues: unresolved citations rendering as `[?]` and acronym casing (“Mpc” vs “MPC”) on the GitHub Pages index. The changes are targeted and low risk.

## Issues

### Issue 1: BibTeX execution policy in CI
**Severity:** Minor  
**Location:** `.github/workflows/build.yml`  
**Description:** CI runs `bibtex` when `\\bibliography{}` or `\\bibliographystyle{}` is present, but it ignores `biblatex` (`\\addbibresource{}`) documents.\n**Suggested Fix:** Either document this limitation or extend CI to support `biber` when `\\addbibresource{}` is detected.\n

**Author Response:** Documented the limitation inline in the workflow (BibTeX supported; biblatex/biber not yet supported).  
**Status:** Resolved
## Status
- [x] Ready to merge
- [ ] Requires changes

