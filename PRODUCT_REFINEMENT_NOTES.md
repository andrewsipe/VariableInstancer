# Product refinement notes — Variable_Instancer

Captured during the 2026-08-21 declutter pass. Use for a later product/release pass. **Not** user-facing docs.

## What was archived (declutter)

| Archived path | Was | Why archived |
|---------------|-----|--------------|
| `_misc/_archive/Variable_Instancer/Adding static instances to variable fonts.md` | ~150 KB design/chat/build-plan dump | Not operator docs; TableEditor already exists. Keep as historical design reference only. |

## Active tree

| Path | Role |
|------|------|
| `VariableFont_Instancer.py` | Extract static instances from VFs (main CLI; STAT/fvar/hybrid naming) |
| `VariableFont_TableEditor.py` | Define/edit STAT axis values + fvar named instances **before** instancing |
| `tests/` | Dedup + PostScript naming tests |
| `README.md` | Instancer-focused (TableEditor called out after declutter) |

## Product-pass refinements (deferred)

1. **Relationship to VarFontStudio** — GUI planning/export vs this CLI batch path; document “when to use which” (CLI for batch/automation; Studio for interactive grids).
2. **Package naming** — Folder `Variable_Instancer` vs scripts `VariableFont_*`; console scripts `vf-instance` / `vf-table-edit`.
3. **Instancer size** — ~4.3k lines in one file; split naming / instantiate / CLI on product pass.
4. **TableEditor maturity** — Design doc claimed early drafts; verify apply/generate paths have tests before calling 1.0.
5. **`raw_github_urls.txt`** — PushCore noise.

## Do not lose

- Naming strategies: STAT / fvar / hybrid.
- TableEditor → Instancer order (STAT/fvar written first).
- Instance dedup + PostScript naming test coverage.
