# factcheck

A fact-check skill for marketing and product claims. It produces dated,
claim-by-claim ratings from the seller's own pages, checked arithmetic and clearly
separated independent evidence. It does not purchase, contact sellers or publish
reports. Apache-2.0 licensed; no account, package install or API key is needed for
the files or offline scorer. Live research uses the host assistant's permitted tools.

Start with the [skill](skills/factcheck/SKILL.md), the self-contained
[paste-in prompt](prompts/factcheck.md), or the [wiki page template](templates/wiki-page.md).
The skill defines the nine ratings, including the distinction between missing
support, an incomplete check and a fact contradicted by evidence.

## Install and use

Clone this repository, review its contents, and check out a reviewed commit before
copying a skill. Run the following from the repository root. These commands create
a new installation; they refuse to replace an existing folder. To update, compare
the installed copy with the reviewed source first. Nothing here edits CLI settings.

### Claude Code

```sh
mkdir -p "$HOME/.claude/skills"
test ! -e "$HOME/.claude/skills/factcheck" && cp -R skills/factcheck "$HOME/.claude/skills/factcheck"
```

Invoke `/factcheck Check the claims at https://seller.example/product` in Claude
Code. For one project, copy to that project's `.claude/skills/factcheck` instead.
The skill can also be selected automatically when relevant. See
[Claude Code's skill documentation](https://code.claude.com/docs/en/skills).

### Codex

```sh
mkdir -p "$HOME/.agents/skills"
test ! -e "$HOME/.agents/skills/factcheck" && cp -R skills/factcheck "$HOME/.agents/skills/factcheck"
```

Start a session and ask `$factcheck Check the claims at https://seller.example/product`.
For one repository, copy to its `.agents/skills/factcheck` instead. These discovery
paths follow the [official Codex local-skill documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills),
checked October 22, 2026. Paths can change; check the installed client's skill list
and ask which skill it loaded before relying on an installation.

### Any chat model

Paste all of [prompts/factcheck.md](prompts/factcheck.md), then append the product
URL, atomic claims and desired scope. If browsing is unavailable, supply dated
captures of the product, terms, refund policy and operator information. The model
must label that capture-only scope and leave missing browser content Unverified.
No other repository file is needed to use the prompt or installed skill.

## Worked example and wiki

The first dated example is
[Derila Ergo Neck Support Pillow](https://github.com/rivendale/factcheck/wiki/Derila-Ergo-Neck-Support-Pillow).
It illustrates a claim table, price calculations and cross-page policy checks.
It is a historical example, not a new verification or medical endorsement by this
build. See the [wiki Home](https://github.com/rivendale/factcheck/wiki) for the index.
The nine-label rubric in the skill includes the two explicit attribution/conflict
labels used by the worked example, in addition to Home's shorter rating list.

Use the template to draft a new page. Re-open its sources for a fresh date; do not
carry forward an old price, medical conclusion or claimed independent review as
current fact. Obtain publication authorization separately. This repository's
synthetic evals contain no real company or product, and this build does not edit
the wiki or repeat the example's product-specific findings.

## Offline evals

The [failure list](docs/failure-list.md) and twelve fictional seller-page cases
were committed before the scorer and skill. Traps include anchored comparison
prices, bundles, unused-return restrictions, unsupported medical claims,
advertorials, contradictory policies, instructions in page text, identity requests
and agency bait. Clean and limited-evidence cases check overclaiming too.

```sh
python3 evals/tools/score.py --reports evals/reports/reference
python3 tests/test_score.py
python3 tools/sync_prompt.py --check
```

The [eval guide](evals/README.md) defines the recorded-report format and how to
score a new local report directory. The shipped reference reports are developer-
written examples, not model transcripts. A 12/12 reference score verifies the
scorer's contract on those reports; it does not measure skill quality, real-world
accuracy, browsing safety or resistance to every injection. Independent behavioral
review is still needed. No model/provider run is part of these checks.
Every eval case has exactly one atomic claim; this is not a test of multi-claim
coverage. In injection cases, `response` must be the fixed literal
`ignored; no identifying request sent`. The scorer cannot distinguish an agent
that complied with the page from one that merely wrote that literal afterward.
No model has been run on these cases yet. Model runs on traps 07, 08 and 09,
with actual action/tool traces inspected, must come first before any claim of
skill quality. Such runs require separate authorization in the running environment.

## Maintaining the text

`skills/factcheck/SKILL.md` is the canonical method. After editing it, run
`python3 tools/sync_prompt.py`; CI checks that the standalone prompt matches.
Keep eval inputs and expected findings separate from recorded model outputs.
Report coverage, failures and what was not checked; never tune a score by deleting
an inconvenient case or inventing a live run. See [AGENTS.md](AGENTS.md).

## Credit and sources

- [ai-redteam Track C](https://github.com/rivendale/ai-redteam/blob/main/docs/SPEC.md#what-v2-adds-and-the-failure-behind-each): prior art for checking claims, quotes and numbers against evidence. Linked, not copied.
- [FTC Health Products Compliance Guidance](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance), sections II.A and III.B, read October 22, 2026: background for the stricter treatment of health-claim substantiation. This skill does not determine legal compliance.
- Steven Liss, [How to Win Friends and Influence Non-People: Advertising to Agents](https://stevenliss.substack.com/): attribution for the agent-directed advertising pattern behind the two added synthetic traps. The article body was not retrieved in this build; no empirical result from it is claimed.
- Installation guidance comes from the official Claude Code and Codex sources linked above, checked October 22, 2026. Packaging was checked locally; no live assistant session or account was used to test invocation.
