# Solus System Book

## Introduction and Design Goals

Solus is a game of heroic gritty realism. Your character can become legendary, but the system makes you earn that power through risk. The world does not grow safer as you improve. Threats keep pace, and victory stays costly.

The system lets you define a character through the skills, magic, and weapons you choose. You can build for optimization or build to concept. The rules test both the same way. When you ask whether a character can do something, the system answers through shared mechanics instead of handing that answer to GM judgment alone.

Those shared mechanics apply across spells, weapons, and influence. The game uses one rules language for action resolution, whether you are playing a character or running the table. The same approach also supports play with or without a GM.

## Core Mechanics

Roll dice to resolve anything that might fail.

### The Base Roll

Roll two ten-sided dice (2d10) and add them together. Add a modifier from your character sheet. That total is your result.

> **Example:** You roll a 6 and a 4. Your modifier is +3. Your result is 13.

Read 2d10 as a sum. A 10 and a 4 is 14, not 104. These are not percentile dice.

The GM names a target number. Meet or beat it to succeed.

### When to Roll

Roll only when the outcome is uncertain. If a task is routine for your character, describe the success without rolling. If a task is beyond them, describe the failure. Roll when the answer could go either way.

### Critical Results

Two 10s is a critical success. The effect hits at its best outcome.

Two 1s is a critical failure. The effect misfires or backfires.

Criticals apply to any 2d10 roll unless a specific rule says otherwise.

### The Two Roll Types

Every Solus roll is one of two types. Both share the 2d10 base. They differ in the modifier you add and the target you compare against.

#### Combat Roll

Use this when you attack a target with a weapon or a spell.

- **Roll:** `2d10 + Body` (for physical/martial attacks) or `2d10 + Magic` (for magical attacks)
- **Target:** the defender's Physical AC (for physical attacks) or Magical AC (for magical attacks)
- **Result:** meet or beat the AC to hit, then apply damage (see Combat)

Physical AC = Physical DR + Body. Magical AC = Magic DR + Magic. See Equipment, Armor, and Weapons for the full AC and DR rules.

> **Example:** You swing a sword at a guard. Your Body is +4, so you roll `2d10 + 4`. The guard wears medium armor (Physical DR 3) and has Body +1, so their Physical AC is 4. You roll 9, total 13. You beat 4 and hit. You roll damage, then the guard's Physical DR (3) reduces the damage dealt.

#### Skill Check

Use this when your character tries something uncertain that is not a combat attack.

- **Roll:** `2d10 + Skill Modifier`
- **Target:** a Difficulty Class (DC) set by the GM
- **Result:** read on the Degree of 5 scale (see Running the Game)

Your skill modifier comes from two attributes. The primary is fixed per skill. The secondary is one of two listed options, picked at character creation. The pick stays fixed. See Attributes and Skills for the list.

> **Example:** The GM sets a DC of 10 to pick a lock. Your Stealth modifier is +4. You roll 8, total 12. You beat the DC by 2 and open the lock. If you had rolled 14 for a total of 18, you would beat the DC by 8 and earn a Degree of 5 bonus on top of the success.

## Character Creation

At character creation, establish the parts of your character that stay fixed and mark the parts that can change in play.

### Step 1: Build Your Concept

Choose the kind of character you want to play. Solus supports martial, magical, social, and hybrid approaches through the same core rules.

### Step 2: Distribute Ability Scores

Your five ability scores use modifiers from `-5` to `+5`.

You have 5 points to spend. Negative modifiers refund points. You must spend all 5 points. No points can remain unspent after assigning stats.

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

Record your race first. Your race sets your base movement speed and character size, and gives you racial bonuses including traits such as dark vision or movement bonuses.

The available races are:

1. Elves
2. Dwarves
3. Orcs
4. Gnomes
5. Constructs
6. Half-Breeds
7. Humans

TODO: define racial traits for each race (speed, size, unique mechanical trait). Jacob has also floated a custom race option where players select from preset racial trait lists, which could become the primary race-creation system.

### Step 4: Choose Your Background

Background determines starting health and mana behavior, but it does not restrict what skills, spells, weapons, or armor you can use.

- Casters start at 100 HP and 100/15 mana.
- Martials start at 120 HP and 30/3 mana.
- Hybrids start at 110 HP and 70/10 mana.

TODO: confirm Hybrid mana. Jacob believes 70/10 is correct; if 75/10 appears more often in playtest sheets, that is the final number.

### Step 5: Choose Your Skills

Record your skill choices and their secondary attribute options.

Skills work like Skill Gems in Path of Exile 2: they are the active abilities your character uses (attacks, spells, buffs, debuffs). Support Skills socket into your Skills and augment them (reduced cooldown, extended range, changed shape, and more). Support Skills are what make two characters who share the same base Skill play differently.

TODO: define when Support Skill slots first become available and the full Support Skill list.

### Step 6: Record Fixed And Changeable Traits

Solus has no character levels. Your skills grow through play (via XP or usage), not through leveling up.

The following parts of a character are fixed at creation:

- Race
- Racial bonuses
- Ability scores
- Base movement speed
- Background
- Character name
- Max health pool
- Max mana pool
- Character size

The following parts can change between sessions or through play:

- Skills
- Support Skills
- Masteries
- Weapons
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

### Step 7: Choose Equipment

Choose weapons, armor, and gear that fit the build.

TODO: add starting equipment rules.

## Attributes and Skills

Characters have five attributes. Each one governs a different part of action resolution.

### Body

Body represents all physicality, whether strength or dexterity. Body is used for physical and martial attacks, physical defense, and contributes to Physical AC. Body is also one of the two Initiative options.

### Mind

Mind represents intellect and emotional state. It covers knowledge, perception, awareness, and mental resilience against non-magical effects. Mind is the combined equivalent of Wisdom and Intelligence in other systems.

### Social

Social represents how you come across to others, for good or ill. It governs persuasion, deception, intimidation, performance, leadership, and social defense. Social has no magical tie-in.

### Magic

Magic represents magical aptitude. All spellcasting uses Magic, regardless of spell category. The type of magic you specialize in is handled through Masteries, not through the Magic attribute itself. Magic contributes to Magical AC and is one of the two Initiative options.

### Sanity

Sanity represents mental fortitude. A lower Sanity does not make you unstable; it reveals more of the world's hidden truths, letting you perceive what others cannot. Sanity governs fear saves, stress tolerance, mental break thresholds, and is the attribute tied to any Madness system.

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

## Equipment, Armor, and Weapons

Armor splits protection between physical damage and magic damage. Each armor tier has a Physical DR and a Magic DR. These feed into two separate Armor Class values:

- **Physical AC** = Physical DR + Body
- **Magical AC** = Magic DR + Magic

AC is the target number an attacker must meet or beat to deal damage. DR is fixed per armor tier and reduces damage after a hit lands. AC and DR are separate: AC determines whether you get hit, DR determines how much damage gets through.

The maximum DR per damage type is 4 (Enchanted armor gets 3/3 for a total of 6). The maximum possible AC is 9 (DR 4 + stat modifier +5).

> **Example:** You wear Light Armor (Physical DR 1, Magic DR 3). Your Body is +3 and your Magic is +1. Your Physical AC is 4 (1 + 3). Your Magical AC is 4 (3 + 1). An attacker swinging a sword must beat 4 to hit you physically. A caster throwing a spell must beat 4 to hit you magically. If either hits, the relevant DR (1 or 3) reduces the damage dealt.

| Armor Tier | Physical DR | Magic DR | Total DR |
| --- | --- | --- | --- |
| Cloth | 0 | 4 | 4 |
| Light | 1 | 3 | 4 |
| Medium | 3 | 1 | 4 |
| Heavy | 4 | 0 | 4 |
| Enchanted | 3 | 3 | 6 |

Magic DR reduces damage from elemental status effects, but it does not stop those effects from applying or escalating. A target can still build stacks and reach a higher condition even while armor cuts the damage from those stacks.

Weapons are organized by category, tag set, and damage format. Base weapon damage uses Body across the current weapon tables, including ranged weapons and firearms.

| Category | Example Weapons | Core Damage |
| --- | --- | --- |
| Light Melee | Dagger, Claw Gauntlet, Short Sword, Chain Blade, Bare Hands | 1d4 + Body to 1d6 + Body |
| Medium Melee | Rapier, Katana, Curved Sword | 1d8 + Body |
| Heavy Melee | Greatsword, Greathammer, Great Axe | 1d8 + Body |
| Reach Weapons | Halberd, Scythe, Whip | 1d6 + Body to 1d10 + Body |
| Ranged / Thrown | Bow, Bomb Flask | 1d6 + Body to 1d8 + Body |
| Firearms | Revolver, Rifle, Shotgun, Sniper Rifle | 1d8 + Body to 1d12 + Body |

Weapon tags define how a weapon behaves in play. Current tags include combinations such as Melee, Light, Medium, Heavy, Reach, Thrown, Splash, One-Handed, Two-Handed, Ranged, Firearm, and Unarmed. Many weapons also carry custom traits that apply stacks, move targets, alter terrain, or unlock finishers once a target reaches the right setup.

TODO: insert the full weapon-by-weapon trait list after the equipment chapter is locked.

TODO: confirm whether shields are missing from the equipment list and need to be added.

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

Each spell parameter has a mana cost (shown in parentheses) and falls into an action cost column based on its position in the spell framework. The framework has four columns:

- **1 Action:** the parameter's lowest cost values
- **2 Actions:** the parameter's mid-range values
- **3 Actions:** the parameter's highest standard values
- **4+ Actions or Ritual:** extreme values (Sight range, Permanent duration, etc.)

A parameter's position in the table determines both its action cost and its mana cost. The values below show mana cost in parentheses.

| Parameter | 1 Action | 2 Actions | 3 Actions | 4+ Actions / Ritual |
| --- | --- | --- | --- | --- |
| Range* | Self-25 ft. (1) | 30-60 ft. (2) | 65-120 ft. (3) | 125-200 ft. (4), Sight (5), Global (6) |
| Size* | 5-15 ft. (1) | 20-30 ft. (2) | 35-60 ft. (3) | |
| Shape | point or none (1) | sphere/cube/line/wall/cylinder (2) | freeform or custom (3) | |
| Duration | Instant (1) | Round (2) | Minute (3) | Hours (4), Permanent (5) |
| Target Count* | Single (1) | Multi 2+ (2) | AOE (3) | |
| Accuracy Type* | Attack Roll (1) | Save (1) | Auto-Hit (4) | |
| Effect Tier | T1 (3) | T2 (6) | T3 (12) | T4 (17) |

Parameters marked with * contribute to spell damage.

Duration applies to spell effects as well as casting time. If a spell effect lasts longer than the casting time chosen, you pay the higher duration's mana cost. Example: casting at Instant speed but with a Minute-long effect costs the Minute mana price.

Effect Tier covers the mana cost of applying Tags at different tiers. Multiple tags of the same tier stack cost: two T2 Tags cost 12 mana total (6 + 6).

### Damage Dice

Three parameters contribute damage dice: Range, Target Count, and Size. Each contributes one die. Die size is determined by the parameter's mana cost:

| Mana Cost | Die |
| --- | --- |
| +1 | d6 |
| +2 | d8 |
| +3 | d10 |
| +5 | d12 |

Die size is capped by the parameter's mana cost. If a parameter maxes at +3 mana, its damage die caps at d10.

Attack Roll accuracy type grants one additional damage die (d6 to d12), with mana cost increasing with die size.

Multi targets: 2 targets = +2 mana, 3 targets = +3 mana, 4 targets = +4 mana (maximum 4 targets).

The caster's casting stat modifier (-5 to +5) always applies as a flat damage bonus.

> **Example:** Range Self-15 ft. +1 (d6), Target Count Single +1 (d6), Size 20-30 ft. +2 (d8), Attack Roll +5 (d12), Stat Modifier +5. Total damage = 1d6 + 1d6 + 1d8 + 1d12 + 5.

### Known Mana Cost Anchors

| Type | Mana |
| --- | --- |
| Minimum spell cost | 8 |
| Maximum 1-action spell | 44 |
| Maximum 3-action spell | 132 |

These anchors are the basis for max mana pools and regeneration rates per background.

### Main and Sub Categories

Magic uses a main and sub category model. Players choose their main and sub lists at character build. Main category spells pay normal cost (x1). Sub category spells pay double cost (x2).

TODO: confirm whether the Main/Sub category system adds enough value to keep, or whether it should be cut to reduce cognitive load.

### Tags

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
- cast a spell
- move
- drink a potion
- interact with an object
- make a skill check
- use a skill

Some spells and skills take more than one action. You can spend those actions on the same turn or across multiple turns unless something interrupts you.

### Reactions

Each character gets 1 reaction per round. That reaction refreshes at the start of that character's turn. Reactions can include skills, counterspells, parries, opportunity attacks, and other triggers written on abilities or equipment. Reactions may interrupt an action unless the effect says otherwise.

### Movement

Each movement action lets you move up to your full movement speed. You can split movement across actions unless a condition prevents it. If you leave an enemy's reach, that enemy may trigger a reaction if one is available. In most cases, that reaction is an opportunity attack.

### Damage And Defense

Armor damage reduction applies after a hit lands. Split physical and magical protection matter both for direct attacks and for ongoing elemental stack damage.

If a character reaches 0 HP, that character becomes incapacitated and follows the injury or death rules.

TODO: add the full attack, hit, and damage-resolution sequence (roll vs. Physical AC or Magical AC, apply DR, apply tags/stacks).

## Conditions, Injuries, and Death

Many conditions begin as stacks.

- A hit applies 1 stack of the relevant type.
- Each stack deals +1 damage per round, equal to the number of active stacks of that type.
- Each stack lasts 2 full rounds from the turn it was applied.
- Reapplying a stack resets that stack's duration.
- Each stack type tracks its own current count, damage per round, and decay.
- All stacks cap at 5. No exceptions.
- Ongoing status effects resolve at the start of the affected creature's turn unless a rule says otherwise.
- Stack damage triggers when applied and again at the start of the target's turn.

Burn and Chilled oppose each other. When one would be gained, it removes one stack of the other on a 1:1 basis. Magic DR reduces damage from elemental stacks, but it does not block the stack itself or stop escalation into a higher condition.

Tags are system-wide mechanical identifiers. They are not limited to spells. Weapons, potions, creature abilities, terrain, and hazards can all apply tags and trigger conditions.

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

**PLAYTEST DRAFT (NOT FINAL):** Madness has a working threshold rule that is still under development. The current version draws inspiration from Elden Ring's Scarlet Rot and Madness mechanics and should not be treated as locked or integrated into other systems until a final version is approved.

At 100 Madness, a creature must use its Action to attack a random nearby target, cannot target itself, lasts `1d4 + 1` rounds in that state, and takes 1 psychic damage at the start of each turn. The condition can end early if time expires, a calming charm hits, an ally succeeds on the stated check against DC 15, magic removes Madness, or the target takes `5 + Vital` damage in one hit.

TODO: redesign Madness system for final version.

TODO: several key stack logic consistency rules are missing from this section. These need to be surfaced in conversation with Jacob before the Conditions chapter can be finalized.

### Dying

**PLAYTEST DRAFT (NOT FINAL):** The following dying system is a concept under discussion. An alternative proposal exists and both are on the table for further development.

When a character starts their turn at 0 HP, that character enters the dying state. Place a `d10` death counter on 10.

While a character is dying, that character can still act. Movement is halved, and attack rolls are at disadvantage.

Resolve the death counter across the dying character's 3 actions each turn.

- If the character does nothing with an action, reduce the counter by 1.
- If the character uses an action, reduce the counter by 2.

If a character does nothing for the full turn, the counter drops from 10 to 7 by the end of that turn. If a character uses 1 action and leaves the other 2 unused, the counter drops from 10 to 6 by the end of that turn.

When the counter reaches 0, the character dies.

This gives a dying character about 3 rounds to receive help if they do nothing and wait. Acting while dying shortens that window.

If the character receives healing that restores them to at least 1 HP, remove the dying state and reset the death counter.

### Playtest Variant: Repeated Knockdowns

**PLAYTEST DRAFT (NOT FINAL):** This variant is under discussion alongside the base dying system.

Use this variant if you want dropping to 0 HP multiple times in quick succession to be more punishing.

If a character leaves the dying state through healing and drops to 0 HP again before 1 full round passes, the death counter resumes at its previous value instead of resetting to 10.

If the character stays above 0 HP for 1 full round, the death counter fully resets.

TODO: add a consolidated condition glossary with stack thresholds and removal rules.

## NPCs, Enemies, and Encounters

All NPCs use the same action economy, equipment, skill system, and spell system as player characters. NPCs are competent. The only differences between NPC ranks are stat modifiers, HP, and mana pools. Minions and Bosses are exceptions to this baseline in specific ways noted below.

NPCs sit inside the core play loop. They can cause problems in the world, keep those problems in motion, appear as consequences for player action, or hand out rewards after the group resolves a situation. Allies follow the same framework as enemies, but they help the characters instead of hindering them.

Each NPC rank also has martial, caster, and hybrid variants. The stat numbers define the rank; the background type determines the NPC's capability profile.

| Rank | HP | Mana | Armor | Stat Modifiers | Use in Play |
| --- | --- | --- | --- | --- | --- |
| Minion | 1 to 5 | 30/3 | None, Phys 0, Magi 0 | Body +0, Mind +0, Social +0, Magic +0, Sanity +0 | Use Minions for swarms and hordes. One Minion is weak. A crowd of them becomes dangerous. |
| Regular | 75 | 30/3 | None, Phys 1, Magi 1 | Body +1, Mind +1, Social +1, Magic +1, Sanity +1 | Use Regular NPCs for townsfolk, shopkeepers, low-ranked guards, and other ordinary people. |
| Enemy or Ally | 100 | 100/15 | Medium, Phys 7, Magi -2 | Body +4, Mind +1, Social +3, Magic -3, Sanity +0 | Use this rank for the most common competent foe or helper. These NPCs are on par with player characters in capability. |
| Mini Boss | 120 | 100/15 | Heavy, Phys 9, Magi 0 | Body +5, Mind +4, Social -3, Magic +0, Sanity -2 | Use a Mini Boss for a foe who stands above a player character in health, gear, and skill investment. |
| Boss | 175 | 100/20 | Enchanted, Phys 8, Magi 8 | Body +5, Mind +3, Social +0, Magic +5, Sanity -5 | Use a Boss for a major threat that demands planning and strong tactics. |

Minions break the normal NPC baseline on the low end. They have +0 in every stat and die fast (1-5 HP). They use the same equipment and spells as player characters. With +0 modifiers their odds are lower, but the danger is real. A crowd of Minions is lethal.

Regular NPCs represent average people. They are sturdier than Minions, but they do not stand on equal footing with player characters.

Enemy and Ally NPCs are the standard challenge template. They are on par with player characters: same action economy, same equipment access, same spell system. Your enemies are competent and can kill you as fast as you can kill them.

Mini Bosses push above that line. Give them stronger gear, higher durability, and deeper skill investment than a standard Enemy or Ally.

Bosses break the normal point-buy expectation. A Boss gets one extra +5 beyond the normal limit. That extra stat increase turns a dangerous NPC into a major threat without changing the rest of the framework.

TODO: add encounter-building procedure, XP awards by enemy rank, and guidance for mixing ranks in one encounter.

## Advancement, Mastery, and Between-Session Play

Character advancement runs through skills. You earn XP by progressing through and interacting with the world in exploration, combat, and conversation. Each enemy type, from Minion through Boss, awards a set amount of XP. Exploration encounters also award XP when the group engages with them. Social and conversation encounters award XP on both success and failure.

You spend XP after each session.

You use XP to buy new skills and to raise the skills you already have. Each skill has an initial cost to acquire it. Each skill then advances through thresholds from Rank 1 to Rank 10. Costs rise as the rank rises, and that increase is exponential. If you buy a new skill, it starts at Rank 1 and advances through the normal rank track from there.

Support Skill Slots open as a skill improves. A Rank 1 skill starts with 1 Support Skill Slot. Every other rank after that, starting at Rank 2, opens another slot, to a maximum of 5 slots per skill. As you raise a skill's rank, you open more room to augment that skill with support options.

Mastery opens from total XP, not from a single skill. After your character reaches certain total XP thresholds, you unlock Mastery Skills and gain a set number of Mastery points to spend on them. Mastery points are finite, and you have fewer Mastery points than total Mastery Skills.

**DESIGN NOTE (IN DEVELOPMENT):** Masteries currently read like classes, but that is not the intent. They should function in the same manner as Skills. This system may be restructured or folded entirely into regular Skills in a future revision. Do not treat Masteries as a locked system.

You can own as many skills as you can afford, but you can only keep 10 skills active at one time.

Between sessions, you can update the parts of the character that the rules mark as changeable. You can gain or swap skills with GM confirmation. You can change Masteries the same way you change normal skills. You can also change weapons within your inventory, update equipment, spend or gain money and resources, and record new languages as your character learns them.

TODO: add the full XP cost tables, the XP thresholds for Mastery, and the exact XP awards for combat, exploration, and conversation encounters.

## Running the Game

Run NPCs from their stat blocks and use the same action economy, equipment rules, skill rules, and spell rules that player characters use. Pick an NPC rank that matches the role you want in the scene, then build the NPC from that frame.

Use NPCs as part of the world, not just as combat pieces. An NPC can create a problem, keep a problem active, show up as a consequence of player action, or deliver a reward after the group resolves a situation. That same framework lets you place allies and enemies inside combat, exploration, and conversation scenes without changing systems.

Keep a clear split between what the players control and what the GM or the system controls.

- Players control their skills, Mastery Skills, equipment, weapons, spells, money, resources, and languages.
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