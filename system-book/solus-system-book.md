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

#### Bare Hands (Simple, Light Melee) — 8 Techniques

**Unique Mechanic: A Fist Like Steel.** Every hit applies 1 Force stack to the target. At 5 Force stacks, the target becomes Staggered. Spend stacks with To The Face before they reach 5 to deal bonus damage and prevent escalation.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | With My Bare Hands | 1 Action | Strike. On hit, choose one free action: Shove (knock prone), Grapple, or Push 5 ft. Make a contested Body check vs. the target's Athletics. Once per turn. |
| 1 | The Old One, Two | 1 Action | Strike twice. Cannot use With My Bare Hands on the second strike. |
| 2 | To The Face | 1 Action, 3 Mana | Strike. On hit, expend any number of Force stacks. Deal bonus damage equal to stacks spent. Spend 3+: also attempt Disarm (Body check vs. your DC). Spend 4+: attempt Stunned instead (same check). These effects replace bonus damage. On a miss, stacks are still lost. |
| 2 | Clinch | 1 Action, 3 Mana | Grapple a target within 5 ft. While the grapple holds, Bare Hands attacks against them deal +2 damage and apply 1 additional Force stack per hit. |
| 3 | Ground and Pound | 1 Action, 5 Mana | Requires an active Grapple. Strike three times against the grappled target. Each hit applies 1 Force stack. |
| 3 | Stand Your Ground | Reaction, 5 Mana | When a target you have Force stacks on attempts to disengage or move away, make a contested Body check vs. their Athletics. On success, they cannot move this turn. |
| 4 | Bone Breaker | 1 Action, 8 Mana | Requires [Staggered]. Strike. On hit, halve the target's movement speed and give them Disadvantage on attack rolls until a short rest. Apply 2 Force stacks. |
| 5 | Haymaker (Capstone) | 2 Actions, 15 Mana | Requires [Staggered]. Deliver one devastating blow. On hit, triple weapon damage and trigger Shattered. Once per long rest. |

##### Bare Hands Weapon Augments (A Fist Like Steel)

Passive. Once learned, these apply to ALL Bare Hands Techniques. Each adds its Mana cost to every Bare Hands Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Iron Fist | Your hits apply 1 additional Force stack. | +1 |
| 2 | Follow Through | After using To The Face, your next Bare Hands attack has Advantage. | +2 |
| 3 | Grappler | Clinch's grapple range extends to 10 ft. | +1 |
| 4 | Concussive | Force stacks deal 1 passive damage per stack at the start of the target's turn. | +2 |
| 5 | Unstoppable | While you have 3+ Force stacks on a target, your Bare Hands attacks cannot be interrupted by Reactions. | +3 |

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

**Unique Mechanic: Shared Risk.** You can choose to take Bleed stacks on yourself to activate stance bonuses. Each stance requires 1+ Bleed on yourself and 2+ Bleed on the target to provide its benefit. Only one stance can be active at a time. If you reach 5 Bleed stacks yourself, you become Shredded.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | First Adventure | 1 Action | Enter Offensive Stance and apply 1 Bleed to yourself. Strike. On hit, apply 1 Bleed to the target. While in stance with 1+ Bleed on yourself and 2+ on the target, attacks deal +1d4 bonus damage. Gain 1 Bleed on yourself at the start of each of your turns while in stance. |
| 1 | Seasoned Traveler | 1 Action | Enter Defensive Stance and apply 1 Bleed to yourself. Strike. On hit, apply 1 Bleed to the target. While in stance with 1+ Bleed on yourself and 2+ on the target, gain +2 Physical DR. Each time you are hit while in stance, take +1d4 bleed damage. |
| 2 | A Real Adventure | 1 Action, 3 Mana | Enter Aggressive Stance and apply 1 Bleed to yourself. Strike. On hit, apply 1 Bleed to the target. While in stance with 1+ Bleed on yourself and 2+ on the target, make 1 extra melee attack as part of your Action. Gain 1 Bleed on yourself each time you use the bonus attack. |
| 2 | Recover | 1–2 Actions, 3 Mana | Purge 2 Bleed stacks from yourself (1 Action) or all Bleed stacks from yourself (2 Actions). You cannot enter a stance until the start of your next turn. |
| 3 | Double Down | 1 Action, 5 Mana | Strike twice. Each hit applies 1 Bleed to the target. If you are in a stance, apply 1 Bleed to yourself as well. |
| 3 | Wound Pressure | Reaction, 5 Mana | When a Bleeding target moves away from you, make a free opportunity attack. On hit, apply 2 Bleed stacks. |
| 4 | Deep Cut | 1 Action, 8 Mana | Requires [Shredded] on target. Strike. On hit, deal bonus damage equal to all active Bleed stacks on the target and apply 1 Bleed to yourself. |
| 5 | Veteran (Capstone) | 2 Actions, 15 Mana | Requires 4+ Bleed on yourself and [Shredded] on target. On hit, transfer all your Bleed stacks to the target. Deal +1d4 damage per stack transferred. Take 1d6 bleed damage per stack transferred as your wounds reopen. If the transfer triggers Exsanguination, this damage bypasses DR. Once per long rest. |

##### Short Sword Weapon Augments (Shared Risk)

Passive. Once learned, these apply to ALL Short Sword Techniques. Each adds its Mana cost to every Short Sword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Sharp Edge | While in a stance, hits apply 1 additional Bleed stack to the target. | +1 |
| 2 | Pain Tolerance | Bleed stacks on yourself deal 1 less damage per round (minimum 0). | +2 |
| 3 | Swift Stance | Switching stances costs 0 Actions and no Bleed stacks. | +1 |
| 4 | Bleeding Edge | While in Aggressive Stance with [Shredded] on target, gain one additional bonus attack. | +2 |
| 5 | Last Stand | When you drop below 25 HP while in any stance, immediately apply 3 Bleed stacks to the target for free. | +3 |

#### Claw Gauntlet (Standard, Light Melee) — 9 Techniques

**Unique Mechanic: Paired Blades.** Claw Gauntlet requires both gauntlets equipped. You cannot hold a shield or off-hand weapon. Only one Damage Mode can be active at a time. Switching modes is a Free Action. Attacks in the active mode may include one extra strike per Action.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | One, Two, I'm Coming for You | 1 Action | Enter Bleed Mode. All attacks apply 1 Bleed on hit. Once per Action, make one extra strike. |
| 1 | They're All Doomed | 1 Action | Enter Acid Mode. All attacks apply 1 Acid on hit. Once per Action, make one extra strike. |
| 2 | He Doesn't Run | 1 Action, 3 Mana | Launch a flurry at one target within 20 ft. Target makes a Body save vs. your DC. Fail: Anchored and full damage. Success: full damage, no Anchor. |
| 2 | Rend | Reaction, 3 Mana | When an adjacent enemy attacks you, slash back. On hit, apply 1 Bleed and 1 Acid stack. |
| 3 | Tear Through | 1 Action, 5 Mana | Make 4 strikes (2 per gauntlet). Each hit applies the active mode's condition stack. |
| 3 | Mode Shift | Free Action, 5 Mana | Switch Damage Modes. Your next attack in the new mode applies 2 condition stacks instead of 1. |
| 4 | I Wanna See What Your Insides Look Like | 2 Actions, 8 Mana | Requires [Shredded] and [Corroded] on target. Make 2 strikes. If either hits, trigger He Doesn't Run with an automatic save failure. Gain 3 Bleed and 3 Acid stacks yourself. |
| 4 | Predator's Pace | 1 Action, 8 Mana | Move up to your full speed. Until end of turn, attacks have Advantage and each hit applies the active mode's condition. |
| 5 | Final Claw (Capstone) | 2 Actions, 15 Mana | Requires [Shredded] and [Corroded] on target. Make 4 strikes. Each hit applies 2 Bleed and 2 Acid stacks. If target is Anchored, all strikes have Advantage. Once per long rest. |

##### Claw Gauntlet Weapon Augments (Paired Blades)

Passive. Once learned, these apply to ALL Claw Gauntlet Techniques. Each adds its Mana cost to every Claw Gauntlet Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Dual Poison | While in Acid Mode, attacks also apply 1 Bleed stack. | +1 |
| 2 | Death Grip | He Doesn't Run's save DC increases by 2. | +2 |
| 3 | Serrated | Bleed stacks you apply deal +1 damage per stack per round. | +1 |
| 4 | Mode Lock | After switching modes with Mode Shift, your first attack has Advantage. | +2 |
| 5 | Total Dissolution | While target has both [Shredded] and [Corroded], your attacks ignore Physical DR. | +3 |

#### Sickle (Standard, Light Melee)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: On kill, transfer remaining Bleed stacks to one adjacent enemy. Harvest-chain kills spread Bleed across groups.

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

#### Longsword (Standard, Medium Melee)

TODO: full Technique list. Condition signature: Bleed (one-handed) / Force (two-handed). Unique mechanic: Grip-switching determines condition path. Versatile damage (1d10/1d12).

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

#### Curved Sword (Standard, Medium Melee) — 9 Techniques

**Unique Mechanic: Liquid Metal.** Once per turn, extend your attack's reach to 10 ft at no cost. The blade shifts between three forms: Quicksilver (liquid, Bleed), Mercury (flat sweep, Force), and Galinstan (teardrop tip, Force + Knockback). Switching forms is a Free Action.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Quicksilver | 1 Action | Liquefy the blade. Slashing damage. Apply 1 Bleed on hit. Spend 2 Bleed stacks: deal +1d4 Bleed damage. Spend 4: extend reach to 10 ft, deal +1d4 Bleed damage, and hit one creature directly behind the target for the same damage. Each target struck gains 2 Bleed stacks on hit (1 Bleed on miss). |
| 1 | Mercury | 1 Action | Flatten the blade into a wide sweep. Slashing damage. Apply 1 Force on hit. Spend 2 Force stacks: deal +1d4 bonus damage. Spend 4: extend reach to 10 ft and apply 4 Force stacks on hit (1 Force on miss). |
| 2 | Galinstan | 1 Action, 3 Mana | Shift the blade's mass to its tip. Bludgeoning damage. Apply 1 Force on hit. Spend 2 Force stacks: attempt Knockback (target makes Body save vs. your DC). Spend 4: extend reach to 10 ft, hit up to 2 adjacent enemies, each saves vs. Knockback and gains 4 Force stacks on fail (1 Force on miss). |
| 2 | Form Transition | Free Action, 3 Mana | Switch forms. Your next attack in the new form applies 2 condition stacks instead of 1. |
| 3 | Quicksilver Chain | 1 Action, 5 Mana | Enter Quicksilver form. Strike, then strike again if the first hits. Each hit applies 2 Bleed stacks. |
| 3 | Mercury Sweep | 1 Action, 5 Mana | Enter Mercury form. Strike all enemies within 10 ft in a single sweep. Each hit applies 1 Force stack. |
| 4 | Volatile Flow | 1 Action, 8 Mana | Requires [Shredded] or [Staggered]. Strike. On hit, deal bonus damage equal to the total active Bleed and Force stacks on the target. Clear all those stacks. |
| 4 | Form Lock | Free Action, 8 Mana | Commit to your current form until end of your next turn. All attacks in this form have Advantage. Condition stacks applied by this form are doubled. |
| 5 | Liquid Ruin (Capstone) | 2 Actions, 15 Mana | Requires [Shredded] and [Staggered]. Strike once in each form: Quicksilver, Mercury, Galinstan. Each hit applies that form's conditions at double value. If all three hit, trigger Exsanguination and Shattered simultaneously. Once per long rest. |

##### Curved Sword Weapon Augments (Liquid Metal)

Passive. Once learned, these apply to ALL Curved Sword Techniques. Each adds its Mana cost to every Curved Sword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Flow State | Form Transition costs 0 Mana. | +1 |
| 2 | Pressure Wave | Mercury hits push the target 5 ft. | +2 |
| 3 | Serrated Liquid | Quicksilver attacks apply 1 additional Bleed stack. | +1 |
| 4 | Mass Shift | Galinstan Knockback saves are made at Disadvantage. | +2 |
| 5 | True Liquefaction | Once per turn, when a hit clears all condition stacks, immediately apply 2 stacks of the clearing form's condition. | +3 |

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

TODO: full Technique list. Condition signature: Force. Unique mechanic: Force stacks impose -1 per stack to mental Proficiency Checks. At Staggered (5 Force): disadvantage on all Proficiency Checks.

#### Flail (Standard, Medium Melee)

TODO: full Technique list. Condition signature: Force. Unique mechanic: Bypass and Chain properties mean Force stacks land against Shields and cannot be Parried. Anti-tank weapon.

#### War Pick (Standard, Medium Melee)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: Pierce extends to Bleed damage. Bleed ticks also ignore 2 Physical DR. Capstone: Total Dissolution (T4, destroys armor).

#### Bastard Sword (Complex, Medium Melee / Heavy Melee)

TODO: full Technique list. Condition signature: Bleed (one-handed) or Force (two-handed). Unique mechanic: Adaptive. Switches category by grip. At Mastery 3, access Category Techniques from both Medium Melee and Heavy Melee.

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

#### Great Axe (Standard, Heavy Melee) — 9 Techniques

**Unique Mechanic: Double Tick.** Great Axe Bleed stacks deal 2 damage per stack per round instead of 1. Once the target reaches [Shredded], all Great Axe attacks ignore Physical DR entirely.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Heavy Swing | 1 Action | Strike. Apply 2 Bleed stacks on hit. |
| 1 | UP and DOWN | 1 Action | Strike. On hit, target makes a Body save vs. your DC. Fail: launch target 10 ft airborne and deal half weapon damage. If you have 10+ ft of movement remaining, leap and slam for half weapon damage (auto-hit). Target falls prone on impact. Success: grounded, half weapon damage. |
| 2 | Stick and KICK | 1 Action, 3 Mana | Strike. On hit, target makes a Body save vs. your DC. Fail: axe embeds (target Pinned). Spend your next Action to Kick the Pinned target (repeat save at Disadvantage: fail → Push 5 ft or knock prone; success → Kick still deals 2 damage). Success: not Pinned, half weapon damage. Attempt Kick normally on either result. |
| 2 | Wide Arc | 1 Action, 3 Mana | Sweep through up to 2 adjacent enemies with a single attack roll. Apply 1 Bleed stack to each target hit. |
| 3 | Deep Wound | 1 Action, 5 Mana | Strike. Apply 3 Bleed stacks on hit. If the target already has active Bleed, deal +1d6 bonus damage. |
| 3 | Rend Armor | 1 Action, 5 Mana | Strike. On hit, reduce the target's Physical DR by 2 until end of your next turn. Apply 1 Bleed stack. If the target is already Shredded, the DR reduction lasts until a short rest. |
| 4 | Axe Slam | 1 Action, 8 Mana | Requires [Shredded]. Strike, ignoring all Physical DR. Apply 2 additional Bleed stacks on hit. Target makes a Body save or falls prone. |
| 4 | Bleeding Frenzy | 1 Action, 8 Mana | Requires [Shredded]. Strike twice, ignoring all Physical DR. Apply 1 Bleed stack per hit. |
| 5 | Reaping Blow (Capstone) | 2 Actions, 15 Mana | Requires [Shredded]. Strike, ignoring all Physical DR. On hit, triple weapon damage and trigger Exsanguination. Once per long rest. |

##### Great Axe Weapon Augments (Double Tick)

Passive. Once learned, these apply to ALL Great Axe Techniques. Each adds its Mana cost to every Great Axe Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Savage Swing | Each hit applies 1 additional Bleed stack. | +1 |
| 2 | Launch Mastery | UP and DOWN's slam at the apex deals full weapon damage instead of half. | +2 |
| 3 | Embedded | Stick and KICK's Pinned condition lasts 1 extra round. | +1 |
| 4 | Hemorrhage | While target is Shredded, hits splash 1 Bleed stack to all other enemies within 5 ft. | +2 |
| 5 | Execution | When a target reaches Exsanguination, your next Great Axe attack automatically critically hits. | +3 |

#### Greatclub (Simple, Heavy Melee)

TODO: full Technique list (caps at Rank 3). Condition signature: Force. Unique mechanic: Knockback into walls or terrain grants bonus Force stacks. Environmental combo weapon.

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

#### Halberd (Standard, Reach) — 9 Techniques

**Unique Mechanic: Dual Edge.** The halberd's blade and pole are distinct attack modes. Blade Mode applies Bleed (Slashing) and Pole Mode applies Force (Bludgeoning). Switching modes is a Free Action. Certain techniques specify the required mode.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Blade | 1 Action | Blade Mode. Make a single attack roll against the higher AC of two adjacent enemies. On hit, deal full damage to both. Each target reduces damage using the highest DR between them. Apply 1 Bleed to each target hit. |
| 1 | Pole Strike | 1 Action | Pole Mode. Strike one target. Apply 1 Force stack on hit. If the target is within 5 ft, apply 2 Force stacks instead. |
| 2 | Hook | 1 Action, 3 Mana | On hit, drag the target up to 10 ft in a direction of your choice. If this pulls the target out of an ally's reach, that ally makes an Opportunity Attack with Advantage. |
| 2 | Pole | 2 Actions, 3 Mana | Pole Mode. Make two attacks against the same target. If both hit, apply 2 Bleed stacks in addition to normal Force stacks. |
| 3 | Extended Blade | 1 Action, 5 Mana | Blade Mode. Strike all enemies in a 10 ft line extending from you. Apply 1 Bleed to each target hit. |
| 3 | Haft Block | Reaction, 5 Mana | Interpose the haft against a melee attack. Reduce incoming damage by 1d6 + Body. If the attacker is within reach, apply 1 Force stack to them. |
| 4 | Sweep and Pin | 1 Action, 8 Mana | Requires [Staggered] or [Shredded]. Blade Mode. Strike all enemies within 10 ft. Each target hit makes a Body save or falls prone. Apply 1 Bleed to each target hit. |
| 4 | Impale | 1 Action, 8 Mana | Blade Mode. Strike. On hit, pin the target (Restrained) until you move or attack again. Apply 3 Bleed stacks. Target makes a Body save at the end of each of their turns to break free. |
| 5 | Battlefield Reaper (Capstone) | 2 Actions, 15 Mana | Requires [Staggered] on at least one target. Sweep through all enemies within 10 ft in one motion. One attack roll vs. each. On hit: apply 3 Force and 3 Bleed to each. Any target already at 5 Force immediately triggers Staggered. Once per long rest. |

##### Halberd Weapon Augments (Dual Edge)

Passive. Once learned, these apply to ALL Halberd Techniques. Each adds its Mana cost to every Halberd Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Extended Reach | Pole Strike range increases to 15 ft. | +1 |
| 2 | Decisive Hook | Hook's drag distance increases to 15 ft. | +2 |
| 3 | Blade Guard | After any Blade Mode Technique, gain +1 Physical DR until your next turn. | +1 |
| 4 | Force Transfer | When Hook moves a target into another enemy's space, both take 1d6 bonus damage. | +2 |
| 5 | Cleave Through | Blade Mode hits apply 1 Bleed stack to all enemies adjacent to the primary target. | +3 |

#### Scythe (Complex, Reach) — 9 Techniques

**Unique Mechanic: Harvest.** When you kill a target that has Bleed active, transfer all their Bleed stacks to one adjacent enemy of your choice. Once per turn, spend 1 Action to purge all Bleed stacks from one ally within reach. That ally takes no damage from those stacks.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Reaper's Spiral | 1 Action | All enemies within 10 ft make a Body save vs. your DC. Fail: full weapon damage and 1 Bleed stack. Success: half damage. Does not provoke opportunity attacks. |
| 1 | Reap | 1 Action | Strike. On hit, the target gains 1 Reap stack (max 1 per target per turn). At 3 Reap stacks, spend 1 Action to consume all stacks and deal 10 damage (reduced by DR). Reap stacks are lost if the target is healed or if you fail to hit them for 2 consecutive rounds. |
| 2 | Wraith Arc | 1 Action, 3 Mana | Move up to 15 ft through 2 or more enemies. Attack range drops to 5 ft during movement. No opportunity attacks while moving. Make 1 attack roll vs. the highest AC among enemies passed through. On hit, all passed-through enemies take full damage (each reduces damage using the highest DR among them). |
| 2 | Death's Mercy | 1 Action, 3 Mana | Purge all Bleed stacks from one ally within reach. Redirect half the purged stack count as damage to one enemy within reach (DR applies). |
| 3 | Spiral Surge | 1 Action, 5 Mana | All enemies within 10 ft make a Body save. Fail: full weapon damage and 2 Bleed stacks. Success: half damage and 1 Bleed stack. Does not provoke opportunity attacks. |
| 3 | Grave Hunger | 1 Action, 5 Mana | Requires 3+ Bleed on target. Strike. On hit, deal bonus damage equal to the target's active Bleed stack count. Apply 2 additional Bleed stacks. |
| 4 | Spectral Harvest | 1 Action, 8 Mana | Requires [Shredded]. Strike. On hit, transfer all Bleed stacks from this target to all other enemies within 10 ft (split evenly, round down). The original target takes full weapon damage. |
| 4 | Reaper's Stride | 1 Action, 8 Mana | Move up to your full speed. Every enemy you pass adjacent to makes a Body save. Fail: 1d6 damage and 2 Bleed stacks. No opportunity attacks during this movement. |
| 5 | Final Harvest (Capstone) | 2 Actions, 15 Mana | Requires [Shredded]. Strike every enemy within 10 ft once. Each hit deals double weapon damage. Transfer all Bleed stacks from each hit target to one adjacent enemy of your choice. Any target already at Shredded triggers Exsanguination. Once per long rest. |

##### Scythe Weapon Augments (Harvest)

Passive. Once learned, these apply to ALL Scythe Techniques. Each adds its Mana cost to every Scythe Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Curved Blade | Reaper's Spiral and Spiral Surge radius extends to 15 ft. | +1 |
| 2 | Reap Mastery | Reap stacks cap at 4 instead of 3. Reap detonation deals 14 damage instead of 10. | +2 |
| 3 | Soul Drain | When Harvest transfers stacks on a kill, you gain 5 HP. | +1 |
| 4 | Ghost Arc | Wraith Arc movement increases to 20 ft. Attack roll gains +2 to hit. | +2 |
| 5 | Endless Reaping | Final Harvest does not consume its long rest use if all targets were already Shredded at the start of the technique. | +3 |

#### Whip (Standard, Reach) — 8 Techniques

**Unique Mechanic: Extended Reach.** The whip's reach is 15 ft (3 spaces). At Mastery Rank 3, once per turn when you hit a Bleeding target, pull them up to 10 ft toward you as a free action. No contested check required.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Control Lash | 1 Action | Strike. On hit, choose one: Trip (target makes Body save vs. your DC → prone), Disarm (Body save → drops one held item), Pull 5 ft toward you (Body check vs. your DC), or Hold (Restrained until start of your next turn; you cannot attack while holding, releasing is free). One option per hit. Once per turn. |
| 1 | Serpent's Tempo | 1 Action | Strike. Apply 1 Force stack on hit. If you hit the same target again this turn with another Whip attack, apply 1 additional Force stack on that second hit. |
| 2 | Crack the Air | 1 Action, 3 Mana | Snap the whip in a 10 ft cone. All creatures in the cone make a Body save vs. your DC. Fail: Deafened until end of their next turn and apply 1 Force stack. Deals no damage. |
| 2 | Wrap and Rip | 1 Action, 3 Mana | Strike. On hit, wrap the whip around the target's limb (Restrained). On your next turn, spend 1 Action to tear free: deal 1d6 bleed damage and apply 2 Bleed stacks. |
| 3 | Snap Pull | 1 Action, 5 Mana | Strike a target within 15 ft. On hit, pull them up to 10 ft toward you and apply 2 Bleed stacks. If pulled within an ally's reach, that ally may make an Opportunity Attack with Advantage. |
| 3 | Ensnare | 1 Action, 5 Mana | Strike at a target's legs. On hit, Restrained and speed drops to 0 until they spend 1 Action to break free (Body save vs. your DC). Apply 1 Bleed stack. |
| 4 | Shredding Lash | 1 Action, 8 Mana | Requires [Shredded]. Strike. On hit, double weapon damage and apply 2 Bleed stacks. The target cannot remove Bleed stacks by any means until end of your next turn. |
| 5 | Serpent's Wrath (Capstone) | 2 Actions, 15 Mana | Requires [Shredded] or [Staggered]. Strike every enemy within 15 ft. Each hit applies 3 Bleed and 3 Force stacks. Targets already at 5 Bleed trigger Shredded. Targets already at 5 Force trigger Staggered. Once per long rest. |

##### Whip Weapon Augments (Extended Reach)

Passive. Once learned, these apply to ALL Whip Techniques. Each adds its Mana cost to every Whip Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Long Reach | Extend Whip reach to 20 ft. | +1 |
| 2 | Barbed | Bleed stacks you apply cannot be removed until the start of your next turn. | +2 |
| 3 | Coiled Strike | After using Control Lash, your next Whip attack has Advantage. | +1 |
| 4 | Trip Expert | Tripped targets must spend their full Action to stand and immediately gain 1 Bleed stack. | +2 |
| 5 | Whiplash | After pulling a target with Snap Pull or the Rank 3+ free pull, your next Whip attack against them deals +1d6 damage. | +3 |

#### Staff (Standard, Reach)

TODO: full Technique list. Condition signature: Force. Unique mechanic: Force stacks catalyze elemental stacks, dealing an extra tick on hit against targets with active elemental stacks. Primary gish bridge weapon. Arcane property boosts spell range.

#### Trident (Standard, Reach)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: Impaled targets do not lose Bleed stacks to natural decay. Sustained pressure on pinned targets.

#### Chain (Complex, Reach)

TODO: full Technique list. Condition signature: Force. Unique mechanic: Entangled targets gain 1 Force stack per turn (constricting). Escalates to Staggered without additional attacks. Capstone: Cascade Failure (T4).

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

#### Crossbow (Standard, Ranged)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: Deep Penetration extends Pierce to Bleed ticks. High single-shot damage offset by Loading. Higher ranks unlock faster reload Techniques.

#### Hand Crossbow (Standard, Ranged)

TODO: full Technique list. Condition signature: Poison. Unique mechanic: Every hit applies 1 Poison stack. Rapid-fire rushes Venomous (5 Poison). Rank 3: 2 Poison per hit. Capstone: Lethal Dose (T4, Neurotoxin).

#### Bomb Flask (Standard, Ranged) — 9 Techniques

**Unique Mechanic: Flask Types.** Before combat, choose one flask type. The loaded type determines what condition your flask applies and its special area effect. Switch flask types on a short rest.

| Flask Type | Condition | Special AoE Effect |
|---|---|---|
| Fire | Burn | AoE may ignite terrain for 2 rounds |
| Cold | Chill | AoE creates difficult terrain for 2 rounds |
| Lightning | Shock | Wet targets in AoE may escalate Shock stacks |
| Poison | Poison | AoE deals 1 ongoing poison damage per stack per round |
| Frenzyflame | Burn | Deals 20 Madness to targets, 15 Madness to self. No AoE. |

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Lob | 1 Action | Throw a flask up to 20 ft. Direct hit: 1d6 + Body damage and apply 1 condition stack. On landing, 10 ft AoE: each target makes a Body save or takes half damage and gains 1 condition stack per round for 2 rounds. AoE may hit allies. |
| 1 | Slam | 1 Action | Melee bash with the flask (5 ft). 1d6 + Body damage. Choose: Wall of Sparks (5 ft radius AoE, 1 condition stack/round, 2 rounds) or Rolling Sparks (10 ft line AoE, 1 condition stack/round, 2 rounds). Apply 1 condition stack to the direct target. AoE may hit allies. |
| 2 | Dead On | 1 Action, 3 Mana | Aim for a direct hit. On hit, deal 2d6 + Body damage and apply 2 condition stacks. On miss, resolve as a normal Lob with no direct-hit bonus. |
| 2 | Delayed Burst | 1 Action, 3 Mana | Throw a flask up to 30 ft. It detonates at the start of your next turn. Targets in the 10 ft AoE cannot avoid the detonation unless they moved out of range. Apply 2 condition stacks on detonation. |
| 3 | Ricochet | 1 Action, 5 Mana | Throw a flask to bounce off a surface or target and hit up to 2 creatures behind cover or around corners. Each hit applies 1 condition stack. Any direct target also takes 1d6 + Body damage. |
| 3 | Saturation | 2 Actions, 5 Mana | Throw two flasks at the same point. AoE radius expands to 15 ft. Each target in the area gains 2 condition stacks per round for 2 rounds. AoE may hit allies. |
| 4 | Frenzy Surge | 1 Action, 8 Mana | Frenzyflame Flask only. Throw or slam. Deal 2d6 fire damage and apply 2 Burn stacks. Targets gain 20 Madness. You gain 15 Madness. No AoE. |
| 4 | Chain Reaction | 1 Action, 8 Mana | Requires target at T2 condition (Ignited, Frozen, Shocked, or Venomous). Throw a flask at that target. Detonation triggers that condition's T2 effect on all enemies in a 10 ft AoE, not just the direct target. |
| 5 | Maximum Payload (Capstone) | 2 Actions, 15 Mana | Requires at least one target at T2 condition. Throw up to 3 flasks in sequence, each landing in a different location within 30 ft. Full damage and condition stacks per flask. Each successive flask expands the previous AoE by 5 ft (overlapping areas stack conditions). Once per long rest. |

##### Bomb Flask Weapon Augments (Flask Types)

Passive. Once learned, these apply to ALL Bomb Flask Techniques. Each adds its Mana cost to every Bomb Flask Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Volatile Mix | Direct hits apply 1 additional condition stack. | +1 |
| 2 | Precision Lob | Lob and Saturation AoE radius increases by 5 ft. | +2 |
| 3 | Quick Brew | Switching flask types during combat is a Free Action. | +1 |
| 4 | Concentrated Formula | Condition stacks you apply last 1 extra round before decaying. | +2 |
| 5 | Catalytic Overflow | When a target reaches T2 condition from your flask, all other enemies within 5 ft of them gain 2 stacks of the same condition. | +3 |

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

#### Revolver (Standard, Firearms) — 9 Techniques

**Unique Mechanic: Last Words.** The revolver holds 6 rounds. Track consecutive hits across a full cylinder. If all 6 shots hit without a miss, the 6th gains Piercing (ignores half Physical DR, rounded down) and applies 1 Burn stack. A miss resets the streak. Reload costs 1 Action and refills all 6 rounds.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Quick Draw | 1 Action | Fire 1 round. Apply 1 Force stack on hit. Counts toward the Last Words streak. |
| 1 | Hair Trigger | 1 Action | Fire at 2–3 adjacent targets (all within 5 ft of each other). 1 attack roll vs. the highest AC. Each hit uses the highest DR among those hit. Costs 2 rounds per target (4–6 rounds total). Apply 1 Force stack per hit. Each hit counts toward the Last Words streak. |
| 2 | Roulette | 1 Action, 3 Mana | Enter Roulette mode. Before each shot, call evens or odds and roll 1d6. Hit + correct call: normal damage + 1d6 bonus. Miss + correct call: round spent, no damage. Incorrect call: misfire (1d6 damage to yourself, ignores DR, shot wasted). Roulette ends when you choose to stop, reload, or run out of rounds. Roulette shots do not count toward Last Words. |
| 2 | Fan the Hammer | 1 Action, 3 Mana | Fire 3 rounds at one target in rapid sequence. Each hit applies 1 Force stack. The second shot has Advantage if the first hit. The third has Advantage if the second hit. Each hit counts toward the Last Words streak. |
| 3 | Dead Aim | 1 Action, 5 Mana | Take careful aim. Your next shot has Advantage and deals +1d6 on hit. Counts toward the Last Words streak. |
| 3 | Suppressive Shot | Reaction, 5 Mana | When an enemy moves within range, fire 1 round at them. On hit, their movement ends for this turn. Apply 1 Force stack. Counts toward the Last Words streak. |
| 4 | Feelin' Lucky | 1 Action, 8 Mana | Requires exactly 2 rounds remaining. Discard 1, leaving 1 round. Call evens or odds and roll 1d6. Correct: this shot gains Piercing + 1 Burn stack (as Last Words). Incorrect: misfire (1d6 damage, ignores DR) + 1 Burn on self. Either result resets Last Words. |
| 4 | Execution Shot | 1 Action, 8 Mana | Requires [Staggered]. Fire 1 round. On hit, double damage and apply 2 Force stacks. Target makes a Body save or falls prone. |
| 5 | Last Round (Capstone) | 2 Actions, 15 Mana | Requires [Staggered] and Last Words streak active (all prior shots this cylinder hit). Fire the final round. Ignores all Physical DR, deals triple weapon damage, and triggers Shattered. Once per long rest. |

##### Revolver Weapon Augments (Last Words)

Passive. Once learned, these apply to ALL Revolver Techniques. Each adds its Mana cost to every Revolver Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Hair-Trigger Tension | Fan the Hammer fires 4 rounds instead of 3. | +1 |
| 2 | Gambler's Eye | Roulette's correct call bonus increases to +1d8. | +2 |
| 3 | Quick Reload | Reload costs a Free Action if you have 2+ Actions remaining. | +1 |
| 4 | Steel Streak | Fan the Hammer shots each count individually toward the Last Words streak. | +2 |
| 5 | One in the Chamber | After triggering Last Words, immediately load 1 free round before reloading. | +3 |

#### Rifle (Standard, Firearms) — 9 Techniques

**Unique Mechanic: Ammo Switch.** The rifle carries two ammo types. Standard Rounds apply Bleed on hit. Penetrating Rounds apply Force on hit. Switching active ammo type costs 1 Action and commits all remaining shots to the new type until you switch again or reload.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Aimed Shot | 1 Action | Fire 1 round. Apply 1 stack of the active ammo type's condition on hit. |
| 1 | Take The Shot | 1 Action | Fire a 2-round burst. Each hit applies 1 condition stack (active ammo type). Activate Precision Mode as part of this action: fire 3 rounds per burst instead, each hit applies 2 stacks, and you gain 1 stack of the active condition yourself. |
| 2 | Game Over Man | 1 Action, 3 Mana | Fire 5 rounds at one target. Each hit applies 2 Bleed stacks regardless of active ammo. Grants access to Suppressing Fire on your next Action this turn. |
| 2 | Penetrating Burst | 1 Action, 3 Mana | Switch to Penetrating Rounds and fire 2 rounds. Each hit ignores half Physical DR (rounded down) and applies 2 Force stacks. |
| 3 | Suppressing Fire | 1 Action, 5 Mana | Requires Game Over Man used this turn or 5+ rounds remaining. Empty the remaining magazine in a 15 ft horizontal arc. All creatures in the arc make a Body save vs. your DC. Fail: full damage + Frightened + 2 Force stacks. Success: half damage + 1 Force stack. You gain 2 Bleed stacks. |
| 3 | Overwatch | Reaction, 5 Mana | When an enemy moves within range, fire 1 round. On hit, their movement ends and they gain 2 stacks of the active condition. |
| 4 | Panic Burst | 2 Actions, 8 Mana | Fire 5 rounds distributed across up to 3 targets. Each hit applies Frightened and 2 condition stacks (active ammo type). |
| 4 | Scope In | Free Action, 8 Mana | Double effective range until end of your turn. Your next shot ignores cover bonuses and has Advantage. |
| 5 | Going Out Shooting (Capstone) | 2 Actions, 15 Mana | Requires [Shredded] or [Staggered]. Fire the remaining magazine at up to 3 targets (distribute shots freely). Each hit deals full weapon damage + 3 condition stacks (active ammo type). If any target reaches Exsanguination or Shattered, immediately reload as a free action. Once per long rest. |

##### Rifle Weapon Augments (Ammo Switch)

Passive. Once learned, these apply to ALL Rifle Techniques. Each adds its Mana cost to every Rifle Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Fast Switch | Switching ammo type is now a Free Action. | +1 |
| 2 | Hollow Point | Standard Round hits apply 1 additional Bleed stack. | +2 |
| 3 | Armor Piercer | Penetrating Round hits ignore 1 additional point of Physical DR. | +1 |
| 4 | Rapid Reload | After Suppressing Fire empties the magazine, reload immediately as a Free Action. | +2 |
| 5 | Terminal Velocity | When a shot kills a target with active condition stacks, transfer 2 of those stacks to one adjacent enemy. | +3 |

#### Shotgun (Standard, Firearms) — 9 Techniques

**Unique Mechanic: Two Modes.** Switch freely between Hip Fire Mode (15 ft cone — all targets make a Body save, 1 Force stack on fail) and ADS Mode (direct fire, 10 ft range — can use Hasta la Vista and Flesh Hook). Switching is a Free Action. Point-blank shots at 5 ft apply 2 Force stacks instead of 1 and deal +1d6 bonus damage in either mode.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Buckshot | 1 Action | ADS Mode. Fire at one target. Apply 1 Force stack on hit. At point blank (5 ft): apply 2 Force stacks and deal +1d6 damage. |
| 1 | Flesh Hook | 1 Action | ADS Mode only. Launch a barbed hook at a creature within 20 ft. Roll vs. target AC. On hit, you are pulled toward the target. This movement does not provoke opportunity attacks and does not count against your movement. |
| 2 | Hasta la Vista | 1 Action, 3 Mana | ADS Mode only. Fire both barrels at one target within 5 ft. Single attack roll. On hit: deal 2d10 bonus damage and push 10 ft. Target makes a Body save vs. your DC or falls prone. You take half the damage rolled. You make a Body save vs. your own DC or fall prone. |
| 2 | Hip Fire Blast | 1 Action, 3 Mana | Hip Fire Mode. All creatures in a 15 ft cone make a Body save vs. your DC (8 + Body modifier). Fail: full damage + 1 Force stack. Success: half damage. Cannot use Hasta la Vista in this mode. |
| 3 | Close Quarter Press | 1 Action, 5 Mana | ADS Mode. Move up to 10 ft and fire at a target within 5 ft of your destination. Apply 2 Force stacks. Target makes a Body save or falls prone. This movement does not provoke opportunity attacks. |
| 3 | Spread Panic | 1 Action, 5 Mana | Hip Fire Mode. Fire in a 15 ft cone. All targets that fail the Body save also become Frightened until end of your next turn. Force stacks apply as normal. |
| 4 | Double Barrel Fury | 1 Action, 8 Mana | Requires [Staggered]. ADS Mode. Fire both barrels at one target. Double weapon damage. Apply 3 Force stacks. Target makes a Body save or falls prone and loses their next Reaction. |
| 4 | Breach and Clear | 2 Actions, 8 Mana | Move through a doorway, barrier, or adjacent space occupied by an enemy. Fire as part of the move. All targets adjacent to the breach point make a Body save. Fail: full damage + 2 Force stacks + knocked prone. Success: half damage. |
| 5 | Buckshot Apocalypse (Capstone) | 2 Actions, 15 Mana | Requires [Staggered]. Hip Fire Mode at maximum output. All enemies in a 20 ft cone make a Body save. Fail: triple weapon damage + 4 Force stacks + prone. Success: full weapon damage + 2 Force stacks. Any target already at 5 Force triggers Staggered. Once per long rest. |

##### Shotgun Weapon Augments (Two Modes)

Passive. Once learned, these apply to ALL Shotgun Techniques. Each adds its Mana cost to every Shotgun Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Point-Blank Master | Point-blank bonus damage increases to +1d8. | +1 |
| 2 | Recoil Absorber | After using Hasta la Vista, you do not make a save to avoid falling prone. | +2 |
| 3 | Wide Choke | Hip Fire cone expands to 20 ft. | +1 |
| 4 | Slug Round | Once per combat, fire a single slug. On hit: ignore all Physical DR and deal +1d10 damage. Apply 2 Force stacks. | +2 |
| 5 | Last Shell | When you have exactly 1 round remaining, it automatically deals maximum damage and applies 3 Force stacks. | +3 |

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