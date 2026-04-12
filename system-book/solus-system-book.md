# Solus System Book

## Introduction and Design Goals

Solus is a game of heroic gritty realism. Your character can become legendary, but the system makes you earn that power through risk. The world does not grow safer as you improve. Threats keep pace, and victory stays costly.

The system lets you define a character through the skills, magic, and weapons you choose. You can build for optimization or build to concept. The rules test both the same way. When you ask whether a character can do something, the system answers through shared mechanics instead of handing that answer to GM judgment alone.

Those shared mechanics apply across spells, weapons, and influence. The game uses one rules language for action resolution, whether you are playing a character or running the table. The same approach also supports play with or without a GM.

## Core Mechanics

Most rolls use 2d10, added together instead of read as percentile dice.

### Combat Rolls

Combat rolls use `2d10 + Stat Modifier` against `Armor DR + Stat Modifier`.

A critical success is double 10s.

A critical failure is double 1s.

### Resist Rolls

When you resist an effect, roll `2d10 + Stat Modifier`.

Compare the result against a gradient from `-5/-10` to `+5/+10`.

Each attribute governs resistance to a category of threats. Resist rolls use degrees of outcome instead of a pass or fail result. Success is not always desirable. Failure is not always negation.

### Skill Checks

When you try to determine information or take an actionable step, make a skill check.

A skill check uses `2d10 + Skill Modifier`.

Each skill modifier comes from two attributes.

- The primary attribute is fixed for that skill and does not change.
- The secondary attribute comes from one of two listed options, chosen by the player.

## Character Creation

At character creation, establish the parts of your character that stay fixed and mark the parts that can change in play.

### Step 1: Build Your Concept

Choose the kind of character you want to play. Solus supports martial, magical, social, and hybrid approaches through the same core rules.

### Step 2: Distribute Ability Scores

Your five ability scores use modifiers from `-5` to `+5`.

You have 5 points to spend. Negative modifiers refund points, and you must spend those refunded points.

| Modifier | Cost |
| --- | --- |
| +5 | +6 |
| +4 | +4 |
| +3 | +3 |
| +2 | +2 |
| +1 | +1 |
| 0 | +0 |
| -1 | -1 |
| -2 | -2 |
| -3 | -3 |
| -4 | -4 |
| -5 | -5 |

### Step 3: Choose Your Race

Record your race first. Your race sets your base movement speed and character size, and it also gives you your racial bonuses, including traits such as dark vision or movement bonuses when your race grants them.

TODO: add the full race list and race traits.

### Step 4: Choose Your Background

Background determines starting health and mana behavior, but it does not restrict what skills, spells, weapons, or armor you can use.

- Casters start at 100 HP and 100/15 mana.
- Martials start at 120 HP and 30/3 mana.
- Hybrids start at 110 HP and 70/10 mana.

The current sample playtest sheets use 75/10 mana for Hybrids in some cases.

TODO: confirm the final Hybrid mana values.

### Step 5: Choose Your Skills

Record your skill choices and their secondary attribute options.

### Step 6: Record Fixed And Changeable Traits

The following parts of a character are fixed at creation or by level.

- Race
- Racial bonuses
- Ability scores
- Skill modifiers
- Base movement speed
- Background
- Character name
- Max health pool
- Max mana pool
- Character size

The following parts can change between sessions or through play.

- Skills
- Armor damage resistance
- Weapons
- Level
- Spells
- Money
- General resources
- Equipment
- Languages

The following parts are temporary and should be tracked separately.

- Modified movement speed
- Status effects
- Current health
- Current mana
- Environmental effects
- Short-duration curses

The following parts are long-term and should stay on the sheet until they are resolved.

- Lingering injuries
- Long-term curses
- Madness
- Reputation

### Step 7: Choose Starting Weapons

Pick one or two weapons from the tables in Weapons, Techniques, and Augments. You begin at Mastery Rank 1 in your chosen weapon(s). This grants access to that weapon's tier 1 Techniques and its category's tier 1 Techniques.

Choose your starting Techniques. You can prepare up to 10 Techniques from your available pools (Universal, Category, and Weapon-Specific). You can change prepared Techniques on a short or long rest.

### Step 8: Choose Equipment

Choose armor from the tables in Armor and Defense. Your background does not restrict your choices. You begin with one set of armor (any tier except Enchanted).

TODO: add starting equipment rules for gear and supplies.

## Attributes and Skills

Characters have five attributes. Each one defines a different part of action resolution.

### Body

Body measures physical prowess.

- Physical attacks and damage
- Defense and mobility
- Durability

### Mind

Mind measures learned and worldly knowledge.

- Knowledge and skills
- Perception and awareness
- Mental saves that do not rely on emotion

### Social

Social measures communicative prowess.

- Social influence
- Leadership and morale
- Social defenses

### Magic

Magic measures magical aptitude.

- Spellcasting effectiveness
- Magical control

### Sanity

Sanity measures mental fortitude.

- Fear and madness saves
- Stress tolerance
- Mental break thresholds

### Skills

Each skill uses one fixed primary attribute and one player-chosen secondary attribute from the listed pair.

| Skill | Primary | Use | Secondary |
| --- | --- | --- | --- |
| Athletics | Body | Used to overcome physical challenges through strength, endurance, speed, or bodily control. | Mind<br>Sanity |
| Stealth | Body | Used to move, act, or remain unnoticed by others. | Mind<br>Sanity |
| Investigation | Mind | Used to actively search for, analyze, and piece together clues or hidden details. | Body<br>Sanity |
| Knowledge | Mind | Used to recall, understand, or contextualize learned information about the world. | Social<br>Sanity |
| Medicine | Mind | Used to assess health, diagnose conditions, treat injuries, or stabilize the wounded. | Body<br>Sanity |
| Survival | Mind | Used to endure, navigate, track, hunt, or live off the land in hostile or natural environments. | Body<br>Sanity |
| Animal Handling | Social | Used to calm, train, control, or intuit the behavior of animals or similar creatures. | Body<br>Mind |
| Performance | Social | Used to entertain, inspire, distract, or convey emotion through artistic or dramatic expression. | Body<br>Sanity |
| Speech | Social | Used to persuade, deceive, negotiate, command, or otherwise influence others through words. | Body<br>Mind |
| Arcana | Magic | Used to identify, understand, manipulate, or reason about magical, supernatural forces. | Mind<br>Sanity |
| Insight | Sanity | Used to uncover and comprehend hidden cosmic, occult, eldritch, or existential truths revealed through fractured perception or loss of mental stability. | Body<br>Mind |

## Armor and Defense

Armor splits protection between physical damage and magic damage. Each armor tier carries a damage reduction value for each side, and that same split also feeds into Armor AC. To calculate Armor AC, add Physical DR to Body for physical defense, and add Magic DR to Magic for magical defense. DR reduces damage after a hit lands.

| Armor Tier | Physical DR | Magic DR | Total DR |
| --- | --- | --- | --- |
| Cloth | 0 | 4 | 4 |
| Light | 1 | 3 | 4 |
| Medium | 3 | 1 | 4 |
| Heavy | 4 | 0 | 4 |
| Enchanted | 3 | 3 | 6 |

Magic DR reduces damage from elemental status effects, but it does not stop those effects from applying or escalating. A target can still build stacks and reach a higher condition even while armor cuts the damage from those stacks.

## Weapons, Techniques, and Augments

Every character fights with weapons. Weapons deal damage, apply condition stacks, and unlock Techniques. Your choice of weapon defines your combat role as much as your attributes do.

This chapter covers three systems:

- **Weapons** grant base damage, properties, and condition signatures.
- **Techniques** are active combat abilities. They cost Actions and sometimes Mana. You prepare up to 10 at a time, changeable on a short or long rest. Each Technique requires its associated weapon equipped.
- **Augments** modify Techniques. You socket Augments into Augment Slots unlocked by Weapon Mastery.

### Weapon Mastery

Each weapon has its own Mastery track, ranked 0 through 5. You buy Mastery Ranks with XP from your shared advancement budget. Higher ranks unlock stronger Techniques and more Augment Slots.

| Mastery Rank | Unlock | Augment Slots per Technique | XP Cost |
|---|---|---|---|
| 0 (Untrained) | Universal Techniques only | 0 | — |
| 1 | Category Techniques (tier 1) + Weapon Techniques (tier 1) | 1 | TODO: XP cost |
| 2 | Category Techniques (tier 2) + Weapon Techniques (tier 2) | 1 | TODO: XP cost |
| 3 | Category Techniques (tier 3) + Weapon Techniques (tier 3) | 2 | TODO: XP cost |
| 4 | Weapon Techniques (tier 4) | 2 | TODO: XP cost |
| 5 | Weapon Techniques (tier 5) + Capstone | 3 | TODO: XP cost |

Weapon complexity determines how high the Mastery track goes and how many Techniques are available.

| Complexity | Max Rank | Weapon Techniques | Total Pool |
|---|---|---|---|
| Simple | 3 | 4–5 | ~10–12 |
| Standard | 5 | 7–9 | ~16–20 |
| Complex | 5 | 10–14 | ~20–25 |

Simple weapons cap at Rank 3. Standard and Complex weapons reach Rank 5.

### Technique Layers

Techniques come from three sources. Each layer has different unlock requirements and scope.

| Layer | Source | Scope |
|---|---|---|
| Universal | Available to all characters | Any equipped weapon |
| Category | Unlocked by Mastery Rank 1+ in any weapon in that category | Any weapon in that category |
| Weapon-Specific | Unlocked by that weapon's Mastery Rank | Only that specific weapon |

You prepare up to 10 Techniques at a time from any combination of layers. You can swap your prepared list on a short or long rest.

### Augment Layers

Augments modify Techniques. Three layers exist, mirroring the Technique architecture.

| Layer | How Equipped | Scope | Count |
|---|---|---|---|
| Universal Augments | Socketed into Technique Augment Slots | Any Technique, any weapon | 22 |
| Weapon Augments | Passive (always active once learned) | All Techniques from that weapon | 5 per weapon |
| Technique Augments | Socketed into that Technique's Augment Slots | One specific Technique only | 2-3 per Technique |

**Weapon Augments are passive.** Learn them with XP. Once learned, they apply to every Technique from that weapon automatically. They do not consume Augment Slots. They add Mana cost to every Technique from that weapon.

| Weapon Mastery Rank | Weapon Augments Available |
|---|---|
| 1 | 0 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 (all) |

**Universal Augments and Technique Augments share Augment Slots.** Each prepared Technique has slots based on Weapon Mastery Rank (0/1/1/2/2/3). Fill each slot with one Universal Augment or one Technique Augment.

**Mana cost stacking.** Every Augment adds Mana cost. Multiple Augments on one Technique stack additively. Weapon Augments add their cost to every Technique from that weapon.

> **Example:** Rapier Lunge (0 Mana base) with Flourish weapon augment (+1 Mana) and Retreating Lunge technique augment (+1 Mana) costs 2 Mana total.

**Exclusivity.** Condition augments (Burn, Chill, Shock, Force, Bleed, Poison) are mutually exclusive on the same Technique. One added condition per Technique. The weapon's innate condition stacks freely.

The full augment catalog for all 32 weapons lives in the companion web reference. This chapter covers all Universal Augments, Weapon Augments for each weapon, and full Technique Augments for Rapier and Katana as worked examples.

### Universal Techniques

Every character has access to these four Techniques regardless of weapon or Mastery Rank.

**Brace.** Plant your feet. Until your next turn, gain +2 AC. You cannot move. Free Action to enter; costs your movement for the turn.

**Shove.** Push an adjacent creature 1 space. Roll `2d10 + Body` vs. target's `2d10 + Body`. Costs 1 Action.

**Taunt.** Force a target within 6 spaces to roll `2d10 + Social` vs. your `2d10 + Social`. On failure, the target must attack you on their next turn if able. Costs 1 Action.

**Second Wind.** Recover `1d10 + Body modifier` HP. Costs 1 Action. Once per combat. Cannot use while Dying.

### Universal Augments

Twenty-two Augments are available to all characters. Characters know all Universal Augments at creation. The first eighteen work with any Technique on any weapon. The last four (Spellblade Augments) bridge weapon attacks and spellcasting.

| Augment | Effect | Mana Cost Increase |
|---|---|---|
| Reach | Range +1 space (melee) or +10 ft (ranged). | +2 |
| Splash | On hit, half damage to all adjacent to target. | +3 |
| Potency | +1 die of damage (same type as weapon). | +2 |
| Efficiency | -1 Action cost (minimum 1). | +3 |
| Momentum | If you moved 2+ spaces this turn, +1d6 damage. | +1 |
| Duration | Conditions applied last 1 extra round. | +2 |
| Trigger | Choose a trigger condition. Technique auto-fires as a Reaction when triggered. | +4 |
| Chain | On hit, make a second attack at a different target at -4 to hit. | +3 |
| Siphon | On hit, recover HP equal to 25% of damage dealt. | +3 |
| Condition: Burn | On hit, apply 1 Burn stack. | +2 |
| Condition: Chill | On hit, apply 1 Chill stack. | +2 |
| Condition: Shock | On hit, apply 1 Shock stack. | +2 |
| Condition: Force | On hit, apply 1 Force stack. | +2 |
| Condition: Bleed | On hit, apply 1 Bleed stack. | +2 |
| Condition: Poison | On hit, apply 1 Poison stack. | +2 |
| Execute | +50% damage to targets below 25% HP. | +3 |
| Knockback | On hit, push target 1 space. | +1 |
| Fortify | After using this Technique, gain +2 AC until your next turn. | +2 |

#### Spellblade Augments

These four Augments connect weapon combat and spellcasting. Any character with Mana can use them.

| Augment | Effect | Mana Cost Increase |
|---|---|---|
| Spell Strike | Deliver one Touch spell alongside a weapon attack. One roll, two payloads. Miss = spell not expended. | +0 (spell Mana paid separately) |
| Arcane Infusion | After casting a spell this turn, your next Technique deals +1d8 elemental damage (matching the spell's element). | +2 |
| Channeling | While concentrating on a spell, the Technique costs 2 less Mana (minimum 0). | +0 |
| Mana Reave | On hit, restore Mana equal to your weapon's base damage die (e.g., 1d8 weapon = roll 1d8 Mana restored). Once per round. | +3 |

### Weapon Properties Reference

Weapons carry properties that modify how they function in combat.

| Property | Effect |
|---|---|
| Finesse | Use Body or Magic modifier for attack rolls (player's choice). |
| Light | Can be dual-wielded. One weapon in each hand. |
| Paired | Comes as a set. Always dual-wielded. |
| Heavy | -2 to hit for characters with Body modifier below +1. |
| Two-Handed | Requires both hands. Cannot use a Shield. |
| Versatile (XdY) | Wield one-handed or two-handed. Two-handed uses the listed die. |
| Adaptive | Changes weapon category based on grip. |
| Reach | Attack targets 2 spaces away (default). |
| Reach (N spaces) | Attack targets up to N spaces away. |
| Thrown (N ft) | Make a ranged attack up to N feet. Uses Body modifier. |
| Defensive (+N AC) | +N AC while equipped. |
| Bash | Can make melee attacks with a Shield. |
| Hooked | On hit, free Disarm attempt. Target rolls `2d10 + Body` vs. your attack roll. |
| Bludgeon | Bludgeoning damage. +2 to hit vs. Heavy armor. |
| Pierce | Ignores 2 Physical DR. |
| Bypass | Ignores Shield AC bonuses. |
| Chain | Target cannot Parry this weapon. |
| Sweeping | Attacks can hit two adjacent targets. Once per turn, free. |
| Entangle | On hit, attempt to Restrain target. Costs 1 extra Action. |
| Disarm | On hit, free Disarm attempt. |
| Arcane | Spells gain +1 range tier while equipped. Bonus, not a requirement for casting. |
| Ammunition (N) | Holds N shots before requiring a Reload. |
| Reload | 1 Action to reload. Some Techniques modify reload speed. |
| Loading | 1 Action to reload after each shot. |
| Consumable | Destroyed on use. Must be crafted or purchased. |
| Spread | Point-blank range: +1d6 damage. Maximum range: -1d6 damage. |
| AoE (radius) | Hits all targets in the listed radius on impact. |
| Unarmed | Cannot be disarmed. Compatible with grappling Techniques. |
| Grapple | Advantage on grapple checks. |
| Conduit | Spell attack rolls gain +1 to hit while equipped. Bonus, not a requirement. |
| Spellforged | Legendary property. Contains one spell, castable once per long rest as a free action (0 Actions, 0 Mana). |

### Weapon Categories

Weapons are grouped into seven categories. Each category shares a fighting style and a set of Category Techniques. Category Techniques have their own Technique Augments, shared across all weapons in that category.

---

### Light Melee

Fast, low-damage, high-frequency attacks. Light Melee favors evasion, combos, and condition application. These weapons strike often and stack conditions faster than any other category.

#### Light Melee Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Quick Draw | Free Action | Switch to this weapon as a free action. If you attack in the same turn, +1 to hit. |
| 1 | Flurry | 1 Action | Two attacks as a single Action. Each deals half weapon damage. |
| 2 | Slip Away | Free (on hit) | After hitting, move 1 space without provoking reactions. |
| 2 | Exploit Opening | Reaction | When an adjacent enemy misses an attack, make a free attack against them. |
| 3 | Assassinate | 2 Actions | Attack an unaware target. On hit, double damage. |

#### Light Melee Category Technique Augments

| Technique | Augment | Effect | Mana Cost |
|---|---|---|---|
| Quick Draw | Lightning Draw | +1d4 bonus damage on the attack after Quick Draw. | +1 |
| Quick Draw | Concealed Draw | Attack after Quick Draw has advantage if target was unaware of this weapon. | +2 |
| Flurry | Triple Flurry | Add a third attack at -2 to hit. | +3 |
| Flurry | Precise Flurry | Remove the half-damage penalty on both attacks. Full damage, twice. | +3 |
| Slip Away | Dancing Steps | Move 2 spaces instead of 1. | +1 |
| Slip Away | Counter Slip | If the enemy follows you (moves adjacent on their turn), make a free attack at +1d4. | +2 |
| Exploit Opening | Punishing Opening | Free attack deals +1d6 bonus damage. | +2 |
| Exploit Opening | Crippling Opening | On hit, target has -2 to hit until their next turn. | +1 |
| Assassinate | Vanishing Strike | After Assassinate, enter hiding if you have cover within 1 space. Repeatable kills. | +3 |
| Assassinate | Lethal Ambush | Triple damage instead of double against unaware targets. | +3 |

#### Light Melee Weapons

| # | Weapon | Complexity | Base Damage | Properties |
|---|---|---|---|---|
| 1 | Bare Hands | Simple | 1d6 | Unarmed, Grapple |
| 2 | Dagger | Standard | 1d6 | Finesse, Thrown (20 ft), Light |
| 3 | Short Sword | Standard | 1d8 | Finesse, Light |
| 4 | Claw Gauntlet | Standard | 1d6 | Finesse, Light, Paired |
| 5 | Sickle | Standard | 1d6 | Finesse, Light, Hooked |
| 6 | Shield | Standard | 1d6 | Defensive (+2 AC), Bash |

Shield occupies the off-hand. It functions as both a defensive item (+2 AC while equipped) and a weapon with its own Mastery track. Shield Techniques include bashes, blocks, pushes, and formation abilities.

#### Light Melee Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Bare Hands | Force | — | Burn Force stacks on yourself for bonus unarmed damage. Grapple Techniques pin targets while Force stacks tick. |
| Dagger | Bleed | Poison | Paired with Flurry, applies stacks faster than any other weapon. Rank 3+: apply Bleed AND Poison on a single hit. |
| Short Sword | Bleed | — | Every hit applies 1 Bleed. No variance. Rank 3: guaranteed 2 Bleed stacks per hit. |
| Claw Gauntlet | Bleed | — | Dual-wield mandatory (Paired). Each Flurry hits twice. Fastest path to Shredded (5 Bleed) in the game. |
| Sickle | Bleed | — | On kill, transfer remaining Bleed stacks to one adjacent enemy. |
| Shield | Force | — | Shield Bash applies 1 Force stack. Repeated bashes build toward Staggered while maintaining high AC. |

#### Bare Hands (Simple, Light Melee) — 5 Techniques

**Unique Mechanic: Iron Fist.** Bare Hands Techniques apply Force stacks to you, not the target. Spend stacks on your next hit for bonus damage. If you reach 5 Force stacks, you gain Staggered (T2 Force) on yourself. Manage your stacks or pay the price.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Steel Fist | 1 Action | 1d6 Bludgeon. Gain 1 Force stack on yourself. |
| 1 | Grab and Slam | 1 Action | 1d6 Bludgeon. On hit, attempt a free Shove, Grapple, or Push (contested `2d10 + Body` check). Once per turn. |
| 2 | One-Two Combo | 1 Action, 3 Mana | Strike twice. 1d6 Bludgeon each hit. Gain 1 Force stack per hit. Cannot trigger Grab and Slam on the second strike. |
| 2 | Burning Knuckles | 1 Action | Consume all Force stacks on yourself. 1d6 Bludgeon + 1d6 per stack consumed. 3+ stacks: target rolls `2d10 + Body` vs. DC 14 or is Disarmed. 4+ stacks: target rolls `2d10 + Body` vs. DC 16 or is Stunned. Stacks consumed whether you hit or miss. |
| 3 | Iron Hold | 1 Action, 5 Mana | Requires a Grappled target. Pin the target. While pinned, your Force stacks tick damage to the pinned target (1 damage per stack per round). Target breaks free with `2d10 + Body` vs. your `2d10 + Body`. |

##### Bare Hands Weapon Augments (Iron Fist)

Passive. Once learned, these apply to ALL Bare Hands Techniques. Each adds its Mana cost to every Bare Hands Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Thick Skin | While you have 3+ Force stacks on yourself, gain +1 AC. | +0 |
| 2 | Momentum | When you consume Force stacks with Burning Knuckles, gain temporary HP equal to stacks consumed × 2. | +1 |
| 3 | Haymaker | When you consume 4+ Force stacks, add 1d6 Bludgeon on top of the per-stack bonus. | +2 |

#### Dagger (Standard, Light Melee) — 8 Techniques

**Unique Mechanic: Toxic Edge.** Dagger Techniques apply Bleed or Poison as listed. At Mastery Rank 3, all damaging Dagger Techniques also apply 1 Bleed and 1 Poison stack on hit. Pairs with Flurry for the fastest condition stacking in the game.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Lacerate | 1 Action | 1d6 Slashing. Apply 1 Bleed stack. |
| 1 | Poison Prick | 1 Action | 1d6 Piercing. Apply 1 Poison stack. |
| 2 | Fan of Blades | 1 Action, 3 Mana | Throw daggers at up to 2 targets within 20 ft. 1d6 Piercing each. Apply 1 Poison stack per target. |
| 2 | Sidestep | Reaction | When an enemy misses you in melee, strike back. 1d6 Piercing. Apply 1 Bleed stack. |
| 3 | Hemorrhaging Strike | 1 Action, 5 Mana | 2d6 Slashing. Apply 2 Bleed stacks. If the target has Poison stacks, apply 1 additional Poison stack. |
| 3 | Venomous Ambush | 1 Action, 7 Mana | Requires hiding or an unaware target. 3d6 Piercing. Apply 2 Poison stacks. This attack has advantage. |
| 4 | Crimson Venom | 1 Action, 8 Mana | Requires Shredded (T2 Bleed) and Venomous (T2 Poison) on the target. 2d6 Piercing. Apply Neurotoxin (T3): target movement becomes 0, Poison damage doubles each round. |
| 5 | Lethal Dose (Capstone) | 1 Action, 15 Mana | Requires Neurotoxin (T3) on the target. Poison stacks jump to 35. Target permanently loses 1 Action per turn. Once per long rest. |

##### Dagger Weapon Augments (Toxic Edge)

Passive. Once learned, these apply to ALL Dagger Techniques. Each adds its Mana cost to every Dagger Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Envenomed Blade | Poison stacks from Dagger Techniques deal +1 per tick (+2 total per stack per round instead of +1). | +2 |
| 2 | Twin Fangs | When dual-wielding daggers, each Dagger Technique strikes with both blades. Second strike deals half damage. | +3 |
| 3 | Coat Blade | Before a Dagger Technique, spend 1 additional Action to coat your blade. Next hit applies 2 extra Poison stacks. | +0 (costs Action) |
| 4 | Arterial Cut | Bleed applied by Dagger Techniques cannot be removed by mundane healing. Only magical healing removes Dagger Bleed. | +1 |
| 5 | Shadowstep | After a Dagger Technique reduces a target to 0 HP, teleport up to 3 spaces to another enemy. | +2 |

#### Short Sword (Standard, Light Melee) — 8 Techniques

**Unique Mechanic: Steady Blade.** Every damaging Short Sword Technique applies 1 Bleed stack on hit. At Mastery Rank 3, every damaging Short Sword Technique applies 2 Bleed stacks on hit instead. No variance. Consistent pressure.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Slash | 1 Action | 1d6 Slashing. Apply 1 Bleed stack. |
| 1 | Thrust | 1 Action | 1d6 Piercing. Apply 1 Bleed stack. Target cannot take Reactions until start of their next turn. |
| 2 | Lunging Cut | 1 Action, 3 Mana | Move 2 spaces toward target. 1d8 Slashing. Apply 1 Bleed stack. Does not provoke opportunity attacks. |
| 2 | Parry Riposte | Reaction, 3 Mana | When an enemy hits you in melee, reduce damage by 1d6. Strike back: 1d6 Slashing. Apply 1 Bleed stack. |
| 3 | Relentless Cuts | Passive | When you hit a target that already has Bleed stacks, deal +1 damage per existing Bleed stack on the target. |
| 3 | Deep Gash | 1 Action, 5 Mana | 2d6 Slashing. Apply 2 Bleed stacks. If target has 3+ Bleed stacks, apply 3 stacks instead. |
| 4 | Hemorrhage Strike | 1 Action, 8 Mana | Requires Shredded (5 Bleed stacks) on the target. 2d8 Slashing. Apply Hemorrhage (T3): Bleed damage doubles, healing 50% effective, persists 2 extra rounds. |
| 5 | Bloodletting Flurry (Capstone) | 2 Actions, 12 Mana | 3 strikes. 1d8 Slashing each. Each strike applies 2 Bleed stacks. If Hemorrhage (T3) is active, all Bleed damage on the target ticks immediately after the last strike. Once per long rest. |

##### Short Sword Weapon Augments (Steady Blade)

Passive. Once learned, these apply to ALL Short Sword Techniques. Each adds its Mana cost to every Short Sword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Keen Edge | Short Sword Techniques score a critical hit on double 9s in addition to double 10s. | +1 |
| 2 | Pressure Fighter | While the target has 3+ Bleed stacks, your Short Sword Techniques deal +1d4 Slashing. | +2 |
| 3 | Clean Cuts | Bleed stacks from Short Sword Techniques last 1 extra round before expiring. | +1 |
| 4 | Swordsman's Focus | After landing 3 consecutive Short Sword hits on the same target, your next Short Sword Technique against that target has advantage. | +0 |
| 5 | Bloodletter | When Hemorrhage (T3) is active on the target, your Short Sword Techniques apply +1 additional Bleed stack. | +2 |

#### Claw Gauntlet (Standard, Light Melee) — 8 Techniques

**Unique Mechanic: Twin Rend.** Claw Gauntlets have the Paired property (dual-wield mandatory). Each Flurry (Universal Technique) lands twice when using Claw Gauntlets. Fastest path to Shredded (5 Bleed stacks) in the game.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Rake | 1 Action | 1d6 Slashing. Apply 1 Bleed stack. If target already has Bleed stacks, apply 2 instead. |
| 1 | Pounce | 1 Action | Move 2 spaces toward target. 1d6 Slashing. Apply 1 Bleed stack. |
| 2 | Shredding Swipe | 1 Action, 3 Mana | Strike with both gauntlets. 1d6 Slashing per gauntlet (2d6 total). Apply 1 Bleed stack per gauntlet. |
| 2 | Deflecting Claws | Reaction | When an enemy hits you in melee, reduce damage by 1d4. Counterattack: 1d6 Slashing. Apply 1 Bleed stack. |
| 3 | Savage Frenzy | 1 Action, 5 Mana | 3 rapid strikes. 1d4 Slashing each. Apply 1 Bleed stack per strike. |
| 3 | Predator's Instinct | Passive | When you reduce a target to Shredded (5 Bleed stacks), gain +2 to hit against that target until Bleed expires. |
| 4 | Rending Maul | 1 Action, 8 Mana | Requires Shredded (5 Bleed stacks) on the target. 2d8 Slashing. Apply Hemorrhage (T3): Bleed damage doubles, healing 50% effective, persists 2 extra rounds. |
| 5 | Eviscerate (Capstone) | 2 Actions, 15 Mana | Requires Hemorrhage (T3) on the target. 6 strikes, 1d6 Slashing each. Each strike applies 1 Bleed stack. Bleed stacks from this Technique ignore the stack cap of 5 (maximum 11 total). Once per long rest. |

##### Claw Gauntlet Weapon Augments (Twin Rend)

Passive. Once learned, these apply to ALL Claw Gauntlet Techniques. Each adds its Mana cost to every Claw Gauntlet Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Serrated Edges | Bleed stacks from Claw Gauntlet Techniques deal +1 per tick. | +2 |
| 2 | Feral Reflexes | After using a Claw Gauntlet Technique, gain +1 AC until start of your next turn. | +1 |
| 3 | Lacerating Grip | When you Grapple a target, apply 2 Bleed stacks. Each round the Grapple persists, apply 1 additional Bleed stack. | +1 |
| 4 | Blood Scent | You have advantage on attacks against targets with Shredded (5 Bleed stacks). | +2 |
| 5 | Relentless Mauling | When Hemorrhage (T3) is active on the target, your Claw Gauntlet Techniques deal +1d6 Slashing. | +3 |

#### Sickle (Standard, Light Melee) — 8 Techniques

**Unique Mechanic: Reaping.** When a target with Bleed stacks dies, transfer all remaining Bleed stacks to one enemy within 1 space of the dying target. Harvest kills to spread Bleed across groups.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Reap | 1 Action | 1d6 Slashing. Apply 1 Bleed stack. |
| 1 | Hooking Slash | 1 Action | 1d6 Slashing. Apply 1 Bleed stack. Pull target 1 space toward you. |
| 2 | Sweeping Harvest | 1 Action, 3 Mana | Strike all enemies within 1 space. 1d6 Slashing each. Apply 1 Bleed stack per target hit. |
| 2 | Sever Tendon | 1 Action, 3 Mana | 1d8 Slashing. Apply 2 Bleed stacks. Target's movement halved until end of their next turn. |
| 3 | Blood Harvest | Passive | When Reaping transfers Bleed stacks, add 1 extra Bleed stack to the receiving target. |
| 3 | Rending Hook | 1 Action, 7 Mana | 2d6 Slashing. Apply 2 Bleed stacks. Pull target 2 spaces toward you. If target collides with another enemy, both take 1d6 Bludgeon. |
| 4 | Crimson Harvest | 1 Action, 8 Mana | Requires Shredded (5 Bleed stacks) on the target. 2d8 Slashing. Apply Hemorrhage (T3): Bleed damage doubles, healing 50% effective, persists 2 extra rounds. |
| 5 | Grim Reaping (Capstone) | 2 Actions, 15 Mana | Requires Hemorrhage (T3) on the target. 4d6 Slashing. If the target dies, Reaping triggers on ALL enemies within 2 spaces instead of 1. Transferred stacks include the Hemorrhage (T3) condition. Once per long rest. |

##### Sickle Weapon Augments (Reaping)

Passive. Once learned, these apply to ALL Sickle Techniques. Each adds its Mana cost to every Sickle Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Harvest Moon | Reaping transfer range increases from 1 space to 2 spaces. | +0 |
| 2 | Sowing Pain | Sickle Techniques that apply Bleed to an already-bleeding target deal +1d4 Slashing. | +1 |
| 3 | Chain Reaping | When Reaping transfers stacks, split them between up to 2 adjacent enemies instead of 1. | +2 |
| 4 | Cruel Hook | Sickle Techniques that Pull ignore forced movement immunity. | +1 |
| 5 | Death's Harvest | When Reaping triggers, regain 3 Mana per Bleed stack transferred. | +2 |

#### Shield (Standard, Light Melee) — 8 Techniques

**Unique Mechanic: Guard.** +2 AC while equipped (base Defensive property). Shield Techniques enhance defense and provide offense. Tank/controller hybrid.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Shield Bash | 1 Action | 1d6 Bludgeon. Push target 1 space. |
| 1 | Raise Shield | 1 Action | +4 AC total until your next turn. Costs movement. |
| 2 | Shield Slam | 1 Action, 3 Mana | Charge 2 spaces and bash. Target rolls `2d10 + Body` vs. DC 12 or falls prone. |
| 2 | Cover Ally | Reaction | Redirect an attack on an adjacent ally to yourself. Gain Shield AC bonus against the redirected attack. |
| 3 | Shield Wall | Passive | When adjacent to an ally also using Raise Shield, both gain +6 AC instead of +4. |
| 3 | Rebounding Bash | 1 Action, 5 Mana | Bash bounces to a second adjacent target. Both take 1d6 Bludgeon and are pushed 1 space. |
| 4 | Fortress | 2 Actions, 5 Mana | +6 AC. Immune to forced movement. Adjacent allies gain +2 AC. You cannot move or attack. Lasts until your next turn. |
| 5 | Aegis (Capstone) | Reaction, 10 Mana | Negate all damage from one attack targeting you or an adjacent ally. Once per long rest. |

##### Shield Weapon Augments (Guard)

Passive. Once learned, these apply to ALL Shield Techniques. Each adds its Mana cost to every Shield Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Shield Master | Your Shield's +2 AC bonus also applies to all allies within 1 space. | +0 |
| 2 | Battering Ram | Shield Techniques that push deal +1d4 Bludgeon per space pushed. | +1 |
| 3 | Reflective Guard | When you negate a ranged attack with a Shield Technique, reflect it back at the attacker at -4 to hit. | +2 |
| 4 | Tower Shield | Raise Shield and Fortress provide full cover from one direction. Blocks line of sight for ranged attacks through your space. | +1 |
| 5 | Shield Throw | Shield Techniques can be performed at 20 ft range (Thrown). Shield bounces back at end of your turn. | +3 |

---

### Medium Melee

Balanced offense and defense. One-handed weapons that pair with shields or off-hand weapons. Medium Melee favors positioning, counterplay, and adaptability.

#### Medium Melee Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Parry | Reaction | Add your weapon damage die to AC against one melee attack. |
| 1 | Riposte Stance | Free Action | Enter stance. While in Riposte Stance, a successful Parry triggers a free counterattack. |
| 2 | Press the Advantage | Free (on hit) | After hitting, your next attack this turn has advantage. |
| 2 | Disarming Strike | 1 Action | On hit, target rolls `2d10 + Body` vs. your attack roll or drops their weapon. |
| 3 | Measured Assault | 3 Actions | Commit all 3 Actions to one attack. Add your weapon die twice to damage. If the target dies, refund 1 Action. |

#### Medium Melee Category Technique Augments

| Technique | Augment | Effect | Mana Cost |
|---|---|---|---|
| Parry | Iron Parry | Parry also works against ranged attacks within 10 ft. | +2 |
| Parry | Deflecting Parry | On successful Parry, redirect the attack to another enemy within 1 space (your Parry roll vs. new target's AC). | +3 |
| Riposte Stance | Aggressive Riposte | Counterattack deals +1d6 bonus damage. | +2 |
| Riposte Stance | Persistent Stance | Riposte Stance lasts until you choose to end it, not just until next turn. | +1 |
| Press the Advantage | Overwhelming Advantage | Next TWO attacks have advantage instead of one. | +3 |
| Press the Advantage | Pressing Wound | The advantage attack also applies 1 Bleed stack on hit. | +1 |
| Disarming Strike | Shattering Disarm | Dropped weapon flies 2 spaces. If it hits another creature, 1d4 damage. | +1 |
| Disarming Strike | Follow-Up Disarm | After disarming, make a free attack against the now-unarmed target at +2 to hit. | +2 |
| Measured Assault | Devastating Assault | +3 weapon dice instead of +2. | +3 |
| Measured Assault | Momentum Assault | On kill, refund 2 Actions instead of 1. | +3 |

#### Medium Melee Weapons

| # | Weapon | Complexity | Base Damage | Properties |
|---|---|---|---|---|
| 7 | Longsword | Standard | 1d10 | Versatile (1d12 two-handed) |
| 8 | Rapier | Complex | 1d8 | Finesse |
| 9 | Curved Sword | Standard | 1d8 | Finesse |
| 10 | Katana | Complex | 1d10 | Finesse, Two-Handed |
| 11 | Mace | Standard | 1d8 | Bludgeon |
| 12 | Flail | Standard | 1d8 | Bypass, Chain |
| 13 | War Pick | Standard | 1d8 | Pierce |
| 14 | Bastard Sword | Complex | 1d10 | Versatile (1d12), Adaptive |

**Bastard Sword and the Adaptive property.** One-handed grip = Medium Melee category. Two-handed grip = Heavy Melee category. At Mastery 3, you access Category Techniques from both categories.

#### Medium Melee Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Longsword | Bleed | Force | One-handed = Bleed. Two-handed = Force. Player chooses stack path by grip. |
| Rapier | Bleed | — | Bleed bypasses 1 Physical DR. Opening-spent Techniques apply 2 Bleed stacks. |
| Curved Sword | Bleed | — | Sweeping Bleed hits two adjacent targets. Spreads Bleed across a group. |
| Katana | Bleed | — | Each consecutive hit in the same turn applies +1 additional Bleed (1st = 1, 2nd = 2, 3rd = 3). |
| Mace | Force | — | Force stacks also impose -1 to mental Proficiency Checks per stack. At Staggered: disadvantage on all Proficiency Checks. |
| Flail | Force | — | Ignores Shield AC and Parry. Force stacks land against defensive opponents. |
| War Pick | Bleed | — | Pierce extends to Bleed: Bleed damage also ignores 2 Physical DR. |
| Bastard Sword | Bleed or Force | — | Matches grip. Switch mid-combat to exploit whichever path is closer to escalation. |

#### Longsword (Standard, Medium Melee) — 8 Techniques

**Unique Mechanic: Versatile Grip.** One-handed Longsword Techniques apply Bleed. Two-handed Longsword Techniques apply Force. Switch grip as part of any Technique or use Grip Shift mid-combo. At Mastery Rank 3, switching grip grants +1 to your next attack roll this turn.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Arming Slash | 1 Action | One-handed. 1d10 Slashing. Apply 1 Bleed stack. |
| 1 | Heavy Chop | 1 Action | Two-handed. 1d12 Bludgeoning. Apply 1 Force stack. |
| 2 | Grip Shift | Free Action, 3 Mana | Switch grip. Your next Longsword Technique this turn uses the new grip's condition path and deals +1d6 damage. |
| 2 | Half-Sword Thrust | 1 Action, 3 Mana | Two-handed grip on blade. 1d10 Piercing, ignores 2 Physical DR. Apply 1 Force stack. |
| 3 | Mordhau | 1 Action, 5 Mana | Two-handed. Strike with the crossguard. 2d8 Bludgeoning. Apply 2 Force stacks. Target rolls `2d10 + Body` vs. DC 14 or drops held item. |
| 3 | Zwerchhau | 1 Action, 7 Mana | One-handed horizontal cut. 2d10 Slashing. Apply 2 Bleed stacks. If target has 3+ Bleed stacks, apply 3 instead. |
| 4 | Versatile Execution | 1 Action, 8 Mana | Choose grip. One-handed: requires Shredded (5 Bleed). Apply Hemorrhage (T3): Bleed damage doubles, healing 50% effective. Two-handed: requires Staggered (5 Force). Apply Concussion (T3): target's Actions halved (minimum 1), mental DR drops to 0. |
| 5 | Master of Arms (Capstone) | 2 Actions, 12 Mana | Two strikes. First (one-handed): 2d10 Slashing, 3 Bleed stacks. Second (two-handed): 2d12 Bludgeoning, 3 Force stacks. If either T3 is active, target rolls `2d10 + Body` vs. DC 18 or Stunned 1 round. Once per long rest. |

##### Longsword Weapon Augments (Versatile Grip)

Passive. Once learned, these apply to ALL Longsword Techniques. Each adds its Mana cost to every Longsword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Fluid Transition | Grip Shift costs 0 Mana. Switching grips is always free. | +0 |
| 2 | Dual Conditioning | One-handed Techniques also apply 1 Force stack. Two-handed Techniques also apply 1 Bleed stack. | +2 |
| 3 | Balanced Weight | +1 AC in one-handed grip. +1 damage die size in two-handed grip (1d12 becomes 2d6). | +1 |
| 4 | Punishing Swap | After switching grips, your next Technique this turn deals +1d6 damage. Stacks with Grip Shift bonus. | +1 |
| 5 | Sustained Escalation | Hemorrhage and Concussion (T3) effects persist 1 additional round. | +2 |

#### Rapier (Complex, Medium Melee) — 12 Techniques

**Unique Mechanic: Openings.** A successful Parry or an enemy miss in melee grants you 1 Opening (maximum 3). Spend Openings to enhance Rapier Techniques. Openings reset at the end of combat.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Lunge | 1 Action | Attack a target up to 2 spaces away. -2 AC until your next turn. |
| 1 | Feinting Thrust | 1 Action | Spend 1 Opening. Attack has advantage. |
| 1 | En Garde | Free Action | Defensive stance. +1 AC. Successful Parries generate 2 Openings instead of 1. |
| 2 | Compound Riposte | Reaction | After a successful Parry, make a free attack at +1d8 damage. Costs 1 Opening. |
| 2 | Derobement | Reaction | Auto-succeed on Disarm resistance. Gain 1 Opening. |
| 2 | Fleche | 1 Action, 3 Mana | Move 3 spaces in a line and attack. +2 to hit. Cannot reuse for 1 round. |
| 3 | Balestra | 1 Action, 5 Mana | Spend 2 Openings. Three rapid thrusts. Roll each separately. |
| 3 | Counter-Tempo | Passive | At 3 Openings, all your attacks deal +1d6 damage. |
| 3 | Passata Sotto | Reaction, 3 Mana | Duck under an attack. The attack auto-misses. Gain 1 Opening. Once per round. |
| 4 | Prise de Fer | 1 Action, 5 Mana | Bind enemy weapon for 1 round. Target rolls `2d10 + Body` to break free. Costs 2 Openings. |
| 4 | Tempo Rubato | Passive | Reactions no longer consume your Reaction for the round. Unlimited Parry/Riposte per round. |
| 5 | Touché (Capstone) | 1 Action, 15 Mana | Spend 3 Openings. Auto-crit, triple damage. Target rolls `2d10 + Body` vs. DC 20 or incapacitated for 1 round. Once per long rest. |

##### Rapier Weapon Augments (Openings)

Passive. Once learned, these apply to ALL Rapier Techniques. Each adds its Mana cost to every Rapier Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Riposte Mastery | Gain 2 Openings instead of 1 from Parries and enemy misses. Maximum Openings increases to 5. | +0 |
| 2 | Flourish | Spend 1 Opening as a Free Action to impose disadvantage on the next attack against you this round. | +1 |
| 3 | Duelist's Grace | While you hold 2+ Openings, +1 AC. At 4+ Openings (requires Riposte Mastery), +2 AC. | +0 |
| 4 | Tempo Control | When you spend Openings on a Technique, the target has -1 to hit per Opening spent until their next turn. | +1 |
| 5 | Fencing Master | Openings generated by Passata Sotto and Derobement are doubled. | +2 |

##### Rapier Technique Augments

Socket into Augment Slots on individual Rapier Techniques. Each Technique has 2-3 options.

**Lunge** (1 Action — Attack up to 2 spaces. -2 AC until next turn.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Retreating Lunge | After Lunge, return to starting position. Negates -2 AC penalty. | +1 |
| Lunging Advance | On hit, move to adjacent space. Gap-closer. | +1 |
| Exposing Lunge | On hit, gain 1 Opening. Lunge becomes an Opening generator. | +2 |

**Feinting Thrust** (1 Action — Spend 1 Opening. Advantage.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Double Feint | Spend 2 Openings. Advantage AND target has disadvantage on next attack. | +2 |
| Feint Chain | On hit, gain 1 Opening. Net 0 cost on hit. Sustained pressure. | +1 |

**En Garde** (Free Action — +1 AC. Parries generate 2 Openings.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Grand Salute | Enemies that miss you (not just Parries) grant 3 Openings. | +2 |
| Aggressive Stance | +1d4 damage while in En Garde. AC bonus drops to +0. | +1 |

**Compound Riposte** (Reaction — After Parry, free attack +1d8. Costs 1 Opening.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Triple Riposte | 2 additional attacks at -2 each. Three strikes after one Parry. | +4 |
| Disarming Riposte | On hit, target drops weapon. | +2 |
| Bleeding Riposte | On hit, apply 2 Bleed stacks. | +1 |

**Derobement** (Reaction — Auto-succeed on Disarm. Gain 1 Opening.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Counter-Disarm | After Derobement, free Disarm attempt against the attacker. | +2 |
| Perfect Defense | Derobement also negates the triggering attack entirely. | +3 |

**Fleche** (1 Action, 3 Mana — Move 3 spaces in a line. +2 to hit. 1-round cooldown.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Passant Fleche | Hit every enemy in the charge line. +2 applies to all. | +3 |
| Retreating Fleche | After Fleche, teleport back to starting position. Hit-and-run. | +2 |
| Accelerating Fleche | 5 spaces. Removes 1-round cooldown. | +2 |

**Balestra** (1 Action, 5 Mana — Spend 2 Openings. Three rapid thrusts.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Cascading Balestra | If all 3 hit, 4th thrust at +1d8 damage. | +3 |
| Scattering Balestra | Each thrust targets a different enemy in reach. AoE burst. | +2 |
| Finishing Balestra | Below 50% HP: each thrust deals +1d6. | +2 |

**Counter-Tempo** (Passive — At 3 Openings, +1d6 damage.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Escalating Tempo | Bonus scales: 3 = +1d6, 4 = +2d6, 5 = +3d6. | +2 per attack |
| Tempo Burst | Spend all Openings for +1d10 per Opening on next attack. | +0 (Openings are cost) |

**Passata Sotto** (Reaction, 3 Mana — Auto-miss. Gain 1 Opening. Once per round.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Rising Thrust | After duck, free attack at +1d8. | +3 |
| Evasive Roll | After Passata Sotto, move 2 spaces. No opportunity attacks. | +1 |

**Prise de Fer** (1 Action, 5 Mana — Bind weapon 1 round. 2 Openings.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Enveloppement | Bind 2 rounds. Break-free DC +2. | +3 |
| Coupé | If target breaks free, free attack. If not, 1d8 at start of their turn. | +2 |

**Tempo Rubato** (Passive — Unlimited Parry/Riposte per round.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Perpetual Motion | Each Parry grants cumulative +1 damage to next attack. Resets at turn start. | +1 per Parry |
| Blade Barrier | At 3+ Openings, melee attackers take 1d4 on miss. Passive retaliation. | +2 |

**Touché** (Capstone, 1 Action, 15 Mana — 3 Openings. Auto-crit, ×3 damage. DC 20 or incapacitated.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Final Curtain | On kill, once-per-long-rest resets. Chain-kill potential. | +5 |
| Dramatic Finish | Enemies within 6 spaces: `2d10 + Social` vs. DC 15 or Frightened 2 rounds. | +3 |

#### Curved Sword (Standard, Medium Melee) — 8 Techniques

**Unique Mechanic: Sweeping Edge.** Each damaging Curved Sword Technique that hits also applies 1 Bleed stack to one adjacent enemy within 1 space of the target. At Mastery Rank 3, Sweeping Edge spreads to 2 adjacent enemies.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Sweeping Cut | 1 Action | 1d8 Slashing. Apply 1 Bleed stack. Sweeping Edge: 1 adjacent enemy takes 1 Bleed stack. |
| 1 | Paired Blades | Passive | Curved Swords may be dual-wielded. While dual-wielding, +2 to attack rolls with Curved Sword Techniques. |
| 2 | Crescent Sweep | 1 Action, 3 Mana | Attack all enemies in a 2-space cone. 1d8 Slashing each. Apply 1 Bleed stack to each. Sweeping Edge triggers per target hit. |
| 2 | Cleave | 1 Action, 3 Mana | On kill, carry remaining damage +1d6 to one adjacent enemy. Apply 2 Bleed stacks to the secondary target. |
| 3 | Deadly Dance | 1 Action, 5 Mana | 3 strikes at different targets in reach. 1d8 Slashing each. Apply 1 Bleed per hit. Sweeping Edge triggers per strike. |
| 3 | Whirlwind | 1 Action, 7 Mana | Strike all enemies within 2 spaces. 2d6 Slashing each. Apply 2 Bleed stacks each. |
| 4 | Hemorrhaging Tide | 1 Action, 8 Mana | Requires Shredded (5 Bleed) on target. Apply Hemorrhage (T3): Bleed damage doubles, healing 50% effective. Sweeping Edge spreads 1 Bleed stack to all enemies within 2 spaces. |
| 5 | Crimson Tempest (Capstone) | 2 Actions, 12 Mana | Strike all enemies within 3 spaces. 2d8 Slashing each. Apply 3 Bleed stacks each. Sweeping Edge applies to every target: each adjacent enemy takes 2 Bleed stacks. Once per long rest. |

##### Curved Sword Weapon Augments (Sweeping Edge)

Passive. Once learned, these apply to ALL Curved Sword Techniques. Each adds its Mana cost to every Curved Sword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Wide Arc | Sweeping Edge range increases from 1 space to 2 spaces. | +1 |
| 2 | Bleeding Momentum | While 3+ enemies have Bleed stacks, Curved Sword Techniques deal +1d4 damage. | +1 |
| 3 | Crimson Spray | When Sweeping Edge applies Bleed, that enemy also takes 1d4 Slashing damage. | +2 |
| 4 | Dual Dance | While dual-wielding, Deadly Dance and Whirlwind gain +1 additional strike. | +2 |
| 5 | Cascade | When any enemy reaches Shredded (5 Bleed), all enemies within 2 spaces take 1 Bleed stack. | +1 |

#### Katana (Complex, Medium Melee) — 12 Techniques

**Unique Mechanic: Momentum Blade.** Each consecutive hit against the same target in one turn applies escalating Bleed: 1st hit = 1 stack, 2nd hit = 2 stacks, 3rd hit = 3 stacks. Switching targets or ending your turn resets the count.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Iaijutsu (Draw Cut) | 1 Action | Requires katana sheathed. Draw and strike in one motion. +2 to hit, +1d6 damage. You may sheathe the katana as a Free Action at end of your turn. |
| 1 | Successive Cuts | Passive | When you attack a target you already hit this turn, +2 to hit. |
| 1 | Chiburi (Blood Flick) | Free Action | After hitting a target 2 or more times this turn, your Bleed stacks on that target last 1 additional round. |
| 2 | Tsubame Gaeshi (Swallow Reversal) | 1 Action, 3 Mana | On hit, reverse the blade for a second strike at -2 to hit. Both hits count separately for Momentum Blade. |
| 2 | Battojutsu (War Draw) | 1 Action, 3 Mana | Requires katana sheathed. Enhanced draw cut. +4 to hit, +1d10 damage. Target rolls `2d10 + Body` vs. DC 14 or loses half movement for 1 round. |
| 2 | Seme (Pressure) | Free Action, 3 Mana | Until end of turn, each Momentum Blade hit applies +1 additional Bleed stack (1st hit = 2, 2nd = 3, 3rd = 4). |
| 3 | Kirioroshi (Cleaving Down-Cut) | 1 Action, 5 Mana | Overhead strike. On hit, deal weapon damage +1d6 per Bleed stack on target (max +5d6). |
| 3 | Tsuki (Piercing Thrust) | 1 Action, 8 Mana | Precision thrust. Auto-hit. Deal 1d10 damage + 2 Bleed stacks. Counts as a consecutive hit for Momentum Blade. |
| 3 | Suriage (Rising Parry-Cut) | Reaction, 5 Mana | When attacked in melee, roll your attack vs. theirs. Win: negate the attack and deal 1d10 damage + 1 Bleed stack. |
| 4 | Zantetsuken (Iron-Cutting Slash) | 2 Actions, 8 Mana | Full-force slash. Weapon damage ×2, ignore Physical DR. If target is Shredded, deal +2d10 damage. |
| 4 | Musō Ken (No-Mind Blade) | Passive | Your third consecutive hit on the same target each turn deals +2d10 damage and ignores Physical DR. |
| 5 | Ōgi: Hitotsume (Capstone — The One Cut) | 3 Actions, 15 Mana | Single perfect draw strike. Auto-hit. Weapon damage ×3 +1d10 per Bleed stack on target. Apply 5 Bleed stacks (triggers Shredded). Target rolls `2d10 + Body` vs. DC 18 or enters Dying. Once per long rest. |

##### Katana Weapon Augments (Momentum Blade)

Passive. Once learned, these apply to ALL Katana Techniques. Each adds its Mana cost to every Katana Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Flow State | Momentum Blade escalation persists if you switch targets mid-turn. First hit on a new target counts as "consecutive" if you hit the previous target this turn. | +0 |
| 2 | Battojutsu Mastery | Iaijutsu and Battojutsu Techniques deal +1d6 damage. Sheathing at end of turn is automatic. | +1 |
| 3 | Crimson Arc | When a Katana Technique applies Bleed, one other enemy within 2 spaces takes 1 Bleed stack. | +1 |
| 4 | Zanshin (Lingering Intent) | After using 3+ Katana Techniques in one turn, the last target hit takes 1 additional Bleed stack at start of their turn. | +0 |
| 5 | Mugen (Infinite Blade) | At 5 Bleed stacks (Shredded), your Momentum Blade count does not reset at end of turn. It continues into the next turn. | +2 |

##### Katana Technique Augments

Socket into Augment Slots on individual Katana Techniques. Each Technique has 2-3 options.

**Iaijutsu (Draw Cut)** (1 Action — Sheathed. +2 to hit, +1d6.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Flash Step | Teleport up to 4 spaces to target before the draw strike. | +3 |
| Returning Draw | Sheathe as part of same Action. Each redraw this combat: +1d6 (stacks to +3d6). | +1 |
| Quickdraw Assault | No longer requires sheathed. -1d6 damage (net +0 vs. normal attack, trades bonus for flexibility). | +2 |

**Successive Cuts** (Passive — +2 to hit on targets hit this turn.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Relentless Pursuit | +3 after 2nd hit, +4 after 3rd. Snowballing accuracy. | +1 per attack |
| Bleeding Edge | Each successive hit applies 1 additional Bleed beyond Momentum Blade. | +2 |

**Chiburi (Blood Flick)** (Free Action — After 2+ hits, Bleed lasts 1 extra round.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Splattering Flick | Bleed splashes to 1 enemy within 2 spaces (half stacks, rounded down). | +2 |
| Cleansing Flick | Remove 1 condition from yourself. Purge debuffs through offense. | +1 |

**Tsubame Gaeshi (Swallow Reversal)** (1 Action, 3 Mana — Second strike at -2. Both count for Momentum.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Triple Reversal | Third strike at -4. Three hits, one Action. All count for Momentum. | +3 |
| Perfect Reversal | Second strike has no penalty. Clean double-hit. | +2 |
| Aerial Reversal | Strikes can target different enemies in reach. Split the reversal. | +2 |

**Battojutsu (War Draw)** (1 Action, 3 Mana — Sheathed. +4 to hit, +1d10. DC 14 half movement.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Thunder Draw | On hit, 2 Force stacks + 1-space shockwave pushes adjacent enemies. Cross-condition draw. | +3 |
| Phantom Draw | Target cannot use Reactions. Delayed damage reveal: target doesn't know they're hit until end of turn. | +4 |

**Seme (Pressure)** (Free Action, 3 Mana — This turn, +1 Bleed per Momentum hit.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Overwhelming Pressure | While active, targets have -1 AC per Bleed stack on them. | +2 |
| Sustained Pressure | Lasts 2 turns instead of 1. | +3 |

**Kirioroshi (Cleaving Down-Cut)** (1 Action, 5 Mana — +1d6 per Bleed stack, max +5d6.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Seismic Cut | Creates 1-space difficult terrain behind target. | +1 |
| Executioner's Cut | Below 25% HP: max bonus increases to +8d6. | +3 |
| Splitting Cut | Hits primary + 1 adjacent enemy (half damage + half Bleed bonus). | +3 |

**Tsuki (Piercing Thrust)** (1 Action, 8 Mana — Auto-hit. 1d10 + 2 Bleed. Counts for Momentum.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Armor Piercing Thrust | Ignores all Physical DR. True damage. | +2 |
| Chain Thrust | Free second thrust at -2 to hit on another target in reach. 1d10 + 1 Bleed. | +3 |

**Suriage (Rising Parry-Cut)** (Reaction, 5 Mana — Your attack vs. theirs. Win: negate + 1d10 + 1 Bleed.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Counter Momentum | Suriage counts as a Momentum Blade hit. Defense feeds offense. | +1 |
| Rising Storm | On negate, make a second strike at +1d6. | +3 |

**Zantetsuken (Iron-Cutting Slash)** (2 Actions, 8 Mana — ×2 damage, ignore Physical DR. +2d10 if Shredded.)

| Augment | Effect | Mana Cost |
|---|---|---|
| All-Cleaving Slash | Hits all enemies in a 2-space cone. AoE devastation. | +5 |
| Material Destruction | On hit, destroy one piece of target's equipment. Permanent until repaired. | +3 |
| Dimensional Slash | Range extends to 3 spaces. Ranged slash wave. | +4 |

**Musō Ken (No-Mind Blade)** (Passive — 3rd consecutive hit: +2d10, ignore Physical DR.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Transcendent Blade | Bonus applies to 4th, 5th+ hits. Uncapped escalation. | +2 per hit beyond 3rd |
| Void Cut | 3rd hit also bypasses Magic DR. True damage strike. | +2 |

**Ōgi: Hitotsume (Capstone)** (3 Actions, 15 Mana — Auto-hit, ×3, +1d10/Bleed, 5 Bleed → Shredded, DC 18 → Dying.)

| Augment | Effect | Mana Cost |
|---|---|---|
| Mugen Ittō (Infinite One-Sword) | On kill, once-per-long-rest resets. Chain-kill potential. | +5 |
| Shinsoku (Godspeed) | Costs 2 Actions instead of 3. Faster execution. | +5 |
| Tsujigiri (Crossroads Kill) | After Hitotsume, enemies within 4 spaces take 1d10 Slashing + 2 Bleed from wind pressure. | +4 |

#### Mace (Standard, Medium Melee) — 8 Techniques

**Unique Mechanic: Concussive Impact.** Force stacks from Mace Techniques impose -1 per stack to mental Proficiency Checks (Investigation, Knowledge, Medicine, Arcana, Insight). At Staggered (5 Force), the target has disadvantage on ALL Proficiency Checks.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Skull Crack | 1 Action | 1d8 Bludgeoning. Apply 1 Force stack. |
| 1 | Jarring Blow | 1 Action | 1d8 Bludgeoning. Apply 1 Force stack. Target rolls `2d10 + Mind` vs. DC 12 or loses concentration on one active effect. |
| 2 | Concussive Slam | 1 Action, 3 Mana | 1d10 Bludgeoning. Apply 2 Force stacks. |
| 2 | Dazing Strike | 1 Action, 3 Mana | 1d8 Bludgeoning. Apply 1 Force stack. Target cannot use Reactions until start of their next turn. |
| 3 | Thundering Strike | 1 Action, 5 Mana | 2d8 Bludgeoning. Apply 2 Force stacks. Adjacent enemies within 1 space take 1d4 Bludgeoning and 1 Force stack. |
| 3 | Rattling Blow | 1 Action, 7 Mana | 2d10 Bludgeoning. Apply 2 Force stacks. Target rolls `2d10 + Mind` vs. DC 15 or loses 1 Action next turn. |
| 4 | Concussion | 1 Action, 8 Mana | Requires Staggered (5 Force) on target. Apply Concussion (T3): target's Actions halved (round down, minimum 1), mental DR drops to 0. Lasts 2 rounds. |
| 5 | Cranial Devastation (Capstone) | 2 Actions, 12 Mana | 3d10 Bludgeoning. Apply 5 Force stacks (triggers Staggered). Target rolls `2d10 + Body` vs. DC 18 or Stunned 1 round. If Concussion (T3) active, Stun lasts 2 rounds. Once per long rest. |

##### Mace Weapon Augments (Concussive Impact)

Passive. Once learned, these apply to ALL Mace Techniques. Each adds its Mana cost to every Mace Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Rattling Impact | Force stacks from Mace Techniques also impose -1 per stack to Body-based Proficiency Checks (Athletics, Survival). | +1 |
| 2 | Armor Dent | Mace Techniques deal +2 damage against targets in Heavy or Medium armor. | +0 |
| 3 | Lingering Concussion | Force stacks from Mace Techniques last 1 additional round. | +1 |
| 4 | Shattering Force | When a target reaches Staggered (5 Force), their Physical DR drops by 1 until end of combat. | +2 |
| 5 | Brain Rattler | Concussion (T3) prevents the target from casting spells for its duration. | +2 |

#### Flail (Standard, Medium Melee) — 8 Techniques

**Unique Mechanic: Unstoppable Chain.** Flail Techniques ignore Shield AC bonus (Bypass) and cannot be Parried (Chain). Force stacks from Flail Techniques cannot be prevented by defensive reactions.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Chain Strike | 1 Action | 1d8 Bludgeoning. Apply 1 Force stack. Ignores Shield AC bonus. Cannot be Parried. |
| 1 | Wrap and Pull | 1 Action | 1d6 Bludgeoning. Apply 1 Force stack. Target rolls `2d10 + Body` vs. DC 12 or pulled 1 space toward you. |
| 2 | Overhead Smash | 1 Action, 3 Mana | 1d10 Bludgeoning. Apply 2 Force stacks. Cannot be Parried. |
| 2 | Disarming Swing | 1 Action, 3 Mana | 1d8 Bludgeoning. Apply 1 Force stack. Target rolls `2d10 + Body` vs. DC 14 or drops weapon. |
| 3 | Crushing Arc | 1 Action, 5 Mana | Swing in a 2-space cone. 2d8 Bludgeoning each. Apply 2 Force stacks each. Cannot be Parried. |
| 3 | Wrecking Blow | 1 Action, 7 Mana | 2d10 Bludgeoning. Apply 2 Force stacks. Destroys target's Shield or reduces Physical DR by 2 until end of combat. |
| 4 | Concussion | 1 Action, 8 Mana | Requires Staggered (5 Force) on target. Apply Concussion (T3): target's Actions halved (round down, minimum 1), mental DR drops to 0. Lasts 2 rounds. Cannot be prevented by defensive abilities. |
| 5 | Siege Breaker (Capstone) | 2 Actions, 12 Mana | 3d10 Bludgeoning. Apply 5 Force stacks (triggers Staggered). Target's armor destroyed: Physical DR and Magic DR drop to 0 until repaired. Target rolls `2d10 + Body` vs. DC 18 or Prone. Once per long rest. |

##### Flail Weapon Augments (Unstoppable Chain)

Passive. Once learned, these apply to ALL Flail Techniques. Each adds its Mana cost to every Flail Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Extended Chain | Flail Techniques gain +1 space reach. | +1 |
| 2 | Weighted Head | Flail Techniques deal +1d4 Bludgeoning against targets with Shield or Heavy armor. | +1 |
| 3 | Entangling Chain | Wrap and Pull range increases to 2 spaces. On success, target is also Restrained until end of their next turn. | +2 |
| 4 | Armor Breaker | Force stacks from Flail Techniques reduce target's Physical DR by 1 per stack (max -5). Resets at end of combat. | +2 |
| 5 | Relentless Assault | Defensive reactions (Parry, Block, Shield Wall) against Flail Techniques auto-fail. | +2 |

#### War Pick (Standard, Medium Melee) — 8 Techniques

**Unique Mechanic: Deep Pierce.** War Pick Techniques and their Bleed ticks ignore 2 Physical DR. At Mastery Rank 3, Bleed ticks from War Pick Techniques ignore 3 Physical DR instead.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Puncture | 1 Action | 1d8 Piercing. Apply 1 Bleed stack. Ignores 2 Physical DR. |
| 1 | Hooking Strike | 1 Action | 1d6 Piercing. Apply 1 Bleed stack. Target rolls `2d10 + Body` vs. DC 12 or loses half movement next turn. |
| 2 | Spike Drive | 1 Action, 3 Mana | 1d10 Piercing. Apply 2 Bleed stacks. Ignores 2 Physical DR. |
| 2 | Rending Tear | 1 Action, 3 Mana | 1d8 Piercing. Apply 1 Bleed stack. Deal +1d6 damage per existing Bleed stack on target (max +5d6). |
| 3 | Armor Crack | 1 Action, 5 Mana | 2d8 Piercing. Apply 2 Bleed stacks. Target's Physical DR drops by 2 until end of combat. Stacks with Deep Pierce. |
| 3 | Impaling Strike | 1 Action, 7 Mana | 2d10 Piercing. Apply 2 Bleed stacks. Target rolls `2d10 + Body` vs. DC 15 or Impaled: movement 0, 1d6 Piercing at start of each turn until freed (1 Action to remove). |
| 4 | Hemorrhage | 1 Action, 8 Mana | Requires Shredded (5 Bleed) on target. Apply Hemorrhage (T3): Bleed damage doubles, healing 50% effective, persists 2 extra rounds. Deep Pierce extends: Hemorrhage ticks also ignore 2 Physical DR. |
| 5 | Total Dissolution (Capstone) | 2 Actions, 15 Mana | Requires Hemorrhage (T3) on target. 3d10 Piercing. Apply Total Dissolution (T4): all Bleed damage ignores ALL Physical DR. Target's armor rating permanently drops by 2 until repaired. Once per long rest. |

##### War Pick Weapon Augments (Deep Pierce)

Passive. Once learned, these apply to ALL War Pick Techniques. Each adds its Mana cost to every War Pick Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Barbed Point | Bleed stacks from War Pick Techniques cannot be removed by mundane healing. Requires magical healing. | +1 |
| 2 | Piercing Focus | War Pick Techniques ignore an additional 1 Physical DR (total 3). | +1 |
| 3 | Serrated Edge | Bleed ticks reduce target's Physical DR by 1 per tick (minimum 0). Resets at end of combat. | +2 |
| 4 | Puncture Wound | Bleed stacks from War Pick Techniques last 1 additional round. | +1 |
| 5 | Exposed Vitals | While target has Shredded (5 Bleed), all attacks from any source ignore 2 Physical DR. | +2 |

#### Bastard Sword (Complex, Medium Melee / Heavy Melee) — 12 Techniques

**Unique Mechanic: Adaptive Stance.** One-handed grip = Medium Melee category, applies Bleed. Two-handed grip = Heavy Melee category, applies Force. At Mastery Rank 3, you can use Category Techniques from both Medium Melee and Heavy Melee.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Adaptive Cut | 1 Action | One-handed. 1d10 Slashing. Apply 1 Bleed stack. Medium Melee. |
| 1 | Crushing Blow | 1 Action | Two-handed. 1d12 Bludgeoning. Apply 1 Force stack. Heavy Melee. |
| 1 | Stance Shift | Free Action | Switch grip. Your next Bastard Sword Technique this turn uses the new grip's category and condition path. |
| 2 | Flowing Slash | 1 Action, 3 Mana | One-handed. 1d10 Slashing. Apply 1 Bleed stack. After the strike, switch to two-handed grip (free). |
| 2 | Overhead Cleave | 1 Action, 3 Mana | Two-handed. 1d12 Bludgeoning. Apply 2 Force stacks. Target rolls `2d10 + Body` vs. DC 13 or loses 1 Action next turn. |
| 2 | Cross Guard Block | Reaction, 3 Mana | Reduce incoming melee damage by 1d8. Works in either grip. |
| 3 | Rending Combination | 1 Action, 5 Mana | One-handed to two-handed. Two strikes: 1d10 Slashing + 2 Bleed, then 1d12 Bludgeoning + 2 Force. Grip switches automatically. |
| 3 | Executioner's Swing | 1 Action, 7 Mana | Two-handed. 2d12 Bludgeoning. Apply 2 Force stacks. If target has 3+ Bleed stacks, deal +1d10 damage. |
| 3 | Counter Stance | Passive | When you reduce damage with Cross Guard Block, apply 1 Force stack (two-handed) or 1 Bleed stack (one-handed) to the attacker. |
| 4 | Hemorrhaging Cut | 1 Action, 8 Mana | One-handed. Requires Shredded (5 Bleed) on target. 2d10 Slashing. Apply Hemorrhage (T3): Bleed damage doubles, healing 50% effective. |
| 4 | Crushing Concussion | 1 Action, 8 Mana | Two-handed. Requires Staggered (5 Force) on target. 2d12 Bludgeoning. Apply Concussion (T3): target's Actions halved (minimum 1), mental DR drops to 0. |
| 5 | Adaptive Mastery (Capstone) | 3 Actions, 15 Mana | Three alternating strikes. First (one-handed): 2d10 Slashing, 3 Bleed stacks. Second (two-handed): 2d12 Bludgeoning, 3 Force stacks. Third (your choice): 3d10 damage, triggers Shredded or Staggered. If both T3s are active, target rolls `2d10 + Body` vs. DC 20 or enters Dying. Once per long rest. |

##### Bastard Sword Weapon Augments (Adaptive Stance)

Passive. Once learned, these apply to ALL Bastard Sword Techniques. Each adds its Mana cost to every Bastard Sword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Fluid Grip | Stance Shift applies 1 Bleed or 1 Force stack (your choice) to one enemy in reach. | +0 |
| 2 | Cross-Conditioning | One-handed Techniques also apply 1 Force stack. Two-handed Techniques also apply 1 Bleed stack. | +2 |
| 3 | Dual Category Mastery | Category Techniques from both Medium Melee and Heavy Melee cost 1 less Mana (minimum 0). | +0 |
| 4 | Adaptive Parry | Cross Guard Block reduces 1d10 instead of 1d8. +1d4 per grip switch this turn. | +1 |
| 5 | Convergence | When target has both Bleed and Force stacks, Bastard Sword Techniques deal +1 damage per combined stack. | +2 |

---

### Heavy Melee

Two-handed, high damage, slow. Heavy Melee favors commitment, area attacks, and overwhelming force. These weapons hit hard but cost more Actions per attack.

#### Heavy Melee Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Cleave | Free (on kill) | On kill, make a free attack against an adjacent enemy. |
| 1 | Power Attack | 1 Action | +1 damage die. -2 to hit. |
| 2 | Staggering Blow | 1 Action | On hit, target loses Reaction and has -2 AC until their next turn. |
| 2 | Whirlwind | 2 Actions | Attack all adjacent enemies. One roll vs. each AC. |
| 3 | Executioner | 2 Actions | If target is below 25% HP, auto-crit on hit. |

#### Heavy Melee Category Technique Augments

| Technique | Augment | Effect | Mana Cost |
|---|---|---|---|
| Cleave | Cascading Cleave | If Cleave also kills, Cleave triggers again. Chain unlimited. | +2 per chain |
| Cleave | Sweeping Cleave | Cleave hits ALL adjacent enemies, not just one. | +3 |
| Power Attack | Brutal Power Attack | +2 dice instead of +1 die. -4 to hit instead of -2. | +2 |
| Power Attack | Focused Power Attack | Remove the -2 penalty. Clean extra damage. | +3 |
| Staggering Blow | Crumbling Blow | Also reduces target's Physical DR by 1 until end of combat. Stacks. | +2 |
| Staggering Blow | Dizzying Blow | Target has disadvantage on attacks until their next turn. | +2 |
| Whirlwind | Expanding Whirlwind | Radius increases to 2 spaces. | +3 |
| Whirlwind | Sustained Whirlwind | Spend 1 Action on subsequent turns to maintain the spin. Deals weapon damage to all enemies within range each turn. | +2 per turn |
| Executioner | Merciful Execution | Threshold increases to below 50% HP. -1d6 damage. | +2 |
| Executioner | Grim Execution | On kill, all enemies within 3 spaces roll `2d10 + Social` vs. DC 13 or Frightened for 1 round. | +1 |

#### Heavy Melee Weapons

| # | Weapon | Complexity | Base Damage | Properties |
|---|---|---|---|---|
| 15 | Greatsword | Complex | 2d6 | Two-Handed, Heavy |
| 16 | Greathammer | Standard | 2d8 | Two-Handed, Heavy, Bludgeon |
| 17 | Great Axe | Standard | 1d12 | Two-Handed, Heavy |
| 18 | Greatclub | Simple | 2d6 | Two-Handed, Heavy, Bludgeon |

#### Heavy Melee Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Greatsword | Force | Bleed | Normal grip = Force. Half-Sword grip = Bleed (1d8, Finesse). |
| Greathammer | Force | — | 2 Force stacks per hit. Fastest single-weapon path to Staggered. At Staggered, Force attacks deal triple bonus damage. |
| Great Axe | Bleed | — | Bleed stacks deal +1 per stack (2 per stack instead of 1). At Shredded, attacks ignore ALL Physical DR. |
| Greatclub | Force | — | 1 Force per hit. Knockback into walls or terrain grants bonus Force stacks. |

#### Greatsword (Complex, Heavy Melee) — 12 Techniques

**Unique Mechanic: Half-Sword.** Grip the blade for close-range precision. Techniques tagged [Half-Sword] use the Greatsword as a Medium Melee weapon (1d8 damage, Finesse).

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Overhead Slash | 1 Action | On hit against Heavy armor, +1d6 damage. |
| 1 | Wide Sweep | 1 Action | Attack target + one adjacent enemy. One roll vs. both ACs. |
| 1 | Mordhau [Half-Sword] | 1 Action | Strike with crossguard. 1d8 Bludgeon. Ignores 2 Physical DR. |
| 2 | Zwerchhaü | 1 Action, 3 Mana | Horizontal cross-cut. Target cannot use Reactions until their next turn. |
| 2 | Winding Thrust [Half-Sword] | 1 Action | Precision thrust. +4 to hit, 1d6 damage. Apply 1 Bleed stack. |
| 2 | Murder Stroke [Half-Sword] | 2 Actions | Pommel strike. 1d10 Bludgeon. Target rolls `2d10 + Body` vs. DC 14 or Stunned for 1 round. |
| 3 | Krumphau | 1 Action, 5 Mana (Reaction) | Counter-cut. When an enemy attacks you in melee, strike simultaneously. If you hit and they miss, they are Staggered. |
| 3 | Blade Cyclone | 2 Actions, 8 Mana | Hit all enemies within 2 spaces. Full damage to each. Once per combat. |
| 3 | Absetzen | Reaction, 3 Mana | Deflect a melee attack. Your attack roll vs. theirs. Win = negate attack + free thrust (1d6 damage). |
| 4 | Schielhau | 1 Action, 5 Mana | Target drops their weapon and takes 1d6 Bleed damage. |
| 4 | Zufechten | Passive | First attack each combat has advantage and deals +1d6 damage. |
| 5 | Meisterhau (Capstone) | 3 Actions, 15 Mana | Auto-hit. Weapon damage × 3. Target rolls `2d10 + Body` vs. DC 18 or falls prone, Stunned, and Staggered. Once per long rest. |

##### Greatsword Weapon Augments (Half-Sword)

Passive. Once learned, these apply to ALL Greatsword Techniques. Each adds its Mana cost to every Greatsword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Grip Flow | Switching between normal and Half-Sword grip is a Free Action (instead of costing an Action). | +0 |
| 2 | Mortal Draw | The first Greatsword Technique after switching grip deals +1d8 bonus damage. | +1 |
| 3 | Zweihänder Reach | Normal-grip Greatsword Techniques gain +1 space reach. | +2 |
| 4 | Half-Sword Precision | [Half-Sword] Techniques gain an additional +2 to hit. | +1 |
| 5 | Swordsmanship | After a [Half-Sword] Technique, your next normal-grip Technique this turn has advantage. After a normal-grip Technique, your next [Half-Sword] Technique deals +1d6 damage. | +2 |

#### Greathammer (Standard, Heavy Melee) — 9 Techniques

**Unique Mechanic: Crushing Force.** Every hit applies 2 Force stacks instead of 1. At Staggered (5 Force stacks), your Force damage ticks deal triple bonus (3 per stack per round instead of 1).

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Skull Crack | 1 Action | On hit, target has disadvantage on their next attack roll. |
| 1 | Driving Blow | 1 Action | On hit, push target 2 spaces. Collision with a wall or creature deals 1d8 bonus damage. |
| 2 | Earthshaker | 2 Actions, 3 Mana | Strike the ground. All enemies within 1 space roll `2d10 + Body` vs. DC 13 or fall prone. |
| 2 | Concussive Blow | 1 Action, 3 Mana | On hit, target loses Reaction until their next turn. If target is Staggered, also Stunned for 1 round. |
| 3 | Tremor | 2 Actions, 5 Mana | All enemies within 2 spaces take 1d8 damage and roll `2d10 + Body` vs. DC 14 or fall prone. |
| 3 | Armor Crush | 1 Action, 5 Mana | On hit, reduce target's Physical DR by 2 until end of combat. Stacks. |
| 4 | Shatter | 1 Action, 8 Mana | Requires Staggered. Triggers Shattered (T3 Enhanced): Physical DR = 0 for 2 rounds. Physical attacks auto-apply 1 Bleed. |
| 4 | Pulverize | 2 Actions, 8 Mana | Requires Staggered. Weapon damage + 2d8. Target rolls `2d10 + Body` vs. DC 16 or Stunned for 1 round. |
| 5 | Obliterate (Capstone) | 3 Actions, 15 Mana | Requires Shattered. Weapon damage × 4. Kill = target cannot be resurrected. Boss: damage × 3, boss loses 1 action permanently. Once per long rest. |

##### Greathammer Weapon Augments (Crushing Force)

Passive. Once learned, these apply to ALL Greathammer Techniques. Each adds its Mana cost to every Greathammer Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Aftershock | Greathammer Techniques that push the target also deal 1d6 Bludgeon to enemies adjacent to the push destination. | +2 |
| 2 | Concussive Waves | When you apply Force stacks with a Greathammer Technique, enemies adjacent to your target each take 1 Force stack. | +3 |
| 3 | Impact Crater | Greathammer Techniques that cause prone create difficult terrain in a 1-space radius for 2 rounds. | +1 |
| 4 | Momentum of Ruin | When you hit a Staggered target with a Greathammer Technique, refund 1 Action. Once per turn. | +0 |
| 5 | Tectonic | Greathammer Techniques against objects, structures, and terrain deal triple damage. Terrain destruction radius +1 space. | +1 |

#### Great Axe (Standard, Heavy Melee) — 8 Techniques

**Unique Mechanic: Savage Rend.** Bleed stacks from Great Axe Techniques tick for +2 damage per stack per round instead of +1. At Shredded (5 stacks), Great Axe attacks ignore all Physical DR.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Heft | Passive | Great Axe attacks gain +2 to hit. |
| 1 | Hewing Strike | 1 Action | On hit, apply 1 Bleed stack. |
| 2 | Primal Rage | Free (on hit), 3 Mana | When you hit a target below 50% HP, deal +1d6 bonus damage. Persists until combat ends. Stacks up to 3 times. |
| 2 | Wild Cleave | 2 Actions, 3 Mana | Attack all enemies within 1 space. Each hit applies 1 Bleed stack. |
| 3 | Rend Asunder | 1 Action, 5 Mana | On hit, ignore all DR. Apply 3 Bleed stacks. |
| 3 | Execution Blow | 1 Action, 8 Mana | Target at or below 25% HP: double damage. On kill: heal 1d10 + Body modifier. |
| 4 | Hemorrhage | 1 Action, 8 Mana | Requires Shredded on target. Triggers Enhanced Escalation (T3): Bleed ticks deal +4 per stack per round. Healing on target is 50% effective for 3 rounds. |
| 5 | Exsanguination (Capstone) | 3 Actions, 15 Mana | Requires Shredded. All Bleed stacks on target become permanent (no natural decay). Apply 3 Bleed stacks per round automatically. Target bleeds out in rounds equal to remaining HP ÷ total Bleed damage per round. Once per long rest. |

##### Great Axe Weapon Augments (Savage Rend)

Passive. Once learned, these apply to ALL Great Axe Techniques. Each adds its Mana cost to every Great Axe Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Blood Scent | After applying Bleed with a Great Axe Technique, your next attack against the same target this turn has advantage. | +0 |
| 2 | Arterial Strike | Great Axe Techniques that apply Bleed stacks apply 1 additional stack. | +2 |
| 3 | Sanguine Fury | While your target has 3+ Bleed stacks, Great Axe Techniques deal +1d6 bonus damage. | +1 |
| 4 | Crimson Harvest | When a target takes Bleed tick damage from your stacks, heal HP equal to half the tick damage dealt. | +2 |
| 5 | Relentless Edge | Bleed stacks applied by Great Axe Techniques last 3 rounds instead of 2. | +1 |

#### Greatclub (Simple, Heavy Melee) — 5 Techniques

**Unique Mechanic: Wallbreaker.** When a Greatclub Technique knocks a target into a wall, obstacle, or terrain feature, apply 2 bonus Force stacks.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Overhead Smash | 1 Action | On hit, push target 1 space in any direction. |
| 1 | Battering Swing | 1 Action | On hit, apply 1 Force stack. |
| 2 | Home Run | 1 Action, 3 Mana | On hit, push target 3 spaces. Collision with a wall or creature deals 1d8 bonus damage. |
| 2 | Ground Pound | 2 Actions, 3 Mana | Strike the ground. All enemies within 1 space take 1d6 damage and are pushed 1 space away. |
| 3 | Demolition | 2 Actions, 5 Mana | On hit, weapon damage + 1d10. Push target 2 spaces. Wall collision applies Staggered (5 Force stacks). Destroys non-magical terrain in the path. |

##### Greatclub Weapon Augments (Wallbreaker)

Passive. Once learned, these apply to ALL Greatclub Techniques. Each adds its Mana cost to every Greatclub Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Rubble Field | When you destroy terrain with a Greatclub Technique, the area becomes difficult terrain for 2 rounds. | +0 |
| 2 | Follow Through | After pushing a target with a Greatclub Technique, move 1 space toward the target as a Free Action. | +0 |
| 3 | Collateral Damage | When a Greatclub push sends a target into another creature, that creature takes 1d6 damage and gains 1 Force stack. | +1 |

---

### Reach

Extended range (2+ spaces) and zone control. Reach weapons punish movement, lock down areas, and protect allies. They favor kiting, formation fighting, and battlefield control.

#### Reach Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Sentinel | Reaction | Enemies entering your reach provoke a free attack. |
| 1 | Sweep | 1 Action | Attack up to two adjacent targets within your reach. One roll vs. both ACs. |
| 2 | Keep at Bay | Free (on hit) | On hit, push target 1 space away from you. |
| 2 | Impale | 1 Action | On hit, target is Restrained until they spend an Action to pull free or you release. You cannot attack other targets while impaling. |
| 3 | Phalanx | Passive | While adjacent to an ally who also wields a Reach weapon, both of you gain +2 AC. |

#### Reach Category Technique Augments

| Technique | Augment | Effect | Mana Cost |
|---|---|---|---|
| Sentinel | Threatening Reach | Sentinel also triggers when enemies move WITHIN your reach, not just on entry. | +2 |
| Sentinel | Stopping Strike | On hit, target's remaining movement becomes 0. | +2 |
| Sweep | Wide Sweep | Hit up to 3 targets instead of 2. | +2 |
| Sweep | Trip Sweep | On hit, each target rolls `2d10 + Body` vs. DC 12 or falls prone. | +2 |
| Keep at Bay | Forceful Push | Push 2 spaces instead of 1. | +1 |
| Keep at Bay | Punishing Distance | If pushed target moves back toward you on their turn, make a free attack as a Reaction. | +2 |
| Impale | Lifting Impale | Impaled target is lifted off the ground. Cannot use movement abilities. Attacks against them have +2 to hit. | +2 |
| Impale | Shared Impale | Impale passes through to a second target behind the first. Both Restrained. | +4 |
| Phalanx | Reinforced Phalanx | With two adjacent Reach allies, bonus increases to +3 AC. | +1 |
| Phalanx | Offensive Phalanx | While in Phalanx, your attacks deal +1d4 damage. | +1 |

#### Reach Weapons

| # | Weapon | Complexity | Base Damage | Properties |
|---|---|---|---|---|
| 19 | Spear | Standard | 1d8 | Reach, Versatile (1d10), Thrown (30 ft) |
| 20 | Halberd | Standard | 1d10 | Reach, Two-Handed, Heavy |
| 21 | Scythe | Complex | 1d10 | Reach, Two-Handed, Sweeping |
| 22 | Whip | Standard | 1d4 | Reach (3 spaces), Finesse, Disarm |
| 23 | Staff | Standard | 1d6 | Reach, Two-Handed, Defensive (+1 AC), Arcane |
| 24 | Trident | Standard | 1d8 | Reach, Thrown (20 ft), Pierce |
| 25 | Chain | Complex | 1d8 | Reach (2 spaces), Two-Handed, Entangle |

**Staff and the Arcane property.** Spells gain +1 range tier while holding a Staff. This is a bonus. Any character with Mana can cast any spell with any weapon or empty-handed. The Staff never gates casting.

#### Reach Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Spear | Bleed | — | Bleed ignores 1 Physical DR. Brace: charging targets take 3 Bleed stacks. |
| Halberd | Force | Bleed | Sweep applies Force on primary target and Bleed on secondary targets. |
| Scythe | Bleed | — | Purge stacks from allies. On kill, transfer stacks to an adjacent enemy. |
| Whip | Bleed | — | Apply Bleed at 3-space range. Rank 3: pull a Bleeding target toward you. |
| Staff | Force | — | Force stacks catalyze elemental stacks (extra tick on hit against targets with active elemental stacks). Gish bridge weapon. |
| Trident | Bleed | — | Impaled targets: Bleed stacks do not decay. |
| Chain | Force | — | Entangled targets gain 1 Force stack per turn (constricting). |

#### Spear (Standard, Reach) — 8 Techniques

**Unique Mechanic: Deep Pierce.** All Bleed applied by Spear attacks ignores 1 Physical DR on tick damage. Defensive Reach weapon optimized for Shield pairing and formation fighting.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Brace | Reaction | When an enemy moves 2+ spaces toward you, make a free attack at reach. On hit, apply 3 Bleed stacks. |
| 1 | Measured Thrust | 1 Action | Attack at reach. On hit, apply 1 Bleed stack. If you did not move this turn, +2 to hit. |
| 2 | Javelin Toss | 1 Action, 3 Mana | Throw your Spear up to 30 ft. +1d8 damage. Apply 2 Bleed stacks on hit. Spear returns to your hand at end of turn. |
| 2 | Goading Thrust | 1 Action, 3 Mana | Attack at reach. On hit, apply 1 Bleed stack. Mark the target until your next turn. If the marked target moves away from you, make a free attack (no Reaction cost). |
| 3 | Hold the Line | Passive | While wielding a Shield, Brace triggers against any enemy entering your reach (no distance requirement). Brace attacks deal +1d6 damage. |
| 3 | Puncture | 1 Action, 5 Mana | Precision thrust. Ignores all Physical DR. On hit, apply 2 Bleed stacks. |
| 4 | Bloodletter | 1 Action, 8 Mana | Attack a Bleeding target. On hit, double the target's Bleed stacks (max 5). If target reaches 5 stacks, immediately trigger Shredded. |
| 5 | Heartstopper (Capstone) | 2 Actions, 12 Mana | Auto-hit. Apply 5 Bleed stacks. Target enters Shredded. Target rolls `2d10 + Body` vs. DC 16 or is Restrained for 1 round. Bleed from Heartstopper does not decay for 3 rounds. Once per long rest. |

##### Spear Weapon Augments (Deep Pierce)

Passive. Once learned, these apply to ALL Spear Techniques. Each adds its Mana cost to every Spear Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Formation Fighting | While an ally is within 2 spaces, Spear Techniques gain +2 to hit. | +0 |
| 2 | Pin Down | Spear Techniques that apply Bleed also reduce target movement by 1 space per Bleed stack active on them. | +1 |
| 3 | Thrown Mastery | After a thrown Spear Technique, the spear returns immediately (no end-of-turn wait). Thrown range +10 ft. | +1 |
| 4 | Vital Strike | Bleed from Spear Techniques ignores 1 additional Physical DR (2 total with Deep Pierce). | +2 |
| 5 | Lance Charge | If you moved 3+ spaces toward a target before using a Spear Technique, +1d8 Piercing damage. | +2 |

#### Halberd (Standard, Reach) — 8 Techniques

**Unique Mechanic: Cleaving Sweep.** Halberd Techniques that hit multiple targets split conditions: the primary target takes Force stacks, all secondary targets take Bleed stacks. Dual-condition zone controller.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Versatile Strike | 1 Action | Choose slash or thrust. Slash: 1d10 Slashing, apply 1 Bleed stack. Thrust: 1d10 Piercing, apply 1 Force stack. |
| 1 | Sweeping Arc | 1 Action, 3 Mana | Hit all enemies in a 2-space frontal arc. 1d8 damage each. Primary target takes 2 Force stacks. All secondary targets take 1 Bleed stack. |
| 2 | Area Denial | Reaction | When an enemy enters your 2-space reach, make a free attack. 1d10 damage. Apply 1 Force stack. |
| 2 | Haft Slam | 1 Action, 3 Mana | Bash with the haft. 1d8 Bludgeoning. Apply 2 Force stacks. Target rolls `2d10 + Body` vs. DC 13 or loses 1 space of movement next turn. |
| 3 | Cleaving Advance | 1 Action, 5 Mana | Move up to 2 spaces and sweep all enemies you pass. 1d10 damage each. Primary target takes 2 Force stacks, secondary targets take 2 Bleed stacks. |
| 3 | Rending Sweep | 1 Action, 5 Mana | Wide arc at 2-space reach. Hit up to 3 targets. 1d10 Slashing each. Primary takes 1 Force stack. Secondary targets take 2 Bleed stacks. If any secondary target already has Bleed, apply 1 additional Bleed stack. |
| 4 | Concussive Cleave | 1 Action, 8 Mana | Requires 3+ Force stacks on primary target or 3+ Bleed stacks on any secondary target. Massive sweep in a 2-space arc. 2d10 damage to all targets. Primary: trigger Staggered (T3 Force). Secondary: trigger Shredded (T3 Bleed). |
| 5 | Reaper's Arc (Capstone) | 2 Actions, 12 Mana | Hit all enemies within 2-space reach (full 360°). 3d10 damage each. Primary target takes 5 Force stacks and enters Staggered. All secondary targets take 5 Bleed stacks and enter Shredded. Once per long rest. |

##### Halberd Weapon Augments (Cleaving Sweep)

Passive. Once learned, these apply to ALL Halberd Techniques. Each adds its Mana cost to every Halberd Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Reach Advantage | Halberd Techniques gain +1 to hit against targets at exactly 2-space reach. | +0 |
| 2 | Splitting Edge | Sweeping Arc and Rending Sweep apply 1 additional Bleed stack to secondary targets. | +1 |
| 3 | Staggering Force | Force stacks from Halberd Techniques reduce target movement by 1 space per stack. | +1 |
| 4 | Dual Condition Mastery | When a Halberd Technique applies both Force and Bleed in one sweep, +1d6 damage to all targets hit. | +2 |
| 5 | Execution Sweep | Halberd Techniques deal +2d10 damage to targets that are Staggered or Shredded. | +2 |

#### Scythe (Complex, Reach) — 12 Techniques

**Unique Mechanic: Death's Harvest.** On kill with a Scythe Technique, transfer all remaining Bleed stacks from the dead target to one enemy within 2 spaces. Scythe has a unique Blood Purge Technique that removes Bleed from allies and heals them.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Reaping Cut | 1 Action | 1d10 Slashing. Apply 2 Bleed stacks. |
| 1 | Blood Purge | 1 Action, 3 Mana | Remove all Bleed stacks from one ally within 2 spaces. Heal that ally 1d6 per stack removed. |
| 1 | Harvest Step | Free Action | After killing a target with a Scythe Technique, move 1 space toward the nearest enemy. Does not provoke reactions. |
| 2 | Reaping Arc | 1 Action, 3 Mana | Sweep all enemies in a 2-space frontal arc. 1d8 Slashing each. Apply 1 Bleed stack per target. |
| 2 | Soul Harvest | Passive | On kill with a Scythe Technique, regain Mana equal to half the dead target's active Bleed stacks (round down, min 1). |
| 2 | Deep Laceration | 1 Action, 5 Mana | 1d10 Slashing. Apply 3 Bleed stacks. If the target already has Bleed, +1d6 damage. |
| 3 | Grim Harvest | 1 Action, 7 Mana | Strike all enemies in a 3-space line. 2d8 Slashing each. Apply 2 Bleed stacks per target. |
| 3 | Sanguine Scythe | 1 Action, 5 Mana | Attack a Bleeding target. 1d10 Slashing +1d6 per Bleed stack on target (max +5d6). |
| 3 | Chain Reap | Passive | When Death's Harvest transfers Bleed to an adjacent enemy, apply 1 additional Bleed stack to the new target. |
| 4 | Hemorrhaging Sweep | 1 Action, 8 Mana | Requires 3+ Bleed stacks on target. 2d10 Slashing. Trigger Shredded (T3 Bleed). Bleed damage doubles, target healing reduced by 50%. |
| 4 | Crimson Tide | 1 Action, 10 Mana | Hit up to 3 targets within reach. 2d8 Slashing each. Apply 3 Bleed stacks per target. On kill, Death's Harvest triggers for each killed target separately. |
| 5 | Exsanguination (Capstone) | 3 Actions, 15 Mana | Requires Shredded (T3 Bleed) on target. Trigger Exsanguination (T4 Bleed): Bleed stacks become permanent and auto-apply 1 additional stack each round. Target loses HP equal to total Bleed stacks ×3 per round. Once per long rest. |

##### Scythe Weapon Augments (Death's Harvest)

Passive. Once learned, these apply to ALL Scythe Techniques. Each adds its Mana cost to every Scythe Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Lingering Wounds | Bleed from Scythe Techniques lasts 1 additional round before decaying. | +0 |
| 2 | Blood Scent | Scythe Techniques gain +2 to hit against targets with 3+ Bleed stacks. | +1 |
| 3 | Harvest Chain | When Death's Harvest triggers, transfer Bleed to up to 2 enemies within 2 spaces (split stacks as you choose). | +1 |
| 4 | Crimson Mist | Blood Purge range increases to 4 spaces. Heal 2d6 per stack removed instead of 1d6. | +2 |
| 5 | Death's Embrace | Enemies killed by Scythe Techniques cannot be resurrected or healed from Dying for 1 minute. Soul Harvest restores double Mana. | +2 |

#### Whip (Standard, Reach) — 8 Techniques

**Unique Mechanic: Lashing Reach.** Whip has 3-space reach, the longest in the game. All Whip Techniques apply Bleed at this extreme range. At Rank 3, you unlock a pull mechanic for Bleeding targets.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Crack | 1 Action | 1d4 Slashing at 3-space reach. Apply 1 Bleed stack. If this is your first attack this turn, costs a Free Action instead. |
| 1 | Lash | 1 Action | 1d6 Slashing at 3-space reach. Apply 1 Bleed stack. +2 to hit against targets at exactly 3 spaces. |
| 2 | Entangle | 1 Action, 3 Mana | Wrap a target within 3 spaces. Target is Restrained. Target breaks free with `2d10 + Body` vs. DC 13 as 1 Action. |
| 2 | Lashing Fury | 1 Action, 5 Mana | Strike 3 times at 3-space reach. 1d4 Slashing each. Apply 1 Bleed stack per hit. |
| 3 | Yank | Free Action, 2 Mana | Pull a Bleeding target up to 2 spaces toward you. Target must be within 3 spaces. |
| 3 | Flaying Strike | 1 Action, 5 Mana | 1d8 Slashing at 3-space reach. Apply 2 Bleed stacks. If target has 3+ Bleed stacks, ignore Physical DR. |
| 4 | Hemorrhaging Lash | 1 Action, 8 Mana | Requires 3+ Bleed stacks on target. 2d8 Slashing at 3-space reach. Trigger Shredded (T3 Bleed). Bleed damage doubles, target healing reduced by 50%. |
| 5 | Scourge (Capstone) | 2 Actions, 12 Mana | Strike all enemies within 3-space reach. 2d8 Slashing each. Apply 5 Bleed stacks per target. All targets with 3+ Bleed are pulled 2 spaces toward you and enter Shredded. Once per long rest. |

##### Whip Weapon Augments (Lashing Reach)

Passive. Once learned, these apply to ALL Whip Techniques. Each adds its Mana cost to every Whip Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Extended Reach | Whip reach increases to 4 spaces. | +0 |
| 2 | Barbed Lash | Whip Techniques apply 1 additional Bleed stack when the target is at maximum reach distance. | +1 |
| 3 | Constricting Wrap | Restrained targets take 1 Bleed stack at the start of each of their turns. | +1 |
| 4 | Savage Crack | Crack deals 1d8 instead of 1d4. Lashing Fury strikes deal 1d6 instead of 1d4. | +2 |
| 5 | Bloodhook | Yank pulls targets 3 spaces instead of 2. Pulled targets take 1d6 Slashing damage on arrival. | +2 |

#### Staff (Standard, Reach) — 8 Techniques

**Unique Mechanic: Arcane Conduit.** Force stacks from Staff Techniques catalyze elemental stacks on the target. When you hit a target with active elemental stacks (Burn, Chill, Volt, Acid, Poison), each Force stack triggers one additional elemental tick. Primary gish (melee + magic hybrid) weapon.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Arcane Strike | 1 Action | 1d8 Bludgeoning. Apply 1 Force stack. If the target has any elemental stacks, trigger 1 elemental tick. |
| 1 | Channel | Free Action | Your next spell this turn gains +2 range (spaces). Costs no Mana. |
| 2 | Resonating Blow | 1 Action, 3 Mana | 1d8 Bludgeoning. Apply 2 Force stacks. Each Force stack triggers one elemental tick on the target. |
| 2 | Spell Weave | Free Action, 3 Mana | After casting a spell that deals elemental damage, strike one adjacent target. 1d6 Bludgeoning. Apply 1 Force stack. |
| 3 | Elemental Burst | 1 Action, 5 Mana | 1d10 Bludgeoning at 2-space reach. Apply 2 Force stacks. All elemental stacks on the target tick simultaneously. |
| 3 | Arcane Ward | Reaction, 5 Mana | When hit by a spell, reduce damage by `2d10 + Magic`. Apply 1 Force stack to the caster if within reach. |
| 4 | Catalytic Overload | 1 Action, 8 Mana | Requires 3+ Force stacks on target and at least 1 elemental stack. 2d10 Bludgeoning. Trigger Staggered (T3 Force). All elemental stacks on the target tick twice. |
| 5 | Arcane Cataclysm (Capstone) | 2 Actions, 15 Mana | All enemies within 2-space reach take 3d10 Force damage. Apply 3 Force stacks each. All elemental stacks on each target tick 3 times. Targets with 3+ active elemental types enter Staggered. Once per long rest. |

##### Staff Weapon Augments (Arcane Conduit)

Passive. Once learned, these apply to ALL Staff Techniques. Each adds its Mana cost to every Staff Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Spell Focus | While wielding a Staff, your spells deal +1 damage per die rolled. | +0 |
| 2 | Conduit Mastery | Arcane Conduit elemental ticks deal +1 damage each. | +1 |
| 3 | Mana Flow | When a Staff Technique triggers 3+ elemental ticks in one hit, regain 2 Mana. | +0 |
| 4 | Elemental Infusion | Staff Techniques inherit the element type of the highest active stack on the target. Damage type changes to match. | +2 |
| 5 | Arcane Overcharge | Force stacks from Staff Techniques trigger 1 additional elemental tick beyond normal (Arcane Strike triggers 2, Resonating Blow triggers 3 per stack). | +2 |

#### Trident (Standard, Reach) — 8 Techniques

**Unique Mechanic: Impaling Tines.** Trident has an Impale Technique that pins a target. While impaled, Bleed stacks do not decay naturally. Sustained Bleed pressure against pinned targets.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Pronged Thrust | 1 Action | 1d8 Piercing at reach. Apply 1 Bleed stack. |
| 1 | Tidal Strike | 1 Action | 1d8 Piercing at reach. Apply 1 Bleed stack. If the target is adjacent to water or is prone, +1d6 damage. |
| 2 | Impale | 1 Action, 3 Mana | Pin a target at reach. 1d8 Piercing. Apply 2 Bleed stacks. Target is Impaled: Bleed stacks do not decay until the target breaks free (`2d10 + Body` vs. DC 13, 1 Action) or you release them. |
| 2 | Barbed Toss | 1 Action, 3 Mana | Throw your Trident up to 30 ft. 1d10 Piercing. Apply 2 Bleed stacks. Trident remains in the target until you spend a Free Action to recall it on your next turn. |
| 3 | Twist the Tines | 1 Action, 5 Mana | Requires Impaled target. 1d10 Piercing. Apply 2 additional Bleed stacks. Bleed on this target ticks twice this round. |
| 3 | Pinning Thrust | 1 Action, 5 Mana | 1d10 Piercing at reach. Apply 2 Bleed stacks. Target rolls `2d10 + Body` vs. DC 14 or movement becomes 0 for 1 round. |
| 4 | Hemorrhaging Impale | 1 Action, 8 Mana | Requires 3+ Bleed stacks on target. 2d10 Piercing. Trigger Shredded (T3 Bleed). If target is Impaled, Shredded persists until the Impale ends. |
| 5 | Neptune's Judgment (Capstone) | 2 Actions, 12 Mana | Auto-hit a target within reach. Apply 5 Bleed stacks. Target is Impaled and enters Shredded. Bleed stacks on this target tick 3 times per round for 3 rounds. Once per long rest. |

##### Trident Weapon Augments (Impaling Tines)

Passive. Once learned, these apply to ALL Trident Techniques. Each adds its Mana cost to every Trident Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Barbed Prongs | Bleed from Trident Techniques requires +2 to the DC to remove via mundane healing. | +0 |
| 2 | Deep Impale | Impaled targets take 1d4 Piercing at the start of each of their turns. | +1 |
| 3 | Trident Recall | Recalling a thrown Trident deals 1d6 Piercing to the target on exit. Apply 1 Bleed stack. | +1 |
| 4 | Relentless Bleed | Bleed from Trident Techniques ignores 2 Magic DR on tick damage. | +2 |
| 5 | Executioner's Pin | Trident Techniques deal +2d10 damage to Impaled targets at or below half HP. | +2 |

#### Chain (Complex, Reach) — 12 Techniques

**Unique Mechanic: Constriction.** Chain Techniques that Entangle or Restrain a target apply 1 Force stack per turn automatically. The target escalates toward Staggered without additional attacks. Zone control with passive Force buildup.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Lashing Chain | 1 Action | 1d8 Bludgeoning at 2-space reach. Apply 1 Force stack. |
| 1 | Iron Bind | 1 Action, 2 Mana | Wrap a target within 2 spaces. Target is Entangled. Target escapes with `2d10 + Body` vs. DC 13 as 1 Action. While Entangled, Constriction applies 1 Force stack per turn. |
| 1 | Chain Sweep | 1 Action | Sweep chain in a 2-space arc. 1d6 Bludgeoning to all enemies in the arc. Apply 1 Force stack each. |
| 2 | Whirling Chains | 1 Action, 5 Mana | Hit all enemies within a 2-space radius. 1d8 Bludgeoning each. Apply 1 Force stack per target. |
| 2 | Iron Grip | Passive | Enemies escaping your Entangle roll at -2. On a failed escape, apply 1 additional Force stack. |
| 2 | Drag | 1 Action, 3 Mana | Pull an Entangled target up to 3 spaces toward you. 1d6 Bludgeoning on arrival. Apply 1 Force stack. |
| 3 | Constricting Bind | 1 Action, 5 Mana | Tighten chains on an Entangled target. Target is now Restrained. Constriction applies 2 Force stacks per turn instead of 1 while Restrained. |
| 3 | Chain Barrier | 1 Action, 5 Mana | Create a chain wall across a 3-space line. Lasts 2 rounds. Enemies crossing the wall take 1d8 Bludgeoning and gain 1 Force stack. |
| 3 | Flailing Strike | 1 Action, 7 Mana | 2d8 Bludgeoning at 2-space reach. Apply 2 Force stacks. If the target is Entangled, +1d8 damage. |
| 4 | Crushing Chains | 1 Action, 8 Mana | Requires 3+ Force stacks on target. 2d10 Bludgeoning. Trigger Staggered (T3 Force). Target's Actions are halved (round down). |
| 4 | Chain Cocoon | 1 Action, 10 Mana | Requires Restrained target. Fully encase the target. Target cannot take Actions or move for 2 rounds. Constriction applies 2 Force stacks per turn. Escape DC increases to 18. |
| 5 | Cascade Failure (Capstone) | 3 Actions, 15 Mana | Requires Staggered (T3 Force) on target. Trigger Cascade Failure (T4 Force): target's Force stacks explode outward. All enemies within 2 spaces gain half the target's Force stacks (round down, min 1) and take 2d10 Bludgeoning. Enemies reaching 3+ Force stacks from this effect enter Staggered. Once per long rest. |

##### Chain Weapon Augments (Constriction)

Passive. Once learned, these apply to ALL Chain Techniques. Each adds its Mana cost to every Chain Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Heavy Links | Force stacks from Chain Techniques reduce target movement by 1 space per stack. | +0 |
| 2 | Tightening Grip | Constriction deals 1d4 Bludgeoning per Force stack each time it triggers. | +1 |
| 3 | Chain Web | Entangling a target adjacent to another enemy applies 1 Force stack to that enemy. | +1 |
| 4 | Relentless Bind | Entangled targets cannot use Reactions. Restrained targets cannot use Reactions or Free Actions. | +2 |
| 5 | Shatter Chains | When Cascade Failure triggers, re-Entangle the primary target as a Free Action. Chain fragments deal 1d6 Bludgeoning to all affected enemies. | +2 |

---

### Ranged

Projectile weapons. Ranged favors kiting, precision, and area denial. You attack from safety, but ammunition and Action costs limit sustained fire.

#### Ranged Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Aimed Shot | 2 Actions | Spend 1 extra Action aiming. Advantage and +2 to hit. |
| 1 | Quick Shot | 1 Action | Ranged attack at -1 die size on damage. |
| 2 | Suppressing Fire | 2 Actions | Target a 2-space area. All enemies in the area have disadvantage on attacks until your next turn. |
| 2 | Volley | 2 Actions | Attack up to 3 targets. Roll separately for each. |
| 3 | Kill Shot | 2 Actions | If the target hasn't moved since your last turn, double damage. |

#### Ranged Category Technique Augments

| Technique | Augment | Effect | Mana Cost |
|---|---|---|---|
| Aimed Shot | Precision Aim | +4 to hit instead of +2. | +2 |
| Aimed Shot | Headshot | On hit, target has disadvantage on their next attack. | +2 |
| Quick Shot | Rapid Fire | Make 2 Quick Shots in one Action at -2 to hit each. | +3 |
| Quick Shot | Snap Accuracy | Remove the -1 die size penalty. Full damage, fast shot. | +2 |
| Suppressing Fire | Extended Suppression | Area increases to 3 spaces. Duration extends to 2 rounds. | +3 |
| Suppressing Fire | Psychological Pressure | Enemies in the area roll `2d10 + Social` vs. DC 12 or Frightened until they leave. | +2 |
| Volley | Storm Volley | Attack 5 targets instead of 3. | +3 |
| Volley | Focused Volley | All 3 attacks target the same enemy. Concentrated burst. | +2 |
| Kill Shot | Patient Kill Shot | If you haven't moved for 2 rounds, triple damage instead of double. | +2 |
| Kill Shot | Kill Zone | Kill Shot applies to any target within a 2-space area you designate. | +3 |

#### Ranged Weapons

| # | Weapon | Complexity | Base Damage | Range | Properties |
|---|---|---|---|---|---|
| 26 | Bow | Complex | 1d8 | 60 ft | Two-Handed, Ammunition |
| 27 | Crossbow | Standard | 1d10 | 80 ft | Two-Handed, Ammunition, Loading, Pierce |
| 28 | Hand Crossbow | Standard | 1d6 | 30 ft | Light, Ammunition, Loading |
| 29 | Bomb Flask | Standard | 2d4 | 30 ft | Thrown, AoE (2-space radius), Consumable |

**Crossbow and Loading.** The Crossbow requires 1 Action to reload after each shot. Higher Mastery ranks unlock Techniques that reduce or bypass reload time.

#### Ranged Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Bow | Varies | — | Condition changes by Technique. Elemental Arrow: Burn/Chill/Shock/Corrode. Base attacks: Bleed. |
| Crossbow | Bleed | — | Deep Penetration: Bleed ignores 2 Physical DR (Pierce extends to Bleed). |
| Hand Crossbow | Poison | — | Every hit applies 1 Poison. Rapid-fire rushes Venomous. Rank 3: 2 Poison per hit. |
| Bomb Flask | Varies | — | AoE stacks: Fire Flask = Burn, Acid Flask = Acid, Frost Flask = Chill. Area denial condition weapon. |

#### Bow (Complex, Ranged) — 12 Techniques

**Unique Mechanic: Draw.** Extra Actions spent drawing before firing increase power. Quick Shot = 0 Draw. Standard attack = 1 Draw. Full Draw = 2 Draw.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Power Shot | 2 Actions (1 Action + 1 Draw) | +1d8 damage. |
| 1 | Snap Shot | 1 Action (0 Draw) | Quick shot at -2 to hit. Allows 3 attacks per turn. |
| 1 | Pin Down | 1 Action | On hit, target's movement halved next turn. |
| 2 | Rain of Arrows | 2 Actions, 5 Mana | 3-space area. All creatures in the area take 1d8 (roll vs. each AC). |
| 2 | Trick Shot | 1 Action, 3 Mana | Shoot a specific object (rope, chandelier, weapon strap). Auto-hit objects. |
| 2 | Hunter's Mark | 1 Action, 3 Mana | Mark a target. All your ranged attacks vs. that target gain +2 to hit for the rest of combat. |
| 3 | Multishot | 1 Action, 5 Mana | Fire 3 arrows at up to 3 targets. Roll each separately. |
| 3 | Elemental Arrow | 1 Action, 5 Mana | Imbue an arrow with Burn, Chill, Shock, or Corrode. On hit, apply 2 stacks. |
| 3 | Perfect Draw | Passive | Full Draw attacks deal +2d8 damage instead of +1d8. |
| 4 | Arrow Storm | 3 Actions, 10 Mana | 5-space line. All creatures in the line take 2d8 damage. Once per combat. |
| 4 | Thread the Needle | 1 Action, 5 Mana | Ignores cover, Shield bonuses, and 50% of target's DR. |
| 5 | Deadeye (Capstone) | 2 Actions, 15 Mana | Auto-hit, auto-crit. Target rolls `2d10 + Body` vs. DC 18 or takes +3d8 damage. Once per long rest. |

##### Bow Weapon Augments (Draw)

Passive. Once learned, these apply to ALL Bow Techniques. Each adds its Mana cost to every Bow Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Power Draw | Full Draw attacks (2+ Actions aiming) deal +2d8 instead of +1d8. Stacks with Perfect Draw passive (+3d8 total). | +2 |
| 2 | Rapid Nock | After using a Bow Technique, your next Bow Technique this turn costs 1 less Action (minimum 1). Once per turn. | +2 |
| 3 | Pinning Shot | Bow Techniques that hit a target within 1 space of a wall or solid object pin them (Restrained until they spend 1 Action to pull the arrow free). | +2 |
| 4 | Windage | Bow Techniques ignore cover penalties (half cover and three-quarter cover). | +1 |
| 5 | Arrow Recovery | After combat, recover 50% of spent ammunition (round down). | +0 |

#### Crossbow (Standard, Ranged) — 8 Techniques

**Unique Mechanic: Deep Penetration.** Bleed ticks from Crossbow Techniques ignore 2 Physical DR. The Crossbow requires 1 Action to reload after each shot (Loading). Higher-rank Techniques reduce or bypass reload time.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Piercing Bolt | 1 Action | 1d10 Piercing. Apply 1 Bleed stack. |
| 1 | Steady Shot | 2 Actions (includes reload) | If you haven't moved this turn, +4 to hit. 1d10 Piercing. Apply 1 Bleed stack. |
| 2 | Quick Reload | Passive | Reload costs 0 Actions once per turn. You can fire and reload without spending an extra Action. |
| 2 | Barbed Bolt | 1 Action, 3 Mana | 1d10 Piercing. Apply 2 Bleed stacks. Bleed from Barbed Bolt lasts 3 rounds instead of 2. |
| 3 | Hemorrhaging Shot | 1 Action, 5 Mana | Requires Bleeding target. 2d10 Piercing. Double the target's Bleed stacks (max 5). If target reaches 5 stacks, trigger Shredded. |
| 3 | Armor Breaker | 1 Action, 5 Mana | Ignores all Physical DR. 1d10 Piercing. Apply 2 Bleed stacks. |
| 4 | Hemorrhage | 1 Action, 8 Mana | Requires Shredded (T2 Bleed) on target. Bleed damage doubles for 3 rounds. Target's healing received reduced by 50% for the duration. |
| 5 | Deathmark (Capstone) | 2 Actions, 15 Mana | Auto-hit. Apply 5 Bleed stacks. Target enters Shredded. Bleed ticks ignore all Physical DR for 3 rounds. Target rolls `2d10 + Body` vs. DC 16 or Stunned for 1 round. Once per long rest. |

##### Crossbow Weapon Augments (Deep Penetration)

Passive. Once learned, these apply to ALL Crossbow Techniques. Each adds its Mana cost to every Crossbow Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Heavy Draw | Crossbow Techniques deal +1d10 damage against targets 40 ft or farther away. | +2 |
| 2 | Serrated Bolts | Bleed applied by Crossbow Techniques deals +1 per tick. | +2 |
| 3 | Bipod Rest | While you haven't moved this turn, Crossbow Techniques gain +2 to hit. Stacks with Steady Shot. | +1 |
| 4 | Bleed Through | Deep Penetration ignores 3 Physical DR instead of 2 on Bleed ticks. | +2 |
| 5 | Bolt Recovery | After combat, recover 50% of spent Crossbow ammunition (round down). | +0 |

#### Hand Crossbow (Standard, Ranged) — 8 Techniques

**Unique Mechanic: Toxic Bolts.** Every damaging Hand Crossbow Technique applies 1 Poison stack. At Mastery Rank 3, every damaging Hand Crossbow Technique applies 2 Poison stacks instead. Rapid-fire platform designed to rush Venomous (5 Poison stacks).

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Venom Shot | 1 Action | 1d6 Piercing. Apply 1 Poison stack (Toxic Bolts). |
| 1 | Rapid Volley | 2 Actions | Fire twice. 1d6 Piercing each hit. Apply 1 Poison stack per hit. Reloads between shots automatically. |
| 2 | Quick Load | Passive | Hand Crossbow reload costs 0 Actions once per turn. |
| 2 | Weakening Bolt | 1 Action, 3 Mana | 1d6 Piercing. Apply 1 Poison stack. Target's next attack deals -2 damage. |
| 3 | Concentrated Toxin | Passive | Upgrades Toxic Bolts. All damaging Hand Crossbow Techniques apply 2 Poison stacks instead of 1. |
| 3 | Barrage | 1 Action, 5 Mana | Fire 3 bolts at up to 3 targets within 30 ft. 1d6 Piercing each. Apply Poison stacks per hit (Toxic Bolts). |
| 4 | Neurotoxin | 1 Action, 8 Mana | Requires Venomous (5 Poison stacks) on target. Target's movement becomes 0. Poison damage doubles each round. Lasts 3 rounds. |
| 5 | Lethal Dose (Capstone) | 1 Action, 15 Mana | Requires Neurotoxin on target. Poison stacks jump to 35. Target permanently loses 1 Action per turn. Once per long rest. |

##### Hand Crossbow Weapon Augments (Toxic Bolts)

Passive. Once learned, these apply to ALL Hand Crossbow Techniques. Each adds its Mana cost to every Hand Crossbow Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Dual Wield | When wielding two Hand Crossbows, fire both with a single Technique. Second shot deals half damage. | +3 |
| 2 | Rapid Toxin | Poison stacks from Hand Crossbow Techniques deal +1 per tick. | +2 |
| 3 | Crippling Venom | Targets with 3+ Poison stacks from your Hand Crossbow have -2 to all attacks. | +2 |
| 4 | Coated Bolts | First Hand Crossbow Technique each combat applies 2 extra Poison stacks. | +0 |
| 5 | Bolt Recovery | After combat, recover 50% of spent Hand Crossbow ammunition (round down). | +0 |

#### Bomb Flask (Standard, Ranged) — 8 Techniques

**Unique Mechanic: Volatile Mixture.** Bomb Flasks are consumable thrown weapons. Each Technique specifies which flask type to use: Fire Flask (Burn), Acid Flask (Acid/Corrode), Frost Flask (Chill). Each use consumes a flask. Flasks must be crafted or purchased.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Fire Flask | 1 Action | 2-space AoE. 2d4 Fire. Apply 2 Burn stacks to all targets. Area burns for 2 rounds (creatures entering take 1d4 Fire). Consumes 1 Fire Flask. |
| 1 | Frost Flask | 1 Action | 2-space AoE. 2d4 Cold. Apply 2 Chill stacks to all targets. Area becomes difficult terrain for 2 rounds. Consumes 1 Frost Flask. |
| 2 | Acid Flask | 1 Action, 3 Mana | 2-space AoE. 2d4 Acid. Apply 2 Acid stacks to all targets. Reduce targets' Physical DR by 1 for 2 rounds. Consumes 1 Acid Flask. |
| 2 | Sticky Bomb | 1 Action, 3 Mana | Attach a flask to a single target (vs. Physical AC). 2d4 damage matching flask type. Apply 2 stacks of that condition. Stacks last 3 rounds instead of 2. Consumes 1 flask. |
| 3 | Combining Flasks | 2 Actions, 8 Mana | Throw 2 different flasks at the same 2-space area. Combined effect: Fire+Frost = Steam Cloud (Blinded, 2 rounds). Fire+Acid = Explosion (double damage). Acid+Frost = Brittle (double DR reduction). Consumes 2 flasks. |
| 3 | Cluster Toss | 1 Action, 5 Mana | Throw 2 flasks of the same type. 3-space AoE. 3d4 damage. Apply 3 stacks of that condition. Consumes 2 flasks. |
| 4 | Volatile Eruption | 2 Actions, 8 Mana | Requires 5+ Burn, Chill, or Acid stacks on target. Trigger matching T3 escalation: Ignited (no healing), Frozen (movement 0, 1 Action to break free), or Corroded (DR reduced to 0 for 3 rounds). 2-space AoE centered on target applies 2 stacks to all other creatures in the area. Consumes 1 matching flask. |
| 5 | Inferno (Capstone) | 3 Actions, 12 Mana | Throw 3 Fire Flasks. 3-space AoE. 4d4 Fire. Apply 4 Burn stacks. Area burns for 3 rounds. All targets with Burn stacks trigger Ignited. Once per long rest. Consumes 3 Fire Flasks. |

##### Bomb Flask Weapon Augments (Volatile Mixture)

Passive. Once learned, these apply to ALL Bomb Flask Techniques. Each adds its Mana cost to every Bomb Flask Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Expanded Blast | Bomb Flask AoE radius increases by 1 space. | +2 |
| 2 | Lingering Residue | Bomb Flask area effects (burning ground, difficult terrain, DR reduction) last 1 additional round. | +2 |
| 3 | Efficient Mixture | Once per combat, a Bomb Flask Technique does not consume a flask. | +0 |
| 4 | Concentrated Formula | Bomb Flask Techniques apply 1 additional stack of their condition type. | +2 |
| 5 | Flask Recovery | After combat, recover 1 flask of each type you used (max 3 total). | +0 |

---

### Firearms

Mechanical ranged weapons. Firearms deal high damage per shot but are limited by ammunition and reload requirements.

#### Firearms Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Fan the Hammer | 1 Action | Fire twice in one Action. Half damage each. Revolver and Hand Crossbow only. |
| 1 | Steady Aim | Passive | If you haven't moved this turn, +2 to hit on all ranged attacks. |
| 2 | Covering Fire | 1 Action | Choose an ally. Until your next turn, if an enemy attacks that ally, you may fire at the attacker as a Reaction. |
| 2 | Penetrating Round | 1 Action | Ignores all Physical DR. Costs 2 ammunition. |
| 3 | Dead Eye | 3 Actions | Auto-hit, maximum damage. Once per combat. |

#### Firearms Category Technique Augments

| Technique | Augment | Effect | Mana Cost |
|---|---|---|---|
| Fan the Hammer | Full Fan | Fire 4 times at half damage instead of 2. | +3 |
| Fan the Hammer | Aimed Fan | First shot deals full damage instead of half. | +2 |
| Steady Aim | Dead Calm | Bonus increases to +4 if you haven't moved for 2 consecutive rounds. | +1 |
| Steady Aim | Prone Aim | While prone, +2 additional to hit on ranged attacks. | +0 |
| Covering Fire | Suppressive Cover | Cover applies to 2 allies instead of 1. | +2 |
| Covering Fire | Warning Shots | Enemies who attack the covered ally have disadvantage. | +2 |
| Penetrating Round | Overcharged Round | Also ignores Magic DR. True damage round. | +3 |
| Penetrating Round | Through-and-Through | Projectile continues through the target. One enemy behind takes half damage. | +2 |
| Dead Eye | Double Tap | Fire twice. Both auto-hit at maximum damage. 2x ammunition. | +5 |
| Dead Eye | Calm Before the Storm | Dead Eye doesn't consume your Reaction for the round. | +1 |

#### Firearms Weapons

| # | Weapon | Complexity | Base Damage | Range | Properties |
|---|---|---|---|---|---|
| 30 | Revolver | Standard | 1d8 | 40 ft | Light, Ammunition (6), Reload |
| 31 | Rifle | Standard | 1d10 | 80 ft | Two-Handed, Ammunition (8), Reload |
| 32 | Shotgun | Standard | 2d6 | 20 ft | Two-Handed, Ammunition (2), Reload, Spread |

#### Firearms Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Revolver | Force | — | Each shot applies 1 Force stack. Fan the Hammer applies 2 Force in one Action. |
| Rifle | Bleed | Force | Standard shots apply Bleed. Penetrating Round applies Force. Switch by Technique. |
| Shotgun | Force | — | Point-blank: 2 Force stacks. Maximum range: 1 Force stack. Spread: 1 Force to adjacent targets. |

#### Revolver (Standard, Firearms)

TODO: full Technique list. Condition signature: Force. Unique mechanic: Fan the Hammer for rapid Force stacking. 6-round cylinder with Reload. Light property allows dual-wielding.

#### Rifle (Standard, Firearms)

TODO: full Technique list. Condition signature: Bleed/Force. Unique mechanic: Condition switches by Technique. Standard shots = Bleed. Penetrating Round = Force. Long range and high per-shot damage.

#### Shotgun (Standard, Firearms)

TODO: full Technique list. Condition signature: Force. Unique mechanic: Spread property. Point-blank shots deal bonus damage and apply 2 Force stacks. Close-range area pressure weapon.

---

### Condition Escalation and Techniques

Weapon Techniques interact with the condition stack system. Every condition follows the same pipeline: apply stacks → reach 5 stacks → trigger T2 escalation. Weapon Techniques extend this pipeline into T3 and T4.

#### Escalation Pipeline

1. **Stacks (T1).** Apply condition stacks through weapon hits and Techniques. Each stack deals +1 damage per round.
2. **T2 Escalation.** At 5 stacks, the condition escalates automatically. Bleed → Shredded. Force → Staggered. Burn → Ignited. Chill → Frozen. Shock → Shocked. Acid → Corroded. Poison → Venomous.
3. **T3 Enhancement.** Requires a T2 escalated condition active on the target. Costs 12 Mana. Accessed through Rank 3–4 Weapon Techniques.
4. **T4 Ultimate.** Requires a T3 enhancement active on the target. Costs 17 Mana. Once per long rest. Accessed through Rank 5 Capstone Weapon Techniques.

#### T3 Enhanced Escalations

T3 enhancements require the T2 escalated condition already active on the target. Weapon Techniques at Rank 3–4 deliver these. Spellcasters can cast T3 effects directly for 12 Mana.

| T3 Enhancement | Requires | Effect | Weapon Access |
|---|---|---|---|
| Hemorrhage | Shredded (Bleed 5) | Bleed doubles to 2 per stack per tick. Healing 50% effective. Shredded persists 2 extra rounds after Purge. | Scythe, Great Axe, Claw Gauntlet, Katana |
| Shattered | Staggered (Force 5) | Physical DR = 0 for 2 rounds. Physical attacks auto-apply 1 Bleed. | Greathammer, Mace, Greatclub, Flail |
| Immolation | Ignited (Burn 5) | Burn spreads: 1 Burn stack to all within 1 space each round. Double Burn tick damage. | Bow (Elemental Arrow), Bomb Flask (Fire), Condition: Burn Augment |
| Permafrost | Frozen (Chill 5) | Target re-freezes at end of turn for 2 rounds. Physical damage vs. Frozen target: +1d8. | Staff (gish), Condition: Chill Augment |
| Overload | Shocked (Volt 5) | Arc: 1 Volt stack per round to all within 2 spaces. Target loses Reaction for the rest of combat. | Chain, Whip, Condition: Shock Augment |
| Dissolution | Corroded (Acid 5) | Weapon or shield degrades: weapon loses 1 die size, shield loses 1 AC. At 0, the item breaks. | War Pick, Sickle, Bomb Flask (Acid) |
| Neurotoxin | Venomous (Poison 5+) | Target's movement = 0. Poison accelerates at 5 stacks instead of 10. | Dagger, Hand Crossbow |

#### T4 Ultimate Escalations

T4 ultimates require the T3 enhancement already active on the target. These cost 17 Mana, are once per long rest, and represent the pinnacle of a weapon's Mastery track.

| T4 Ultimate | Requires | Effect | Weapon Capstone |
|---|---|---|---|
| Exsanguination | Hemorrhage | Target rolls `2d10 + Body` vs. DC 18 or enters Dying regardless of current HP. On success: 4d10 Bleed damage. | Scythe, Great Axe |
| Obliterate | Shattered | Weapon damage × 4. Kill = target cannot be resurrected. Boss: damage × 3, boss loses 1 action permanently. | Greathammer |
| Detonation | Immolation | Target explodes: 4d12 fire damage to all within 3 spaces. Kill. Boss: 4d12 damage + Ignited for 3 rounds. | Bomb Flask |
| Absolute Zero | Permafrost | Incapacitated for 2 rounds. All damage doubled during incapacitation. Boss: 1 round, damage × 1.5. | Staff (gish capstone) |
| Cascade Failure | Overload | 2d12 Lightning damage to all creatures with Volt stacks within 5 spaces. All become Shocked. Boss: Shocked for 2 rounds. | Chain |
| Total Dissolution | Dissolution | Armor destroyed (DR = 0, permanent). No armor: 4d10 Acid damage. Boss: DR -4 for rest of combat. | War Pick |
| Lethal Dose | Neurotoxin | Poison stacks jump to 35. Target loses 1 action permanently. Boss: stacks jump to 20, loses 1 action for 3 rounds. | Dagger |

#### Escalation Paths

Three paths reach T3 and T4. They combine freely.

| Path | How T3 | How T4 |
|---|---|---|
| Weapon Techniques | Build stacks over turns → T2 at 5 stacks → T3 Technique enhances | T3 active → T4 capstone Technique (once per long rest) |
| Spellcasting | Pay 12 Mana for T3 spell directly | Pay 17 Mana for T4 spell directly |
| Gish combo | Spells rush to T2 → weapon T3 Technique enhances | Either path to T3 → weapon T4 or spell T4 |

> **Example:** A Staff-wielding Hybrid casts Chill spells to reach Frozen (T2). On the next turn, the Hybrid uses a Staff Technique to apply Permafrost (T3, 12 Mana). The enemy re-freezes each round and takes +1d8 from physical attacks. Two turns later, the Hybrid triggers Absolute Zero (T4, 17 Mana), incapacitating the target for 2 rounds with all damage doubled.

---

### Magic Weapons

Magic weapons are rare, named items with innate properties. You find or earn them. They cannot be crafted through normal means.

| Tier | Innate Augments | Bonus Augment Slots | Unique Techniques | Rarity |
|---|---|---|---|---|
| Enchanted | 1 | +1 | 0 | Uncommon |
| Rare | 1 | +1 | 1 | Rare |
| Legendary | 2 | +2 | 2–3 | Legendary |

**Innate Augments** are permanently socketed into the weapon. They do not consume your Augment Slots.

**Bonus Augment Slots** add +1 or +2 Augment Slots to every Technique used with this weapon, stacking with Mastery-granted slots.

**Unique Techniques** are exclusive to the weapon. They cannot be learned any other way. They count toward your 10 prepared Technique limit.

**Elemental Attunement.** Some magic weapons carry an elemental attunement. All attacks with that weapon apply 1 stack of the attuned element.

> **Example:** A Legendary Greatsword might have Innate: Potency and Condition: Burn, +2 Augment Slots per Technique, and 2 Unique Techniques (a fire-enhanced Wide Sweep and a flame dash). The wielder applies Burn on every hit without spending Augment Slots, has 5 total Augment Slots per Technique at Mastery 5, and can prepare the 2 Unique Techniques alongside their standard choices.

---

### Gish Synergies

Spellcasting requires only Mana. No weapon, item, or property gates casting. Any character with Mana can cast any spell with any weapon equipped or empty-handed. Weapons grant bonuses but never act as prerequisites.

Five bridges connect weapon combat and spellcasting.

**Spell Strike.** The Spell Strike Augment bundles a Touch spell with a weapon attack. One roll resolves both. If you miss, the spell is not expended. Mana for the spell is paid separately from the Technique's Mana cost.

**Arcane Infusion.** The Arcane Infusion Augment rewards casting before attacking. After you cast a spell, your next Technique deals +1d8 elemental damage matching the spell's element.

**Stack Exploitation.** Spell stacks and Technique stacks share the same counter per condition type. A Burn spell adds to the same Burn counter as a Condition: Burn Augment or a weapon's innate Burn application. Gish characters cycle stacks faster than pure martials or pure casters.

**Action Economy Weaving.** You have 3 Actions per turn. Split them between Spells and Techniques in any combination. You are never locked into one mode. Cast a spell with Action 1, attack with Action 2, attack with Action 3.

**Mana Reave.** The Mana Reave Augment restores Mana on weapon hits equal to your weapon's base damage die. This enables sustained Technique use for Hybrid builds that would otherwise run dry.

---

### Mana Economy

Technique costs scale with power. Universal Techniques are free or cost 0–1 Mana. Rank 1 Techniques cost 0–3 Mana. Rank 3 Techniques cost 3–8 Mana. Rank 5 Capstones cost 10–15 Mana. Augments add their listed Mana cost on top.

| Background | HP | Mana | Regen/Round | Technique Budget (10-round combat) |
|---|---|---|---|---|
| Martial | 120 | 30 | 3 | ~10 Techniques at 3 Mana average |
| Hybrid | 110 | 70 | 10 | ~23 Techniques at 3 Mana average |
| Caster | 100 | 100 | 15 | Spells, not Techniques |

Martial characters rely on free Universal Techniques and low-cost Rank 1–2 weapon Techniques. Their 30 Mana reserves power a few high-impact Rank 3+ abilities per combat.

Hybrid characters weave Techniques and Spells. Their 70 Mana pool and 10 Mana regen per round sustain both Augmented Techniques and spell combos across a full fight.

Caster characters spend Mana on Spells. They use Universal Techniques and unaugmented weapon attacks for Action economy when Mana runs low.

---

### Build Examples

#### The Duelist (Rapier + Shield)

- **Mastery:** Rapier 4, Shield 2. Background: Martial.
- **Role:** Counter-fighting tank.
- **Core loop:** En Garde stance → Parry incoming attacks → generate Openings → Compound Riposte for bonus damage. Shield for Cover Ally and emergency Raise Shield.
- **Key Techniques:** En Garde, Parry (Medium Melee), Compound Riposte, Fleche, Tempo Rubato, Shield Bash, Cover Ally.
- **Weapon Augments (passive):** Riposte Mastery (2 Openings per Parry), Duelist's Grace (+1 AC at 2+ Openings), Tempo Control (-1 to hit per Opening spent).
- **Technique Augments (socketed):** Feint Chain (free Openings on Feinting Thrust hits), Bleeding Riposte (Bleed on Compound Riposte), Rising Thrust (attack after Passata Sotto).
- **Condition path:** Bleed through Rapier → Shredded at 5 stacks. Openings accelerate Bleed application.

#### The Berserker (Great Axe)

- **Mastery:** Great Axe 5. Background: Martial.
- **Role:** All offense. Rush in, AoE, execute.
- **Core loop:** Charge in → Power Attack → Cleave on kills → Executioner to finish wounded targets. Double Bleed ticks pressure everything.
- **Key Techniques:** Power Attack, Cleave, Whirlwind, Executioner, Staggering Blow.
- **Category Technique Augments:** Cascading Cleave (chain kills), Brutal Power Attack (+2 dice), Expanding Whirlwind (2-space radius).
- **Condition path:** Bleed at double tick rate → Shredded → Hemorrhage (T3) → Exsanguination (T4 capstone, once per long rest).

#### The Sentinel (Spear + Shield)

- **Mastery:** Spear 3, Shield 3. Background: Martial.
- **Role:** Pure tank and controller. Lock down movement, protect allies.
- **Core loop:** Sentinel (Reaction attacks on approach) → Impale to pin targets → Shield Wall with adjacent ally → Raise Shield for durability.
- **Key Techniques:** Sentinel, Sweep, Impale, Keep at Bay, Phalanx, Shield Bash, Raise Shield, Shield Wall.
- **Weapon Augments (passive):** Formation Fighting (+2 to hit near allies), Pin Down (Bleed slows movement), Shield Master (AC bonus to nearby allies).
- **Category Technique Augments:** Threatening Reach (Sentinel triggers within reach), Trip Sweep (prone on Sweep hits).
- **Condition path:** Bleed through Spear (ignores 1 Physical DR). Impaled targets do not lose Bleed to decay. Force through Shield Bash.

#### The Hybrid (Staff + Spellcasting)

- **Mastery:** Staff 3. Background: Hybrid (110 HP, 70 Mana, 10 regen).
- **Role:** Gish condition accelerator.
- **Core loop:** Cast Burn/Chill spells → Staff attacks catalyze elemental stacks (extra ticks) → push to T2 escalation → T3 enhancement Technique → T4 if fight goes long.
- **Key Techniques:** Staff weapon Techniques (TODO), Sentinel, Sweep. Spells: Burn/Chill/Shock varieties.
- **Universal Augments (socketed):** Condition: Burn (add stacks to Staff Techniques), Elemental Shift (change damage type on any Technique).
- **Spellblade Augments:** Arcane Infusion (+1d8 elemental after spell), Spell Strike (Touch spell + melee attack), Mana Reave (+3 Mana on Technique kills).
- **Condition path:** Spell stacks + Staff catalysis → Frozen (Chill T2) → Permafrost (T3, 12 Mana) → Absolute Zero (T4 capstone, 17 Mana, once per long rest).

#### The Assassin (Dagger + Hand Crossbow)

- **Mastery:** Dagger 4, Hand Crossbow 3. Background: Hybrid or Martial.
- **Role:** Dual-condition poison and bleed specialist. Ambush predator.
- **Core loop:** Open at range with Hand Crossbow → apply Poison stacks (1 per hit, 2 at Rank 3) → close to melee → Dagger Flurry for Bleed + Poison → double escalation (Shredded + Venomous). Against bosses: Neurotoxin (T3) + Hemorrhage (T3) for layered pressure.
- **Key Techniques:** Quick Draw, Flurry, Assassinate, Hand Crossbow Techniques (TODO). Quick Shot for ranged Poison, Flurry for melee combo.
- **Weapon Augments (passive):** Envenomed Blade (+1 Poison tick damage), Arterial Cut (mundane healing can't remove Dagger Bleed), Shadowstep (teleport on kill).
- **Category Technique Augments:** Triple Flurry (3rd attack), Vanishing Strike (stealth after Assassinate), Lethal Ambush (×3 damage).
- **Condition path:** Poison at range → Venomous (T2) → Neurotoxin (T3, movement = 0). Bleed in melee → Shredded (T2) → Hemorrhage (T3). Against bosses: stack both T3s, then Lethal Dose (T4 capstone, once per long rest).

### Full Augment Catalog

The book includes all Universal Augments and worked examples for Rapier and Katana (Weapon Augments + Technique Augments). The full catalog of all 32 weapons, their Weapon Augments, and all Technique Augments is available through the Solus character builder web app. TODO: web app URL.

## Magic and Spellcasting

Magic uses a spell framework instead of a fixed spell list. A caster builds each spell by filling out a full set of parameters. No field can stay empty.

A spell must define:

- Category
- Function
- Range
- Size
- Shape
- Duration
- Target Count
- Accuracy Type
- Effect Tier

Current spell categories are Elemental, Force, Mind or Psychological, Temporal, Creation or Transmutation, Order or Binding, Summoning, Life, Death, and Corruption or Chaos.

Current function costs are:

- Utility: +0
- Movement: +1
- Defensive: +1
- Offensive: +2

If a spell does more than one thing, add both function costs.

Current framework values are:

- Range: Self to 25 ft. (1), 30 to 60 ft. (2), 65 to 120 ft. (3), 125 to 200 ft. (4), Sight (5), Global (6)
- Size: 5 to 15 ft. (1), 20 to 30 ft. (2), 35 to 60 ft. (3)
- Shape: point or none (1), sphere/cube/line/wall/cylinder (2), freeform or custom (3)
- Duration: Instant (1), Round (2), Minute (3), Hours (4), Permanent (5)
- Target Count: Single (1), Multi (2+), AOE (3)
- Accuracy Type: Attack Roll (1), Save (1), Auto-Hit (4)
- Effect Tier: T1 (3), T2 (6), T3 (12), T4 (17)

Damage comes from three spell parameters: range, target count, and size. Each one contributes one damage die. Raising those parameters raises die size. Mixed dice are allowed. Attack roll spells can add one floating damage die, and the caster's casting stat always adds a flat bonus from -5 to +5.

Current die scaling by mana is:

- d6 for +1
- d8 for +2
- d10 for +3
- d12 for +5

Magic also uses a main and sub category model. Players choose their main and sub lists at character build. Main category spells pay normal cost. Sub category spells pay double cost.

Tags sit under the spell framework and define what an effect actually does. Tags are not spells. They are mechanical identifiers that any source can apply, including magic, weapons, potions, creature abilities, terrain, and hazards.

TODO: draft the full spellcasting chapter in final reader-facing form.

## Core Gameplay Loop

Play moves through a repeating loop.

1. The world presents a problem.
2. The players act based on that problem.
3. The system or the GM resolves consequences.
4. Rewards follow.
5. Characters adjust between sessions.
6. The next problem begins.

The world or the GM can present a conversational, combative, exploratory, puzzle-based, or timed problem. Players respond with the tools their characters have, including attributes, skills, equipment, and magic. Consequences can help or hurt them. Rewards can include XP, money, weapons, or other loot. Between sessions, players may replace skills, increase them, or leave them unchanged.

## Combat

Combat starts with initiative. Each character rolls a d10 and adds either Body or Magic, chosen by the player to match that character's fighting style. Combat runs from highest result to lowest.

If two or more combatants tie, break the tie in one of three ways.

- Compare the higher stat modifier.
- Roll another d10 between the tied combatants.
- Let players and allies act at the same time.

Enemies do not share a simultaneous turn and must use one of the first two tie-break methods.

Each combat round lasts 3 seconds.

### Actions

On your turn, you can take up to 3 actions in any order. Resolve each action before taking the next. You can repeat an action unless a specific ability, spell, or item says otherwise.

You can spend an action to:

- attack with a weapon
- use a Technique
- cast a spell
- move
- drink a potion
- interact with an object
- make a skill check
- use a skill

Techniques are active combat abilities tied to your equipped weapon. They cost 1 or more Actions and sometimes Mana. See Weapons, Techniques, and Augments for the full system.

Some spells, skills, and Techniques take more than one action. You can spend those actions on the same turn or across multiple turns unless something interrupts you.

### Reactions

Each character gets 1 reaction per round. That reaction refreshes at the start of that character's turn. Reactions can include skills, counterspells, parries, opportunity attacks, and other triggers written on abilities or equipment. Reactions may interrupt an action unless the effect says otherwise.

### Movement

Each movement action lets you move up to your full movement speed. You can split movement across actions unless a condition prevents it. If you leave an enemy's reach, that enemy may trigger a reaction if one is available. In most cases, that reaction is an opportunity attack.

### Damage And Defense

Armor damage reduction applies after a hit lands. Split physical and magical protection matter both for direct attacks and for ongoing elemental stack damage.

If a character reaches 0 HP, that character becomes incapacitated and follows the injury or death rules.

TODO: add the full attack, hit, save, and damage-resolution sequence once the combat core is finalized.

## Conditions, Injuries, and Death

Many conditions begin as stacks.

- A hit applies 1 stack of the relevant type.
- Each stack deals +1 damage per round, equal to the number of active stacks of that type.
- Each stack lasts 2 full rounds from the turn it was applied.
- Reapplying a stack resets that stack's duration.
- Each stack type tracks its own current count, damage per round, and decay.
- Most tracked elemental stacks cap at 5.
- Ongoing status effects resolve at the start of the affected creature's turn unless a rule says otherwise.
- Stack damage triggers when applied and again at the start of the target's turn.

Burn and Chilled oppose each other. When one would be gained, it removes one stack of the other on a 1:1 basis. Magic DR reduces damage from elemental stacks, but it does not block the stack itself or stop escalation into a higher condition.

The current tag system confirms these conditions and effects.

- Ignited: the target takes Burn each turn and cannot gain healing from any source while Ignited.
- Drown: the target loses its Reaction and must spend an Action to escape. Breath duration depends on Body.
- Frozen: movement becomes 0, and the target must spend an Action to break free.
- Shocked: the target has disadvantage on Actions and loses half its movement speed.
- Corroded: severe acid saturation weakens armor, eats through terrain, and can cause lasting bodily harm.
- Venomous: the target loses Actions as poison escalates through its thresholds.
- Stunned: the target has disadvantage on Actions and loses its Reaction.
- Restrained: the target's movement is physically limited or partly prevented.
- Crush: maintained pressure on a Restrained target that continues to apply Force stacks.
- Blind: the target loses visual perception while the effect lasts.

Several named conditions appear in weapon rules without a full general entry yet, including Poisoned, Anchored, Concussed, Weaken, and Frightened.

Life magic can reverse some of this damage.

- Restore repairs recent damage and stabilizes injuries that have not caused permanent loss.
- Regenerate restores lost body parts and reverses severe trauma while active.
- Rouse returns a recently deceased target to life if the body is intact and death was recent.
- Revive returns a long-dead target to life at extreme cost or risk.

Death effects also exist as tags.

- Pyroptosis causes the target to detonate with necrotic energy in a 5 ft. radius.
- Apoptosis causes immediate death.
- Reanimate restores temporary motion to lifeless matter.
- Vivify tethers spirit or essence to a vessel beyond natural death.

Madness also has a working threshold rule. At 100 Madness, a creature must use its Action to attack a random nearby target, cannot target itself, lasts `1d4 + 1` rounds in that state, and takes 1 psychic damage at the start of each turn. The condition can end early if time expires, a calming charm hits, an ally succeeds on the stated check against DC 15, magic removes Madness, or the target takes `5 + Vital` damage in one hit.

### Dying

When a character drops to 0 HP, set a death counter to `10 + Body modifier` (minimum 5, maximum 15). Place a die or token on that number. The counter only goes down. When it hits 0, the character dies.

A dying character can still act. Movement is halved. Attack rolls are at disadvantage. All active conditions (Burn stacks, Frozen, Venomous, etc.) continue to apply using their normal rules.

#### Each Turn While Dying

At the start of your turn, reduce the death counter by your total active stack damage after Magic DR. Then resolve your 3 action slots:

- Unused action slot: counter drops by 1.
- Used action slot: counter drops by 2.

If the counter hits 0 at any point during the turn, the character dies immediately.

A character with no active stacks who does nothing for a full turn loses 3 from the counter. A character who uses all 3 actions loses 6. A character with 2 net Burn damage (after DR) who does nothing loses 5.

#### Recovery

Healing that restores a dying character to 1 HP or more removes the dying state. The character then rolls once for consequences.

Roll `2d10 + Body` against DC `15 minus the death counter value at the time of healing`.

| Counter When Healed | Recovery DC |
| --- | --- |
| 10+ | 5 or less |
| 7-9 | 6-8 |
| 4-6 | 9-11 |
| 1-3 | 12-14 |

Apply the Degree of 5 outcome from the roll:

| Degree | Outcome |
| --- | --- |
| Beat DC by 10+ | Clean recovery. |
| Beat DC by 5-9 | Minor wound. Disadvantage on one action category (physical, magical, or social) until the next long rest. |
| Beat DC by 0-4 | Lingering injury. Persists until treated. |
| Miss DC by 1-5 | Serious injury. Roll twice on the Lingering Injury table. Both persist until treated. |
| Miss DC by 6+ | Grievous injury. Permanent scar, lost limb, or organ damage. Requires Regenerate or stronger magic to reverse. |

TODO: create the Lingering Injury table with specific entries.

#### Repeated Knockdowns

If a character leaves the dying state and drops to 0 HP again before 1 full round passes, the death counter resumes at its previous value instead of resetting.

If the character stays above 0 HP for 1 full round, the counter resets to `10 + Body` on the next knockdown.

Each recovery triggers its own consequence roll.

TODO: add a consolidated condition glossary with stack thresholds and removal rules.

## NPCs, Enemies, and Encounters

NPCs use a modified player-character stat block. The lower an NPC's rank, the less health, fewer actions, less power, and less equipment that NPC brings into play. A GM should run each NPC from a stat block built from one of the rank templates below.

NPCs sit inside the core play loop. They can cause problems in the world, keep those problems in motion, appear as consequences for player action, or hand out rewards after the group resolves a situation. Allies follow the same framework as enemies, but they help the characters instead of hindering them.

All NPCs use the same action economy, equipment, skill system, and spell system as player characters. Minions and Bosses break that baseline in specific ways.

| Rank | HP | Mana | Armor | Stat Modifiers | Use in Play |
| --- | --- | --- | --- | --- | --- |
| Minion | 1 to 5 | 30/3 | None, Phys 0, Magi 0 | Body +0, Mind +0, Social +0, Magic +0, Sanity +0 | Use Minions for swarms and hordes. One Minion is weak. A crowd of them becomes dangerous. |
| Regular | 75 | 30/3 | None, Phys 1, Magi 1 | Body +1, Mind +1, Social +1, Magic +1, Sanity +1 | Use Regular NPCs for townsfolk, shopkeepers, low-ranked guards, and other ordinary people. |
| Enemy or Ally | 100 | 100/15 | Medium, Phys 7, Magi -2 | Body +4, Mind +1, Social +3, Magic -3, Sanity +0 | Use this rank for the most common competent foe or helper. These NPCs should feel close to player characters in capability. |
| Mini Boss | 120 | 100/15 | Heavy, Phys 9, Magi 0 | Body +5, Mind +4, Social -3, Magic +0, Sanity -2 | Use a Mini Boss for a foe who stands above a player character in health, gear, and skill investment. |
| Boss | 175 | 100/20 | Enchanted, Phys 8, Magi 8 | Body +5, Mind +3, Social +0, Magic +5, Sanity -5 | Use a Boss for a major threat that demands planning and strong tactics. |

Minions break the normal NPC baseline on the low end. They always have +0 in every stat. They die fast, deal little damage, and work best in numbers.

Regular NPCs represent average people. They are sturdier than Minions, but they do not stand on equal footing with player characters.

Enemy and Ally NPCs form the standard challenge template. Build them as near-mirrors of player characters, then shift health, equipment, and skills to fit the role.

Mini Bosses push above that line. Give them stronger gear, higher durability, and deeper skill investment than a standard Enemy or Ally.

Bosses break the normal point-buy expectation. A Boss gets one extra +5 beyond the normal limit. That extra stat increase turns a dangerous NPC into a major threat without changing the rest of the framework.

TODO: add encounter-building procedure, XP awards by enemy rank, and guidance for mixing ranks in one encounter.

## Advancement and Between-Session Play

Character advancement runs through skills. You earn XP by progressing through and interacting with the world in exploration, combat, and conversation. Each enemy type, from Minion through Boss, awards a set amount of XP. Exploration encounters also award XP when the group engages with them. Social and conversation encounters award XP on both success and failure.

You spend XP after each session.

XP is a shared budget across three investment tracks:

- **Proficiency ranks.** Buy new proficiencies or raise existing ones. Each proficiency advances from Rank 1 to Rank 10. Costs rise exponentially.
- **Weapon Mastery ranks.** Buy Mastery Ranks in individual weapons (Rank 1 to 5). Higher ranks unlock more Techniques and Augment Slots.
- **Augments.** Purchase Weapon Augments and learn Technique Augments to socket into your prepared Techniques. All 22 Universal Augments are known at creation.

Spreading XP gives breadth. Focusing XP gives depth. A character with three weapons at Mastery 2 plays differently from one weapon at Mastery 5.

Your character has 10 prepared Technique slots for active abilities used in fights. These are independent of proficiencies. See Weapons, Techniques, and Augments for the full system.

You can own as many proficiencies as you can afford.

Between sessions, you can update the parts of the character that the rules mark as changeable. You can gain or swap proficiencies with GM confirmation. You can also change prepared Techniques and re-socket Augments on a short or long rest, change weapons within your inventory, adjust spells, update equipment, spend or gain money and resources, and record new languages as your character learns them.

TODO: add the full XP cost tables and the exact XP awards for combat, exploration, and conversation encounters.

## Running the Game

Run NPCs from their stat blocks and use the same action economy, equipment rules, skill rules, and spell rules that player characters use. Pick an NPC rank that matches the role you want in the scene, then build the NPC from that frame.

Use NPCs as part of the world, not just as combat pieces. An NPC can create a problem, keep a problem active, show up as a consequence of player action, or deliver a reward after the group resolves a situation. That same framework lets you place allies and enemies inside combat, exploration, and conversation scenes without changing systems.

Keep a clear split between what the players control and what the GM or the system controls.

- Players control their skills, equipment, weapons, spells, money, resources, and languages.
- The GM or the system controls status effects, environmental effects, lingering injuries, long-term curses, madness, and reputation changes.

Track temporary and long-term changes on the character sheet as separate layers. If a spell raises a character's health for a short time, record that change as a temporary condition instead of rewriting the character's fixed maximum values.

### Degree of 5

Social and situational mechanics use degrees of 5.

Set a DC based on the challenge, then raise or lower that DC to reflect the character's familiarity, competence, or lack of experience. The current guidance assumes most DC shifts will fall between 0 and 10.

A roll is only needed when the outcome is uncertain.

| Degree | Result | Outcome |
| --- | --- | --- |
| +10 | Beat the DC by 10 or more | Gain a positive result and a big bonus |
| +5 | Beat the DC by 5 or more | Gain a positive result and a small bonus |
| +/-0-4 | Meet, beat, or miss the DC by 0 to 4 | The expected result happens with no added swing |
| -5 | Miss the DC by 5 or more | Gain a negative result and a small setback |
| -10 | Miss the DC by 10 or more | Gain a negative result and a big setback |

This model lets competence lower a DC when the task fits the character and lets inexperience raise a DC when the character lacks the right frame of reference.

TODO: add broader GM guidance for encounter pacing, difficulty, and adjudication.

## Reference and Playtest Tools

The current manuscript already includes several tools for running tests at the table.

### Systems Reference

A quick-lookup summary of each major mechanic. For full rules, see the chapter listed in parentheses.

#### Resolution (Core Mechanics)

Roll `2d10` and add together. Add your relevant modifier. Compare to the target number.

- **Attack:** `2d10 + Stat Modifier` vs. target's `Armor AC (relevant stat + DR)`
- **Proficiency Check:** `2d10 + Skill Modifier` vs. GM-set DC
- **Critical success:** both dice show 10. **Critical failure:** both dice show 1.
- **Degree of 5:** beat DC by 10+ = big bonus; 5–9 = small bonus; 0–4 = expected; miss by 5–9 = small setback; miss by 10+ = big setback.

#### Attributes and Modifiers (Attributes and Skills)

Five attributes: Body, Mind, Social, Magic, Sanity. Modifiers run −5 to +5.

Point buy at creation: 5 points. Costs: +5=6, +4=4, +3=3, +2=2, +1=1, 0=0. Negative modifiers refund points; refunded points must be spent.

Skill modifier = primary attribute + one chosen secondary attribute from two listed options.

#### Armor and Defense (Armor and Defense)

Two independent defense values:

- **Physical AC** = relevant Stat Modifier + Physical DR
- **Magical AC** = relevant Stat Modifier + Magic DR

DR reduces damage after a hit lands. Magic DR does not block elemental stack application or escalation.

| Armor Tier | Physical DR | Magic DR |
|---|---|---|
| Cloth | 0 | 4 |
| Light | 1 | 3 |
| Medium | 3 | 1 |
| Heavy | 4 | 0 |
| Enchanted | 3 | 3 |

#### Action Economy (Combat)

3 Actions per turn. 1 Reaction per round (refreshes at start of that character's turn). Initiative: `d10 + Body` or `d10 + Magic` (player chooses to match fighting style).

Free Actions do not cost from the 3-Action pool.

#### HP, Mana, and Backgrounds (Character Creation)

| Background | HP | Mana | Mana Regen |
|---|---|---|---|
| Martial | 120 | 30 | 3/turn |
| Hybrid | 110 | 70 | 10/turn |
| Caster | 100 | 100 | 15/turn |

#### Elemental Stacks and Conditions (Conditions, Injuries, and Death)

Stacks cap at 5 per element. Each active stack deals +1 damage per round (modified by Magic DR). Stacks last 2 full rounds and reset on reapplication. Burn and Chilled cancel 1:1.

**Escalation tiers:**

| Tier | Mana | Requirement | Effect |
|---|---|---|---|
| T1 | 3 | — | Apply base stacks |
| T2 | 6 | — | Skip to escalation condition |
| T3 | 12 | T2 active, Mastery 3+ | Enhanced escalation |
| T4 | 17 | T3 active, Rank 5 capstone | Ultimate escalation, once per long rest |

Magic DR reduces stack tick damage but does not block stack application or T2/T3/T4 escalation.

#### Dying (Conditions, Injuries, and Death)

At 0 HP, set a death counter: `10 + Body modifier` (minimum 5, maximum 15). Each turn the counter drops by:

- Active stack damage (after Magic DR)
- +1 per unused Action slot, or +2 per used Action slot

Healing restores from Dying. Roll `2d10 + Body` vs. DC `(15 − counter value at time of healing)` for consequences using the Degree of 5 table.

#### Weapons, Techniques, and Augments (Weapons, Techniques, and Augments)

Three independent layers:

**Weapon Mastery (Rank 0–5):** Spent XP unlocks higher-rank Techniques and more Augment Slots per Technique. Rank 1 = access to Rank 1 Techniques. Each rank up also unlocks Weapon Augments.

**Techniques:** Active combat abilities. Prepare 10 at a time (changeable on rest). Weapon must be equipped to use its Techniques. Category Techniques require any weapon in that category. Three layers of Technique scope: Universal → Category → Weapon-specific.

**Augments — three layers:**

| Layer | How equipped | Scope |
|---|---|---|
| Universal Augments (22) | Socket into Technique Augment Slots | Any Technique, any weapon |
| Weapon Augments (~5 per weapon) | Passive, always active once learned | All Techniques from one weapon |
| Technique Augments (~2–3 per technique) | Socket into that Technique's Augment Slots | One specific Technique only |

Augment Slots per Technique by Mastery Rank: 0 / 1 / 1 / 2 / 2 / 3.
Weapon Augments available by Mastery Rank: 0 / 0 / 2 / 3 / 4 / 5.
Each Weapon Augment costs 10 XP. Universal Augments are known at creation.

#### Spellcasting (Magic and Spellcasting)

No spell list. Build each spell from parameters: Category, Function, Range, Size, Shape, Duration, Target Count, Accuracy Type, Effect Tier. No field can stay empty. No weapon or class requirement. Only mana gates casting.

Mana cost = base + Function cost + die upgrades + tier cost.

Function costs: Utility +0, Movement +1, Defensive +1, Offensive +2. Multi-function: add both. Die scaling: d6 = +1, d8 = +2, d10 = +3, d12 = +5.

Main spell category costs normal. Sub category costs double.

#### Proficiency Checks (Attributes and Skills)

11 skills: Athletics, Stealth, Investigation, Knowledge, Medicine, Survival, Animal Handling, Performance, Speech, Arcana, Insight.

Skills are NOT combat abilities. They cover non-combat checks only. Proficiency Check modifier = primary attribute + chosen secondary attribute (pick from two options when the check is called).

Ranks 1–10 (higher rank = higher modifier). No maximum count on known proficiencies.

#### Advancement (Advancement and Between-Session Play)

XP earned through combat, exploration, and conversation. Spent on:

- New proficiency knowledge
- Proficiency rank increases (Rank 1–10, exponential cost)
- Weapon Mastery rank increases
- Weapon Augment purchases (10 XP each)

XP is a shared budget. Spending on one area trades off against another.

#### NPCs by Rank (NPCs, Enemies, and Encounters)

| Rank | HP | Mana | Notes |
|---|---|---|---|
| Minion | 1–5 | 30/3 | All modifiers +0 |
| Regular | 75 | 30/3 | All modifiers +1 |
| Enemy/Ally | 100 | 100/15 | Body +4, Mind +1, Social +3, Magic −3 |
| Mini Boss | 120 | 100/15 | Body +5, Mind +4, Social −3 |
| Boss | 175 | 100/20 | Body +5, Mind +3, Magic +5, Sanity −5; one stat at +6 |

Bosses use Enchanted armor. Each rank above Regular has more varied ability access and higher Weapon Mastery.

---

### Sample Character Builds

The sample character sheets provide six player builds. Each sheet tracks HP, mana, split armor values, split Armor AC, stat modifiers, and full skill totals. Taken together, they show the intended spread from martial-heavy bodies to magic-heavy casters.

### NPC Templates By Rank

The current reference set also includes benchmark creature blocks.

- Minion Block: 1 to 5 HP, 30/3 mana, no armor
- Regular Block: 75 HP, 30/3 mana, 1/1 armor
- Enemy or Ally Block: 100 HP, 100/15 mana
- Mini Boss Block: 120 HP, 100/15 mana
- Boss Block: 175 HP, 100/20 mana

Use these blocks as balance anchors when testing new weapons, spell builds, or encounter pacing.

### Playtest Checklist

The current playtest checklist asks the table to verify these points.

- Can you assign a race?
- Can you give the character a name?
- Can you distribute ability scores?
- Can you fill out skill checks?
- Can you give the character a background?
- Can you give the character equipment, weapons, and armor?
- Can you give the character skills?
- Can you tell enemy ranks apart at a glance?
- Can you read an enemy's HP, stats, equipment, weapons, and armor from the block?
- Can you run the NPC with the information given?
- Can you roll initiative and create a turn order?
- Can you use skills, weapons, and the DR system cleanly?
- Can you track HP, mana, and mana regeneration during play?

TODO: finalize the reference appendix.
TODO: reconcile playtest-sheet values against the core rules where they disagree.