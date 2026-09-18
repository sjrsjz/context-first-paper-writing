# Cross-Language Reconstruction Workflow

## Core rule

Translation is a new writing pass over preserved scientific propositions. Do not translate sentence by sentence. Different languages choose subjects, information order, omissions, clauses, and connectors differently, so source-language sentence boundaries are not semantic invariants.

Read `writing-workflow.md` first. A translation must execute every writing step again in the target language. Source-language artifacts provide evidence; they do not replace target-language artifacts.

## What must remain invariant

Preserve:

- mathematical definitions and objects;
- proposition subjects, actions, inputs, and outputs;
- assumptions, parameter domains, budgets, and boundary cases;
- claim strength and evidence level;
- comparison methods, metrics, aggregation, and protocol;
- equations, values, figures, citations, and their support relationships;
- limitations that restrict the corresponding claims.

Sentence count, sentence order, clause structure, grammatical subject, and connectors may change when the target language requires it. Reordering is allowed only among propositions without a dependency edge.

## Step 0: Freeze the source

Record the authoritative source files and revision, translated scope, paper type, figures and generated data, and known obsolete historical translations. If the source changes materially, invalidate and rerun affected artifacts.

Output: `00-source-version.md`.

## Steps 1--3: Recover meaning before language

Run the writing workflow's Context and paragraph analysis on the source. Extract atomic propositions without retaining source syntax. Audit each proposition against equations, tables, generated results, citations, or explicit design choices.

Outputs:

- `01-context-and-mainline.md`
- `02-source-paragraph-map.md`
- `03-source-propositions-and-evidence.md`

## Steps 4--7: Write independently in the target language

Build a target paragraph map from obligations and dependencies. Write a target-language skeleton with explicit subjects and actions. Create a new target Context ledger and dependency graph. Restore terminology, equations, values, citations, and restrictions only after the skeleton passes.

Outputs:

- `04-target-paragraph-map.md`
- `05-target-skeleton.md`
- `06-target-context-and-relations.md`
- `07-expanded-translation.md`
- `terminology.md`

These artifacts must collectively cover every step in `writing-workflow.md`; translation-specific names do not waive any writing check.

## Step 8: Build a bilingual proposition map

Use a many-to-many mapping:

| Source proposition | Source Context and conditions | Target sentence | Argument role | Evidence | Obligation discharged |
|---|---|---|---|---|---|

Every source proposition must be retained, explicitly removed, or changed with author authorization. Every target proposition must trace to the authoritative source or a separately verified revision. Check that merged target sentences do not lose local conditions.

Output: `08-bilingual-proposition-map.md`.

## Step 9: Read the target without the source

Hide the source and perform the complete sentence and paragraph readback on the target. Only afterward compare languages for semantic completeness. This order prevents source knowledge from silently repairing missing target Context.

Output: `09-target-readback.md`.

## Step 10: Audit versions and document mechanics

Check section, equation, figure, table, citation, value, unit, percentage, sample count, parameter range, experiment protocol, and claim correspondence. Detect stale content copied from historical translations. Compile or render the target document and check references, fonts, page limits, and layout.

Output: `10-cross-version-audit.md`.

## Source errors discovered during translation

Do not silently repair only the target version. Fix the authoritative source or record an author-approved source amendment, rerun the affected Context and claim-evidence checks, and then synchronize the target.

## Chinese-to-English checks

- Do not translate a Chinese topic phrase into an unmotivated English declaration. Recover the higher-level obligation first.
- Do not fill every omitted agent with “we.” Choose the method, constraint, equation, experiment, or authors according to the proposition role.
- Resolve the relation behind “其中,” “同时,” “进一步,” “可以,” “得到,” and “表明” before choosing an English connector or verb.
- Prefer explicit English subjects and known-to-new information order. Move conditions early enough that readers cannot overgeneralize the claim.
- Split a source sentence that combines definition, condition, contrast, and result. Do not reproduce the bundle with a semicolon, colon, participial phrase, or noun stack.
- Explain why an equation is needed before it appears and which obligation it resolves afterward.

## Translation hard failures

Reject the target text if:

- target sentence boundaries default to source sentence boundaries;
- the target has no independent Context ledger and dependency graph;
- a reader needs the source to resolve a subject, pronoun, relation, or scope;
- a source condition exists only in the bilingual map, not the target prose;
- an empirical observation becomes a theorem, a design choice becomes a consequence, or structural support becomes system validation;
- current and obsolete claims, experiments, or values coexist;
- the target invents an unsupported claim;
- compact target grammar hides unrelated propositions;
- terminology varies for stylistic reasons;
- target-only readback fails but source-assisted reading succeeds.

Write the abstract and introduction after the target methods, experiments, and limitations stabilize. Reconstruct them from the finished target paper rather than translating a historical abstract or narrative.
