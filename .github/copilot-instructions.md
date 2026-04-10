# Solus Prerelease — Copilot Instructions

## Project Overview

Solus is a tabletop RPG system book in active development. The primary work is writing and editing markdown content, not code. The single active manuscript is `system-book/solus-system-book.md`. Archive folders are read-only reference material — never write into them.

## Build and Test

Run the vault build script (Python 3.12+):

```bash
python scripts/build_obsidian_vault.py
# Output: dist-vault/ and dist-vault.zip
```

Run the build test (verifies expected output paths and content):

```bash
python scripts/test_build_obsidian_vault.py
# Output: "Vault build test passed."
```

CI runs both on push and PR to `main`. On `main` push, the workflow also publishes a rolling `obsidian-preview` prerelease to GitHub Releases.

## Architecture

The build pipeline reads `system-book/solus-system-book.md` and:

1. Splits it into per-chapter files by matching `## Heading` markers (order is positional — do not reorder headings)
2. Copies archive folders verbatim
3. Generates three Obsidian navigation notes (`Home.md`, `System Book.md`, `Archive Index.md`)
4. Zips everything into `dist-vault.zip`

Chapter files are named `{index:02d} {sanitized-title}.md` in `system-book/chapters/`. The chapter index is derived from heading order in the manuscript, so heading order must stay stable.

Archive folders (`archive/epics-and-stories/`, `archive/rough-notes/`, `archive/playtest-materials/`) are **read-only source material**. Pull mechanics, values, and procedures from them when the manuscript is missing something; do not write into them.

## Chapter Order

Keep this sequence. Do not reorder unless asked.

1. Introduction and Design Goals
2. Core Mechanics
3. Character Creation
4. Attributes and Skills
5. Armor and Defense
6. Weapons, Techniques, and Augments
7. Magic and Spellcasting
8. Core Gameplay Loop
9. Combat
10. Conditions, Injuries, and Death
11. NPCs, Enemies, and Encounters
12. Advancement and Between-Session Play
13. Running the Game
14. Reference and Playtest Tools

## Open TODOs and Design Gaps

The full catalog of open questions is in `docs/superpowers/specs/2026-04-08-solus-open-todos-design.md`. Each entry names the gap, its file location, what it blocks, and what design decisions are still needed.

**Blocks the most other work — resolve these first:**

- **XP awards and encounter building** (spec #16) — no XP values per enemy tier or encounter type; blocks advancement and GM chapters
- **Save resolution** (spec #9) — Accuracy Type "Save" has no working mechanic since Resist Rolls were removed; blocks spellcasting completion

**Blocks a single section each:**

- **Atraxia pool restoration, modifier thresholds, and experience tables** (spec #3, #4, #5) — pool has no recovery rule; threshold effects are undefined
- **Short-term injury table** (spec #15) — Dying references rolling on this table but it doesn't exist
- **GM pacing and DCs** (spec #18) — Running the Game chapter lacks encounter pacing and DC calibration guidance
- **Full weapon Technique lists** — 28 of 32 weapons need full Technique tables (4 complete: Greatsword, Rapier, Shield, Bow)

**Quick confirmations needed from the designer:**

- Hybrid mana: 70/10 or 75/10? (spec #19)
- Main/Sub affinity system: keep, modify, or cut? (spec #11)
- Starting equipment: budget, packages, or open pick? (spec #21)
- Spell parameter table layout: group by action cost tier? (spec #14)
- Spell-created physical projectiles: Physical AC or Magical AC? (spec #8)

**Resolved (do not re-open):**

- Bleed (Shredded) and Force (Staggered) escalation conditions — fully written in both files ✅
- Poisoned mechanical effect — confirmed as standard stack damage pattern ✅
- Combat abilities system (spec #6, #7) — now "Weapons, Techniques, and Augments" chapter with 32 weapons, 3-layer Techniques, 2-layer Augments ✅
- T3/T4 effect tiers (spec #10) — T3 = Enhanced Escalation (12 mana, Rank 3+), T4 = Ultimate Escalation (17 mana, Rank 5 capstone) ✅
- Weapon trait list (spec #12) — full per-weapon properties and condition signatures written ✅
- Shields (spec #13) — Shield is a Light Melee weapon with its own Mastery track and 8 Techniques ✅

## Core Mechanics Reference

**Resolution:** `2d10` added together (not percentile).

- **Combat roll:** `2d10 + Stat Modifier` vs. `Armor DR + Stat Modifier`
- **Skill check:** `2d10 + Skill Modifier`
- **Resist roll:** `2d10 + Stat Modifier` vs. a degree gradient from `-5/-10` to `+5/+10`
- **Critical success:** double 10s. **Critical failure:** double 1s.

**Attributes:** Body, Mind, Social, Magic, Sanity. Modifiers from `-5` to `+5`.

**Point buy:** 5 points at creation. Negative modifiers refund points; refunded points must be spent. Cost: +5=6, +4=4, +3=3, +2=2, +1=1, 0=0; negatives refund that amount.

**Skill modifier:** fixed primary attribute + one player-chosen secondary attribute from two listed options. Skills: Athletics, Stealth, Investigation, Knowledge, Medicine, Survival, Animal Handling, Performance, Speech, Arcana, Insight.

**Armor:** Physical DR and Magic DR split. Armor AC = relevant stat + matching DR. DR reduces damage after a hit lands. Magic DR does not block elemental stacks or their escalation.

| Armor Tier | Physical DR | Magic DR |
|---|---|---|
| Cloth | 0 | 4 |
| Light | 1 | 3 |
| Medium | 3 | 1 |
| Heavy | 4 | 0 |
| Enchanted | 3 | 3 |

**Action economy:** 3 actions per turn, 1 reaction per round (refreshes at start of that character's turn). Initiative: `d10 + Body or Magic` (player chooses to match fighting style).

**HP and mana by background:** Caster 100 HP / 100 mana (15 regen). Martial 120 HP / 30 mana (3 regen). Hybrid 110 HP / 70 mana (10 regen) — *confirmation pending, spec #19*.

**Dying:** at 0 HP, set death counter to `10 + Body modifier` (min 5, max 15). Counter drops each turn by active stack damage (after Magic DR) + 1 per unused action slot or 2 per used action slot. Healing restores from dying; roll `2d10 + Body` vs. DC `15 minus counter value at time of healing` for consequences using the Degree of 5 table.

**Degree of 5 outcomes:** beat DC by 10+ = big bonus; 5–9 = small bonus; 0–4 = expected result; miss by 5–9 = small setback; miss by 10+ = big setback.

**Elemental stacks:** cap at 5 per type, deal `+1 damage per active stack` per round, last 2 full rounds, reset on reapplication. Burn and Chilled cancel on a 1:1 basis. Magic DR reduces stack damage but does not block stack application or escalation.

**Active conditions:** Ignited (no healing), Drown (lose Reaction, must spend Action to escape), Frozen (movement 0, Action to break free), Shocked (disadvantage on Actions, half movement), Corroded (weakens armor), Venomous (lose Actions as poison escalates), Stunned (disadvantage on Actions, lose Reaction), Restrained (movement limited), Crush (maintained Force stacks on Restrained target), Blind (lose visual perception).

**NPC ranks:**

| Rank | HP | Mana | Stat Modifiers |
|---|---|---|---|
| Minion | 1–5 | 30/3 | All +0 |
| Regular | 75 | 30/3 | All +1 |
| Enemy / Ally | 100 | 100/15 | Body +4, Mind +1, Social +3, Magic -3, Sanity +0 |
| Mini Boss | 120 | 100/15 | Body +5, Mind +4, Social -3, Magic +0, Sanity -2 |
| Boss | 175 | 100/20 | Body +5, Mind +3, Social +0, Magic +5, Sanity -5 |

Boss gets one extra +5 beyond the normal limit. Bosses use Enchanted armor.

**Spell framework:** spells are built from parameters (Category, Function, Range, Size, Shape, Duration, Target Count, Accuracy Type, Effect Tier). No field can stay empty. Function costs: Utility +0, Movement +1, Defensive +1, Offensive +2; multi-function spells add both. Damage comes from range, target count, and size (one die each). Die scaling: d6 = +1 mana, d8 = +2, d10 = +3, d12 = +5. Main category costs normal; Sub category costs double. T3 (12 mana) = Enhanced Escalation, T4 (17 mana) = Ultimate Escalation.

**Weapons, Techniques, and Augments:** 32 weapons across 6 categories (Light Melee, Medium Melee, Heavy Melee, Reach, Ranged, Firearms). Each weapon has its own Mastery track (Rank 0-5). Techniques are active combat abilities at three layers: Universal (any weapon), Category (any weapon in that category), Weapon-Specific (only that weapon). Characters prepare 10 Techniques at a time, changeable on rest. Augments socket into Technique slots to modify behavior. Universal Augments (16) work on any Technique; Category Augments (3 per category) only on that category's Techniques. Augment Slots per Technique scale with Mastery Rank (0/1/1/2/2/3). Spellcasting requires only mana, never a weapon.

**Advancement:** XP earned through combat, exploration, and conversation. Spent after sessions on new proficiencies, proficiency rank increases (Rank 1-10, exponential cost), Weapon Mastery ranks, and Augment purchases. Techniques: 10 slots available from character creation, changeable on short/long rests. XP is a shared budget across proficiencies, Weapon Mastery, and Augments.

## Writing Standard

The target format is a short, dense, procedure-first zine. Think Shadowdark, Cairn, Mausritter — not the D&D Player's Handbook.

**Voice:** Address the reader as "you." Address the GM as "the GM" in GM-facing sections.

**Sentence rules:**
- Active voice. Name the actor. "You roll 2d10 + Body," not "A roll is made."
- Short paragraphs (2–4 sentences max).
- No adverbs, intensifiers, or hedges.
- No em dashes. Use commas or periods.
- No throat-clearing ("Here's the thing," "It turns out," "The truth is").
- No binary contrasts ("Not X, but Y"). State Y.
- Vary sentence length. Two items beat three.

**Structure:**
- Bullet procedures for multi-step processes (turn order, character creation steps, dying resolution).
- Tables for data (modifier costs, condition thresholds, weapon stats, DC targets).
- Short examples only when bullet text cannot convey the rule. Label as `> **Example:**` blockquotes.
- Headings: H2 for chapters, H3 for sections, H4 for subsections. No deeper nesting.

**Cut:** lore that doesn't teach a rule, design journal language ("We wanted the system to feel..."), sprint/epic/story/backlog references, repeated explanations of the same mechanic, filler transitions.

**Preserve:** existing mechanics, specific numbers/DCs/thresholds/costs/ranges, named conditions and defined game terms.

## Stop-Slop Scoring Gate

Before committing any chapter, score it on five dimensions (1–10 each). Minimum passing score: **35/50**.

| Dimension | Question |
|---|---|
| Directness | Does the text state rules or announce them? |
| Rhythm | Are sentence lengths varied or metronomic? |
| Trust | Does the text respect the reader's intelligence? |
| Authenticity | Does the text sound human-written? |
| Density | Is anything cuttable without losing meaning? |

## Per-Chapter Workflow

1. Read the chapter in full. Identify stated rules, duplication, gaps, and design notes masquerading as rules.
2. Search the archive for mechanics the chapter is missing.
3. Rewrite. One canonical version of each rule. Deduplicate. Compress. Format for table use.
4. Mark unresolvable gaps with short `TODO:` inline. Do not invent mechanics to fill holes.
5. Score with stop-slop (35/50+ required before committing).
6. Commit: one commit per chapter, message like `rewrite: chapter 4 attributes and skills`.

## Git Workflow

- Feature branches: `rewrite/system-book` or similar.
- One commit per chapter rewrite.
- Push after each chapter (CI builds the Obsidian vault artifact for review).
- PR to `main` when all chapters are done, with a per-chapter summary.
