---
name: context-first-paper-writing
description: Plan, draft, restructure, or translate academic-paper prose through explicit semantic Context, typed propositions, dependency graphs, and claim-evidence constraints. Use for substantive manuscript writing and cross-language reconstruction; do not use for referee verdicts, literature reviews, or mechanical proofreading alone.
---

# Context-First Paper Writing

Use this skill to construct academic prose whose sentences are motivated by an explicit argument. Treat writing as a typed Context transition rather than a sequence of locally plausible sentences.

## Route the task

- For drafting, restructuring, or substantive rewriting, read [references/writing-workflow.md](references/writing-workflow.md).
- For translation or bilingual reconstruction, read both the writing workflow and [references/translation-workflow.md](references/translation-workflow.md). Translation must rerun the complete writing workflow in the target language.
- When creating workflow artifacts, use [references/artifact-templates.md](references/artifact-templates.md).
- For referee judgments, novelty assessment, experiment sufficiency, or acceptance recommendations, use an academic review workflow instead. This skill may expose a claim-evidence mismatch while writing, but it does not issue review verdicts.
- For spelling, punctuation, labels, or mechanical formatting that cannot affect meaning, edit directly without running the full workflow.

## Non-negotiable invariants

1. Scientific correctness, evidence, and user-approved scope override rhetorical fluency.
2. Every candidate sentence must satisfy
   \[
   \Gamma_i\vdash s_i:\tau_i\Longrightarrow\Gamma_{i+1},
   \]
   where $\Gamma_i$ contains the active goal, reader-known objects, established propositions, valid assumptions, and unresolved obligations. The role $\tau_i$ identifies the sentence as a problem, premise, definition, method, inference, evidence, limitation, scope statement, or conclusion.
3. Topic relevance is not a derivation rule. A true statement enters the manuscript only when it uses an established proposition, answers an active question, supplies a required object or condition, supports a claim, or discharges a recorded obligation.
4. Context dependency need not be adjacent. Record the exact earlier proposition or higher-level obligation that motivates a nonlocal dependency. Adjacency alone never proves a relationship.
5. Conclusions, scope statements, roadmaps, and contribution summaries may terminate an argument by discharging a recorded obligation. They do not need an artificial downstream consumer.
6. Write atomic propositions before connectors and prose. A connector may express a verified relation; it cannot create one.
7. Preserve claim type. Mathematical consequences, implementation facts, empirical observations, and limitations require different evidence and wording.
8. Do not hide missing relationships in semicolons, dashes, long noun stacks, or sentences carrying several unrelated predicates.
9. Do not edit the manuscript until the expanded draft and independent readback artifacts are complete for the requested scope.

## Work within the real scope

Before writing, identify the paper type, target reader, active claim, permitted changes, source of truth for equations and numbers, and relevant repository instructions. Read enough surrounding text to recover the paper, section, paragraph, and sentence Context. Do not expand the assignment into new experiments, a different paper type, or a broader application claim.

For a local sentence edit, the workflow may be compact, but it must still record the entering Context, active obligation, atomic proposition, relation, and readback whenever motivation, technical meaning, or claim scope can change.

## Artifacts and enforcement

Keep workflow artifacts outside the repository by default. Create a marked task directory under the operating system's temporary directory:

```text
python scripts/manage_workdir.py init --project <project-root> --task <task-name>
```

The command prints the task directory. Use it for every workflow artifact. Do not place transient ledgers in `auto/`, the manuscript tree, or another repository directory unless the user explicitly requests versioned artifacts.

Use the templates rather than retrospective prose justifying an already written draft. For a substantial task, run:

```text
python scripts/check_workflow_artifacts.py <artifact-directory> --mode writing
python scripts/check_workflow_artifacts.py <artifact-directory> --mode translation
```

The script checks that required artifacts exist and contain substantive text. It cannot validate reasoning. Manually inspect the Context ledger, proposition dependency graph, claim-evidence mapping, and target-language readback.

## Cleanup and retention

Treat intermediate artifacts as temporary process state.

- For a check or audit that does not modify the manuscript, return the findings in the response. If a file report is useful or requested, write `summary.md`, then remove every other intermediate artifact with `manage_workdir.py cleanup <task-directory> --keep-summary`. Otherwise remove the whole task directory.
- For drafting, rewriting, or translation, apply and verify the approved manuscript change, then remove the whole task directory unless the user asked to retain the workflow evidence.
- For blocked work, retain only `summary.md` when it materially helps resumption; otherwise clean the task directory.
- Never remove user files, manuscript files, or an unmarked directory. The cleanup script requires a sentinel, verifies the resolved directory against the recorded temporary root, and refuses to delete the root itself.

Run cleanup from the skill directory:

```text
python scripts/manage_workdir.py cleanup <task-directory>
python scripts/manage_workdir.py cleanup <task-directory> --keep-summary
```

Report what was retained and its path. User instructions to preserve, relocate, or version artifacts override these defaults.

## Stop conditions

Do not write the result into the manuscript when any of these holds:

- a sentence cannot name its Context dependency or active obligation;
- a new object has neither a recorded use nor an obligation it discharges;
- a technical verb lacks a recoverable input, output, or operating condition;
- a connector claims a relation absent from the proposition graph;
- a local condition leaks into a broader claim;
- prose is fluent only because the reader is expected to infer missing steps;
- a translation preserves source sentence boundaries without rebuilding target-language Context;
- a translation changes, omits, or invents a claim, condition, number, comparison, or evidence type.

When a stop condition appears, return to the earliest invalid artifact instead of polishing the prose.

## Completion

Report what changed, which obligations the revision now discharges, how claim and evidence scope were preserved, which checks ran, what temporary state was cleaned or retained, and any material limitation. Keep necessary revisions distinct from optional improvements.
