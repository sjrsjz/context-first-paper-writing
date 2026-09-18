# Context-First Writing Workflow

## Purpose

Use this workflow for substantive academic drafting, restructuring, and rewriting. Its job is to prevent locally grammatical sentences from forming a globally unmotivated argument.

## Context model

For sentence $s_i$, define $\Gamma_i$ to contain:

1. the paper, section, and paragraph goals inherited at the current position;
2. objects, symbols, and definitions already available to the reader;
3. established propositions and their evidence level;
4. assumptions, budgets, parameter domains, datasets, and other active scope limits;
5. unresolved questions, contradictions, proof obligations, and evidence obligations.

Admit $s_i$ only if its argument role is correct, its dependencies are available, and it advances or discharges an obligation. Theme overlap is insufficient.

Context is hierarchical. A section must serve the paper question, a paragraph must serve the section task, and a sentence must serve the paragraph obligation. A paragraph opening can inherit a nonlocal section obligation, but that edge must be recorded. An abstract inherits the title, paper type, and reader contract; its first sentence must still establish the central problem and why it matters.

## Step 1: Establish Context, scope, and main line

Record the edited scope, target reader, paper type, central question, permitted claim changes, and shortest argument path. Define $\Gamma_0$: reader-known material, usable propositions and evidence, active conditions, and unresolved obligations.

Output: `01-context-and-mainline.md`.

## Step 2: Assign one task to each paragraph

State each paragraph task with a concrete verb, such as establishing a contradiction, defining an object needed by the next proof, comparing methods under a shared budget, or explaining an observed failure. Record $\Gamma_{\mathrm{in}}$, the obligation to discharge, propositions added, and $\Gamma_{\mathrm{out}}$.

Reject a paragraph that cannot derive motivation from its entering Context or whose additions are neither used nor terminal conclusions.

Output: `02-paragraph-map.md`.

## Step 3: Write atomic propositions

Do not write prose or connectors. For every proposition, identify:

- Context dependency;
- argument role;
- motivation or obligation;
- subject;
- action or relation;
- input or premise;
- output or object;
- conditions and scope;
- evidence source.

Technical verbs such as invert, match, reconstruct, compute, optimize, determine, improve, and support require explicit endpoints and conditions. A proposition can be grammatically complete and still be invalid if the Context never created a reason for it.

Output: `03-propositions.md`.

## Step 4: Validate Context transitions and dependencies

For each proposition, write

\[
\Gamma_i\vdash p_i:\tau_i\Longrightarrow\Gamma_{i+1}.
\]

Record the dependency, obligation changed, Context addition, and downstream use or terminal obligation. Include higher-level goals and unresolved obligations as nodes in the dependency graph. Every proposition, including paragraph openings, needs an incoming edge. Every addition needs a use or a recorded obligation it discharges.

Then classify each neighboring transition: cause, consequence, restriction, specialization, method to implementation, evidence to claim, comparison, interpretation, or conclusion. If two neighboring propositions have no relation, move, merge, list, tabulate, or remove one. Do not add a connector to conceal the gap.

Output: `04-context-and-relations.md`.

## Step 5: Build the connected skeleton

Choose sentence boundaries and connectors only after Step 4 passes. Prefer explicit complete sentences in argumentative prose. Treat semicolons and dashes as audit triggers: restate the relationship and split the sentence unless the punctuation has a clear nonargumentative role.

Annotate each skeleton sentence with its minimal Context citation. Remove the annotations and confirm that an ordinary reader can still recover the dependency.

Output: `05-connected-skeleton.md`.

## Step 6: Restore necessary information

Restore definitions, terminology, equations, numbers, citations, restrictions, and only the modifiers needed for precision. Every restored detail must pass Context admission again. Put mechanical derivations, edge-case algebra, audit tables, or implementation detail in an appendix when they do not advance the main-text obligation.

Do not vary established terminology for style. Do not add praise, vague evaluations, or summaries that do not change the reader's state.

Output: `06-expanded-draft.md`. Do not modify the manuscript before this artifact is complete.

## Step 7: Perform independent readback

For every sentence, answer:

1. What answer is the reader waiting for before this sentence?
2. Which object, proposition, condition, or obligation does it use?
3. Why must it appear here?
4. What does the reader gain, and which later content or recorded obligation does that serve?
5. If removed, which dependency fails or which obligation becomes unresolved?

Check technical subjects and objects, scope, evidence level, connector accuracy, paragraph progression, reference resolution, and terminology stability. A terminal conclusion is valid when removing it leaves the paragraph obligation unresolved.

Output: `07-readback.md`.

## Step 8: Apply and verify

Only after readback passes, apply the expanded draft to the manuscript. Recheck the abstract, introduction, contribution list, experiments, limitations, and conclusion when the claim scope changed. Compile or render the document, verify citations and labels, and check page and layout constraints.

## Hard failures

Return to the earliest relevant step if:

- a sentence has no dependency or motivation;
- a statement is included only because it is true or related to the topic;
- a method, result, or term appears before the need for it exists;
- a sentence's argument role exceeds its evidence;
- a local condition disappears when the claim is restated;
- a paragraph opening relies only on the section topic;
- a new fact is unused and discharges no recorded obligation;
- parallel declarative sentences lack a shared comparison dimension or progression;
- a connector substitutes for a missing premise;
- a pronoun, comparison, or technical action has no unique referent.
