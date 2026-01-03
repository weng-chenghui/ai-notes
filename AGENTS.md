# AGENTS.md

Guidelines for AI agents contributing to this repository.

---

## 1. Directory Structure and Naming

### 1.1 Directory Naming Convention

All new document directories **MUST** be prefixed with a datetime stamp:

```
YYYY-MM-DD_<topic-slug>/
```

**Examples:**
- `2026-01-03_quantum-entanglement/`
- `2026-01-04_transformer-architectures/`
- `2026-01-05_measure-theory-notes/`

### 1.2 Multi-Directory Structure

- Each topic **MUST** reside in its own subdirectory under `docs/`.
- One topic per subdirectory—do not mix unrelated content.
- A single directory may contain multiple LaTeX files (e.g., `main.tex`, `appendix.tex`, `proofs.tex`).

---

## 2. Document Format

### 2.1 Default Format

- All documents **MUST** be written in **LaTeX** unless the user explicitly requests a different format (e.g., Markdown, HTML).
- PDFs are compiled and versioned automatically by the CI pipeline.

### 2.2 Required LaTeX Packages

Include the following in your document preamble for proper cross-referencing:

```latex
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{amsmath,amsthm,amssymb}
```

### 2.3 Theorem Environments

Define standard environments for mathematical writing:

```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
```

---

## 3. Writing Standards

### 3.1 Academic Paper Style (Default)

All writing **MUST** follow formal academic tone and conventions unless the user explicitly requests a different style (e.g., tutorial, blog post, informal notes).

**Academic style requirements:**
- Third person perspective (avoid "I", "we" unless following specific conventions)
- Precise, formal language
- Proper document structure (abstract, introduction, sections, conclusion)
- Defined notation before use
- Clear logical flow between statements

### 3.2 Correctness is Paramount

- **Be conservative in claims.** Do not overstate results.
- Every claimed fact **MUST** have reasoning and/or proof.
- If a proof cannot be completed or the agent does not know how to prove something, mark it explicitly as:

```latex
\begin{openquestion}
It remains to be shown that [claim]. The author was unable to verify this assertion.
\end{openquestion}
```

Or use a custom environment:

```latex
\newenvironment{openquestion}{\textbf{Open Question.}\itshape}{}
```

### 3.3 Rigor Over Comprehensiveness

- Prefer a smaller set of well-proven results over a larger set of unverified claims.
- When in doubt, leave it out or mark it as an open question.

---

## 4. Citation Requirements

All references **MUST** follow academic paper citation style with fine-grained precision.

### 4.1 Internal Cross-References

Use LaTeX `\label{}` and `\cref{}` (from `cleveref`) for:

| Element | Label Prefix | Example |
|---------|--------------|---------|
| Sections | `sec:` | `\label{sec:introduction}` |
| Definitions | `def:` | `\label{def:continuity}` |
| Theorems | `thm:` | `\label{thm:main-result}` |
| Lemmas | `lem:` | `\label{lem:technical}` |
| Propositions | `prop:` | `\label{prop:uniqueness}` |
| Corollaries | `cor:` | `\label{cor:implication}` |
| Equations | `eq:` | `\label{eq:schrodinger}` |
| Figures | `fig:` | `\label{fig:diagram}` |
| Tables | `tab:` | `\label{tab:results}` |

**Usage:**
```latex
As shown in \cref{thm:main-result}, the function is continuous.
By \cref{def:continuity}, this implies...
Substituting \cref{eq:schrodinger} into \cref{eq:hamiltonian}...
```

### 4.2 External References

Use BibTeX with proper citation keys. Every external claim **MUST** cite:

- The specific theorem/lemma/definition number from the source
- Page numbers when referencing specific passages

**Examples:**
```latex
\cite[Theorem 3.2]{AuthorYear}
\cite[Definition 2.1, p.~42]{AuthorYear}
\cite[Section 4.3]{AuthorYear}
```

### 4.3 Bibliography Management

- Maintain a `references.bib` file in each document directory.
- Use consistent citation keys: `AuthorYear` or `AuthorTitleYear`.

---

## 5. Self-Review Workflow

**All changes to this repository MUST go through a self-review process.**

### 5.1 Workflow Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        SELF-REVIEW CYCLE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. [Author Role]   Create PR with changes                     │
│         │                                                       │
│         ▼                                                       │
│  2. [Reviewer Role] Review changes, push REVIEW.md             │
│         │                                                       │
│         ▼                                                       │
│  3. [Author Role]   Address issues, respond in REVIEW.md       │
│         │                                                       │
│         ▼                                                       │
│  4. [Reviewer Role] Check fixes, add new comments if needed    │
│         │                                                       │
│         ▼                                                       │
│     Repeat steps 3-4 until no further issues                   │
│         │                                                       │
│         ▼                                                       │
│  5. [Reviewer Role] Approve and merge PR                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Detailed Process

1. **Create a Pull Request**
   - Never push directly to `main`.
   - Create a feature branch: `docs/YYYY-MM-DD_topic-name` or `fix/description`.
   - Open a PR with a clear description of changes.

2. **Switch to Reviewer Role**
   - Assume the persona of a **domain expert peer reviewer**.
   - Review the changes critically and objectively.
   - Create `REVIEW.md` in the PR branch with detailed comments.

3. **REVIEW.md Format**
   ```markdown
   # Review: [Document Title]
   
   **Reviewer:** Domain Expert (AI Agent)
   **Date:** YYYY-MM-DD
   **Round:** 1
   
   ## Summary
   [Brief overview of the changes and general assessment]
   
   ## Issues
   
   ### Issue 1: [Title]
   **Severity:** Critical / Major / Minor
   **Location:** [file:line or section reference]
   **Description:** [Detailed description of the issue]
   **Suggested Fix:** [How to address it]
   
   ### Issue 2: [Title]
   ...
   
   ## Status
   - [ ] Ready to merge
   - [x] Requires changes
   ```

4. **Address Issues as Author**
   - Switch back to the author role.
   - Review the feedback in `REVIEW.md`.
   - Make necessary changes to the documents.
   - Update `REVIEW.md` with responses:
   
   ```markdown
   ### Issue 1: [Title]
   ...
   **Author Response:** [Explanation of how the issue was addressed]
   **Status:** Resolved
   ```

5. **Iterate Until Approved**
   - Switch to reviewer role again.
   - Check if issues are resolved.
   - Add new issues if found.
   - Continue until no further issues remain.

6. **Merge**
   - Update `REVIEW.md` status to "Ready to merge".
   - Merge the PR into `main`.

### 5.3 Reviewer Checklist

The reviewer **MUST** verify the following:

- [ ] **Technical correctness:** Are all claims proven or explicitly marked as open questions?
- [ ] **Citation completeness:** Are all references properly cited with fine-grained precision (theorem numbers, page numbers)?
- [ ] **Style compliance:** Does the writing follow academic paper style?
  - Formal tone
  - Third person perspective
  - Precise language
  - Proper structure
- [ ] **LaTeX quality:** Are labels, cross-references, and bibliography properly formatted?
- [ ] **Naming conventions:** Does the directory follow `YYYY-MM-DD_topic-slug/` format?
- [ ] **Completeness:** Are all necessary components present (main document, bibliography, etc.)?

---

## 6. Example Document Structure

A well-formed document directory should look like:

```
docs/2026-01-03_example-topic/
├── main.tex           # Primary document
├── appendix.tex       # Optional appendices
├── references.bib     # Bibliography
├── figures/           # Optional figures directory
│   └── diagram.pdf
└── REVIEW.md          # Review notes (if PR is in progress)
```

### 6.1 Minimal LaTeX Template

```latex
\documentclass[11pt,a4paper]{article}

% Essential packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amsthm,amssymb}
\usepackage{hyperref}
\usepackage{cleveref}

% Theorem environments
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

% Open question environment
\newenvironment{openquestion}{\par\textbf{Open Question.}\itshape}{\par}

% Document info
\title{Document Title}
\author{AI Notes}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
Brief summary of the document contents.
\end{abstract}

\section{Introduction}
\label{sec:introduction}

Introduction text here.

\section{Preliminaries}
\label{sec:preliminaries}

\begin{definition}[Important Concept]
\label{def:concept}
A formal definition goes here.
\end{definition}

\section{Main Results}
\label{sec:main-results}

\begin{theorem}[Main Theorem]
\label{thm:main}
Statement of the theorem.
\end{theorem}

\begin{proof}
Detailed proof goes here.
\end{proof}

\section{Conclusion}
\label{sec:conclusion}

Concluding remarks.

\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

---

## 7. Summary of Key Rules

1. **Always prefix new directories with datetime:** `YYYY-MM-DD_topic-slug/`
2. **One topic per subdirectory.**
3. **Use LaTeX by default.**
4. **Write in academic paper style.**
5. **Prove all claims or mark as open questions.**
6. **Cite with precision** (theorem numbers, page numbers, section references).
7. **Always create a PR and self-review before merging.**
8. **Iterate review cycles until no issues remain.**
