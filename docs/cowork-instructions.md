# Solus System Book: Claude Cowork Instructions

These instructions tell Claude how to rewrite the Solus system book as a publish-ready rules handbook. Use them with Claude in cowork/session mode.

---

## The Job

Rewrite `system-book/solus-system-book.md` chapter by chapter into a finished rules handbook. The target format is a short, dense, procedure-first zine that a player or GM can learn from and reference at the table. Think Shadowdark, Cairn, Mausritter. Not a D&D Player's Handbook. Not a lore book.

The manuscript has 13 chapters and 12 TODO markers. Some chapters have clean rules. Others have design notes dressed as rules, or gaps marked with TODOs. Your job varies by chapter:

- **Clean chapters** need tightened prose, table formatting, and published-quality language.
- **Rough chapters** need mechanic extraction, deduplication, and rewriting.
- **Incomplete chapters** need the strongest draft possible from archive sources, with honest TODOs for anything missing.

---

## Source Material

- **Active manuscript:** `system-book/solus-system-book.md`
- **Archive (read-only):** `archive/epics-and-stories/`, `archive/rough-notes/`, `archive/playtest-materials/`

Read the archive for mechanics, values, and procedures that the manuscript is missing. Do not treat archive files as active drafts. Do not write into the archive.

---

## Chapter Order

Keep this sequence stable. Do not reorder unless the user asks.

1. Introduction and Design Goals
2. Core Mechanics
3. Character Creation
4. Attributes and Skills
5. Equipment, Armor, and Weapons
6. Magic and Spellcasting
7. Core Gameplay Loop
8. Combat
9. Conditions, Injuries, and Death
10. NPCs, Enemies, and Encounters
11. Advancement, Mastery, and Between-Session Play
12. Running the Game
13. Reference and Playtest Tools

---

## How to Work Through the Book

### Per-Chapter Workflow

For each chapter:

1. **Read the chapter in full.** Identify: What rules are stated? What is duplicated from another chapter? What is missing? What is still a design note instead of a rule?
2. **Search the archive.** Pull any mechanics, tables, values, or procedures the chapter needs that exist in the archive but not in the manuscript.
3. **Rewrite the chapter.** Apply the writing standard below. One canonical version of each rule. Deduplicate. Compress. Format for table use.
4. **Mark gaps.** If a mechanic is missing and the archive does not resolve it, leave a short `TODO:` with what needs resolving. Do not invent mechanics to fill holes.
5. **Commit the chapter.** One commit per chapter rewrite, with a message like `rewrite: chapter 4 attributes and skills`.

### Skill Usage

Use the skills installed in `.agents/skills/` to structure the work:

| Skill | When to Use |
|---|---|
| `brainstorming` | Before rewriting any chapter that has structural problems or missing mechanics. Use it to explore the chapter's needs, propose 2-3 approaches, and get user approval before drafting. |
| `stop-slop` | On every chapter draft. Run the Quick Checks and Scoring rubric against every rewritten section before committing. Score must be 35/50+. |
| `writing-plans` | If a chapter requires major restructuring (new tables, significant archive extraction, resolving conflicting mechanics), write a plan first. Save to `docs/superpowers/plans/`. |
| `executing-plans` | Execute chapter plans task by task. Follow the plan steps, mark progress, verify each task. |
| `subagent-driven-development` | When rewriting multiple independent chapters in one session. Dispatch one subagent per chapter with full context about the writing standard, source material, and that chapter's specific needs. |
| `dispatching-parallel-agents` | When 2+ chapters have no dependencies on each other and can be rewritten concurrently. |
| `requesting-code-review` | After each chapter rewrite. Request review against the writing standard, not code quality. The reviewer should check: Is the prose publish-ready? Does every rule appear once? Are TODOs honest? |
| `verification-before-completion` | Before claiming any chapter is done. Re-read the full chapter output. Run stop-slop scoring. Confirm no duplicate rules across chapters. |

### Recommended Sequence

Start with the chapters that have the most complete source material and affect the most other chapters:

1. **Core Mechanics** (chapter 2) — everything else references this
2. **Attributes and Skills** (chapter 4) — defines the modifier math
3. **Character Creation** (chapter 3) — depends on 2 and 4
4. **Combat** (chapter 8) — biggest chapter, most archive material
5. **Conditions, Injuries, and Death** (chapter 9) — depends on 8
6. **Equipment, Armor, and Weapons** (chapter 5) — feeds combat
7. **Magic and Spellcasting** (chapter 6) — feeds combat
8. **Core Gameplay Loop** (chapter 7) — ties 5-9 together
9. **NPCs, Enemies, and Encounters** (chapter 10) — depends on 8
10. **Advancement** (chapter 11) — standalone
11. **Running the Game** (chapter 12) — standalone
12. **Introduction** (chapter 1) — rewrite last, once the rules are locked
13. **Reference and Playtest Tools** (chapter 13) — compile from finished chapters

---

## Writing Standard

### Voice

Write as a technical author producing a rules manual. The reader is a player or GM at a table who needs to find a rule, understand it, and apply it in seconds.

Address the reader as "you." Address the GM as "the GM" or "you" when writing a GM-facing section. Do not address an abstract "one" or "the player."

### Sentence Rules

- Active voice. Name the actor. "You roll 2d10 + Body," not "A roll is made."
- Short paragraphs. Two to four sentences max.
- No adverbs. No intensifiers. No hedges.
- No em dashes. Use commas or periods.
- No throat-clearing ("Here's the thing," "It turns out," "The truth is").
- No binary contrasts ("Not X, but Y"). State Y.
- No narrator-from-a-distance ("Nobody designed this"). Put the reader in the scene.
- Vary sentence length. Two items beat three. Break any three consecutive sentences of matching length.

### Structure Rules

- One rule stated once in one place. If a rule touches two chapters, define it in one and reference it from the other.
- Bullet procedures for multi-step processes (turn order, character creation steps, dying resolution).
- Tables for data (modifier costs, condition thresholds, weapon stats, DC targets).
- Short examples only when they clarify a rule that bullet text alone cannot convey. Label examples as `> **Example:**` blockquotes.
- Headings at H2 for chapters, H3 for sections, H4 for subsections. No deeper nesting.

### What to Cut

- Lore paragraphs. If flavor doesn't teach a rule, remove it.
- Design journal language ("We wanted the system to feel..."). State the rule instead.
- Marketing voice ("Solus delivers a unique experience...").
- Sprint/epic/story/backlog references.
- Repeated explanations of the same mechanic.
- Filler transitions between sections.

### What to Preserve

- Existing mechanics. Do not redesign a system unless the user asks.
- Specific numbers, DCs, thresholds, costs, ranges.
- Named conditions, tags, and defined game terms.

### Stop-Slop Scoring Gate

Before committing any chapter rewrite, score it on these five dimensions (1-10 each):

| Dimension | Question |
|---|---|
| Directness | Does the text state rules or announce them? |
| Rhythm | Are sentence lengths varied or metronomic? |
| Trust | Does the text respect the reader's intelligence? |
| Authenticity | Does the text sound human-written? |
| Density | Is anything cuttable without losing meaning? |

Minimum passing score: 35/50. Below that, revise before committing.

---

## Git Workflow

- Create a feature branch for the rewrite work: `rewrite/system-book` or similar.
- One commit per chapter rewrite.
- Push after each chapter. The CI will build an Obsidian vault artifact for the editor to review.
- When all chapters are done, open a PR against main with a summary of what changed per chapter.

---

## How to Start a Session

1. Read `CLAUDE.md` and `AGENTS.md` in the repo root for project rules and chapter order.
2. Read the full manuscript (`system-book/solus-system-book.md`).
3. Check the archive folders for any material the manuscript is missing.
4. Pick the next chapter from the recommended sequence above.
5. Use `brainstorming` if the chapter has structural problems. Otherwise go straight to rewriting.
6. Apply `stop-slop` scoring before each commit.
7. Use `requesting-code-review` after each chapter to get a second pass.
8. Use `verification-before-completion` before claiming any chapter is done.

---

## What "Done" Looks Like

A finished chapter:

- States every rule once in published prose
- Uses tables for reference data
- Uses bullet procedures for multi-step processes
- Contains no design notes, no lore padding, no duplicated rules
- Scores 35/50+ on stop-slop
- Has honest TODOs for anything unresolvable from existing material
- Reads like a page from a printed zine someone can run from at a table
