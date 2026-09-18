# Workflow Artifact Templates

Use these schemas as working records. Replace prompts with concrete content. Empty or generic cells do not satisfy the workflow.

## Context and main line

```markdown
# Scope
- Edited object:
- Paper type:
- Target reader:
- Central question:
- Permitted claim changes:
- Evidence sources:

# Entering Context Γ0
- Higher-level goal:
- Reader-known objects:
- Established propositions and evidence:
- Active assumptions and scope:
- Unresolved obligations:

# Shortest argument path
Problem → constraint → method → result → evidence → bounded conclusion
```

## Paragraph map

| Paragraph | $\Gamma_{\mathrm{in}}$ | Concrete task | Obligation discharged | Propositions added | $\Gamma_{\mathrm{out}}$ | Relation to next paragraph |
|---|---|---|---|---|---|---|

## Atomic propositions

| ID | Context dependency | Role | Motivation | Subject | Action/relation | Input/premise | Output/object | Conditions/scope | Evidence |
|---|---|---|---|---|---|---|---|---|---|

## Context ledger

| Sentence/proposition | Items used from $\Gamma_i$ | Active obligation | Role $\tau_i$ | Addition to Context | Use or obligation discharged |
|---|---|---|---|---|---|

Do not enter “related to the topic,” “transition,” “additional detail,” or “for completeness.” Name the exact dependency, use, or obligation.

## Dependency graph

Represent higher-level goals and unresolved obligations as nodes. For every proposition, record at least one incoming edge. For every Context addition, record a consumer or terminal obligation.

```text
[section obligation] -> P1 (establishes problem)
P1 -> P2 (motivates method requirement)
P2 + [definition D] -> P3 (derives result)
P3 + [experiment E] -> P4 (bounded conclusion)
```

## Readback

| Sentence | Expected reader question | Dependency | Why here | Context gained | Failure if removed | Pass/fail and action |
|---|---|---|---|---|---|---|

## Bilingual proposition map

| Source ID/text | Source Context and conditions | Target sentence ID/text | Argument role | Evidence | Obligation discharged | Status |
|---|---|---|---|---|---|---|

Use status values such as `preserved`, `authorized removal`, `authorized revision`, or `blocked`. Explain every status other than `preserved`.

## Claim-evidence audit

| Claim | Scope and conditions | Evidence level | Exact evidence | Restatements checked | Risk/action |
|---|---|---|---|---|---|

Evidence levels may include mathematical structure, proof, implementation, numerical audit, and empirical experiment. Do not collapse them into a single “supported” label.
