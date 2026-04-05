# Create Stack logic

- Apply 1 stack per hit.
- Each stack deals +1 damage per round, equal to the number of active stacks.
- Max 5 stacks total.
- Each stack lasts 2 full rounds from the turn it is applied.
- Reapplying a stack resets that stack’s duration to 2 rounds from the new turn.
- Track damage per round = 1 damage × current active stacks.
- Track each stack’s individual decay.
- Track when exactly 5 stacks are active at the same time.

- Two different stack types ([Burn] and [Chilled]). Only 1 can be applied per hit.
- A single hit applies either 1 stack of [Burn] or 1 stack of [Chilled] (never both).
- Each stack type has independent tracking.
- Each stack adds +1 damage per round, equal to the number of stacks of its type.
- Max 5 stacks per type.
- Each stack lasts 2 full rounds from the turn it is applied.
- Reapplying a stack of the same type resets that stack’s duration to 2 rounds.
- Track each stack type separately:
  - Current active stacks
  - Damage per round
  - Per-stack decay
  - Whether either has reached 5 stacks simultaneously

1. Set a DR cap total 4
Keeps design tight: each armor set gets a total DR budget.
Sample DR Budget Model:

| Armor Tier | Physical DR | Magic/ Elemental DR | Total DR |
| ---------- | ----------- | ------------------- | -------- |
| Cloth      | 0           | 4                   | 4        |
| Light      | 1           | 3                   | 4        |
| Medium     | 3           | 1                   | 4        |
| Heavy      | 4           | 0                   | 4        |
| Enchanted  | 3           | 3                   | 6        |

2. Elemental DR should reduce stack damage, NOT block the effect
This keeps status system balanced. Players still reach 5 stacks and trigger stage-2.

Avoids control effects like [Frozen], [Shocked], [Corroded] becoming useless vs armored enemies.

Elemental DR reduces the damage from elemental statuses, but not their application or escalation. A character with 4 Elemental DR takes 1 damage per [Burn] stack instead of 2, but still gains stacks and can become [Ignited].

Stack damage is triggered when applied and at the start of the targets turn, in this manner should they lose the stacks between application and the targets action there is still an active register of the damage

Ongoing status effects resolve at the start of the affected creature’s turn unless otherwise specified.

Some Stacks can remove other stacks thus reducing the total for either the overall stack number or a single stack or both. 
For example if you have 3 Stacks of [Burn] and 2 stacks of [Chilled] are applied you then remove 2 stacks of [Burn], thus resulting in 1 stack of [Burn] and 2 stacks of [Chilled]

Global Rule A — Environmental Persistence
- If a spell applies a Tag to terrain or an object, that effect persists for the spell’s duration.
    
- If no duration is specified, Tier 1 defaults to 2 rounds; Tier 2 defaults to 4 rounds.
    

Global Rule B — Tag-to-Stack Mapping
- If a Tag has a linked Status Stack (e.g., Fire → Burn), then applying the Tag applies that stack to the target or terrain.
    
- If applied to terrain, the terrain is considered ‘affected’ and triggers the same stack rules for anything interacting with it.

# Combat

Start combat by rolling initiative.
Initiative is a d10 roll + Body or Magic Player's choice (but should be based on their preferred fighting style)
Each round of combat is 3 seconds
The combat order is Highest to lowest, if 2 or more people roll the same number then you can chose to either determine who goes first by the highest Stat Modifier, Rolling a d10 with the highest determining who goes first, or going at the same time (this option is only applicable if the rolls are for Players or Allies, enemies will not go at the same time and one of the first two options must be taken)

In combat you have 3 Actions that you can take
You may use your Action to do several things with some requiring more than one action to accomplish.
Things you can do as an action are
	Attack via Weapon or Spell
	Movement
	Drink a potion
	Interact with an object
	Make a Skill Check
	Use a Skill

Actions may be repeated unless a specific ability, spell, or item states otherwise.

On your turn, you may take up to 3 actions in any order, resolving each action fully before taking the next.

Some spells and Skill require multiple actions. These actions may be taken on the same turn or across multiple turns unless interrupted.

Characters have 1 reaction  a round and will refresh at the start of their turn.
Different things can be used on a reaction and will be stated to do so, some examples are things like Skills, Counterspells, Parries, or Opportunity Attacks 

Each Movement action allows a character to move up to their Movement Speed.  Movement may be split across actions unless restricted by a condition.

Moving outside of melee range of an enemy will trigger a attack of Opportunity.

When a character reaches 0 HP, they are incapacitated and follow the rules for injury or death as defined elsewhere.

Reactions may interrupt an action unless the triggering effect states otherwise.

Characters have 1 reaction  a round and will refresh at the start of their turn.
Different things can be used on a reaction and will be stated to do so, some examples are things like Skills, Counterspells, Parries, or Opportunity Attacks 

Each Movement action allows a character to move up to their Movement Speed.  Movement may be split across actions unless restricted by a condition.

Moving outside of melee range of an enemy will trigger a attack of Opportunity.

Actions may be repeated unless a specific ability, spell, or item states otherwise.

On your turn, you may take up to 3 actions in any order, resolving each action fully before taking the next.

Some spells and Skill require multiple actions. These actions may be taken on the same turn or across multiple turns unless interrupted.

Leaving an enemy’s reach may trigger a reaction if that enemy has one available.


- Parry
    
- Counterspell
    
- Opportunity attack
    
- Defensive skill triggers

Each Movement action allows a character to move up to their Movement Speed.  Movement may be split across actions unless restricted by a condition.

Moving outside of melee range of an enemy will trigger a attack of Opportunity.

Actions may be repeated unless a specific ability, spell, or item states otherwise.

On your turn, you may take up to 3 actions in any order, resolving each action fully before taking the next.

Some spells and Skill require multiple actions. These actions may be taken on the same turn or across multiple turns unless interrupted.

Leaving an enemy’s reach may trigger a reaction if that enemy has one available.

- What happens at 0 HP
    
- Whether combat immediately ends for that character
    

When a character reaches 0 HP, they are incapacitated and follow the rules for injury or death as defined elsewhere.

On your turn, you may take up to 3 actions in any order, resolving each action fully before taking the next.

Some spells and Skill require multiple actions. These actions may be taken on the same turn or across multiple turns unless interrupted.

Leaving an enemy’s reach may trigger a reaction if that enemy has one available.

# Races

#### 1. ***Elves***


#### 2. ***Dwarves***


#### 3. ***Orcs***

Balkalesh-ra (“Great Tusk”)

Konon Milambak (“Tree Children”)

Nen Born (“Water Born”)

Zi Nodog (“Black Swamp”)

Aztar Gijak (“North Blood”)

Mal-zagh (“Mountain”)

Liga Tusk (“Small Tusk”)


#### 4. ***Gnomes***


#### 5. ***Constructs***


#### 6. ***Fey***

Fairy (Slòigh an t-Samhraidh / Slòigh a’ Gheamhraidh)

Leprechaun (Tall/Traditional vs. Short/Modern)

Fey Mara (Sea-Fey Umbrella: Selkies, Finfolk, Merrows)


#### 7. ***Beastkin***

Wolf / Dog Beastkin

Cat Beastkin

Fox Beastkin

Bird Beastkin


#### 8. ***Drakari***


#### 9. ***Half-Breeds***


#### 10. ***Humans***



# Create Masteries

Separate by background type give categories in each to choose from

1. Martial
	1. Warrior 
	2. Ordnance
	3. Shapeshifter
	4. Rage
	5. Stealth 
2. Caster
	1. Arcane 
	2. Divine
	3. Nature
	4. Eldritch 
3. Hybrid
	1. Take any 2 from the list
4. Accursed
	1. Vampire
	2. Lycan
	3. Undead
	4. Aberrant



# Backgrounds

These are chosen at character creation and cannot be changed once selected.
Background determines starting health and mana behavior, not what skills, spells, weapons, or armor a character may use.

- ***Casters***: They are meant to be the ones fully immersed in magic, picking this option allows players to have a larger mana pool at the cost of some health, but with this larger mana pool they will be able to cast more spells often and bigger than the others.

- ***Martials***: They are meant to be the front line fighters, picking this option gives players a larger health pool but at the cost of mana total and regen. With this it will provide a constant mana drain to use skills but at a lower cost, with this they have a way of being "in the zone" and a solid demonstration of a true Martial master.

- ***Hybrids***: They are the in-between of Casters and Martials, their health and mana is slightly higher than a Martials but the mana is still lower than a pure Caster. With this mix they are able to be on the front lines, using martial skills constant drain and and cast consistently as a caster, however neither the health nor mana is capable of fully replacing the other 2 as they can burn everything faster if not carefully managed.

# Max Health & Mana

- ***Casters*** (100 HP, 100/15): With the ever shifting mana costs this will make caster's mana feel like it chunks away dependent on the spell and it's magnitude. Their health is to reflect the inability to have prolonged fights at the front line without some form of outside help.

- ***Martials*** (120 HP, 30/3): With the lower mana cost the Skills themselves are at a lower mana cost but rather than chunks they have a constant "bleed" output once a Skill is activated. Their health is to reflect a front line fighters ability to stay in prolonged fights.

- ***Hybrids*** (110 HP, 70/10): With the mana in-between a Caster and Martial class they will be able to sustain the Martial class mana "bleed" while also being capable of a Caster's mana "chunk" while placing them in a situation to burn their mana faster if they aren't careful on their expenditure of mana. Their health is meant to sit in-between the Caster and the Martial giving them an option of either but never allowing them to fully sit in one position or the other.

# Weapons

Light Melee Weapons

| Name          | Category    | Tags                        | Damage Format |
| ------------- | ----------- | --------------------------- | ------------- |
| Dagger        | Light Melee | [Melee], [Light]            | 1d4 + Body    |
| Claw Gauntlet | Light Melee | [Melee], [Light]            | 1d4 + Body    |
| Short Sword   | Light Melee | [Melee], [Light]            | 1d6 + Body    |
| Chain Blade   | Light Melee | [Melee], [Light]            | 1d4 + Body    |
| Bare Hands    | Light Melee | [Melee], [Light], [Unarmed] | 1d4 + Body    |

Medium Melee Weapons

| Name         | Category     | Tags              | Damage Format |
| ------------ | ------------ | ----------------- | ------------- |
| Rapier       | Medium Melee | [Melee], [Medium] | 1d8 + Body    |
| Katana       | Medium Melee | [Melee], [Medium] | 1d8 + Body    |
| Curved Sword | Medium Melee | [Melee], [Medium] | 1d8 + Body    |

Heavy Melee Weapons

| Name        | Category    | Tags                           | Damage Format |
| ----------- | ----------- | ------------------------------ | ------------- |
| Greatsword  | Heavy Melee | [Melee], [Two-Handed], [Heavy] | 1d8 + Body    |
| Greathammer | Heavy Melee | [Melee], [Two-Handed], [Heavy] | 1d8 + Body    |
| Great Axe   | Heavy Melee | [Melee], [Two-Handed], [Heavy] | 1d8 + Body    |

Reach / Exotic Weapons

| Name    | Category     | Tags                           | Damage Format |
| ------- | ------------ | ------------------------------ | ------------- |
| Halberd | Reach Weapon | [Melee], [Reach], [Two-Handed] | 1d10 + Body   |
| Scythe  | Reach Weapon | [Melee], [Reach], [Two-Handed] | 1d10 + Body   |
| Whip    | Reach Weapon | [Melee], [Reach], [Two-Handed] | 1d6 + Body    |

Ranged / Thrown Weapons

| Name       | Category      | Tags                   | Damage Format |
| ---------- | ------------- | ---------------------- | ------------- |
| Bow        | Ranged Weapon | [Ranged], [Two-Handed] | 1d8 + Body    |
| Bomb Flask | Ranged Weapon | [Ranged], [Thrown]     | 1d6 + Body    |

Firearms (Black Powder / Aethertech)

| Name         | Category | Tags                   | Damage Format |
| ------------ | -------- | ---------------------- | ------------- |
| Revolver     | Firearm  | [Ranged], [One-Handed] | 1d8 + Body    |
| Rifle        | Firearm  | [Ranged], [Two-Handed] | 1d10 + Body   |
| Shotgun      | Firearm  | [Ranged], [Two-Handed] | 1d10 + Body   |
| Sniper Rifle | Firearm  | [Ranged], [Two-Handed] | 1d12 + Body   |


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Dagger
Tags: [Melee], [Light]
Damage: 1d4 + Body
Range: Melee/ Thrown (20ft.)
Trait:

**"Snake Bite"**
On hit this mode will apply 1 stack of [Acid].
At 5 stacks of [Acid], the target becomes [Corroded].
While [Corroded], they suffer –2 DR.

**"Flash"**
On hit this mode will apply 1 stack of [Volt].
At 5 stacks, the target becomes [Shocked].
If already [Wet], they may be [Stunned] for 1 turn.

**"Flash in the Night"**
If the target is [Corroded] and [Shocked], you may take an Action to cause an AoE Poison Cloud (5ft) around them on hit.
If fire is introduced to this cloud, it explodes in a 10ft radius, Igniting everything flammable.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Claw Gauntlets
Tags: [Melee], [Light]
Damage: 1d4 + Body
Range: Melee/ 20ft.
Trait: 

**"One, Two, I’m Coming for You" – Damage Mode**
All attacks in this mode apply 1 stack of [Bleed] on hit.
As part of your Action when attacking in this mode, you may make one extra strike.

(You may be in only one damage mode at a time)

**"They’re All Doomed" – Damage Mode**
All attacks in this mode apply 1 stack of [Acid] on hit.
As part of your Action when attacking in this mode, you may make one extra strike.

(You may be in only one damage mode at a time)

**"He Doesn’t Run" – Action**
Launch a flurry of blades at a target within 20 ft.
The target must make a Body save vs your DC.
On a fail, they become [Anchored] and take full damage.
On a success, they take normal damage but are not anchored.
This does not require a status setup. It can be used at-will.

**"I Wanna See What Your Insides Look Like" – Finisher Combo**
If the target is both [Shredded] and [Corroded], you may spend 2 Actions to make 2 strikes.
If either hit lands, you automatically trigger "He Doesn’t Run" and the target automatically fails the save.
Cost: You gain 3 stacks of [Bleed] and [Acid] immediately.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Short Sword
Tags: [Melee], [Light]
Damage: 1d6 + Body
Range: Melee/ Thrown (20ft.)
Trait:

**"First Adventure"**
Your attacks apply 1 stack of [Burn] on hit.
When a target has 2+ stacks of [Burn], you may choose to gain 1 stack of [Burn] yourself.
While you have at least 1 stack of [Burn], and your target has 2+ stacks, your attacks deal +1d4 fire damage (or flat +2 for balance).
At the start of your turn, gain 1 additional stack of [Burn].
This stance ends if you or the target no longer meet the conditions.

**"Seasoned Traveler"**
Your attacks apply 1 stack of [Chilled] on hit.
When a target has 2+ stacks of [Chilled], you may choose to gain 1 stack of [Chilled] yourself.
While you have at least 1 stack of [Chilled], and your target has 2+ stacks, you gain +2 DR.
However, each time you are hit, you take +1d4 cold damage.
At the start of your turn, gain 1 additional stack of [Chilled].
This stance ends if you or the target no longer meet the conditions.

**"A Real Adventure"**
Your attacks apply 1 stack of [Volt] on hit.
When a target has 2+ stacks of [Volt], you may choose to gain 1 stack of [Volt] yourself.
While you have at least 1 stack of [Volt], and your target has 2+ stacks, you may make 1 extra melee attack as part of your Major Action.
Each time you use this bonus attack, gain +1 stack of [Volt].
At the start of your turn, gain 1 additional stack of [Volt].
This stance ends if you or the target no longer meet the conditions.

Stacks of [Burn] and [Chilled] cancel one another 1:1 when gained — removing one stack of the opposite effect instead.

**"Recover"**
Choose to purge all elemental stacks from yourself. Costs 2 Actions.
Or, purge 1 stack of each element for 1 Action.

**"Veteran"**
You may only use this when you have 4 stacks of each status, [Burn], [Chilled], and [Volt].
On hit, you may activate this stance to transfer all 12 stacks to the enemy.
The enemy immediately becomes [Ignited], [Frozen], and [Shocked].
The attack also deals an extra 1d4 Fire, Cold, and Electric damage (one roll each).
Drawback:
Roll 1d6 to determine what status you suffer in return:
1–2: [Ignited] (take 2 Fire damage)
3–4: [Frozen] (take 4 Cold damage)
5–6: [Shocked] (take 6 Electric damage)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Chain Blade
Tags: [Melee], [Light], [Reach]
Base Damage: 1d4 + Body
Reach: Melee/ 20 ft
Trait: 

**"Here I come"**
When you hit a creature with this weapon as a part of your Action you may choose one of the following:
Pull the target up to 10 feet toward you. The target must succeed a contested Body roll to resist.
Pull yourself up to 20 feet toward the struck target or terrain — no roll required.

**"Like Lightning"**
On hit your target takes 1 [Volt] stack
Alternatively you can take the [Volt] stack instead
When you have stacks of [Volt] you're attacks deal an additional 1d4 Electric damage, However you take the same amount of Electric damage rolled

**"Flash"**
When you have 3 stacks of [Volt], as an Action you may discharge all stacks and [Blind] all creatures in a 15ft. radius
Once discharged you take 1 point of Electric damage

**"Lightning Strikes Twice"**
When you have 4 stacks of [Volt], As an Action on a hit you can choose to send all stacks to the target and they become [Shocked]
The targe will take an additional 1d4 Electric damage and you will take half of the roll.

**"Conductor"**
At any time you may discharge any held [Volt] Stacks as an Attack action.
On a hit you deal Electric damage equal to the [Volt] stacks discharged.
On a miss you still discharge the [Volt] Stacks.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Bare Hands
Tags: [Unarmed], [Melee]
Base Damage: 1d4 + Body
Range: Melee
Effect:

**"A Fist Like Steel"**
Your attacks give you 1 [Force] stack
If you gain 5 stacks of [Force] you become [Concussed]
(You can spend stacks before reaching 5 to avoid this.)

**"With My Bare Hands"**
When you hit a creature with an unarmed melee attack, you may immediately attempt one of the following without spending an action:
-Shove (knock prone)
-Grapple
-Push (5ft)
Make a contested Body check vs. the target’s Athletics.
You can only use this feature once per turn.

**"The Old One, Two"**
As an Action, you may strike a second time with Bare Hands.
You may not use With My Bare Hands on this attack.

**"To The Face"**
As an Action, you may expend any number of [Force] stacks on a hit to deal extra damage equal to the stacks spent.
On a miss, you still lose the stacks.
If you spend 3 or more [Force], you may additionally attempt to Disarm the target (Athletics vs. your DC).
If you spend 4 or more [Force], you may additionally attempt to inflict [Stunned] on the target (same save).
These effects replace the bonus damage and still consume the stacks.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Rapier
Tags: [Melee], [Medium]
Damage: 1d8 + Body
Range: Melee/ Thrown (15ft.)
Effects:

**"First Thunder"**
Once per turn, you may fire a dark cloud in a straight 15 ft. line. This effect does not cost an action and does not deal damage.
-If the cloud hits a creature, you may spend your Action to cause a thunderclap centered on them.
-All creatures in a 10 ft. radius (including allies) gain 1 [Force] stack.

**"Then Lightning"**
If you hit a creature with "First Thunder" you can use an Action to move in a straight line to the target and make a melee attack with this weapon.
-Doing this gives the target 2 [Volt] stacks and gives you 1 [Volt] stack
-This movement triggers opportunity attacks as normal.
-This ability cannot target adjacent creatures.
-The melee strike counts as a normal attack and can trigger other effects.

**"Streaks Of Light"**
As an Action, make a melee attack with this weapon.
-On a hit, the target gains 1 [Volt] stack.
-You may instead choose to gain the [Volt] stack yourself.

If you chose to gain the stack yourself, you may use an Action to:
-Convert any number of your [Volt] stacks into [Force] stacks and apply them to a target on your next hit.
-Or hold them for later

**"Thunderstorm"**
As an Action, if you have stacks of [Volt] and [Force], you may leap as a bolt of lightning to a space you can see within 20 ft. This leap does not consume movement and does not provoke opportunity attacks.

You can do one of the following depending on how many stacks you have

Expend 2 [Volt] and 2 [Force] stacks
when you land all creatures in a 10ft. radius centered on you must make a Body save vs. Player DC
-If they fail the save they take 2 [Volt] and 2 [Force] stacks
-If they succeed they take no stacks

Expend 4 [Volt] and 4 [Force]
when you land all creatures in a 15ft. radius centered on you must make a Body save vs. Player DC
-If they fail the save they take 4 [Volt] and 4 [Force] stacks
-If they succeed they take 2 [Volt] and 2 [Force] stacks

**"Lightning Strikes Twice"**
After using "Thunderstorm" as an Action you can make up a following attack
-On a hit you deal 1 [Volt] stack and deal an additional 1d4 lightning damage
-On a miss you take 1 [Force] stack and receive 1d4 Force damage

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Katana
Tags: [Melee], [Medium]
Damage: 1d8 + Body
Range: Melee/ Thrown (15ft.)
Effect: 

**"Snake Strike"**
With your weapon sheathed you crouch low, and rush forward for an opening strike
As an Action you rush 10ft towards a target unsheathing and striking in one motion. (separate from movement)
On a hit the target takes 1 stack of [Acid]. You can instead choose to take the stack [Acid]
On a miss you take 1 stack of [Acid].

**"Snake Venom"**
As an action after "Snake Strike" you can choose to harden the acid on the blade.
As a follow up attack 
On a hit the target takes 1 stack of [Poison]
On a miss you take 1 stack of [Poison]

If your attack is successful you may choose to instead take the stack of [Poison] instead of the target

If you missed the attack with "Snake Strike" you take 1 [Poison] regardless if "Snake Venom" hit or missed.
If you missed both attacks you only take 1 stack of [Poison]

**"Coiling Snake"**
In a fluid motion you spin and crouch low blade raised for the next strike.
As an Action if you have a stack of [Acid] you can consume it to recoat your blade with [Acid]
As an Action if you have a stack of [Poison] you can consume it to recoat your blade with [Poison]

As an Action if you have a 2 stacks of [Acid] and [Poison] each you can choose to take 1 additional stack of each.
If you do so
On a hit the target will take 1 stack of [Acid] and [Poison]
On a miss you reset to 1 stack of [Acid] and [Poison] each. 
If you only had 1 stack of [Acid] and [Poison] each on a miss you loose all stacks.

**"Water Snake"**
As 2 Actions if you have 4 stacks of [Acid] and [Poison] each
You may make 3 attacks 
If you hit all 3 on a single target you transfer your [Acid] and [Poison] stacks.
The final attack on a hit will release a 5ft. radius cloud of [Poison] centered on you. Giving the target disadvantage on their next attack.

If you miss 1 attack you will only transfer your [Acid] and [Poison] stacks.
If you miss 2 or more attacks you loose all stacks of [Acid] and [Poison].

**"Snake Oil"**
Choose to purge all [Acid] and [Poison] stacks from yourself. Costs 2 Actions.
Or, purge 1 stack of each for an Action.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Curved Sword
Tags: [Reach], [Melee], [Medium]
Damage: 1d8 + Body
Range: Melee/ 10ft. / Throne (15ft.)
Effect:

**"Liquid Metal"**
Once per turn, when you make a melee attack with this weapon, you may increase its range to 10 ft.

**"Quicksilver"**
As an Action your sword liquefies, thinning into a fluid, singular strand.
This version deals [Slashing] damage and gives 1 stack of [Bleed]. Alternatively you can take the stack of [Bleed] 

As an attack action
The blade becomes rigged.
If you have stacks of [Bleed] you may expend them to do one of the following
Stack  Effect 
2      If the attack hits the target you deal 1d4 [Bleed] damage. (Cannot go beyond 5ft.)
4      Extend the attack to 10ft., dealing 1d4 [Bleed] damage stabbing through the target and hitting 1 creature directly behind the target, which receives the same amount of damage.
       Each target will receive 2 stacks of [Bleed]
       (On a miss you are reduced to 1 stack of [Bleed])

**"Mercury"**
As an Action your sword shifts mass and flattens out to a blade
This version deals [Slashing] damage and gives 1 stack of [Volt]. Alternatively you can take the stack of [Volt]

As an attack action
If you have stacks of [Volt] you may expend them to do one of the following
Stack  Effect 
2      If the attack hits the target you can add 1d4 Lightning damage. (Cannot go beyond 5ft.)
4      Extend the attack to 10ft. If the attack hits the target take 4 stacks of [Volt]
       (On a miss you are reduced to 1 stack of [Volt])

**"Galinstan"**
As an Action your sword shifts mass to the tip creating a teardrop shape.
This version deals [Bludgeoning] damage and gives 1 stack of [Force]. Alternatively you can take the stack of [Force]

As an attack action
If you have stacks of [Force] you may expend them to do one of the following
Stack  Effect 
2      If the attack hits the target you can attempt a [Knockback]. It must make a Body save vs Player DC. (Cannot go beyond 5ft.)
4      Extend the attack to 10ft. hitting 2 adjacent enemies. If the attack hits the targets make a Body save vs Player DC and suffer a [Knockback] and take 4 stacks of [Force]
       (On a miss you are reduced to 1 stack of [Force])

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Greatsword
Trait: Moonlight Arc
Tags: [Melee], [Heavy]
Damage: 1d8 + Body
Range: Melee/ 20ft./ Thrown (10ft.)
Trait:

**"Crescent Moon"**
As an Action, you may unleash a wave of frost in a 20 ft straight line. The arc is 15 ft wide, centered on the line of effect.
-All creatures in the area must make a Body save vs your Attack DC.
-On a failure, they take full weapon damage and 1 [Chilled] Stack. On a success, they take half damage and no status effect.

**"Midnight Moon"**
If you hit a creature with a melee attack using this weapon, you may spend your Action at the same time to release an arc that strikes the same target and continues past them.
-This arc travels 10 ft in a straight line behind the target, starting from the space directly behind them.
-All creatures in that line must make a Body save vs your Attack DC, taking full damage and 1 [Chilled] on a failure or half damage and no status on a success.
This trait may only be used once per turn.
(Allies are not exempt — they must also make saves if caught in the arc.)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Greathammer
Seismic Slam
Tags: [Melee], [Heavy]
Damage: 1d8 + Body
Range: Melee/ Thrown (10ft.)
Trait:

**"I Smash"**
You may use an Action to perform one of the following Slam options:
-Leaping Slam: Leap forward up to 15 ft in a straight line and slam the ground.
-Leaping Slam affects a 10 ft radius centered on your landing space.
-On a failure, targets take full weapon damage and are knocked Prone.
-On a success, targets take half damage only.
This leap does not consume movement, but does provoke Opportunity Attacks when leaving engagement range.
You may only use this Slam once per turn.

**"Ground Pound"**
All creatures within the Slam radius must make a contested save (Body) against your Attack DC (8 + Body).
-Vertical Slam: Slam the ground directly beneath you without moving.
-Vertical Slam affects a 5 ft radius centered on you.
-On a failure, targets take full weapon damage and are knocked Prone.
-On a success, targets take half damage only.
This leap does not consume movement, but does provoke Opportunity Attacks when leaving engagement range.
You may only use this Slam once per turn.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Great Axe
Execution Loop
Tags: [Melee], [Heavy]
Damage: 1d8 + Body
Range: Melee/ Thrown (10ft.)
Trait:

When you hit a creature with an Action attack using this weapon, you may choose one of the following effects:

**"UP and DOWN"**
Launch + Slam
The target must make a Body save vs your Attack DC (8 + Body)
On a failure:
-The target is launched 10 ft into the air and becomes [Airborne]
-They take half weapon damage
-If you have at least 10 ft of movement remaining, you may leap upward and slam them down immediately
-This follow-up does half weapon damage
-The target becomes Prone on impact
-No additional hit roll is required
On a success: target remains grounded and takes half weapon damage

**"Stick and KICK"** 
The target must make a Body save vs your Attack DC
On a failure:
-You embed the axe in their body, Pinning them in place
-You may use an Action to Kick them while pinned:
-The target makes the same save again, but with Disadvantage
-On a failure, choose to either Push 5 ft or Knock Prone
-On a success, the Kick still deals 2 damage
On a success: target is not pinned, but still takes half weapon damage, and you may still attempt the Kick normally

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Halberd
Tags: [Two-Handed], [Reach]
Base Damage: 1d10 + Body
Range: 10ft. Reach/ Thrown (15ft.)
Traits:

**"Blade"**
As an Action make a single attack roll against the higher AC of two adjacent enemies.
On a hit, deal full damage to both targets.
Each enemy reduces the damage using the highest DR between them.

**"Hook"**
On hit, you may spend your Action to move the target up to 10 ft in a direction of your choice.
If this movement causes the target to leave an ally’s reach, that ally may make an Opportunity Attack with Advantage.

**"Pole"**
If you use 2 Actions to make attacks with the halberd against the same enemy, and both hit, apply [Bleed] to that target.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Scythe
Tags: [Two-Handed], [Reach]
Base Damage: 1d10 + Body
Range: 10ft. Reach/ Thrown (15ft.)
Traits:

**"Reaper’s Spiral"**
As an Action all enemies in a 10ft. radius centered on you must make a Might or Grace save (DC = 8 + your Scaling Stat + Proficiency).
-On a failure, each enemy takes full weapon damage.
-On a success, they take half damage.
-This action does not provoke opportunity attacks.

**"Wraith Arc"**
As an Action move up to 15 ft, passing through at least 2 enemies during that movement.
-Your attack range is reduced to 5 ft. range.
-You do not provoke opportunity attacks while moving.
-Make 1 attack roll vs the highest AC among the enemies passed through.
-If the attack hits, all enemies passed through take full weapon damage, reduced by the highest DR among them.
-This movement is not part of your regular movement and cannot be combined with other movement abilities.

**"Reap Stacks"**
Each time you deal weapon damage with the Scythe, the target gains 1 Reap stack (max 1 per target per turn).
-As an action when a target reaches 3 stacks, you may choose to consume all stacks to deal 10 damage, reduced by DR.
-This damage is applied immediately and does not require an additional action.
-Reap stacks are removed if the target is healed or if you fail to hit that target for 2 consecutive rounds.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Whip
Tags: [Reach]
Damage: 1d6 + Body
Range: 10 ft. Reach/ Thrown (15ft.)
Traits:

**"Control Lash"**
When you hit a creature with a whip attack, you may immediately attempt one of the following options:
-Trip: Force a contested Body check against your DC. On a failure, the target falls [Prone].
-Disarm: Force a contested Body check. On a failure, the target drops one held weapon or item of your choice.
-Pull: Force a contested Body check. On a failure, the target is pulled 5 feet toward you.
-Hold: You may choose to maintain a grip on the target using the whip.

While holding a creature:
-The target becomes [Restrained] until the start of your next turn
-You cannot make additional whip attacks while holding
-Releasing the target is free (no action)

You may only use one of these options per turn.
This effect does not prevent you from attacking again with an Action.
If a creature is already affected by one of these effects, you cannot apply a second until the first ends.

**"Serpent’s Tempo"**
Each time you hit a creature with a whip attack, they gain 1 [Force].
At 5 stacks, the target becomes [Concussed].

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Bow
Tags: [Ranged]
Base Damage: 1d8 + Body
Range: 80ft.
Traits:

**"Pinning Shot"**
Once per turn, when you hit a creature with an attack using this weapon, the target must succeed on a Body save against your Attack DC or become [Restrained] until the start of your 
next turn, and they take 1 [Bleed]. Alternately you can take the [Bleed] stack. 

**"Linebreaker Shot"**
Once per turn, when you hit a creature with this weapon, you may push the target 5 feet directly backward if they fail a Body save against your Attack DC.
This movement does provoke opportunity attacks as normal, and they take 1 [Bleed]. Alternately you can that the [Bleed] stack.


**"Hail Of Thorns"**
As an action you fire an arrow that splinters and coats the terrain in thorns
Creates a 5ft radius of thorns, this is considered difficult terrain any creature within the radius immediately take damage upon creation otherwise entering, or moving through deals 1d6 Pierce damage and gains 1 [Bleed]. 
This effect lasts until the end of your next turn, unless refreshed. You may only have 1 "Hail of Thorns" active at a time.

Alternately you can that the [Bleed] stack. 

If you have [Bleed] stacks you can expend them to do one of the following
Stack  Effect
2      Increase the radius to 10ft. and extend the time to 2 rounds.
4      Increase the radius to 10ft. and extend the time to 4 rounds and choose a target within to be moved they will take 1d6 as they are moved, they make a Body save vs Player DC.
       On a failure you can move them up to 10ft. 
       On a success you can move them 5ft. but they take no extra damage.
(Forced movement in this way allows AoO)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Bomb Flask
Tags: [Thrown], [Splash], [Light]
Damage: 1d6 + Body (Melee or Direct Hit only)
Range: Melee / 20 ft. (Thrown)
Radius (Blast Area): 5–10 ft. (varies by mode)
Traits:

Functionality

**Melee Use:** The Bomb Flask can be used as a close-combat weapon.
-On hit: 1d6 + Body damage
-Choose one Melee style:
-Wall of Sparks – 5 ft. radius around user
-Rolling Sparks – 10 ft. line directly forward
-These determine your melee AoE pattern and must be chosen per attack (not interchangeable mid-swing).
-Melee AoEs may hit allies — position with care.
-Action attacks are restricted to a 5 ft. line directly in front of the user
-Status build-up and flat damage still apply to hit target(s)

**Thrown Use:** Ranged attack with 20 ft. range.
-On direct hit: 1d6 + Body damage
-All creatures within 10 ft. radius of the impact take flat damage (no stat bonus), and may suffer status buildup based on the Flask’s type.
-Affected creatures must start their turn in the area or pass through it to gain 1 additional stack of the relevant status (Max 2 stacks unless manipulated by terrain or movement effects).

Flask Variants (Tag-Defined)
Each variant changes the damage type and status effect applied on hit and in the AoE zone. Choose one during a Rest:

**Fire Flask**
-Damage Type: Fire
-Status: [Burn] 1 stack on hit; 1 per turn in AoE
-AOE Duration: 2 rounds
-Environment: May ignite terrain
Notes: Can be extinguished by an Action or [Wet]

**Cold Flask**
-Damage Type: Cold
-Status: [Chilled] 1 stack on hit; 1 per turn in AoE
-AOE Duration: 2 rounds
-Environment: Ground becomes Difficult Terrain
Notes: Movement penalty does not stack with Chilled status

**Lightning Flask**
-Damage Type: Lightning
-Status: [Shocked] 1 stack on hit; 1 per turn in AoE
-AOE Duration: 2 rounds
Notes: If target is [Wet], stacks may escalate to [Stunned] as defined by keyword logic

**Poison Flask**
-Damage Type: Poison
-Status: [Poison] 1 stack on hit; 1 per turn in AoE
-AOE Duration: 2 rounds
Notes: Deals ongoing poison damage per stack (2 dmg per turn baseline)

**Frenzyflame Flask**
-Damage Type: Fire
-Status: 1d6 + Body fire damage + 20 [Madness] to targets, 15 [Madness] to user on use (regardless of melee/thrown)
-AOE: No lingering zone
Notes: High-risk, no AoE duration. May trigger [Madness] condition.

**Madness Condition** (For Reference)
When a creature reaches 100 Madness:
-Must use its Action to attack a random nearby target (roll 1d6 to determine direction).
-Cannot target itself.
-Lasts 1d4 + 1 rounds
-Target takes 1 psychic damage at the start of each turn
Ends early if:
-Time expires
-Hit by a [Calming Charm] effect
-An ally succeeds on a Presence/Conviction + (Presence/Conviction or alternate justified stat) check vs DC 15 (as Minor Action)
-A [Magic] effect removes [Madness]
-Target takes 5 + [Vital] damage in a single hit (Overload)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Revolver
Tags: [Ranged], [One-Handed], [Firearm]
Base Damage: 1d8 + Body
Magazine Size: 8 rounds
Range: Standard 60ft.

**Hair Trigger – Action**
You fire in a blind rush, spraying rounds in panic or desperation.
-Choose up to 3 adjacent targets (Min of 2 targets, must be within 5 ft. of each other).
-Roll 1 attack roll with damage as normal.
-All targets use the highest AC and the highest DR among them.
-Costs 2 bullets per target (4–6 total). Must have enough rounds loaded.

**Roulette – Action**
A high-stakes gamble. You empty half the chamber, then bet your life on every pull.
-The remaining bullets become the number of shots before the next reload.
(e.g., 8 rounds → down to 4 → you now have 4 shots to gamble before reloading)
Before each shot, call evens or odds, then roll the attack as normal:
-If you Hit and called correctly, attack hits, deal normal damage +1d6 bonus damage.
-If the attack misses and called correctly, the round is still spent.
If you called wrong, the gun misfires:
-You take 1d6 self-damage (minimum 1), ignores DR. The shot is wasted.
-You may fire the first gamble shot as part of this action.
Roulette ends when you reload, expend all remaining shots, or voluntarily stop.
Cannot trigger [Last Words] while active unless using [Feelin’ Lucky].

**Last Words – Passive**
The final bullet strikes with molten wrath — the barrel glowing with heat.
-The weapon must be fully loaded at the start of the chain (8 rounds).
-Each shot must hit to build the streak — any miss resets the count.
-Reloading at any point resets the counter.
-The final shot (8th) must hit to benefit.

On a successful 8-hit streak:
-Final shot gains [Piercing] (ignores half of target’s DR, rounded down).
-Applies 1 stack of [Burn].

**Synergy:**
-Hair Trigger contributes bullet count (each bullet expended counts),
but Last Words cannot trigger inside a Hair Trigger action — only afterward.
-Roulette disables Last Words unless using [Feelin’ Lucky].

**Feelin’ Lucky – Action**
Optional Combo: [Roulette] + [Last Words]
You’ve hit 6 times. 2 bullets remain. One misfire means pain — one hit means glory.
You push the barrel forward.
“I’m feelin’ lucky.”

-Can only be used when exactly 2 bullets remain.
-Immediately discard one (leave only 1 round).
-Call evens or odds, then roll 1d6:
Correct Call: Fire the final shot — it gains [Piercing] and 1 stack of [Burn] per [Last Words].
Incorrect Call: Misfire — take 1d6 damage (min 1), which ignores DR, and apply 1 stack of [Burn] to yourself.

This is an Action.
Resets Last Words, win or lose.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Shotgun
Tags: [Ranged], [Two-Handed], [Firearm]
Base Damage: 1d10 + Body (No stat bonus in Hip Fire mode)
Range:
ADS Mode: 10 ft. direct line
Hip Fire Mode: 15 ft. cone

**Hasta la vista**
Tags: [Close-Range], [Knockback], [Risky] — Action
Effect:
You fire both barrels at once in a single massive shot.
Range: 5 ft.
-Make a single attack roll against one target.
-On hit: Deal 2d10 damage and push the target 10 ft. back.
-The target must make a Body save vs your DC. On a failure, they fall Prone.
Drawback:
-You take half the damage rolled. DR applies as normal.
-After firing, make a Body save against your own DC.
-On failure, you are knocked Prone.
-On success, you stay standing.

**Flesh Hook**
Tags: [Gap-Close], [Positioning] —Action
Effect:
You launch a barbed hook at a creature within 20 ft. and pull yourself in.
-Make a roll against the target’s AC.
-On success, you are pulled toward the target.
-This movement does not provoke reactions and does not count as movement for your turn.
(You may choose to stop early)

**Hip Fire**
Tags: [AOE], [Cone], [Unsteady] — Toggle Mode
Effect:
You fire the shotgun from the hip in a wide blast.
-All creatures (including allies) in a 15 ft. cone in front of you must make a Body save vs your DC (8 + Body).
-While firing this way, you do not need to reload, but ammo is still spent normally.
-You cannot use [Hasta la vista] while firing this way.
-You may use [Flesh Hook] if available.

**ADS (Aim Down Sights)**
Tags: [Precision], [Point-Blank], [Setup] — Toggle Mode
Effect:
You steady your aim and focus your shot downrange.
-All shotgun attacks made in ADS mode are direct-fire attacks with a maximum range of 10 ft.
-You may use [Hasta la vista] and [Flesh Hook] while in this mode.
-Attacks are made normally — 1 target per shot.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Sniper Rifle
Tags: [Ranged], [Two-Handed], [Firearm]
Base Damage: 1d12 + Body
Magazine Size: 5 rounds
Range: Standard 180ft

**"I Didn’t Hear No Bullet" – Firing Mode**
Any creature beyond 10 ft. from you cannot hear your shot.
While in this mode:
-Magazine size is capped at 3.
-All shots gain [Piercing] and [Burn].
-You are [Vulnerable] until you exit this mode.
-Bonus: If you land 3 hits in a row, your magazine refills to 3.
All traits apply on top of normal damage.
-Note: [Burn] stacks may apply [Ignited] if the threshold is met.

**"Overwatch" – Firing Mode**
While in this mode:
-All shots apply [Chilled] stacks on hit.
-If all 5 shots hit a single target, they become [Frozen].
All traits apply on top of normal damage.

**"One Moment of Clarity" – Action**
As an Action, drop your magazine capacity to 3.
While in this mode:
-Gain +5 to hit, but suffer -5 to damage.
-If DR would reduce damage to 0, deal 1 damage instead.
-Stat modifiers apply as normal.
Buff: If all 3 consecutive shots land while in this mode, your next use of "One Shot, One Kill" will have its self-inflicted status effect reduced by 1 tier:
-[Frozen] becomes 4 [Chilled]
-[Ignited] becomes 2 [Burn]
-This bonus only applies if earned before using "One Shot, One Kill".
-You may not enter this mode while "I Didn’t Hear No Bullet" is active.
All traits apply on top of normal damage.

**"One Shot, One Kill" – Action**
As an Action, reduce your current magazine to 1 round.
If the shot hits:
-Apply [Frozen] (if in Overwatch) or [Ignited] (if in “I Didn’t Hear No Bullet” mode) to the target.
After firing:
-You become [Frozen] or [Ignited], matching the mode used.
-If you earned the bonus from “One Moment of Clarity”, reduce this effect by 1 tier (as above).
-These status effects may progress naturally if not addressed.
All traits apply on top of normal damage.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Rifle
Type: Firearm
Tags: [Ranged], [Two-Handed], [Firearm]
Base Damage: 1d10 + Body
Magazine Size: 15 rounds
Range: 100ft
Firing Modes & Traits

**Take The Shot**
Firing Mode – Precision Rhythm
-Fires 2 rounds per shot, applying 1 [Volt] stack on hit.
-As an Action, you may switch to firing 3 rounds per shot. While in this mode:
-Each hit applies 2 [Volt] stacks.
-You gain 1 [Volt] stack each time you fire.
This trait rewards control and accuracy, at the cost of self-overload if overused.

**Game Over Man**
Firing Mode – Panic Burst
-Fires 5 rounds per shot.
-Each hit applies [Burn] stacks based on GM scaling.
While in this mode, you may access:

**Suppressing Fire**
Special Trait – Area Control
-As an Action, you may empty the remaining magazine to fire a 15 ft. horizontal arc in front of you.
-All creatures in the arc must make a Body save vs. your DC (8 + Body).
--Fail: Take full damage, become [Ignited] and [Frightened]
--Success: Take half damage, become [Ignited]
You take 2 [Burn] stacks
Use with caution — tactical denial at the cost of personal risk and full ammo dump.

**Die Mother Fucker, Die Mother Fucker, Die**
Finisher Trait – Overcharged Rage
-Requires: 4 [Volt] stacks and must be [Ignited]
-As 2 Actions, fire 5 rounds and target up to 3 creatures within range.
-Each hit applies [Shocked] and [Ignited]

You immediately:
-Reduce to 1 [Volt] and 1 [Burn] stack
-Take half the damage of the first target hit
-Immediately retake the damage of the new status stacks

# Armor

1. Set a DR (Damage Reduction) cap total 4
Keeps design tight: each armor set gets a total DR budget.
Sample DR Budget Model:

| Armor Tier | Physical DR | Magic DR | Total DR |
| ---------- | ----------- | -------- | -------- |
| Cloth      | 0           | 4        | 4        |
| Light      | 1           | 3        | 4        |
| Medium     | 3           | 1        | 4        |
| Heavy      | 4           | 0        | 4        |
| Enchanted  | 3           | 3        | 6        |
To calculate Armor Ac you will add the Armor DR to the respective Stat, so Body for Physical and Magic for Magic. 
So for example if you have a -3 to Body and a +5 to Magic then Cloth Armor AC would look like
Cloth= -3 Phys/ +9 Magic.

This is only to hit as the Armor DR is the amount reduced from the attack damage. So even with this example Cloth Armor will only reduce Magic damage by 4 and will reduce Physical damage by 0 as expected.

2. Magic DR should reduce stack damage, NOT block the effect
This keeps status system balanced. Players still reach 5 stacks and trigger stage-2.

Avoids control effects like [Frozen], [Shocked], [Corroded] becoming useless vs armored enemies.

Magic DR reduces the damage from elemental statuses, but not their application or escalation. A character with 4 Magic DR takes 1 damage per [Burn] stack instead of 2, but still gains stacks and can become [Ignited].


# Spells

| Spell Parameters                                                                          |                                  |                                        |                                  |                                                   |                           |                  |           |      |       |                     |
| ----------------------------------------------------------------------------------------- | -------------------------------- | -------------------------------------- | -------------------------------- | ------------------------------------------------- | ------------------------- | ---------------- | --------- | ---- | ----- | ------------------- |
| Category                                                                                  | Elemental                        | Force                                  | Mind or Psychological            | Temporal                                          | Creation or Transmutation | Order or Binding | Summoning | Life | Death | Corruption or Chaos |
| Function                                                                                  | Utility +0                       | Movement +1                            | Defensive +1                     | Offensive +2                                      |                           |                  |           |      |       |                     |
| --The Following is where each parameter now falls into action cost along with mana cost-- |                                  |                                        |                                  |                                                   |                           |                  |           |      |       |                     |
|                                                                                           | Action Cost 1, Value (Mana Cost) | Action Cost 2, Value (Mana Cost)       | Action Cost 3 ,Value (Mana Cost) | Multi-Action Cost 4+ or Ritual, Value (Mana Cost) |                           |                  |           |      |       |                     |
| Range*                                                                                    | Self-25ft. (1)                   | 30ft.-60ft (2)                         | 65ft.-120ft. (3)                 | 125ft.-200ft.(4), Sight(5), Global (6)            |                           |                  |           |      |       |                     |
| Size*                                                                                     | 5ft.-15ft. (1)                   | 20ft.-30ft. (2)                        | 35ft.-60ft. (3)                  |                                                   |                           |                  |           |      |       |                     |
| Shape                                                                                     | none-point (1)                   | Sphere, Cube, Line, Wall, Cylinder (2) | Freeform or Custom (3)           |                                                   |                           |                  |           |      |       |                     |
| Duration**                                                                                | Instant (1)                      | Round (2)                              | Minute (3)                       | Hours (4), Permanent (5)                          |                           |                  |           |      |       |                     |
| Target Count*                                                                             | Single (1)                       | Multi (2+)                             | AOE (3)                          |                                                   |                           |                  |           |      |       |                     |
| Accuracy Type*                                                                            | Attack Roll (1)                  | Save (1)                               | Auto-Hit (4)                     |                                                   |                           |                  |           |      |       |                     |
| Effect                                                                                    | T1 (3)                           | T2 (6)                                 | T3 (12)                          | T4 (17)                                           |                           |                  |           |      |       |                     |

*Accuracy Type: 
Attack Roll: Gain additional damage Die, cost increases with die size. Functions same as other damage dice.

*Target Count:
Multi: Current cost is for 2 targets, after 2 increase cost by 1 to a max of 4 targets. So costs looks like: 2= +1, 3= +2, 4= +3

Casting Time:
Multi-Round: Mana cost increases based on Damage/Effects from 1 to 5 (pending final numbers)

Damage Dice Structure (Final)

Damage based on 3 Spell Parameters: Range, Target Count, Size
Each Parameter contributes 1 die
Increasing Parameters increases dice size.
Mixed dice size is allowed and expected
The damage die is determined by mana cost:
d6 - +1
d8 - +2
d10 - +3
d12 - +5

The damage die is locked to mana cost amount per parameter. So if a damage die stops at +3 the max damage die will be a d10.

+1 floating die from Accuracy (attack roll only) Optional, same scaling rules as others
Dice scale d6 → d12	Player choice
Flat stat bonus = Casting stat (-5 to +5) Always applies

Example math
Range: Self-15ft +1 (d6)
Target Count: Single +1 (d6)
Size: 20ft.-30ft. +2 (d8)
Attack Roll: +5 (d12)
Stat Modifier: +5

1d6+1d6+1d8+1d12 + 5 = Total Damage

Multi-Target	+1 per target	Temp cap assumption = 5-6
Upkeep/Sustain	+1 to +5 per round	⚠️ Not finalized

Known Cost Anchors

| Type | Mana |
| ---- | ---- |
| Min  | 8    |
| Max  | 44   |
| Max  | 132  |

these are not base costs but cost math based on Spell Skeleton Framework

Use flat adders so Functions have real weight:
Offensive +2
Defensive +1
Movement +1
Utility +0
(Multi-function spells add both—for example, damage + reposition = +3.)

2) Main / Sub per Casting Type (no fractions)
Keep your “double for Sub” — it’s the clearest.
Main Category: normal cost (×1)
Sub Category: double cost (×2)
Players choose their Main/Sub list at character build.

Every effect must be describable by one of five kinds of mechanical impact.
This ensures “what the spell can do” is bounded even when players invent new names or visuals.

Duration is for both cost and spell effect. Should you want to create a spell effect that lasts longer than the casting time chosen you will always pay the higher mana cost. So if you cast a spell with a Duration of "Instant" but the spell effect lasts for 1 "Minute" then you will use the mana cost for the 1 "Minute" instead of the "Instant" cost.

All spells must have ***every*** parameter filled, there can be no empty fields.

# The Tag System

The Tag System is a universal interaction framework that defines how effects, objects, environments, and abilities interact with the game world.

Tags are not spells.  
They are not limited to magic.

They are standardized mechanical identifiers that describe **what an effect does**, regardless of its source.

Any system element—spell, weapon, potion, creature ability, artifact, environmental hazard, or terrain feature—may reference or apply Tags.

## What a Tag Represents

Each Tag represents:
1. A defined domain of influence (Fire, Gravity, Illusion, Decay, etc.)
2. A specific type of mechanical interaction within that domain
3. A scalable intensity (Tier 1 or Tier 2)

Tags do not describe narrative flavor.  
They define mechanical behavior.

If an effect applies a Tag, it inherits that Tag’s mechanical definition.

## Tier Structure

Each Tag exists in two tiers.

### Tier 1 — Foundational State

Represents the baseline functional expression of a domain.
- Establishes the type of interaction.
- Applies the domain’s default condition or behavior.
- Interacts with Stack Logic for progression.
- Does not inherently determine duration or damage magnitude.

Tier 1 introduces the state.

### Tier 2 — Escalated State

Represents a structurally intensified or transformed expression of the same domain.

- Alters how the domain behaves at a higher impact level.
- Changes interaction rules (not just numbers).
- Often introduces systemic consequences (loss of actions, environmental alteration, structural damage, etc.).
- Still relies on Stack Logic for timing and scaling unless overridden.

Tier 2 changes the _mode of interaction_, not just the amount.
## Example

Tier 1 Fire:

- Establishes combustion.
- Applies Burn.
- Stack Logic determines whether it fades or escalates.
- If unattended, it either dies or escalates.
- Stack Logic governs how long it persists unless modified.
- Spell Framework can override duration or scale.

Tier 2 Fire:

- Represents sustained ignition.
- Alters healing interaction.
- Stack Logic governs how long it persists unless modified.
- Spell Framework can override duration or scale.

The Tag does not define “2 rounds” or “5 damage.”  
The Tag defines _what burning is_ and _what ignition changes mechanically_.

Tier 1:

 Establishes the baseline state and interaction rules of a domain.  
 Progression and duration are governed by Stack Logic unless otherwise modified.

Tier 2:

Represents an escalated state that alters the interaction rules of the domain in a more disruptive or structurally impactful way.  
Progression and duration are governed by Stack Logic unless otherwise modified.

## Delivery Methods

Tags are source-agnostic.

They may originate from:
- Magic
- Weapons
- Environmental effects
- Creature abilities
- Potions
- Artifacts
- Structural failures
- Terrain conditions

Magic may directly invoke either Tier at cost.

Non-magical sources typically escalate through buildup, environmental logic, or material properties.

The Tag definition remains constant regardless of origin.

## Combination Logic

Tags are modular.
Effects may combine multiple Tags to create compound interactions.

For example:
- Fire + Wind may increase spread.
- Acid + Force may alter delivery method.
- Illusion + Manipulate may combine perception and compulsion.
- Gravity + Stone may produce structural collapse.

The Tag System does not prescribe combinations.  
It defines how each Tag behaves so combinations resolve consistently.

## Domain Boundaries

Each Tag defines what it affects and how it interacts with the world.

Tags should:
- Operate within their defined domain.
- Avoid duplicating another Tag’s function.
- Escalate cleanly from Tier 1 to Tier 2.
- Remain mechanically readable in isolation.

Tags do not describe casting method, cost, or narrative justification.  
Those are defined elsewhere in the system.

## Purpose of the Tag System

The Tag System exists to:
- Standardize interaction logic across the entire game.
- Remove ambiguity from effect resolution.
- Allow free-form construction while maintaining mechanical clarity.
- Enable cross-system compatibility between magic, items, creatures, and environments.

It provides structure without prescribing specific spell shapes.

The Tags define reality.  
The framework defines how reality is accessed.  
The source defines cost and delivery.


# Tags

## 1. Elemental

1. Fire
	1. Tier 1: [Fire] — Base heat, open flame capable of ignition or starting a fire; applies [Burn].
	2. Tier 2: [Ignited] — Sets target on fire; takes [Burn] each turn, and cannot gain healing from any source while [Ignited].

2. Water
	1. Tier 1: [Water] — The presence or projection of liquid water capable of soaking surfaces and creatures; applies [Wet]
	2. Tier 2: [Drown] — Complete or overwhelming submersion in water that impairs breathing and restricts action; the target loses its Reaction and must use an Action to escape. Breath duration is determined by Body modifier.

3. Earth 
	1. Tier 1: [Earth] — Loose soil and particulate matter under your control; dirt, sand, and gravel can be created, shifted, shaped, or hurled. Applies standard Earth damage when used offensively. 
		1. [Create] — Dirt 
		2. [Move] — Dirt, Sand, Gravel
		3. [Shape] — Dirt, Sand
		4. [Hurl] — Dirt, Sand, Gavel
	2. Tier 2: [Stone] — Solid mineral mass under your control; stone, raw ore, and crystal can be created, shifted, shaped, or hurled. May form rigid, load-bearing structures or barriers.
		1. [Create] — Stone, [Loose Earth]
		2. [Move] — Stone, Raw Ore, Crystal, [Loose Earth]
		3. [Shape] — Stone, Raw Ore, Crystal, [Loose Earth]
		4. [Hurl] — Stone, Raw Ore, Crystal, [Loose Earth]

4. Air 
	1. Tier 1: [Air] — Moving air and directed gusts; creates breathable currents, gentle breezes, or compressed air capable of impact. Can disperse smoke, mist, or steam and extinguish small open flames. 
		1. [Create] Air (damage), gentle breeze
		2. [Extinguish] Open flames from candles to Torches
		3. [Move] Smoke, Mist, and Steam
	2. Tier 2: [Wind] — Violent and sustained air currents; generates powerful gusts capable of pushing objects, knocking back targets, and shaping battlefield-scale airflow. Can disperse dense fog or extinguish large open flames.
		1. [Create] Large winds and weather-scale effects; Also able to create strong winds that can push objects and [Knockback] targets. 
		2. [Extinguish] Open flames such as campfires, pyres and bonfires 
		3. [Move] Fog, thick smoke, Clouds

5. Ice
	1. Tier 1: [Ice] — Freezing cold and surface frost; lowers temperature rapidly and forms thin ice or rime. Applies [Chilled].
	2. Tier 2: [Frozen] — Solid encasement in thick ice; movement becomes 0 and the target must use an Action to break free.

6. Lightning
	1. Tier 1: [Electric] — Sudden electrical discharge; arcs of lightning capable of shocking a target. Applies [Volt].
	2. Tier 2: [Shocked] — Overloaded nervous or conductive systems; disadvantage on Actions and –½ movement Speed.

7. Acid 
	1. Tier 1: [Acid] — Corrosive liquid that begins eating into armor and flesh and melts surfaces slightly; applies [Acid]. 
	2. Tier 2: [Corroded] — Severe corrosive saturation; material begins dissolving rapidly, weakening armor, eating through terrain, and causing progressive structural damage if not neutralized. This effects **everything** in a 10ft. radius from a center point, be it target or AOE center, in the following ways
		1. [Armor] — It weakens Armor (–2 DR to either Magic or Physical DR, one or the other, until repaired)
			1. This can stack but only on a new application of Tier 2 [Corroded] 
		2. [Terrain] — The acid also burns through surfaces, continuing each round 
			1. At a rate of 5ft. of Material thickness towards the point of gravity if no direction is applied. 
			2. If no duration is given it will stop after 20ft.) 
		3. [Organic] — Direct contact with Organic Material will begin a 3-round Corrosion Countdown. If not removed in 3 rounds, depending on location, you will lose a limb or suffer sever permanent body impairment. 
			1. [Location] — must be specified upon application and must be an exposed area. If no area is called or exposed center mass will become the default target.
			2. [Removal] — You can spend 2 actions to either apply [Chill] or [Burn] stacks to the Acid ending the dissolving effect and removing the acid, but you will still take damage from the acid as well as from the [Chill] or [Burn] this round.  
			3. [Corrosion Counter] — Each time a Corrosion Countdown completes on the same body location, increase that location’s Corrosion Counter by 1 (max 3). 
				1. If healing is applied **after** removing the acid and **before** new exposure, reset that location’s Corrosion Counter to 0. 
				2. At Corrosion Counter 3, further Tier 2 exposure to that location causes immediate catastrophic damage.

8. Poison
	1. Tier 1: [Poison] — Toxic substance; applies [Poisoned]
	2. Tier 2: [Venomous] — System-wide toxic overload; bodily functions are impaired, and the target takes ongoing incremental damage until cured. 
		1. The Target loses 1 Action
		2. On the second round after the initial activation round, the poison will increase by 1 each round and refresh its own stack timer.
			1. Once the stack count reaches 10 the will now increase by 5 each round.
			2. At 15 stacks the target will lose their 2nd Action for a total of 2 lost Actions
			3. At 20 stacks the target will lose their 3rd Action for a total of 3 lost Actions.
			4. At 35 stacks the target will permanently lose 1 Action.
		3. If the target has received any form of [Radiant] or similar at 10 stacks or below the poison is removed. 
		4. If the target is at 15 stacks or higher the poison can only be removed with any form of [Purge] or similar. 
			1. This alone does not restore a lost action from 35 stacks.

## 2. Force

1. Force
	1. Tier 1: [Force] — Directed kinetic impact; a surge of physical momentum that strikes, pushes, or pulls a target. May [Push], [Pull], [Impact], or [Blast]. [Impact] and [Blast] apply [Force] stacks.
	2. Tier 2: [Stunned] — Violent kinetic trauma; the target’s body is rattled by sustained force. Disadvantage on Actions and loses Reaction. [Slam] and [Repulse] apply [Force] stacks.

2. Hold
	1. Tier 1: [Restrained] — An external binding force grips the target; movement is physically limited or partially prevented.
	2. Tier 2: [Crush] — Sustained constricting pressure compresses the restrained target. Applies [Force] stacks while maintained.

3. Gravity 
	1. Tier 1: [Gravity] — Localized alteration of weight; a target’s weight may be increased or decreased by up to half its normal value. The target may also be lifted vertically up to 10 ft. Gravity still pulls downward.
	2. Tier 2: [Crushed] — Overwhelming gravitational distortion; weight may be doubled or reduced to zero, and the direction of gravitational pull may be altered. Movement is halved under increased weight. Weight removal allows controlled flight. Directional manipulation allows gravity to pull toward a chosen vector instead of straight down.

4. Barrier **
	1. Tier 1: [Block] — A solid or energy obstruction formed to intercept incoming force; stops or redirects a single instance of impact.
	2. Tier 2: [Shield] — A sustained protective field or structure that absorbs or deflects repeated impact. Grants +1 Magic DR (max).

## 3. Mind

1. Psychic 
	1. Tier 1: [Psychic] — Focused mental intrusion or psychic force that deals mental damage; may transmit a short telepathic message (up to 20 words) to a target; applies [Psychic]
	2. Tier 2: [Telepath] — Sustained mental linkage that allows two-way transmission of thoughts, images, sensations, and intentional communication between minds.

2. Manipulate **
	1. Tier 1: [Influence] — Direct mental pressure that alters emotional state or decision priority without removing agency.
		1. [Charmed] — Block hostility toward source.
			1. **Mechanical Effects**
				1. Cannot target charmer with hostile action.
				2. Cannot include charmer in area effects knowingly.
				3. Charmer gains advantage/bonus on social checks against target.
				4. Target may still act freely otherwise.
			2. **What it does NOT do**
				1. Does not force obedience.
				2. Does not alter loyalty.
				3. Does not prevent self-defense against others.
		2. [Frightened] —  Force avoidance behavior.
			1. **Mechanical Effects**
				1. Cannot willingly move closer to fear source.
				2. Disadvantage on attacks or checks against source.
				3. If unable to increase distance, suffers defensive penalties.
		3. [Confused] —  Disrupt decision reliability.
			1. **Mechanical Effects (standard model)**  
			2. At start of turn, roll:
				1. 1–2: Move randomly.
				2. 3–4: Attack nearest creature.
				3. 5–6: Act normally.
			3. Or:
				1. Cannot take reactions.
				2. Must use action to reorient before complex tasks.
		4. [Suggested] — Impose a specific behavioral directive.
			1. **Mechanical Effects**
				1. Must spend next action pursuing suggested task.
				2. If task becomes obviously self-harmful, may repeat save.
				3. Directive must be phrased as achievable and finite.
			2. Difference from Dominate:
				1. Limited scope.
				2. Not continuous control.
				3. Ends when task ends.
	2. Tier 2: [Override] — Forced mental control that replaces or binds a target’s decision authority.
		1. [Dominated] — Replace action ownership.
			1. **Mechanical Effects**
				1. Controller chooses target’s action each round.
				2. May dictate movement.
				3. Target retains awareness but cannot refuse.
				4. Typically concentration-based and short duration.
			2. Escalation from Suggestion:
				1. No requirement for reasonableness.
				2. No player choice in execution.
		2. [Possessed] —  Replace character operator.
			1. **Mechanical Effects**
				1. Controller uses full stat block.
				2. Controls movement, actions, reactions.
				3. Target consciousness suppressed or displaced.
				4. Ends only on exorcism, damage threshold, or contest.
			2. Difference from Dominate:
				1. No partial autonomy.
				2. Often indefinite until broken.
		3. [Geas-bound] —  A binding directive that imposes automatic consequences for disobedience.
			1. **Mechanical Effects**
				1. A specific objective is defined.
				2. When the target attempts to act against that objective:
					1. Immediate penalty triggers (damage, condition, resource drain, etc.).
				3. The system enforces compliance without the controller selecting actions.
				4. Target retains moment-to-moment agency but is constrained by consequence.
			2. Difference from Suggestion:
				1. Persistent.
				2. Punitive enforcement.
				3. Survives combat rounds.
		4. [Memory Rewritten] — Alter character history.
			1. **Mechanical Effects**
				1. Remove or replace specific memories.
				2. Implant false allegiance or event history.
				3. May alter Bonds/Ideals/Background tags.
				4. Typically no recurring save once complete.
			2. Difference from Confusion:
				1. Not temporary disruption.
				2. Sheet-level alteration.

3. Sleep 
	1. Tier 1: [Drowsy] — Induced mental fatigue that slows awareness and reaction; perception is dulled and reactions are lost; applies [Drowsy] 
	2. Tier 2: [Unconscious] — Forced loss of conscious awareness; the target is unresponsive and unable to act until awakened or released; applies [Unconscious]

4. Illusion 
	1. Tier 1: [Illusion] — Artificial sensory distortion that inserts or alters limited sensory input without replacing reality.
		1. [Mirage] — 
			1. **Scope**
				1. Small area (room, clearing, hallway) 
				2. Visual only, possibly faint sound
				3. Static or looping
			2. **What it can do**
				1. Make a wall appear broken
				2. Conceal a pit as solid ground
				3. Make dry land look like water (purely visual)
			3. **What it cannot do**
				1. Support weight
				2. Block passage
				3. Cause damage
				4. React dynamically
			4. **Interaction**
				1. Physical contradiction reveals it
				2. Does not resist scrutiny
		2. [Glamour] — 
			1. **Scope**
				1. Superficial disguise
				2. Visual only
			2. **What it can do**
				1. Change clothing appearance
				2. Alter hair color
				3.  Shift apparent age slightly
				4. Blur distinguishing marks
			3. **What it cannot do**
				1. Change silhouette drastically
				2. Alter size category
				3. Change voice
			4. **Interaction**
				1. Physical contradiction may reveal inconsistency
				2. Close scrutiny exposes flaws
		3. [Sensory] — 
			1. **Scope**
				1. Single target
				2. One sensory channel at a time
			2. **What it can do**
				1. Insert a false sound (whisper, footstep)
				2. Insert a false visual flicker (shadow movement)
				3.  Alter taste of food slightly
				4. Simulate a brief tactile sensation (tap, warmth)
				5. Create a false smell
			3. **What it cannot do**
				1. Replace an entire scene
				2. Sustain multi-sensory coherence
				3. Override ongoing physical contradiction
				4. Induce strong pain
				5. Persist through deliberate scrutiny
			4. **Example**
				1. A target hears approaching footsteps that are not there.
				2. A drink tastes sour instead of sweet.
				3. Minor effects are distractions, not perceptual takeovers.
	2. Tier 2: [Hallucination] — Full sensory override that replaces perceived reality within a defined scope, without altering physical substance.
		1. [Mirage] — 
			1. **Scope**
				1. Large terrain (battlefield, forest section, city block)
				2. May simulate atmospheric conditions (dust, mist)
			2. **What it can do**
				1. Replace an entire landscape visually
				2. Simulate illusory structures
				3.  Conceal armies or buildings
			3. **What it cannot do**
				1. Alter actual terrain physics
				2. Inflict physical harm
				3. Fully override tactile reality
			4. **Max limit**  
				1. It can replace perception of space — but not the geometry of space.
		2. [Glamour] — 
			1. **Scope**
				1. Full identity replacement
				2. Multi-sensory (voice, scent, posture illusion)
			2. **What it can do**
				1. Appear as a specific individual
				2. Mask injuries
				3.  Conceal carried items visually
				4. Mimic species within similar body plan
			3. **What it cannot do**
				1. Grant abilities of imitated form
				2. Change physical mass
				3. Pass invasive biological tests
			4. **Max limit**  
				1. Physical contradiction may reveal inconsistency
				2. It changes _perception_, not substance.
		3. [Sensory] — 
			1. **Scope**
				1. One or several targets
				2. Multiple sensory channels simultaneously
			2. **What it can do**
				1. Insert sustained or complex false sounds (voices, layered movement, environmental noise)
				2. Insert persistent or detailed visual phenomena (clear figures, defined movement)
				3. Completely alter the taste of food or drink
				4. Simulate sustained tactile sensations (pressure, heat, texture)
				5. Create strong or layered smells
				6. Coordinate multiple false sensory inputs into a coherent experience
			3. **What it cannot do**
				1. Replace an entire scene
				2. Remove real stimuli
				3. Override ongoing physical contradiction
				4. Impose belief, emotion, or compulsion
				5. Cause real physical injury
				6. Alter the physical environment
			4. **Example**  
				1. Hears multiple distinct voices speaking around them
				2. Sees a clearly defined illusory figure moving in the room
				3. Smells smoke enough to begin coughing
				4. Feels intense heat on their skin
				5. Tastes ash in their mouth

5. Sound
	1. Tier 1: [Sound] — Directed vibration or shockwave capable of transmitting audible force or concussive impact; applies [Sonic]
	2. Tier 2: [Deafened] — Disruption of auditory processing that prevents the target from perceiving sound; applies [Deafened]

6. Sanity
	1. Tier 1: [Disturb] — Destabilizing psychological pressure that disrupts emotional stability or self-perception. [Disturb]
	2. Tier 2: [Break] — Severe psychological fracture that collapses coherent thought, identity stability, or emotional control; applies [Madness]

## 4. Temporal

1. Time 
	1. Tier 1: [Cadence] — Localized alteration of how time flows for a target, affecting movement speed, perception speed, short sequences of actions, or the outcome of a single resolved event.
		1. Velocity (Physical Time)
			1. [Slow] — Halve target movement speed.
			2. [Fast] — Doubles target movement speed.
		2. Awareness (Perceptual Time) 
			1. [Tachypsychia] — A distorted perception of time, causing it to feel slowed down or rapidly sped up. A targets perception of time doubles to either twice as fast (1min feels 30sec) or twice as slow (30sec feels 1min). This only effects perception, movement speed remains the same. 
		3. Sequencing (Narrative Time)
			1. [Dyschronometria] — You can [Rewind] Or [Fast-forward] a target's time mentally (ie. thoughts or conversation) or physically (ie. actions or movement) up to 10 seconds. Choosing to effect a target physically does not erase or alter their mental awareness of events. 
		4. Causality (Outcome Time) 
			1. [Terms] — You may change up to 1 Actions worth of an outcome to be either a [Positive] or [Negative], this is done through either a [Reroll], Adding or Subtracting 2 from the end result, shift the gradient roll result up or down by 1. Whatever you chose you will roll once on the Wild Magic Table.
	2. Tier 2: [Flux] — Severe distortion of time flow that suspends, accelerates, extends, or forcefully alters action sequences or resolved outcomes beyond normal limits.
		1. Velocity (Physical Time) 
			1. [Stasis] — A near-total suspension of temporal flow around a target, halting progression through time. Target loses 1 Action in addition to half movement speed. (You gain 1 [Exhaustion] for every Action removed removed from target, and 1 [Exhaustion] when effects end.)
			2. [Overclocked] — An extreme surge of temporal acceleration that pushes a target beyond natural limits. Target gains 1 additional Action, move once per turn without expending an action. (Target gains 1 [Exhaustion] for every free movement taken, and 1 [Exhaustion] when effects end.)
		2. Awareness (Perceptual Time) 
			1. [Tachysensia]  — A significant distortion of time and sound perception. A targets perception of time doubles to either twice as fast (1min feels 30sec) or twice as slow (30sec feels 1min). The targets response time is adjusted to their current perception of time (either twice as fast or slow). From the moment it's applied to every round after this is active the target will gain 1 [Madness] stack, If you are not the target you take half the [Madness] stacks the target took min 1 stack. 
		3. Sequencing (Narrative Time) 
			1. [Cerebellar Ataxia] — You can [Rewind] or [Fast-forward] a target's time mentally (ie. thoughts or conversation) and physically (ie. actions or movement) the time frame is based on the Spell Framework (ie. Instant to Hours/ permeant). For each level of duration increase, starting at Instant, you will take 1 [Exhaustion] and 1 [Madness] stacks.
		4. Causality (Outcome Time) 
			1. [Terms & Conditions] — You may change up to 2 Actions worth of an outcome to be either a [Positive] or [Negative], this is done through either a [Reroll], Adding or Subtracting 4 from the end result, shift the gradient roll result up or down by 2. Whatever you chose you will roll twice on the wild magic table. Alternatively you may choose to have the outcome absolutely succeed or fail, if you do you will roll 5 times on the Wild Magic Table and gain 2 [Exhaustion] 

2. Blink
	1. Tier 1: [Blink] — A brief spatial shift that relocates a target a short distance without traversing the intervening space.
	2. Tier 2: [Teleport] — An immediate and decisive relocation across space, ignoring intervening distance and obstacles.

3. Displace
	1. Tier 1: [Displace] — A forced repositioning that moves a target from its current location to another valid space within range.
	2. Tier 2: [Rewrite Position] — A direct override of spatial arrangement that replaces a target’s position regardless of prior placement.
		1. (swap locations, forced relocation)

## 5. Transmutation

1. Harden
	1. Tier 1: [Harden] — Temporarily increases a material’s toughness, making it more resistant to damage, pressure, or deformation.
	2. Tier 2: [Reinforce] — Greatly strengthens a material beyond its normal limits, increasing its resistance to breaking, bending, or being destroyed.

2. Soften
	1. Tier 1: [Soften] — Reduces rigidity, making a material flexible, bendable, or easier to deform.
	2. Tier 2: [Melt] — Breaks down solidity, causing the material to lose shape and behave like liquid or unstable matter.

3. Shapeshift
	1. Tier 1: [Partial] — Alters specific physical features such as limbs, facial traits, or body proportions while the core body remains the same.
	2. Tier 2: [Full] — Completely transforms the target’s physical body into a different form.

4. Grow
	1. Tier 1: [Enlarge] — Increases the target’s size beyond its natural dimensions.
	2. Tier 2: [Overgrow] — Greatly increases size beyond normal proportion, potentially straining structure or stability.

5. Reduce
	1. Tier 1: [Shrink] — Decreases the target’s size below its natural dimensions.
	2. Tier 2: [Miniaturize] — Reduces the target to a drastically smaller scale.

6. Multiply
	1. Tier 1: [Duplicate] — Creates one additional copy of the original form.
	2. Tier 2: [Replicate] — Creates multiple copies that persist and function as separate entities.

7. Transmute
	1. Tier 1: [Alter Material] — Changes a material’s properties (such as hardness, flexibility, weight, or texture) while keeping it fundamentally the same substance.
	2. Tier 2: [Convert Material] — Completely changes one substance into a different substance.

## 6. Order

1. Smite
	1. Tier 1: [Strike] — Delivers a direct, targeted burst of force or energy to a chosen target; applies [Bleed]
	2. Tier 2: [Judgement] — Delivers a decisive, targeted strike that applies additional consequence beyond damage (such as marking, weakening, or enforcing a condition tied to the effect); applies [Shredded] 

2. Bind
	1. Tier 1: [Restrict] — Limits a target’s movement or available actions through magical or imposed constraint.
	2. Tier 2: [Seal] — Completely contains or locks a target, object, area, or effect so that it cannot escape, be altered, or interact beyond defined boundaries.

3. Ward **
	1. Tier 1: [Suppression] — Creates a defined boundary or area that reduces the effectiveness or intensity of specified non-organic forces or effects (Force, Temporal, Order).
	2. Tier 2: [Nullify] — Creates a defined boundary or area that completely cancels specified non-organic forces or effects (Force, Temporal, Order) while active.

4. Truth
	1. Tier 1: [Reveal Fact] — Detects or exposes hidden information, lies, disguises, or concealed data within range.
	2. Tier 2: [Compel Truth] — Forces a target to answer questions or speak without deliberate falsehood while the effect persists.

5. Reveal
	1. Tier 1: [Expose] — Removes visual, magical, or physical concealment from a target or area.
	2. Tier 2: [Lay Bare] — Completely strips concealment, disguise, illusion, invisibility, or hidden properties from a target or area.

## 7. Life

1. Restoration
	1. Tier 1: [Restore] — Repairs recent damage to a living target, restoring lost health or stabilizing injuries that have not resulted in permanent loss.
	2. Tier 2: [Regenerate] — Restores lost body parts, reverses severe physical trauma, and provides ongoing recovery while active.

2. Resurrect
	1. Tier 1: [Rouse] — Returns a recently deceased target to life, provided the body is intact and death occurred within a limited timeframe.
	2. Tier 2: [Revive] — Returns a long-dead target to life by reuniting body and soul, even after extended separation or decay, subject to extreme cost or risk.

3. Radiance **
	1. Tier 1: [Radiant] — Emits concentrated light-infused energy that damages or disrupts organic or corrupted targets and may illuminate an area; applies [Radiant]
	2. Tier 2: [Purge] — Removes or suppresses a chosen active organic or biological condition or effect within a target or area (Elemental, Mind, Life domains as defined).

4. Light
	1. Tier 1: [Illuminate] — Creates light within a defined area or on a target, removing darkness and enabling normal visual perception.
	2. Tier 2: [Blind] — Removes a target’s ability to perceive visually while the effect persists.

## 8. Death

1. Necrotic
	1. Tier 1: [Necrosis] — Dark energy destabilizes living material and siphoning of vitality or essence from a target; applies [Necrotic]
	2. Tier 2: [Necroptosis] — A lethal internal cascade that forces the body to tear itself apart fully absorbing or devouring the vitality of the target.

2. Death
	1.  Tier 1: [Pyroptosis] — The target detonates with necrotic energy, spreading lethal corruption outward 5ft.
		1. The target exudes a 5ft radius of [Necrotic] damage that can infect others with the same condition.
	2. Tier 2: [Apoptosis] — A terminal effect causing the target to shut down instantly.
		1. (immediate death) 

3. Undeath
	1. Tier 1: [Reanimate] — The temporary restoration of motion to lifeless matter.
	2. Tier 2: [Vivify] — The forced tethering of spirit or essence to a vessel beyond natural death.

4. Rot
	1. Tier 1: [Decay] — The slow weakening and deterioration of vitality or structure; applies [Weaken]
	2. Tier 2: [Wither] — The final failure of integrity resulting in structural or biological breakdown; applies [Vulnerable]

5. Darkness
	1. Tier 1: [Obscure] — The spreading of shadow that diminishes clarity and visibility.
	2. Tier 2: [Blackout] — An engulfing absence of light that consumes presence and suppresses illumination.

## 9. Chaos

1. Chaos
	1. Tier 1: [Instability] — A disruptive force that undermines structure, predictability, and controlled outcomes.
	2. Tier 2: [Wild Magic] — A fully unbound expression of chaotic power that manifests without stable form or reliable control.

## 10. Summoning

1. Conjure
	1. Tier 1: [Invite] — The act of drawing an entity or presence from elsewhere into proximity.
	2. Tier 2: [Summon] — The enforced tethering of a summoned entity to sustained service or containment.


# Create conditions

