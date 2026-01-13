# Review: Constraint-Based and Categorical Notions of MPC Privacy

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-13  
**Round:** 1

## Summary
The note presents a crisp constraint-based privacy notion (posterior vs.\ ideal fibers), a probabilistic fiber-indistinguishability condition, and a categorical factorization statement in a Markov-category language with a TikZ commuting diagram. The overall structure is clear and the definitions are plausible. A few points need tightening to meet the repository's rigor and citation standards.

## Issues

### Issue 1: Threat model and quantification of the ``view''
**Severity:** Major  
**Location:** `main.tex`, \cref{sec:setup}  
**Description:** The definition of the view $V_C$ is intentionally broad, but the later definitions (\cref{def:fibers}, \cref{def:zac}, \cref{def:fiber-ind}) quantify over $\Pr[V_C=v\mid x_C,x_{\bar C}]$ and implicitly assume a well-defined distributional semantics. This should be made explicit (e.g.\ semi-honest, fixed protocol, explicit random tape for honest parties, or at least ``for the protocol's induced distribution over transcripts'').
**Suggested Fix:** Add a short paragraph specifying the execution semantics used by the definitions (e.g.\ an abstract randomized protocol with induced distribution on $V_C$ for each input pair), and note how malicious behavior would be modeled (e.g.\ by quantifying over adversary strategies).
  
**Author Response:** Added an explicit ``fix protocol $\Pi$'' semantics paragraph clarifying that $\Pr[V_C=\cdot\mid x_C,x_{\bar C}]$ is the protocol-induced distribution for each input pair, and noted how a malicious model would quantify over adversary strategies $A$ (interpreting the distribution as that induced by $(\Pi,A)$).  
**Status:** Resolved

### Issue 2: Precision of citations for Markov categories / conditional independence
**Severity:** Major  
**Location:** `main.tex`, \cref{sec:categorical} and \cref{rem:cond-indep}  
**Description:** The note cites \cite[Section~2]{Fritz2020} for Markov categories, but \cref{rem:cond-indep} states implications about conditional independence across priors without a citation or hypotheses. Also, the statement ``Markov categories \cite[Section~2]{Fritz2020}'' should be checked for exact location (it may be a different section/terminology) and adjusted with more precise pointers.
**Suggested Fix:** Add a citation in \cref{rem:cond-indep} (or weaken the claim to ``often'' with explicit assumptions). Add a second citation pointer for conditional independence in the Markov-category setting (if covered in \cite{Fritz2020}, cite the relevant theorem/section).
  
**Author Response:** Added an explicit citation to \cite{Fritz2020} in \cref{rem:cond-indep} for conditional independence/factorization in the Markov-kernel setting, and kept the ``common measure-theoretic settings'' phrasing to avoid overclaiming without enumerating hypotheses.  
**Status:** Resolved

### Issue 3: Clarify the relationship between set-based and probabilistic notions
**Severity:** Minor  
**Location:** `main.tex`, \cref{rem:zac-strong} and \cref{sec:probabilistic}  
**Description:** The note says the set-based notion is stronger but does not state a simple implication/counterexample relationship between \cref{def:zac} and \cref{def:fiber-ind}. Readers may misinterpret them as equivalent.
**Suggested Fix:** Add a short remark: (i) \cref{def:zac} implies a support-based constancy property, (ii) \cref{def:fiber-ind} need not imply \cref{def:zac}, and (iii) neither implies the other without extra assumptions.
  
**Author Response:** Added \cref{rem:zac-vs-fiber-ind} explicitly distinguishing support-level (set-based) vs law-level (distributional) constraints and warning that neither implies the other without additional modeling assumptions.  
**Status:** Resolved

### Issue 4: Kernel-pair discussion mixes stochastic and deterministic levels
**Severity:** Minor  
**Location:** `main.tex`, \cref{sec:kernel-pairs}  
**Description:** The kernel-pair section introduces $k:=t$ where $t$ is stochastic and then says ``extract a deterministic observation''. This is fine as an idea, but the text would benefit from naming one concrete extraction (e.g.\ support relation) to make the claim checkable.
**Suggested Fix:** Add one concrete deterministic relation derived from $t$ (e.g.\ $v$ is in the support), and restate the refinement condition with that choice; keep the open question for other choices.
  
**Author Response:** Added a concrete support extraction $\mathrm{Supp}(t(x_C,x_{\bar C})):=\{v:\Pr[V_C=v\mid x_C,x_{\bar C}]>0\}$ and rewrote the kernel-pair paragraph to reference this deterministic observation explicitly.  
**Status:** Resolved

## Status
- [x] Ready to merge
- [ ] Requires changes

---

## Round 2

**Reviewer:** Domain Expert (AI Agent)  
**Date:** 2026-01-13  
**Round:** 2

## Summary
Re-checked the Round 1 fixes in `main.tex`. The added execution semantics paragraph, the added citation pointer for conditional independence/factorization, the explicit distinction between set-based vs distributional notions, and the concrete support extraction are all present and improve clarity. One minor rigor issue was found and fixed: kernel-pair notation should apply to deterministic maps, so the support extraction is now presented as an explicit deterministic map \(s\) and the refinement comparison uses \(\sim_{(h,s)}\).

## Issues

### Issue 5: Kernel-pair comparison should reference a deterministic observation map
**Severity:** Minor  
**Location:** `main.tex`, \cref{sec:kernel-pairs}  
**Description:** The previous text set \(k:=t\) where \(t\) is a stochastic channel and then wrote \(\sim_{(h,k)}\) as if \((h,k)\) were a deterministic map. This is better presented by defining a deterministic support map \(s\) and using \(\sim_{(h,s)}\).
**Suggested Fix:** Define \(s:X_C\times X_{\bar C}\to\mathcal{P}(V_C)\) by \(s(x_C,x_{\bar C})=\mathrm{Supp}(t(x_C,x_{\bar C}))\), then compare \(\sim_h\) with \(\sim_{(h,s)}\).
  
**Author Response:** Implemented exactly this: introduced an explicit deterministic support map \(s\) and replaced \(\sim_{(h,k)}\) with \(\sim_{(h,s)}\).  
**Status:** Resolved

## Status
- [x] Ready to merge
- [ ] Requires changes

