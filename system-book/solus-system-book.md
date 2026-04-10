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

Augments modify Techniques. You socket them into Augment Slots. Two layers exist.

| Layer | Scope |
|---|---|
| Universal Augments | Any Technique, any weapon |
| Category Augments | Only Techniques from that weapon category |

No weapon-specific Augments exist. Augments add Mana cost to the Technique they modify. Stacking multiple Augments on one Technique adds their Mana costs together.

### Universal Techniques

Every character has access to these four Techniques regardless of weapon or Mastery Rank.

**Brace.** Plant your feet. Until your next turn, gain +2 AC. You cannot move. Free Action to enter; costs your movement for the turn.

**Shove.** Push an adjacent creature 1 space. Roll `2d10 + Body` vs. target's `2d10 + Body`. Costs 1 Action.

**Taunt.** Force a target within 6 spaces to roll `2d10 + Social` vs. your `2d10 + Social`. On failure, the target must attack you on their next turn if able. Costs 1 Action.

**Second Wind.** Recover `1d10 + Body modifier` HP. Costs 1 Action. Once per combat. Cannot use while Dying.

### Universal Augments

Sixteen Augments are available to all characters. The first twelve work with any Technique on any weapon. The last four (Spellblade Augments) bridge weapon attacks and spellcasting.

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

Weapons are grouped into seven categories. Each category shares a fighting style, a set of Category Techniques, and Category Augments.

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

#### Light Melee Category Augments

| Augment | Effect | Mana Cost Increase |
|---|---|---|
| Feint | Force target to take the hit or spend their Reaction to dodge. If dodged, you gain advantage on your next attack. | +2 |
| Poisoned Edge | On hit, apply 1 Venom stack. | +2 |
| Twin Strike | If dual-wielding Light Melee weapons, hit with both weapons. Second weapon deals half damage. | +2 |

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

#### Bare Hands (Simple, Light Melee)

TODO: full Technique list. Condition signature: Force. Unique mechanic: Burn Force stacks on yourself to boost unarmed strikes. Grapple pin combos with Force tick damage.

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

#### Short Sword (Standard, Light Melee)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: Guaranteed Bleed on every hit (1 stack, scaling to 2 at Rank 3). No variance. Consistent pressure.

#### Claw Gauntlet (Standard, Light Melee)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: Paired property forces dual-wield. Each Flurry lands twice. Fastest path to Shredded (5 Bleed stacks) in the game.

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

#### Medium Melee Category Augments

| Augment | Effect | Mana Cost Increase |
|---|---|---|
| Precision | +2 to hit, -1 die size on damage. Apply a condition based on body part targeted: arm = Disarm, leg = Slow, head = Stun. | +2 |
| Shield Synergy | +1 AC until end of turn if you have a Shield in your off-hand. | +1 |
| Flowing Form | After using a Technique, enter or switch stances as a free action. | +1 |

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

#### Curved Sword (Standard, Medium Melee)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: Sweeping Bleed hits two adjacent targets per attack. Best group-Bleed spreader in Medium Melee.

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

#### Mace (Standard, Medium Melee)

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

#### Heavy Melee Category Augments

| Augment | Effect | Mana Cost Increase |
|---|---|---|
| Follow-Through | On kill, gain +1 Action this turn. | +3 |
| Sundering | On hit, reduce target's Physical DR by 1 until end of combat. Stacks. | +2 |
| Earthquake | All creatures within 1 space of target roll `2d10 + Body` vs. DC 12 or fall prone. | +3 |

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

#### Great Axe (Standard, Heavy Melee)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: Bleed stacks deal double tick damage (+2 per stack instead of +1). At Shredded (5 stacks), attacks ignore all Physical DR. Capstone: Exsanguination (T4).

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

#### Reach Category Augments

| Augment | Effect | Mana Cost Increase |
|---|---|---|
| Extended Reach | +1 space range for Reach weapons (+2 total from default). | +2 |
| Trip | On hit, target rolls `2d10 + Body` vs. your attack roll or falls prone. | +2 |
| Brace | If you haven't moved this turn, +1d6 damage vs. enemies who moved toward you. | +1 |

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

#### Halberd (Standard, Reach)

TODO: full Technique list. Condition signature: Force/Bleed. Unique mechanic: Sweep splits conditions. Primary target takes Force, secondary targets take Bleed. Dual-condition zone controller.

#### Scythe (Complex, Reach)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: Purge stacks from allies as a Technique. On kill, transfer remaining stacks to an adjacent enemy. Harvest-chain combos. Capstone: Exsanguination (T4).

#### Whip (Standard, Reach)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: 3-space reach. Apply Bleed at extreme range. Rank 3 Technique pulls Bleeding targets toward you. Control + punishment.

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

#### Ranged Category Augments

| Augment | Effect | Mana Cost Increase |
|---|---|---|
| Arcing | Ignore half-cover. | +1 |
| Piercing Shot | Projectile passes through the first target. Second target behind takes half damage. | +2 |
| Scatter | On hit, 1d4 splash damage to all adjacent to target. | +2 |

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

#### Crossbow (Standard, Ranged)

TODO: full Technique list. Condition signature: Bleed. Unique mechanic: Deep Penetration extends Pierce to Bleed ticks. High single-shot damage offset by Loading. Higher ranks unlock faster reload Techniques.

#### Hand Crossbow (Standard, Ranged)

TODO: full Technique list. Condition signature: Poison. Unique mechanic: Every hit applies 1 Poison stack. Rapid-fire rushes Venomous (5 Poison). Rank 3: 2 Poison per hit. Capstone: Lethal Dose (T4, Neurotoxin).

#### Bomb Flask (Standard, Ranged)

TODO: full Technique list. Condition signature: Varies by flask type (Burn, Acid, Chill). Unique mechanic: AoE condition application. Consumable. Must be crafted or purchased. Area denial and group condition stacking.

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

#### Firearms Category Augments

| Augment | Effect | Mana Cost Increase |
|---|---|---|
| Rapid Reload | Reload as a free action after using a Technique. | +2 |
| Hollow Point | +1d6 damage. Loses Pierce property for this attack. | +2 |
| Ricochet | On a miss, projectile bounces to a random adjacent enemy. Re-roll the attack at -4. | +2 |

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

- **Mastery:** Rapier 4, Shield 2.
- **Role:** Counter-fighting tank.
- **Core loop:** En Garde stance → Parry incoming attacks → generate Openings → Compound Riposte for bonus damage. Shield for Cover Ally and emergency Raise Shield.
- **Key Techniques:** En Garde, Parry (Medium Melee), Compound Riposte, Fleche, Tempo Rubato, Shield Bash, Cover Ally.
- **Augments:** Precision (targeted conditions on ripostes), Shield Synergy (+1 AC), Siphon (sustain HP through ripostes).
- **Condition path:** Bleed through Rapier → Shredded at 5 stacks. Openings accelerate Bleed application.

#### The Berserker (Great Axe)

- **Mastery:** Great Axe 5.
- **Role:** All offense. Rush in, AoE, execute.
- **Core loop:** Charge in → Power Attack → Cleave on kills → Executioner to finish wounded targets. Double Bleed ticks pressure everything.
- **Key Techniques:** Power Attack, Cleave, Whirlwind, Executioner, Staggering Blow.
- **Augments:** Follow-Through (kill = +1 Action), Sundering (strip DR), Momentum (+1d6 after moving).
- **Condition path:** Bleed at double tick rate → Shredded → Hemorrhage (T3) → Exsanguination (T4 capstone, once per long rest).

#### The Sentinel (Spear + Shield)

- **Mastery:** Spear 3, Shield 3.
- **Role:** Pure tank and controller. Lock down movement, protect allies.
- **Core loop:** Sentinel (Reaction attacks on approach) → Impale to pin targets → Shield Wall with adjacent ally → Raise Shield for durability.
- **Key Techniques:** Sentinel, Sweep, Impale, Keep at Bay, Phalanx, Shield Bash, Raise Shield, Shield Wall.
- **Augments:** Trip (prone on hit), Brace (+1d6 vs. chargers), Shield Synergy (+1 AC).
- **Condition path:** Bleed through Spear. Impaled targets do not lose Bleed stacks to decay. Force through Shield Bash for Staggered.

#### The Hybrid (Staff + Spellcasting)

- **Mastery:** Staff 3. Background: Hybrid (110 HP, 70 Mana, 10 regen).
- **Role:** Gish condition accelerator.
- **Core loop:** Cast Burn/Chill spells → Staff attacks catalyze elemental stacks (extra ticks) → push to T2 escalation → Staff T3 enhancement Technique → T4 if fight goes long.
- **Key Techniques:** Staff weapon Techniques (TODO), Sentinel, Sweep. Spells: Burn/Chill/Shock varieties.
- **Augments:** Arcane Infusion (+1d8 elemental after spell), Spell Strike (Touch spell + Staff attack), Mana Reave (sustain Mana through hits).
- **Condition path:** Spell stacks + Staff catalysis → Frozen (Chill T2) → Permafrost (T3, 12 Mana) → Absolute Zero (T4 capstone, 17 Mana, once per long rest).

#### The Assassin (Dagger + Hand Crossbow)

- **Mastery:** Dagger 4, Hand Crossbow 3. Background: Hybrid or Martial.
- **Role:** Dual-condition poison and bleed specialist. Ambush predator.
- **Core loop:** Open at range with Hand Crossbow → apply Poison stacks (1 per hit, 2 at Rank 3) → close to melee → Dagger Flurry for Bleed + Poison → double escalation (Shredded + Venomous). Against bosses: Neurotoxin (T3) + Hemorrhage (T3) for layered pressure.
- **Key Techniques:** Quick Draw, Flurry, Assassinate, Hand Crossbow Techniques (TODO). Quick Shot for ranged Poison, Flurry for melee combo.
- **Augments:** Poisoned Edge (extra Venom stack), Feint (force hits through), Twin Strike (dual-wield bonus).
- **Condition path:** Poison at range → Venomous (T2) → Neurotoxin (T3, movement = 0). Bleed in melee → Shredded (T2) → Hemorrhage (T3). Against bosses: stack both T3s, then Lethal Dose (T4 capstone, once per long rest).

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
- **Augments.** Purchase Universal and Category Augments to socket into your prepared Techniques.

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