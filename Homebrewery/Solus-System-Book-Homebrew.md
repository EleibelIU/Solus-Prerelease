```metadata
title: Solus Frostmaiden Theme
description: 'Frostmaiden-style theme for Solus rulebook'
tags:
- meta:Theme
systems:
- 5e
renderer: V3
theme: 5ePHB
```

```css
@import url('https://rawcdn.githack.com/Kaiburr-kath-hound/HomebreweryStyles/be88dc909ce74e765dc546aed91b1499fa5d6e7b/FrostmaidenFonts.css');

.page {
	background-image	: url(https://i.imgur.com/9uez4Wb.jpg);
	background-size		: cover;
}
.page:nth-of-type(odd) {
	background-image	: url(https://i.imgur.com/mGKSuw3.jpg);
}

.page h1, 
.page h2, 
.page h3, 
.page h4, 
.page h5 {
	letter-spacing    : 1px;
  font-weight       : normal;
}

.page h1 {
  padding-bottom      :10px;
}
.page h1+p::first-letter,
.page h1+.quote::first-letter {
	font-size           : 12.5em;
  padding-right       : 4px;
  margin-top          : -20px;
  margin-left         : -30px;
	color               : black;
}
.page:has(h1):not(.page:has(.none),
                  .page:has(.toc),
                  .page:has(.credits),
                  .page:has(.insideCover))::before {
	content						: '';
	position					: absolute;
	width							: 280px;
	height						: 280px;
	top								: 10px;
	left							: 0;
	z-index						: -2;
	background-image	: url(https://i.imgur.com/g7RTsXo.png);
	background-size		: cover;
}

.page h5 {   
  font-weight       : bold;
  text-shadow	      : #000 0 0 0.1px; 
}

.page .note {
	background-color		: #d2d6db;
}
.page .note { 
	border-image				: url(https://i.imgur.com/KtrHa62.png) 14 stretch;
	border-image-outset	: 6px 0px;
	border-image-width  : 11px;
}

.page img:not(.logo img):not(.frontcredit img) {
	position		: absolute;
	z-index			: -2;
	user-select	: none;
}
.page .emblem img {
	z-index			: 1!important;
}

.page .descriptive {
	background-color		: #e7e8eb;
}
.page .descriptive {
	border-image				: url(https://i.imgur.com/cfyTOm4.png) 12 stretch;
	border-image-outset : 4px;
}

.page table tr:nth-child(odd) td {
	background-color		: #dbdee2;
}

.page .monster.frame {
	background-color		: #f9ecbd;
}
.page .monster table tr:nth-child(odd) td {
	background-color		: transparent;
}

.page .note { 
	margin-top : 5mm; 
}
.page .note + .note { 
	margin-top : 2.5em; 
}

.page .note ol > li {
	padding: 0 0 0 0.4em;
	text-indent: -1.5em;
	list-style-type: none;
	counter-increment: item;
}
.page .note ul {
	margin-top: 0.6em;
}

.page ol {
	margin: 0.4em 0 0.5em;
	padding: 0;
}
.page ol > li {
	padding: 0 0 0 1.3em;
	text-indent: -1.5em;
	list-style-type: none;
	counter-increment: item;
}
.page ol > li:before {
	display: inline-block;
	width: 1em;
	padding-right: 0.5em;
	font-weight: bold;
	text-align: right;
	content: counter(item) '.';
}

.page .artist {
  position          : absolute !important;
	bottom						: 100px;
	left							: 60px;
	transform					: rotate(-90deg);
	transform-origin	: bottom left;
  text-align        : left;
	font-family			  : ScalySansSmallCapsRemake;
	font-size				  : 13px;
  text-transform    : lowercase;
	color							: #818892;
}
.page:nth-of-type(even):not(:has(.insideCover)) .artist {
	left						  : unset;
	right						  : 60px;
	transform					: rotate(90deg);
	transform-origin	: bottom right;
}

.page caps {
	font-variant	: small-caps;
}
.page .backcover caps {
	font-size			: 120%;
}

.page [class*="watercolor"] {
	background-color	: #7a0000;
}

.page:after {
	bottom						: -10px;
	height						: 70px;
	background-image	: url(https://i.imgur.com/c8LZtAy.png);
}

.page:not(:has(.frontCover),:has(.credits)) .footnote {
	left						: 90px;
	bottom					: 45px;
	font-size				: 11px;
	color						: #818892;
	text-transform	: uppercase;
	text-align			: left;
	width						: 400px;
	font-weight			: 800;
	font-family			: Marco Polo;
	letter-spacing	: 1.2px;
	z-index					: -3;	
	--shadow-x0			: #fcfcfc 0 0 5px;
	--shadow-x1	: var(--shadow-x0), var(--shadow-x0), var(--shadow-x0);
	text-shadow	: var(--shadow-x1), var(--shadow-x1), var(--shadow-x0);
}

.page:nth-of-type(even):not(:has(.frontCover),:has(.credits)) .footnote {
  left            : unset;
  right           : 90px;
  text-align      : right;
}

.page .pageNumber {
	left 				    : 15px;
	bottom					: 34px;
	font-size				: 16px;
	color						: #818892;
	text-align			: center;
	font-family			: Marco Polo;
	font-weight			: 100;
	--shadow-x0			: #fcfcfc 0 0 3px;
	--shadow-x1	: var(--shadow-x0), var(--shadow-x0), var(--shadow-x0);
	text-shadow	: var(--shadow-x1), var(--shadow-x1), var(--shadow-x1);
}

.page:nth-of-type(even) .pageNumber {
  left            : unset;
  right           : 15px;
}

.page a {
	color						: inherit;
	text-decoration	: none;
	font-weight			: inherit;
}
.page a:hover{
	text-decoration	: underline;
}

.page .quote {
	font-family 		: Cormorant;
	font-size				: 15px;
	line-height			: 1em;
	margin-top			: 0;
	padding-bottom	: 4px;
}

.page .quote.author p:last-child {
	font-family 		: BookInsanityRemake;
	font-size				: 0.34cm;
	margin-top			: 4px;
	text-align			: right;
}

.page:has(.frontCover) .logo {
  top             : 23px;
}
.page:has(.frontCover) {
  padding-top     : 78px;
}
.page:has(.frontCover) h1 {
  margin-top      : 12px;
  text-transform  : none;
  font-size       : 98px;
}

.page:has(.frontCover) hr {
  width           : 10cm;
}

.page:has(.frontCover) h2,
.page:has(.frontCover) h3 {
  filter          : drop-shadow(0 0 1.3px black) drop-shadow(0 0 0 black)
                    drop-shadow(0 0 0 black)  drop-shadow(0 0 0 black)
                    drop-shadow(0 0 0 black)  drop-shadow(0 0 0 black)
                    drop-shadow(0 0 0 black)  drop-shadow(0 0 0 black);
	font-family     : 'Modesto Expanded';
  font-size       : 0.8cm;
  letter-spacing  : 0.1cm;
  margin-top      : 10px;
  transform       : ScaleX(0.9);
}

.page:has(.frontCover) h3 {
  color           : white;
  border-bottom   : none;
  font-size       : 0.64cm;
}

.page:has(.frontCover) .footnote {
	font-family		  : VeraCruz;
  letter-spacing  : 1px;
  z-index         : 1;
	width						: fit-content;
}

.page small {
  position			  : relative;
  text-transform  : lowercase;
  bottom				  : 10px;
  font-size			  : 90%;
}
      
.page:has(.frontCover) .emblem,
.page:has(.frontCover) .color {
  position					  : absolute;
  top								  : 0; 
  left							  : 0;
  background-size		  : 100% 100%;
  background-repeat	  : no-repeat;
}
.page:has(.frontCover) .color {
  height						  : 19px;
  width							  : 650px;
  background-color	  : black;
  opacity						  : 75%;
  z-index						  : -1;
  -webkit-mask-image  : url(https://i.imgur.com/bURATrX.png);
  -webkit-mask-size	  : 100% 100%;   
}
.page:has(.frontCover) .emblem {
  height						  : 80px;
  width							  : 340px;
  z-index						  : 0;
  background-image	  : url(https://i.imgur.com/y2xctk4.png);
}
.page:has(.frontCover) .emblem img {
  left							  : 20px;
  top								  : 0;
  min-width					  : unset;
  max-width					  : 50%;
  max-height				  : 100%;
  z-index						  : 1;
}

.page:has(.insideCover) h1 {
	font-size				: 88px;
}

.page:has(.insideCover) h2 {
	font-family			: Nodesto;
	font-size				: 3em;
	letter-spacing	: 0.8px;
}

.page:has(.insideCover) h3 {
	font-family     : 'Modesto Expanded';
	font-weight     : normal;
	font-size       : 31px;
	letter-spacing  : 1px;
 	border-bottom   : unset;
  margin          : 10px -80px 20px;
  width           : 816px;
}

.page:has(.credits) h1+p::first-letter, 
.page:has(.credits) h1+p::first-line,
.page:has(.credits)::after {
	all	: unset;
}

.page:has(.credits) h1 {
	font-size	: 40px;
}

.page:has(.credits h2), 
.page:has(.credits h5) {
	margin-bottom	:14px;
}

.page:has(.credits) p {
	font-family	: Martel_SansRegular;
	font-style	: normal;
	font-size		: 0.83em;
	line-height	: 1.5em;
	text-indent	: -1em; 
	margin-left	: 1em;
}

.page:has(.credits) strong {
	font-family	: Martel_SansExtraBold;
}

.credits a {
	color				: #6c0007;
	font-weight	: bold;
}

.page .frontcredit {
	position						: relative;
	right								: 10px;
	width               : 340px;
	height              : 240px;
	margin-top					: 15px;
	margin-bottom				: 110px;
}

.frontcredit::before {
	content							: '';
	position						: absolute;
	top									: 4px;
	left								: -20px;
	height							: 98%;
	width								: 109.2%;
	background-image		: url(https://i.imgur.com/VToJGxP.png);
	background-size			: 100% 100%;
  z-index             : 1;
}

.frontcredit img {
	position							: relative;
	top										: 5px;
	left									: -18px;
	width									: 108.5%;
	height								: 234px;
	-webkit-mask-image		: url(https://i.imgur.com/PN6zgvK.png);
	-webkit-mask-position	: top;
	-webkit-mask-size			: 100% 234px;
	-webkit-mask-repeat		: no-repeat;
}

.frontcredit h5 {
	margin-top		: 10px;
	margin-bottom	: -2px;
	text-shadow		: #000 0px 0px 0.1px;
}

.page .frontcredit p {
	text-indent	: 0em; 
	margin-left	: 0em;
}

.credits .footnote {
	bottom					: 20px;
	left						: 0;
	width						: 100%;
	font-size				: 1em;
	text-transform	: none;
	text-align			: left;
	color						: black;
}

.credits .footnote p {
	padding			    : 4.5em;
	text-indent	    : 0;
}

.page:has(.toc) h1 {
	text-align			: left;
}
	
.page .toc h3,
.page .toc h4 {
	font-family			: BookInsanityRemake;
	font-size				: 12px;
	letter-spacing	: 0;
}
  
.page .toc h3 {
	font-weight			: bold;
	border-bottom		: unset;
}

.page .toc h4 {
	margin-top			: 2px;
	color						: black;
}

.page .toc ul h3 span:first-child::after {
	border-bottom   : 0.05cm dotted #000;
}
	
.page .toc ul li + li h3 {
	margin-top	    : 8px;
}

.page .toc.wide {
	columns			    : 3;
  column-gap      : 16px;
}

.page .tome {
	position						: relative;
	border-width        : 1px;
	border-image				: url(https://i.imgur.com/YLID50W.png) 38 27;
	border-image-outset	: 22px 10px;
	border-image-width	: 19px;
	padding             : 0.13cm 0.16cm;
	margin					    : 16px 0 46px;
}

.tome p {
  padding         : 0 14px;
}

.quote.tome p::first-line {
	font-variant 		: small-caps;
	font-family 		: BookInsanityRemake;
	font-size				: 15px;
	text-transform	: lowercase;
	line-height			: 14px;
}

.quote.tome p + p::first-line {
	font-variant 		: unset;
	font-family 		: inherit;
	font-size				: inherit;
	text-transform	: inherit;
	line-height			: inherit;
}

.tome.quote.author p:last-child {
	font-family 		: Cormorant;
	font-size				: 0.4cm;
	margin-top			: 4px;
	text-align			: right;
}

.page:has(.backCover)	.backCover {
	filter			: drop-shadow(0 0 30px rgba(237, 31, 36, 0));
}

.page:has(.backCover) h1 {
	font-size		: 58px;
}

.page:has(.backCover) p {
	font-family	: martel_sanssemibold;
	font-size		: 11.7px;
	line-height	: 1.6em;
	text-indent	: 0em;
}

.page:has(.backCover) caps {
	font-size		: 125%;
}
```

<!-- COVER PAGE -->

![Solus Cover](https://github.com/EleibelIU/Solus-Prerelease/blob/main/Homebrewery/Assets/Solus%20Cover.png?raw=true){right:0px,bottom:0px,top:unset,height:100%}


\page

<!-- TABLE OF CONTENTS -->

{{toc,wide

# Contents

- ### [{{ Ch. 1: Welcome to Solus}}{{ 3}}](#p3)
  - #### [{{ What You Need}}{{ 3}}](#p3)
  - #### [{{ Roles at the Table}}{{ 3}}](#p3)
  - #### [{{ How a Session Plays}}{{ 4}}](#p4)
- ### [{{ How to Use This Book}}{{ 6}}](#p6)
- ### [{{ Ch. 2: Core Mechanics}}{{ 7}}](#p7)
  - #### [{{ Key Terms}}{{ 7}}](#p7)
  - #### [{{ How Dice Work}}{{ 7}}](#p7)
  - #### [{{ The Two Roll Types}}{{ 7}}](#p7)
- ### [{{ Ch. 3: Character Creation}}{{ 9}}](#p9)
  - #### [{{ Steps 1–4: Concept, Attributes, Race, Background}}{{ 9}}](#p9)
  - #### [{{ Steps 5–6: Initiative Modifier, Tag Affinities}}{{ 9}}](#p9)
  - #### [{{ Steps 7–9: Proficiencies, Equipment, Review}}{{ 10}}](#p10)
- ### [{{ Ch. 4: Attributes and Proficiencies}}{{ 11}}](#p11)
  - #### [{{ The Five Attributes}}{{ 11}}](#p11)
  - #### [{{ Proficiencies}}{{ 12}}](#p12)
  - #### [{{ Proficiency List}}{{ 12}}](#p12)
- ### [{{ Ch. 5: Armor and Defense}}{{ 13}}](#p13)
- ### [{{ Ch. 6: Weapons, Techniques, and Augments}}{{ 14}}](#p14)
  - #### [{{ Armor}}{{ 13}}](#p13)
  - #### [{{ Weapons}}{{ 14}}](#p14)
- ### [{{ Ch. 6: Magic and Spellcasting}}{{ 15}}](#p15)
  - #### [{{ Tag Affinities}}{{ 15}}](#p15)
  - #### [{{ Building a Spell: Fire Bolt}}{{ 16}}](#p16)
- ### [{{ Ch. 7: Core Gameplay Loop}}{{ 17}}](#p17)
- ### [{{ Ch. 8: Combat}}{{ 18}}](#p18)
  - #### [{{ Actions and Reactions}}{{ 18}}](#p18)
  - #### [{{ Resolving an Attack}}{{ 18}}](#p18)
  - #### [{{ Worked Example}}{{ 19}}](#p19)
- ### [{{ Ch. 9: Conditions, Injuries, and Death}}{{ 20}}](#p20)
  - #### [{{ Tags and Stacks}}{{ 21}}](#p21)
  - #### [{{ Condition Profiles}}{{ 22}}](#p22)
  - #### [{{ Other Conditions}}{{ 23}}](#p23)
  - #### [{{ Dropping to 0 HP}}{{ 23}}](#p23)
- ### [{{ Ch. 10: NPCs, Enemies, and Encounters}}{{ 24}}](#p24)
- ### [{{ Ch. 11: Advancement and Between-Session Play}}{{ 25}}](#p25)
- ### [{{ Ch. 12: Running the Game}}{{ 26}}](#p26)
- ### [{{ Ch. 13: Reference and Playtest Tools}}{{ 27}}](#p27)
  - #### [{{ Reference Tables}}{{ 27}}](#p27)
  - #### [{{ Systems Reference}}{{ 29}}](#p29)
  - #### [{{ Glossary}}{{ 32}}](#p32)

}}

<!-- Remove footer on TOC page -->
<style> .page#p2:after {all: unset} </style>

\page

<!-- CHAPTER 1: WELCOME TO SOLUS -->

# Welcome to Solus

Solus is a tabletop roleplaying game for three to six people. One person runs the world as the Game Master. Everyone else plays a character inside it. You describe what your character does, roll dice when the outcome is uncertain, and discover the consequences together. The system rewards tactical choices and punishes carelessness. Your character can grow powerful, but the world grows dangerous to match.

### What You Need

**Two ten-sided dice (2d10).** Each die is numbered 1 through 10. You add the two dice together for a single total. A roll of 7 and 5 gives you 12. Solus does not use percentile dice, twenty-sided dice, or any other die type for core rolls.

**A character sheet.** This records your five attributes (Body, Mind, Social, Magic, Atraxia), your Atraxia Pool, your skills, your equipment, your health, and your mana. The Character Creation chapter walks you through filling one out.

**Friends.** Solus works best with three to five players and one GM.

**Pencils and scratch paper.** You will track health, mana, conditions, and initiative during play.

\column

### Roles at the Table

**The Game Master (GM)** describes the world, controls all non-player characters (NPCs), sets target numbers for uncertain actions, and adjudicates the rules. The GM does not play against you. The GM plays the world around you.

**Players** each control one character. You decide what your character attempts, roll dice when the rules call for it, and describe how your character reacts to what happens. Your character sheet tells you what your character is good at. The dice tell you whether it works.

{{footnote Welcome to Solus}}
{{pageNumber,auto}}

\page

## How a Session Plays

The best way to learn Solus is to watch a round of play. The scene below uses real rules. Every roll, modifier, and target number works the way the full chapters describe. You do not need to memorize the math yet. Read it once to see how the pieces fit. Come back after reading the rules to see why each number lands where it does.

Terms used in this scene are defined in the chapters that follow. If you see a bolded term you do not recognize, check the Glossary at the end of this book.

{{footnote Welcome to Solus}}
{{pageNumber,auto}}


### The Setup

Three players sit at a table with their GM.

- **Jake** is a martial fighter. Body +4, Mind +1, Social +0, Magic -2, Atraxia +2. He carries a greatsword (1d8 damage, Heavy tag) and wears Medium armor (Physical DR 3, Magic DR 1).

- **Chris** is a hybrid spellblade. Body +2, Mind +0, Social +1, Magic +3, Atraxia -1. She carries a shortsword (1d6 damage) and wears Light armor (Physical DR 1, Magic DR 3).

- **Liz** is a social infiltrator. Body +1, Mind +3, Social +4, Magic -1, Atraxia -2. She carries a dagger (1d4 damage) and wears Cloth armor (Physical DR 0, Magic DR 0).

#### Scene: The Collapsed Bridge

{{descriptive
**The GM speaks:** "You've been tracking a stolen shipment through the forest for two days. The trail leads to a stone bridge over a ravine. The bridge is half-collapsed. The far side still holds, but the gap is twelve feet wide. You can hear voices on the other side."

**Liz's player says:** "I want to listen and figure out how many people are over there."
}}

The GM calls for a **Proficiency Check**. The proficiency is **Investigation**. Investigation's primary attribute is Mind. Liz's player picks Body as her secondary for this check—she is pressing close to the ground, using her position to catch sound across the ravine. Her Mind is +3 and her Body is +1, so her Investigation modifier for this roll is **+4**. The GM sets the **Difficulty Class (DC)** at 14, because the targets are speaking quietly across a ravine with wind.

Liz's player rolls 2d10: **6 + 9 = 15**, plus her modifier of +4 = **19**. She beats the DC of 14 by 5. The GM uses the **Degree of 5** scale: beating a DC by 5 or more earns a bonus.

{{descriptive
**The GM says:**
"You count three distinct voices. One sounds frustrated, barking orders. You also catch the glint of a fourth figure crouched behind a rock. Four enemies total."
}}


If Liz had rolled a 4 + 3 = 7, plus 4 = 11, she would have missed the DC by 3. 

{{descriptive
**Jake's player says:** "I want to jump the gap."
}}

Twelve feet is a serious distance. The GM calls for an **Athletics** Proficiency Check, DC 13. Athletics uses Body as its primary. Jake's player picks Mind as his secondary for this check—trained jumping technique over brute force. His Body is +4 and Mind is +1, giving him an Athletics modifier of **+5**.

Jake rolls 2d10: **8 + 7 = 15**, plus 5 = **20**. He clears the gap by a wide margin. The GM describes him landing in a crouch on the far side. Because he beat the DC by 7 (more than 5), the GM rules he lands silently and keeps his footing.

Chris follows. Same DC, but her Athletics modifier is lower (Body +2, secondary Mind +0 = **+2**). She rolls: **5 + 6 = 11**, plus 2 = **13**. She meets the DC exactly. She makes it across, but stumbles on the landing. The enemies hear the noise.

#### Combat Begins

{{descriptive
**The GM says:** "A bandit with a crossbow shouts an alarm. Roll initiative."
}}

**Initiative** uses a d10 (one ten-sided die) plus Body or Magic, your choice per character.

| Character | Roll | Modifier | Total |
|:---|:---:|:---:|:---:|
| Jake | 7 | +4 (Body) | 11 |
| Chris | 5 | +3 (Magic) | 8 |
| Bandit Leader | 7 | +3 (Body) | 10 |
| Bandit Archer | 4 | +0 (Body) | 4 |

Turn order: Jake (11), Bandit Leader (10), Chris (8), Bandit Archer (4). Ties go to the higher modifier. If still tied, the GM decides.

Each character gets **3 actions** per turn. The most common actions for a player to use are *Move*, *Attack*, *Defend*, *Use Item*, and *Cast Spell*.


{{descriptive
**Jake's player says:** "I spend my first action to Move toward the bandit leader. Second action: Attack with my greatsword. Third action: Attack again."
}}

- **First Attack.** Jake rolls a **Combat Roll**: `2d10 + Body` because the greatsword is a physical weapon. He rolls **6 + 8 = 14**, plus Body +4 = **18**. The Bandit Leader (100 HP) wears Medium armor (Physical DR 3) and has Body +3, giving a **Physical AC of 6** (DR 3 + Body 3). Jake's 18 beats 6, so he hits. He rolls greatsword damage: **1d8 = 5**, plus Body +4 = **9**. The bandit's Physical DR of 3 absorbs 3 points. The bandit takes **6 damage** and drops to 94 HP.

\page

- **Second Attack.** Jake rolls again: **3 + 4 = 7**, plus 4 = **11**. Still beats the AC of 6. Damage: **1d8 = 7**, plus 4 = **11**, minus 3 DR = **8 damage**. The bandit leader drops to 86 HP.

{{footnote Welcome to Solus}}
{{pageNumber,auto}}


{{descriptive
**Chris's player says:** "First action: Move to flank the archer. Second action: Attack the archer with my shortsword. Third action: Cast a fire bolt at the bandit leader."
}}

- **Shortsword Attack.** Physical weapon, so she rolls `2d10 + Body`. Her Body is +2. She rolls **9 + 5 = 14**, plus 2 = **16**. The archer is a Minion (5 HP, Cloth armor, Physical DR 0, Body +0), so Physical AC is **0**. She hits. Shortsword damage: **1d6 = 4**, plus Body +2 = **6**, minus 0 DR = **6 damage**. The archer had 5 HP and drops to 0. When a character drops to 0 HP, they are incapacitated (see Conditions, Injuries, and Death).

- **Fire Bolt.** Spell, so she rolls `2d10 + Magic`. Her Magic is +3. She rolls **4 + 7 = 11**, plus 3 = **14**. The bandit leader's **Magical AC** is Magic DR 1 (Medium armor) + Magic -1 = **0**. She hits. Spell damage: **1d6 + 1d8 + 3 = 3 + 5 + 3 = 11**, minus Magic DR 1 = **10 damage**. The bandit leader drops to 76 HP. The fight continues.

{{footnote Welcome to Solus}}
{{pageNumber,auto}}


#### What Just Happened

In a few minutes of play, the group used three systems:

**Proficiency Checks** resolved Liz's Investigation (hearing enemies) and Jake's Athletics (jumping the gap). Both used `2d10 + Proficiency Modifier` against a DC the GM set. Each player chose which secondary attribute to add for that specific roll.

**Combat Rolls** resolved Jake's greatsword swings and Chris's shortsword strike using `2d10 + Body`, and Chris's fire bolt using `2d10 + Magic`. Physical attacks targeted Physical AC. The spell targeted Magical AC.

Each character had 3 **actions** per turn, spent on movement, attacks, and spells in any combination.

These three systems carry the game. The chapters that follow teach each one in full.

{{footnote Welcome to Solus}}
{{pageNumber,auto}}

\page

# How to use this book

{{wide 
| If you want to... | Go to... |
|:---|:---|
| Learn how dice, rolls, and target numbers work | Core Mechanics (Ch. 2) |
| Build a character from scratch | Character Creation (Ch. 3) |
| Understand your five attributes and eleven proficiencies | Attributes and Proficiencies (Ch. 4) |
| Choose armor | Armor and Defense (Ch. 5) |
| Choose weapons and Techniques | Weapons, Techniques, and Augments (Ch. 6) |
| Learn how spells are built and cast | Magic and Spellcasting (Ch. 6) |
| Understand how sessions and encounters flow | Core Gameplay Loop (Ch. 7) |
| Run a full combat encounter | Combat (Ch. 8) |
| Look up a condition or what happens at 0 HP | Conditions, Injuries, and Death (Ch. 9) |
| Build or reference NPCs and encounters | NPCs, Enemies, and Encounters (Ch. 10) |
| Advance your character between sessions | Advancement and Between Sessions (Ch. 11) |
| Run the game as a GM | Running the Game (Ch. 12) |
| Quick-reference tables, playtest checklist, glossary | Reference and Playtest Tools (Ch. 13) |
}}

{{pageNumber,auto}}

\page

<!-- CHAPTER 2: CORE MECHANICS -->

# Core Mechanics

This chapter covers the rules that every other chapter builds on: how dice work, what the numbers on your sheet mean, and the two types of rolls you will make during play.

## Key Terms

Before you read further, here are four numbers you will see on every character sheet:

**Hit Points (HP)** measure how much damage your character can take. When your HP reaches 0, your character is incapacitated (see Conditions, Injuries, and Death). Your maximum HP is set by your background during character creation and does not change.

**Mana** is the resource you spend to use skills and cast spells. Your mana pool starts full at the beginning of each session. During combat, mana regenerates at the start of each of your turns by an amount set by your background (see Character Creation, Step 4). Outside of combat, mana refills between encounters.

**Atraxia Pool** is a tracked number generated at character creation that represents your long-term tolerance for punishment. It drains when you enter the dying state and does not regenerate on its own. When it reaches 0, your character is permanently dead. (See Attributes and Proficiencies: The Atraxia Pool, and Conditions, Injuries, and Death: Dropping to 0 HP.)

**Experience Points (XP)** are the currency of character growth. You earn XP from combat, exploration, and social encounters. You spend XP between sessions to buy new skills and raise existing ones (see Advancement and Between-Session Play).

**Modifiers** are numbers from -5 to +5 that represent your character's capability in a given area. You add a modifier to your dice roll. For most attributes, a higher modifier produces stronger results. Atraxia is the exception: low Atraxia is not worse, it is different (see Attributes and Proficiencies).

## How Dice Work

Solus uses two ten-sided dice, written as **2d10**. Each die is numbered 1 through 10. Roll both and add the numbers together to get a single total.

After adding the dice, add a number from your character sheet called a **modifier**. Modifiers range from -5 to +5. The final number is your **result**.

{{note
**Example:** You roll a 7 and a 5. That's 12. Your modifier is +3. Your result is 15.
}}

The two dice are added, not read side by side. A roll of 10 and 4 is 14, not 104. Solus does not use percentile dice.

The GM sets a **target number**. If your result meets or beats the target, you succeed. If it falls short, you fail.

### When You Roll

 An adventurer is competent at adventuring. If your character would reasonably succeed at a task given who they are and the circumstances are calm, the GM describes the success without dice. If the task is impossible given the situation, the GM describes the failure. Dice come out when pressure, complexity, or opposition make the result genuinely uncertain.


### Critical Results

If both dice show 10 (a natural 20), you score a **critical success**. The effect lands at its best possible outcome.

If both dice show 1 (a natural 2), you score a **critical failure**. The effect backfires or misfires.

Critical results apply to any 2d10 roll unless a specific rule says otherwise.

### Advantage and Disadvantage

Some conditions, abilities, or circumstances give you **advantage** or **disadvantage** on a roll.

**Advantage:** Roll 3d10 instead of 2d10. Drop the lowest die. Add the remaining two together, then add your modifier.

**Disadvantage:** Roll 3d10 instead of 2d10. Drop the highest die. Add the remaining two together, then add your modifier.

If you have both advantage and disadvantage at the same time, they cancel out. Roll 2d10 as normal.

{{note
**Example:** You attack while Stunned (disadvantage). You roll 3d10: 8, 3, 6. Drop the highest (8). Your roll is 3 + 6 = 9, plus your modifier.
}}

### The Two Roll Types

Solus has two kinds of rolls. Both use 2d10 plus a modifier. The difference is which modifier you add and what target number you compare against.

#### Combat Roll

Roll a Combat Roll when you attack with a weapon or cast an offensive spell.

1. Choose your attack. Physical and martial attacks (a sword swing, a punch, an arrow) add your **Body** modifier. Spells add your **Magic** modifier.
2. Roll `2d10 + Body` or `2d10 + Magic`.
3. Compare your result to the defender's **Armor Class** (AC). Physical attacks target **Physical AC**. Spells target **Magical AC**. (See Armor and Defense for how AC is calculated.)

{{footnote Core Mechanics}}
{{pageNumber,auto}}

\page

4. If your result meets or beats the AC, you hit. Roll damage. The defender's **Damage Reduction** (DR) subtracts from the damage dealt.
5. If your result falls short, you miss.

{{descriptive
**TODO:** Jacob, how should spells that create physical projectiles (hurling a boulder, creating an earth spike) interact with AC? Does the target use Physical AC because the impact is physical, or Magical AC because a spell created it? This needs a ruling.
}}

{{note
**Example:** You swing a greatsword at a bandit. Your Body is +4. You roll 2d10 and get 6 + 8 = 14, plus 4 = 18. The bandit wears Medium armor (Physical DR 3) and has Body +1, so their Physical AC is 4. You beat 4, so you hit. You roll 1d8 + 4 for damage and deal 10. The bandit's Physical DR of 3 absorbs 3 points. The bandit takes 7 damage.
}}

#### Proficiency Check

Roll a Proficiency Check when your character attempts something uncertain that is not a combat attack. Picking a lock, tracking footprints, persuading a guard, recalling a piece of lore, treating a wound: these are Proficiency Checks.

1. The GM names the relevant proficiency and sets a **Difficulty Class** (DC), a target number reflecting how hard the task is.
2. Roll `2d10 + your Proficiency Modifier`.
3. Compare your result to the DC.
4. The GM reads the outcome using the **Degree of 5** scale (see Running the Game). Beating the DC by 5 or more earns a bonus. Missing the DC by 5 or more adds a setback. The wider the gap, the bigger the swing.

Your **Proficiency Modifier** is the sum of two attributes: a fixed **primary** attribute and a **secondary** attribute you choose when you make the roll. Each proficiency lists two secondary options. You pick whichever fits the situation. See Attributes and Proficiencies for the full list.

{{note
**Example:** You try to calm a spooked horse. The GM calls for Animal Handling against DC 12. Animal Handling uses Social as its primary. The secondary options are Body and Mind. You choose Mind for this roll because you are reading the horse's body language, not wrestling it into submission. Your Social is +3 and your Mind is +4, so your modifier is +7. You roll 2d10 and get 4 + 5 = 9, plus 7 = 16. You beat DC 12 by 4 and the horse calms down. If you had rolled 3 + 2 = 5, plus 7 = 12, you would meet the DC exactly: a bare success with no bonus or setback.
}}

{{footnote Core Mechanics}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 3: CHARACTER CREATION -->

# Character Creation

Character creation follows seven steps. By the end, you will have a complete character sheet ready for play. You do not need to read the full rulebook first. Each step tells you what to write down and points you to the chapter that explains it.

### Step 1: Build Your Concept

Decide what kind of character you want to play. Ask yourself three questions: How does this character fight? How does this character solve problems outside of combat? What is this character bad at?

Solus does not restrict your choices by class or archetype. A character with high Body and high Magic can swing a greatsword and cast spells in the same turn. A character with high Social and low Body can talk their way past guards but will struggle in a fistfight. The attributes and proficiencies you choose in the next steps define your strengths and weaknesses mechanically.

### Step 2: Distribute Attribute Scores

You have five attributes: Body, Mind, Social, Magic, and Atraxia. Each gets a modifier between -5 and +5. The Attributes and Proficiencies chapter describes what each attribute does.

You have **5 points** to spend across all five attributes. Higher modifiers cost more points. Negative modifiers refund points. You must spend all 5 points, with zero remaining.

##### Attribute Point Costs
| Modifier | Point Cost |
|:---:|:---:|
| +5 | 6 |
| +4 | 4 |
| +3 | 3 |
| +2 | 2 |
| +1 | 1 |
| 0 | 0 |
| -1 | -1 |
| -2 | -2 |
| -3 | -3 |
| -4 | -4 |
| -5 | -5 |

{{note
**Example:** You want a melee fighter who can take a hit. You set Body +4 (costs 4), Mind +1 (costs 1), Social +0 (costs 0), Magic -2 (refunds 2), Atraxia +2 (costs 2). Total spent: 4 + 1 + 0 - 2 + 2 = **5**. All points used.
}}

Notice that +5 costs 6 points, more than the full budget. You can reach +5 in one attribute, but you will need deep negatives elsewhere to pay for it.

{{footnote Character Creation}}
{{pageNumber,auto}}

### Step 3: Choose Your Race

Your race sets your base movement speed, character size, and racial traits. Record your speed, size, and all traits on your sheet.

##### Race Summary
| Race | Speed | Size | Traits |
|:---|:---:|:---:|:---|
| Humans | 30 ft. | Medium | Adaptable, Determined |
| Elves | 35 ft. | Medium | Darkvision, Keen Senses, Trance |
| Dwarves | 25 ft. | Medium | Darkvision, Hardy, Stone Steady |
| Orcs | 30 ft. | Medium | Powerful Build, Aggressive |
| Gnomes | 25 ft. | Small | Darkvision, Small Frame, Arcane Cunning |
| Constructs | 30 ft. | Medium | Living Machine, No Rest Required |
| Half-Breeds | 30 ft. | Medium or Small | Dual Heritage |

#### Humans

**Adaptable.** You start with one extra active proficiency slot (11 instead of 10).

**Determined.** Once per encounter, reroll one failed Proficiency Check. Keep the new result.

#### Elves

**Darkvision.** See in darkness up to 60 ft.

**Keen Senses.** Advantage on Investigation checks that rely on sight or hearing.

**Trance.** 4 hours of rest counts as a full rest for you.

#### Dwarves

**Darkvision.** See in darkness up to 60 ft.

**Hardy.** Immune to the Venomous escalated condition. Advantage on saves against Poison effects.

**Stone Steady.** Heavy armor and stone or earth terrain do not reduce your speed.

#### Orcs

**Powerful Build.** Count as one size larger for grappling, shoving, and carrying capacity.

**Aggressive.** On your turn, move up to your speed toward a visible hostile creature as part of another action. You must end closer to the target.

{{footnote Character Creation}}
{{pageNumber,auto}}

\page

#### Gnomes

**Darkvision.** See in darkness up to 60 ft.

**Small Frame.** Move through spaces occupied by Medium or larger creatures. Advantage on Stealth checks when using cover.

**Arcane Cunning.** Advantage on Mind saves against spells and magical effects.

#### Constructs

**Living Machine.** Immune to Poison and Bleed tags. You cannot gain stacks or escalated conditions from either. Vulnerable to Acid: take +1 additional stack per Acid hit.

**No Rest Required.** You do not sleep or eat. You remain alert during rest periods and cannot be caught off-guard while resting.

#### Half-Breeds

Choose your size: Medium or Small.

**Dual Heritage.** Choose two other races. Gain one non-immunity trait from each. Record both source races on your sheet.

{{note
**Expanded Races:** Future supplements may add races such as Fey, Beastkin, and Drakari. GMs who want these races now can use Half-Breed as a template and assign two thematic traits.
}}

{{footnote Character Creation}}
{{pageNumber,auto}}

\page

### Step 4: Choose Your Background

Your background sets your starting hit points (HP), maximum mana pool, and mana regeneration rate. It does not restrict which skills, spells, weapons, or armor you can use. Any background can use any equipment.

The first number after mana is your **maximum mana**. The second is your **mana regeneration per round**.

##### Backgrounds
| Background | HP | Max Mana | Mana Regen / Round |
|:---|:---:|:---:|:---:|
| Caster | 100 | 100 | 15 |
| Martial | 120 | 30 | 3 |
| Hybrid | 110 | 70 | 10 |

A Caster has the deepest mana pool and fastest regeneration but the lowest health. A Martial has the most health and a smaller mana pool, enough to fuel martial skills and the occasional utility spell. A Hybrid splits the difference.

### Step 5: Initiative Modifier

At the start of each combat, choose whether to roll initiative with **Body** or **Magic**. Roll 1d10 + the chosen modifier to determine turn order (see Combat: Starting Combat). You can pick a different modifier each fight.

### Step 5.5: Roll Your Atraxia Pool

Your GM chose a Campaign Tone at session zero. That tone sets the number of dice and the die type. Roll that many dice, add your Atraxia modifier to each one (minimum 1 per die). The total is your **Atraxia Pool**. Write it on your sheet. This number tracks how many times you can cheat death across your career. (See Attributes and Proficiencies: The Atraxia Pool for the full table and examples.)

{{footnote Character Creation}}
{{pageNumber,auto}}

\page

### Step 6: Choose Your Tag Affinities

Pick two tag affinities from the ten listed in Magic and Spellcasting.

- Your **Main affinity (×1)** has no mana cost penalty.
- Your **Sub affinity (×2)** doubles the mana cost of any spell using it.

If your character does not cast spells, you still pick two affinities. They define what tag categories your character can draw on if circumstances change.

### Step 7: Choose Your Proficiencies

Pick proficiencies from the proficiency list in the Attributes and Proficiencies chapter. Each proficiency has a fixed primary attribute and two secondary attribute options. When you roll a proficiency check, you choose which secondary to use for that roll (see Attributes and Proficiencies: How Proficiency Modifiers Work).

You start with a limited set of proficiencies and can gain more through play.
Your character also has access to 10 **combat ability slots** for active abilities used in fights. These are independent of proficiencies. See the combat abilities chapter (coming soon) for the full system. Martial characters use mana-fueled combat abilities. Casters use the freeform spell builder. Both draw from the same mana pool.

{{footnote Character Creation}}
{{pageNumber,auto}}

### Step 8: Choose Starting Weapons

Pick one or two weapons from the tables in Weapons, Techniques, and Augments. You begin at **Mastery Rank 1** in your chosen weapon(s). This grants access to that weapon's tier 1 Techniques and its category's tier 1 Techniques.

Choose your starting Techniques. You can prepare up to **10 Techniques** from your available pools (Universal, Category, and Weapon-Specific). You can change prepared Techniques on a short or long rest.

### Step 9: Choose Equipment

Choose armor from the tables in Armor and Defense. Your background does not restrict your choices. A Caster can wear Heavy armor. A Martial can carry a staff.

You begin with **one set of armor** (any tier except Enchanted).

Your armor determines your Physical DR, Magic DR, Physical AC, and Magical AC (see Armor and Defense). Your weapon determines your damage dice, tags, and traits.

TODO: add starting equipment rules for gear and supplies.

### Step 9: Review Your Sheet

Check your sheet against this reference. If anything is blank, go back to the step that fills it in.

##### Character Sheet Reference
| Category | What to record | Can it change? |
|:---|:---|:---|
| Name | Character name | Fixed |
| Race | Race, size, speed, racial traits | Fixed |
| Background | Caster, Martial, or Hybrid | Fixed |
| Attributes | Body, Mind, Social, Magic, Atraxia | Fixed |
| Initiative | Body or Magic modifier | Chosen each combat |
| Tag Affinities | Main affinity, Sub affinity | Fixed |
| HP / Mana | Max HP, Max Mana, Mana Regen | Fixed (set by background) |
| Atraxia Pool | Rolled at creation (Campaign Tone dice + modifier) | Permanent; drains during dying |
| Proficiencies | Active proficiencies | Proficiencies can be swapped between sessions |
| Weapon Mastery | Mastery Rank per weapon (Rank 1-5) | Permanent (XP investment) |
| Techniques | 10 prepared Technique slots | Changeable on short/long rest |
| Equipment | Weapons, armor, gear | Changeable |



Solus has no character levels. Your character grows by earning XP and spending it on proficiency ranks, Weapon Mastery ranks, and Augments (see Advancement and Between-Session Play). The attributes, race, background, and name you chose in these steps are permanent. Everything else can change between sessions with GM confirmation.

See Reference and Playtest Tools for nine sample character builds covering all three backgrounds.

{{footnote Character Creation}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 4: ATTRIBUTES AND PROFICIENCIES -->
{{wide
# Attributes and Proficiencies

Your character has five **attributes**. Each attribute is a number from -5 to +5 that measures a broad area of capability. Attributes feed into combat rolls, Armor Class, initiative, and your proficiency modifiers. Every attribute matters; there are no dump stats.

## The Five Attributes

#### Body

Body covers all physical capability: strength, speed, endurance, coordination. 

- Body is added to physical and martial combat rolls and contributes to **Physical AC** (see Armor and Defense). Body is one of the two attributes you can choose for **initiative** at the start of combat.

- A character with high Body hits harder with weapons, resists physical attacks, and endures punishment. A character with low Body is fragile, inaccurate with weapons, and easy to hit with physical force.

#### Mind

Mind covers intellect, reasoning, perception, and emotional composure. A character with high Mind spots hidden details, recalls useful lore, resists tricks that target reasoning, and holds steady under fear and stress. A character with low Mind overlooks clues, forgets critical knowledge, falls for deceptions, and panics under pressure.

#### Social

Social covers how you present yourself. It governs persuasion, deception, intimidation, performance, leadership, and your ability to resist social manipulation. A character with high Social commands attention, reads a room, and turns conversations in their favor. A character with low Social struggles to lie, inspire, or talk their way past obstacles.

#### Magic

Magic covers all spellcasting. Every spell you cast uses Magic, regardless of its tag affinity (elemental, death, summoning, or otherwise). 

- Magic is added to magical combat rolls and contributes to **Magical AC**. Magic is the other attribute you can choose for **initiative**.

- A character with high Magiccasts powerful spells, resists magical attacks, and reacts quickly in combat. A character with low Magic casts weak spells and is easy to hit with magic.

#### Atraxia

Atraxia measures how deeply your character perceives the true nature of the world.

- Atraxia is the only attribute that can change during play. All other attributes stay fixed at creation.
- A character with low Atraxia sees things others cannot: hidden layers of reality, presences beyond normal perception, truths the world conceals. They can interact with these things, and those things can interact with them.
- A character with high Atraxia is grounded and stable but perceives only the surface.
- Once your Atraxia drops past a threshold, the awareness is permanent. Raising Atraxia back up restores your composure but does not erase what you have seen.

Characters choose low Atraxia to access hidden knowledge and interact with forces invisible to others. Those forces can reach back.

#### The Atraxia Pool

Your **Atraxia Modifier** (-5 to +5) governs proficiency checks, the same as any other attribute. Your **Atraxia Pool** is a separate resource that represents how much punishment your body and mind can absorb before they give out for good. When your Pool hits 0, you are dead. 

You generate your Atraxia Pool at character creation. You and the GM collaborate to choose a **Campaign Tone** that sets the number of dice and the die type. You roll that many dice, adding your Atraxia modifier to each roll (minimum 1 per die, even if your modifier would drag it lower). The total is your starting Atraxia Pool.

##### Atraxia Pool by Campaign Tone
| Campaign Tone | Dice | Die Type | Description |
|:---|:---:|:---:|:---|
| Brutal | 4 | d4 | Short runs. Death is the expected outcome. |
| Gritty | 6 | d6 | Survival matters. Every hit leaves a mark. |
| Standard | 8 | d6 | A full campaign with real stakes and room to breathe. |
| Heroic | 10 | d8 | Long arcs. Characters die from accumulated recklessness, not one bad night. |

{{note
**Example:** The GM declares a Standard campaign (8d6). Your Atraxia modifier is +2. You roll 8d6: 3, 5, 1, 4, 6, 2, 5, 3. Add +2 to each: 5, 7, 3, 6, 8, 4, 7, 5. Your starting Atraxia Pool is **45**.

Another player has Atraxia -2. They roll the same 8d6: 4, 1, 3, 6, 2, 5, 1, 4. Add -2 to each (minimum 1): 2, 1, 1, 4, 1, 3, 1, 2. Their starting Atraxia Pool is **15**.

Both players rolled the same number of dice. The modifier shaped the outcome. The character who sees beyond the veil paid for it in resilience.
}}

Your Atraxia Pool does not regenerate between encounters nor sessions. Entering the "Dying" condition reduces the maximum value of your Atraxia pool. Atraxia can be gained and lost by other means at the GM's discretion, and it is encouraged to play off the mechanic and consult various tables as to what characters may see or experience (TODO). 

{{descriptive
**TODO:** Jacob — define Atraxia Pool restoration mechanics. Can Life magic (Restoration) restore Pool points? Can rest? NPC services? Quest rewards? Or is this a one-way drain? The answer reshapes how the pool feels across a campaign.
}}

{{descriptive
**TODO:** Jacob — define Atraxia modifier thresholds and perception consequences. At what modifier values does the world change around the character? (e.g., at -2 you start seeing echoes of things that aren't there; at -4 those things see you back.) This is where the Bloodborne Insight influence lives. Needs a threshold table and descriptions of what each tier of awareness looks and feels like in play.
}}
}}
{{footnote Attributes and Proficiencies}}
{{pageNumber,auto}}

\page

## Proficiencies

A **proficiency** is a trained ability your character uses in and out of combat. Skills include climbing a wall, picking a lock, landing a precise combo, channeling energy through a weapon, persuading a merchant, or tracking an animal through snow. Martial characters fuel their combat skills with a steady mana drain at low cost. Casters spend mana in larger amounts per spell. Both draw from the same shared mana pool.

When you attempt a non-combat action and the outcome is uncertain, the GM calls for a **Proficiency Check** (see Core Mechanics) using the relevant proficiency from the table below. The 11 proficiencies in the table cover non-combat Proficiency Checks and their attribute pairings.

Your character does not start with every proficiency.You choose which proficiencies to take during character creation, and you can gain or swap proficiencies between sessions.

Proficiencies grow through play. As you earn XP and spend it, your proficiencies advance through ranks (Rank 1 to Rank 10), becoming more effective.

\column

### How Proficiency Modifiers Work

When you make a Proficiency Check, you roll `2d10` and add your **Proficiency Modifier**. That modifier comes from two of your attributes added together.

Every proficiency has a **primary** attribute and a **secondary** attribute.

The **primary** is fixed. It never changes for that proficiency. Athletics always uses Body. Arcana always uses Magic. The primary represents the core capability the proficiency draws on.

The **secondary** is your choice each time you roll. Every proficiency lists two options. When you make a check, you pick whichever secondary fits the situation. The secondary represents how your character approaches that proficiency in the moment: do you climb this wall through trained technique (Mind) or through sheer refusal to let go (Atraxia)?

**Proficiency Modifier** = primary attribute + secondary attribute.

{{note
**Example:** Your character has Body +4, Mind +1, and Atraxia -2. Athletics uses Body as its primary. The secondary options are Mind or Atraxia.

- With Mind: Athletics = +4 + 1 = **+5**.
- With Atraxia: Athletics = +4 + (-2) = **+2**. 

You choose which secondary to use each time you roll, based on how your character approaches the task.
}}

This system means every attribute contributes to multiple proficiencies. A character who invests heavily in one attribute will be strong in some proficiencies and dangerously weak in others. Two characters with the same proficiency can have different modifiers because they chose different secondaries.


{{wide 

## Proficiency List

The table below shows all 11 proficiencies. When you make a Proficiency Check, find the proficiency, add the primary and your chosen secondary together, and that is the modifier you roll with.



##### Proficiencies
| Proficiency | Primary | Secondary (pick one) | What it covers |
|:---|:---:|:---:|:---|
| Athletics | Body | Mind or Atraxia | Climbing, jumping, sprinting, swimming, feats of strength or endurance |
| Stealth | Body | Mind or Atraxia | Moving unseen, hiding, acting without drawing attention |
| Investigation | Mind | Body or Atraxia | Searching for clues, analyzing evidence, piecing together hidden details |
| Knowledge | Mind | Social or Atraxia | Recalling lore, history, culture, religion, or technical information |
| Medicine | Mind | Body or Atraxia | Diagnosing conditions, treating wounds, stabilizing the dying |
| Survival | Mind | Body or Atraxia | Tracking, hunting, navigating, enduring harsh environments |
| Animal Handling | Social | Body or Mind | Calming, training, controlling, or reading the behavior of animals |
| Performance | Social | Body or Atraxia | Entertaining, inspiring, distracting through art, music, or drama |
| Speech | Social | Body or Mind | Persuading, deceiving, negotiating, intimidating, commanding |
| Arcana | Magic | Mind or Atraxia | Identifying, understanding, or manipulating magical and supernatural forces |
| Insight | Atraxia | Body or Mind | Perceiving hidden truths, occult knowledge, cosmic or otherworldly comprehension |

}}

{{footnote Attributes and Proficiencies}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 5: EQUIPMENT, ARMOR, AND WEAPONS -->

# Armor and Defense

## Armor

Armor in Solus does two things: it makes you harder to hit, and it absorbs damage when you do get hit. These are two separate systems, and understanding the difference is critical.

##### Armor Class (AC)

Every character has two **Armor Class** values:

- **Physical AC** = your armor's Physical DR + your Body modifier
- **Magical AC** = your armor's Magic DR + your Magic modifier

When someone attacks you, they roll `2d10 + their attack modifier` and compare the result to your AC. If they meet or beat your AC, the attack hits. If they fall short, it misses.

Physical attacks (swords, arrows, fists) target your Physical AC. Spells target your Magical AC. Because you have two separate ACs, a character can be tough against swords but vulnerable to spells, or the reverse. Your armor choice and attribute spread determine where your defenses are strong and where they are weak.

##### Damage Reduction (DR)

When an attack lands, your armor's **Damage Reduction** absorbs part of the blow. DR is a flat number subtracted from the damage dealt.

- **Physical DR** reduces damage from weapons, unarmed strikes, falls, and other physical sources.
- **Magic DR** reduces damage from spells and elemental status effects. Magic DR does not stop status effects from applying or escalating; it only reduces the damage those effects deal.

DR is fixed per armor tier. Your attributes do not change it.

### Armor Tiers
| Tier | Physical DR | Magic DR | Total DR |
|:---|:---:|:---:|:---:|
| Cloth | 0 | 4 | 4 |
| Light | 1 | 3 | 4 |
| Medium | 3 | 1 | 4 |
| Heavy | 4 | 0 | 4 |
| Enchanted | 3 | 3 | 6 |

Every standard tier provides 4 total DR, split between physical and magical protection. The split forces a tradeoff: Cloth gives maximum magical protection and zero physical. Heavy gives maximum physical and zero magical. Enchanted armor is the exception, providing 6 total DR with an even split.

The maximum DR on a single damage type is 4. The maximum possible AC is 9 (DR 4 + attribute modifier +5).

{{footnote Armor and Defense}}
{{pageNumber,auto}}

### Taking Hits

When an attack targets you, resolve it in two steps:

1. **Compare the attack roll to your AC.** If the attacker's result meets or beats your Physical AC (for weapons) or Magical AC (for spells), the attack lands. Otherwise it misses, and no damage is dealt.
2. **Subtract your DR from the damage.** The attacker rolls damage. Your relevant DR (Physical or Magic) subtracts from the total. You take the remainder.

{{note
**Example:** A mage casts a fire bolt at you. You wear Light Armor (Magic DR 3) and have Magic +2, so your Magical AC is 5. The mage rolls `2d10 + 4` and gets 16. That beats your Magical AC of 5, so the spell hits. The mage rolls 8 damage. Your Magic DR of 3 reduces it to 5. You take 5 damage.
}}

{{note
**Example:** You wear Heavy Armor (Physical DR 4, Magic DR 0) with Body +3 and Magic +0. Your Physical AC is 7. Your Magical AC is 0. A sword fighter rolls 11 against your Physical AC of 7, hits, and deals 9 damage. Your Physical DR of 4 absorbs 4, leaving 5 damage. A caster rolls the same 11 against your Magical AC of 0, also hits, and deals 9 damage. With Magic DR 0, nothing absorbs. You take the full 9. Heavy armor makes you a fortress against blades and a glass window against magic.
}}

{{footnote Armor and Defense}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 6: WEAPONS, TECHNIQUES, AND AUGMENTS -->

# Weapons, Techniques, and Augments

Every character fights with weapons. Weapons deal damage, apply condition stacks, and unlock Techniques. Your choice of weapon defines your combat role as much as your attributes do.

This chapter covers three systems:

- **Weapons** grant base damage, properties, and condition signatures.
- **Techniques** are active combat abilities. They cost Actions and sometimes Mana. You prepare up to 10 at a time, changeable on a short or long rest. Each Technique requires its associated weapon equipped.
- **Augments** modify Techniques. You socket Augments into Augment Slots unlocked by Weapon Mastery.

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Weapon Mastery

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

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Technique Layers

Techniques come from three sources. Each layer has different unlock requirements and scope.

| Layer | Source | Scope |
|---|---|---|
| Universal | Available to all characters | Any equipped weapon |
| Category | Unlocked by Mastery Rank 1+ in any weapon in that category | Any weapon in that category |
| Weapon-Specific | Unlocked by that weapon's Mastery Rank | Only that specific weapon |

You prepare up to 10 Techniques at a time from any combination of layers. You can swap your prepared list on a short or long rest.

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Augment Layers

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

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Universal Techniques

Every character has access to these four Techniques regardless of weapon or Mastery Rank.

**Brace.** Plant your feet. Until your next turn, gain +2 AC. You cannot move. Free Action to enter; costs your movement for the turn.

**Shove.** Push an adjacent creature 1 space. Roll `2d10 + Body` vs. target's `2d10 + Body`. Costs 1 Action.

**Taunt.** Force a target within 6 spaces to roll `2d10 + Social` vs. your `2d10 + Social`. On failure, the target must attack you on their next turn if able. Costs 1 Action.

**Second Wind.** Recover `1d10 + Body modifier` HP. Costs 1 Action. Once per combat. Cannot use while Dying.

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Universal Augments

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

### Spellblade Augments

These four Augments connect weapon combat and spellcasting. Any character with Mana can use them.

| Augment | Effect | Mana Cost Increase |
|---|---|---|
| Spell Strike | Deliver one Touch spell alongside a weapon attack. One roll, two payloads. Miss = spell not expended. | +0 (spell Mana paid separately) |
| Arcane Infusion | After casting a spell this turn, your next Technique deals +1d8 elemental damage (matching the spell's element). | +2 |
| Channeling | While concentrating on a spell, the Technique costs 2 less Mana (minimum 0). | +0 |
| Mana Reave | On hit, restore Mana equal to your weapon's base damage die (e.g., 1d8 weapon = roll 1d8 Mana restored). Once per round. | +3 |

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Weapon Properties Reference

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

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Weapon Categories

Weapons are grouped into seven categories. Each category shares a fighting style and a set of Category Techniques. Category Techniques have their own Technique Augments, shared across all weapons in that category.

---

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Light Melee

Fast, low-damage, high-frequency attacks. Light Melee favors evasion, combos, and condition application. These weapons strike often and stack conditions faster than any other category.

### Light Melee Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Quick Draw | Free Action | Switch to this weapon as a free action. If you attack in the same turn, +1 to hit. |
| 1 | Flurry | 1 Action | Two attacks as a single Action. Each deals half weapon damage. |
| 2 | Slip Away | Free (on hit) | After hitting, move 1 space without provoking reactions. |
| 2 | Exploit Opening | Reaction | When an adjacent enemy misses an attack, make a free attack against them. |
| 3 | Assassinate | 2 Actions | Attack an unaware target. On hit, double damage. |

### Light Melee Category Technique Augments

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

### Light Melee Weapons

| # | Weapon | Complexity | Base Damage | Properties |
|---|---|---|---|---|
| 1 | Bare Hands | Simple | 1d6 | Unarmed, Grapple |
| 2 | Dagger | Standard | 1d6 | Finesse, Thrown (20 ft), Light |
| 3 | Short Sword | Standard | 1d8 | Finesse, Light |
| 4 | Claw Gauntlet | Standard | 1d6 | Finesse, Light, Paired |
| 5 | Sickle | Standard | 1d6 | Finesse, Light, Hooked |
| 6 | Shield | Standard | 1d6 | Defensive (+2 AC), Bash |

Shield occupies the off-hand. It functions as both a defensive item (+2 AC while equipped) and a weapon with its own Mastery track. Shield Techniques include bashes, blocks, pushes, and formation abilities.

### Light Melee Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Bare Hands | Force | — | Burn Force stacks on yourself for bonus unarmed damage. Grapple Techniques pin targets while Force stacks tick. |
| Dagger | Bleed | Poison | Paired with Flurry, applies stacks faster than any other weapon. Rank 3+: apply Bleed AND Poison on a single hit. |
| Short Sword | Bleed | — | Every hit applies 1 Bleed. No variance. Rank 3: guaranteed 2 Bleed stacks per hit. |
| Claw Gauntlet | Bleed | — | Dual-wield mandatory (Paired). Each Flurry hits twice. Fastest path to Shredded (5 Bleed) in the game. |
| Sickle | Bleed | — | On kill, transfer remaining Bleed stacks to one adjacent enemy. |
| Shield | Force | — | Shield Bash applies 1 Force stack. Repeated bashes build toward Staggered while maintaining high AC. |

### Bare Hands (Simple, Light Melee) — 5 Techniques

**Unique Mechanic: Iron Fist.** Bare Hands Techniques apply Force stacks to you, not the target. Spend stacks on your next hit for bonus damage. If you reach 5 Force stacks, you gain Staggered (T2 Force) on yourself. Manage your stacks or pay the price.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Steel Fist | 1 Action | 1d6 Bludgeon. Gain 1 Force stack on yourself. |
| 1 | Grab and Slam | 1 Action | 1d6 Bludgeon. On hit, attempt a free Shove, Grapple, or Push (contested `2d10 + Body` check). Once per turn. |
| 2 | One-Two Combo | 1 Action, 3 Mana | Strike twice. 1d6 Bludgeon each hit. Gain 1 Force stack per hit. Cannot trigger Grab and Slam on the second strike. |
| 2 | Burning Knuckles | 1 Action | Consume all Force stacks on yourself. 1d6 Bludgeon + 1d6 per stack consumed. 3+ stacks: target rolls `2d10 + Body` vs. DC 14 or is Disarmed. 4+ stacks: target rolls `2d10 + Body` vs. DC 16 or is Stunned. Stacks consumed whether you hit or miss. |
| 3 | Iron Hold | 1 Action, 5 Mana | Requires a Grappled target. Pin the target. While pinned, your Force stacks tick damage to the pinned target (1 damage per stack per round). Target breaks free with `2d10 + Body` vs. your `2d10 + Body`. |

#### Bare Hands Weapon Augments (Iron Fist)

Passive. Once learned, these apply to ALL Bare Hands Techniques. Each adds its Mana cost to every Bare Hands Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Thick Skin | While you have 3+ Force stacks on yourself, gain +1 AC. | +0 |
| 2 | Momentum | When you consume Force stacks with Burning Knuckles, gain temporary HP equal to stacks consumed × 2. | +1 |
| 3 | Haymaker | When you consume 4+ Force stacks, add 1d6 Bludgeon on top of the per-stack bonus. | +2 |

### Dagger (Standard, Light Melee) — 8 Techniques

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

#### Dagger Weapon Augments (Toxic Edge)

Passive. Once learned, these apply to ALL Dagger Techniques. Each adds its Mana cost to every Dagger Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Envenomed Blade | Poison stacks from Dagger Techniques deal +1 per tick (+2 total per stack per round instead of +1). | +2 |
| 2 | Twin Fangs | When dual-wielding daggers, each Dagger Technique strikes with both blades. Second strike deals half damage. | +3 |
| 3 | Coat Blade | Before a Dagger Technique, spend 1 additional Action to coat your blade. Next hit applies 2 extra Poison stacks. | +0 (costs Action) |
| 4 | Arterial Cut | Bleed applied by Dagger Techniques cannot be removed by mundane healing. Only magical healing removes Dagger Bleed. | +1 |
| 5 | Shadowstep | After a Dagger Technique reduces a target to 0 HP, teleport up to 3 spaces to another enemy. | +2 |

### Short Sword (Standard, Light Melee) — 8 Techniques

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

#### Short Sword Weapon Augments (Steady Blade)

Passive. Once learned, these apply to ALL Short Sword Techniques. Each adds its Mana cost to every Short Sword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Keen Edge | Short Sword Techniques score a critical hit on double 9s in addition to double 10s. | +1 |
| 2 | Pressure Fighter | While the target has 3+ Bleed stacks, your Short Sword Techniques deal +1d4 Slashing. | +2 |
| 3 | Clean Cuts | Bleed stacks from Short Sword Techniques last 1 extra round before expiring. | +1 |
| 4 | Swordsman's Focus | After landing 3 consecutive Short Sword hits on the same target, your next Short Sword Technique against that target has advantage. | +0 |
| 5 | Bloodletter | When Hemorrhage (T3) is active on the target, your Short Sword Techniques apply +1 additional Bleed stack. | +2 |

### Claw Gauntlet (Standard, Light Melee) — 8 Techniques

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

#### Claw Gauntlet Weapon Augments (Twin Rend)

Passive. Once learned, these apply to ALL Claw Gauntlet Techniques. Each adds its Mana cost to every Claw Gauntlet Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Serrated Edges | Bleed stacks from Claw Gauntlet Techniques deal +1 per tick. | +2 |
| 2 | Feral Reflexes | After using a Claw Gauntlet Technique, gain +1 AC until start of your next turn. | +1 |
| 3 | Lacerating Grip | When you Grapple a target, apply 2 Bleed stacks. Each round the Grapple persists, apply 1 additional Bleed stack. | +1 |
| 4 | Blood Scent | You have advantage on attacks against targets with Shredded (5 Bleed stacks). | +2 |
| 5 | Relentless Mauling | When Hemorrhage (T3) is active on the target, your Claw Gauntlet Techniques deal +1d6 Slashing. | +3 |

### Sickle (Standard, Light Melee) — 8 Techniques

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

#### Sickle Weapon Augments (Reaping)

Passive. Once learned, these apply to ALL Sickle Techniques. Each adds its Mana cost to every Sickle Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Harvest Moon | Reaping transfer range increases from 1 space to 2 spaces. | +0 |
| 2 | Sowing Pain | Sickle Techniques that apply Bleed to an already-bleeding target deal +1d4 Slashing. | +1 |
| 3 | Chain Reaping | When Reaping transfers stacks, split them between up to 2 adjacent enemies instead of 1. | +2 |
| 4 | Cruel Hook | Sickle Techniques that Pull ignore forced movement immunity. | +1 |
| 5 | Death's Harvest | When Reaping triggers, regain 3 Mana per Bleed stack transferred. | +2 |

### Shield (Standard, Light Melee) — 8 Techniques

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

#### Shield Weapon Augments (Guard)

Passive. Once learned, these apply to ALL Shield Techniques. Each adds its Mana cost to every Shield Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Shield Master | Your Shield's +2 AC bonus also applies to all allies within 1 space. | +0 |
| 2 | Battering Ram | Shield Techniques that push deal +1d4 Bludgeon per space pushed. | +1 |
| 3 | Reflective Guard | When you negate a ranged attack with a Shield Technique, reflect it back at the attacker at -4 to hit. | +2 |
| 4 | Tower Shield | Raise Shield and Fortress provide full cover from one direction. Blocks line of sight for ranged attacks through your space. | +1 |
| 5 | Shield Throw | Shield Techniques can be performed at 20 ft range (Thrown). Shield bounces back at end of your turn. | +3 |

---

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Medium Melee

Balanced offense and defense. One-handed weapons that pair with shields or off-hand weapons. Medium Melee favors positioning, counterplay, and adaptability.

### Medium Melee Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Parry | Reaction | Add your weapon damage die to AC against one melee attack. |
| 1 | Riposte Stance | Free Action | Enter stance. While in Riposte Stance, a successful Parry triggers a free counterattack. |
| 2 | Press the Advantage | Free (on hit) | After hitting, your next attack this turn has advantage. |
| 2 | Disarming Strike | 1 Action | On hit, target rolls `2d10 + Body` vs. your attack roll or drops their weapon. |
| 3 | Measured Assault | 3 Actions | Commit all 3 Actions to one attack. Add your weapon die twice to damage. If the target dies, refund 1 Action. |

### Medium Melee Category Technique Augments

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

### Medium Melee Weapons

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

### Medium Melee Condition Signatures

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

### Longsword (Standard, Medium Melee) — 8 Techniques

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

#### Longsword Weapon Augments (Versatile Grip)

Passive. Once learned, these apply to ALL Longsword Techniques. Each adds its Mana cost to every Longsword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Fluid Transition | Grip Shift costs 0 Mana. Switching grips is always free. | +0 |
| 2 | Dual Conditioning | One-handed Techniques also apply 1 Force stack. Two-handed Techniques also apply 1 Bleed stack. | +2 |
| 3 | Balanced Weight | +1 AC in one-handed grip. +1 damage die size in two-handed grip (1d12 becomes 2d6). | +1 |
| 4 | Punishing Swap | After switching grips, your next Technique this turn deals +1d6 damage. Stacks with Grip Shift bonus. | +1 |
| 5 | Sustained Escalation | Hemorrhage and Concussion (T3) effects persist 1 additional round. | +2 |

### Rapier (Complex, Medium Melee) — 12 Techniques

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

#### Rapier Weapon Augments (Openings)

Passive. Once learned, these apply to ALL Rapier Techniques. Each adds its Mana cost to every Rapier Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Riposte Mastery | Gain 2 Openings instead of 1 from Parries and enemy misses. Maximum Openings increases to 5. | +0 |
| 2 | Flourish | Spend 1 Opening as a Free Action to impose disadvantage on the next attack against you this round. | +1 |
| 3 | Duelist's Grace | While you hold 2+ Openings, +1 AC. At 4+ Openings (requires Riposte Mastery), +2 AC. | +0 |
| 4 | Tempo Control | When you spend Openings on a Technique, the target has -1 to hit per Opening spent until their next turn. | +1 |
| 5 | Fencing Master | Openings generated by Passata Sotto and Derobement are doubled. | +2 |

#### Rapier Technique Augments

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

### Curved Sword (Standard, Medium Melee) — 8 Techniques

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

#### Curved Sword Weapon Augments (Sweeping Edge)

Passive. Once learned, these apply to ALL Curved Sword Techniques. Each adds its Mana cost to every Curved Sword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Wide Arc | Sweeping Edge range increases from 1 space to 2 spaces. | +1 |
| 2 | Bleeding Momentum | While 3+ enemies have Bleed stacks, Curved Sword Techniques deal +1d4 damage. | +1 |
| 3 | Crimson Spray | When Sweeping Edge applies Bleed, that enemy also takes 1d4 Slashing damage. | +2 |
| 4 | Dual Dance | While dual-wielding, Deadly Dance and Whirlwind gain +1 additional strike. | +2 |
| 5 | Cascade | When any enemy reaches Shredded (5 Bleed), all enemies within 2 spaces take 1 Bleed stack. | +1 |

### Katana (Complex, Medium Melee) — 12 Techniques

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

#### Katana Weapon Augments (Momentum Blade)

Passive. Once learned, these apply to ALL Katana Techniques. Each adds its Mana cost to every Katana Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Flow State | Momentum Blade escalation persists if you switch targets mid-turn. First hit on a new target counts as "consecutive" if you hit the previous target this turn. | +0 |
| 2 | Battojutsu Mastery | Iaijutsu and Battojutsu Techniques deal +1d6 damage. Sheathing at end of turn is automatic. | +1 |
| 3 | Crimson Arc | When a Katana Technique applies Bleed, one other enemy within 2 spaces takes 1 Bleed stack. | +1 |
| 4 | Zanshin (Lingering Intent) | After using 3+ Katana Techniques in one turn, the last target hit takes 1 additional Bleed stack at start of their turn. | +0 |
| 5 | Mugen (Infinite Blade) | At 5 Bleed stacks (Shredded), your Momentum Blade count does not reset at end of turn. It continues into the next turn. | +2 |

#### Katana Technique Augments

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

### Mace (Standard, Medium Melee) — 8 Techniques

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

#### Mace Weapon Augments (Concussive Impact)

Passive. Once learned, these apply to ALL Mace Techniques. Each adds its Mana cost to every Mace Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Rattling Impact | Force stacks from Mace Techniques also impose -1 per stack to Body-based Proficiency Checks (Athletics, Survival). | +1 |
| 2 | Armor Dent | Mace Techniques deal +2 damage against targets in Heavy or Medium armor. | +0 |
| 3 | Lingering Concussion | Force stacks from Mace Techniques last 1 additional round. | +1 |
| 4 | Shattering Force | When a target reaches Staggered (5 Force), their Physical DR drops by 1 until end of combat. | +2 |
| 5 | Brain Rattler | Concussion (T3) prevents the target from casting spells for its duration. | +2 |

### Flail (Standard, Medium Melee) — 8 Techniques

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

#### Flail Weapon Augments (Unstoppable Chain)

Passive. Once learned, these apply to ALL Flail Techniques. Each adds its Mana cost to every Flail Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Extended Chain | Flail Techniques gain +1 space reach. | +1 |
| 2 | Weighted Head | Flail Techniques deal +1d4 Bludgeoning against targets with Shield or Heavy armor. | +1 |
| 3 | Entangling Chain | Wrap and Pull range increases to 2 spaces. On success, target is also Restrained until end of their next turn. | +2 |
| 4 | Armor Breaker | Force stacks from Flail Techniques reduce target's Physical DR by 1 per stack (max -5). Resets at end of combat. | +2 |
| 5 | Relentless Assault | Defensive reactions (Parry, Block, Shield Wall) against Flail Techniques auto-fail. | +2 |

### War Pick (Standard, Medium Melee) — 8 Techniques

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

#### War Pick Weapon Augments (Deep Pierce)

Passive. Once learned, these apply to ALL War Pick Techniques. Each adds its Mana cost to every War Pick Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Barbed Point | Bleed stacks from War Pick Techniques cannot be removed by mundane healing. Requires magical healing. | +1 |
| 2 | Piercing Focus | War Pick Techniques ignore an additional 1 Physical DR (total 3). | +1 |
| 3 | Serrated Edge | Bleed ticks reduce target's Physical DR by 1 per tick (minimum 0). Resets at end of combat. | +2 |
| 4 | Puncture Wound | Bleed stacks from War Pick Techniques last 1 additional round. | +1 |
| 5 | Exposed Vitals | While target has Shredded (5 Bleed), all attacks from any source ignore 2 Physical DR. | +2 |

### Bastard Sword (Complex, Medium Melee / Heavy Melee) — 12 Techniques

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

#### Bastard Sword Weapon Augments (Adaptive Stance)

Passive. Once learned, these apply to ALL Bastard Sword Techniques. Each adds its Mana cost to every Bastard Sword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Fluid Grip | Stance Shift applies 1 Bleed or 1 Force stack (your choice) to one enemy in reach. | +0 |
| 2 | Cross-Conditioning | One-handed Techniques also apply 1 Force stack. Two-handed Techniques also apply 1 Bleed stack. | +2 |
| 3 | Dual Category Mastery | Category Techniques from both Medium Melee and Heavy Melee cost 1 less Mana (minimum 0). | +0 |
| 4 | Adaptive Parry | Cross Guard Block reduces 1d10 instead of 1d8. +1d4 per grip switch this turn. | +1 |
| 5 | Convergence | When target has both Bleed and Force stacks, Bastard Sword Techniques deal +1 damage per combined stack. | +2 |

---

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Heavy Melee

Two-handed, high damage, slow. Heavy Melee favors commitment, area attacks, and overwhelming force. These weapons hit hard but cost more Actions per attack.

### Heavy Melee Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Cleave | Free (on kill) | On kill, make a free attack against an adjacent enemy. |
| 1 | Power Attack | 1 Action | +1 damage die. -2 to hit. |
| 2 | Staggering Blow | 1 Action | On hit, target loses Reaction and has -2 AC until their next turn. |
| 2 | Whirlwind | 2 Actions | Attack all adjacent enemies. One roll vs. each AC. |
| 3 | Executioner | 2 Actions | If target is below 25% HP, auto-crit on hit. |

### Heavy Melee Category Technique Augments

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

### Heavy Melee Weapons

| # | Weapon | Complexity | Base Damage | Properties |
|---|---|---|---|---|
| 15 | Greatsword | Complex | 2d6 | Two-Handed, Heavy |
| 16 | Greathammer | Standard | 2d8 | Two-Handed, Heavy, Bludgeon |
| 17 | Great Axe | Standard | 1d12 | Two-Handed, Heavy |
| 18 | Greatclub | Simple | 2d6 | Two-Handed, Heavy, Bludgeon |

### Heavy Melee Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Greatsword | Force | Bleed | Normal grip = Force. Half-Sword grip = Bleed (1d8, Finesse). |
| Greathammer | Force | — | 2 Force stacks per hit. Fastest single-weapon path to Staggered. At Staggered, Force attacks deal triple bonus damage. |
| Great Axe | Bleed | — | Bleed stacks deal +1 per stack (2 per stack instead of 1). At Shredded, attacks ignore ALL Physical DR. |
| Greatclub | Force | — | 1 Force per hit. Knockback into walls or terrain grants bonus Force stacks. |

### Greatsword (Complex, Heavy Melee) — 12 Techniques

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

#### Greatsword Weapon Augments (Half-Sword)

Passive. Once learned, these apply to ALL Greatsword Techniques. Each adds its Mana cost to every Greatsword Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Grip Flow | Switching between normal and Half-Sword grip is a Free Action (instead of costing an Action). | +0 |
| 2 | Mortal Draw | The first Greatsword Technique after switching grip deals +1d8 bonus damage. | +1 |
| 3 | Zweihänder Reach | Normal-grip Greatsword Techniques gain +1 space reach. | +2 |
| 4 | Half-Sword Precision | [Half-Sword] Techniques gain an additional +2 to hit. | +1 |
| 5 | Swordsmanship | After a [Half-Sword] Technique, your next normal-grip Technique this turn has advantage. After a normal-grip Technique, your next [Half-Sword] Technique deals +1d6 damage. | +2 |

### Greathammer (Standard, Heavy Melee) — 9 Techniques

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

#### Greathammer Weapon Augments (Crushing Force)

Passive. Once learned, these apply to ALL Greathammer Techniques. Each adds its Mana cost to every Greathammer Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Aftershock | Greathammer Techniques that push the target also deal 1d6 Bludgeon to enemies adjacent to the push destination. | +2 |
| 2 | Concussive Waves | When you apply Force stacks with a Greathammer Technique, enemies adjacent to your target each take 1 Force stack. | +3 |
| 3 | Impact Crater | Greathammer Techniques that cause prone create difficult terrain in a 1-space radius for 2 rounds. | +1 |
| 4 | Momentum of Ruin | When you hit a Staggered target with a Greathammer Technique, refund 1 Action. Once per turn. | +0 |
| 5 | Tectonic | Greathammer Techniques against objects, structures, and terrain deal triple damage. Terrain destruction radius +1 space. | +1 |

### Great Axe (Standard, Heavy Melee) — 8 Techniques

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

#### Great Axe Weapon Augments (Savage Rend)

Passive. Once learned, these apply to ALL Great Axe Techniques. Each adds its Mana cost to every Great Axe Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Blood Scent | After applying Bleed with a Great Axe Technique, your next attack against the same target this turn has advantage. | +0 |
| 2 | Arterial Strike | Great Axe Techniques that apply Bleed stacks apply 1 additional stack. | +2 |
| 3 | Sanguine Fury | While your target has 3+ Bleed stacks, Great Axe Techniques deal +1d6 bonus damage. | +1 |
| 4 | Crimson Harvest | When a target takes Bleed tick damage from your stacks, heal HP equal to half the tick damage dealt. | +2 |
| 5 | Relentless Edge | Bleed stacks applied by Great Axe Techniques last 3 rounds instead of 2. | +1 |

### Greatclub (Simple, Heavy Melee) — 5 Techniques

**Unique Mechanic: Wallbreaker.** When a Greatclub Technique knocks a target into a wall, obstacle, or terrain feature, apply 2 bonus Force stacks.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Overhead Smash | 1 Action | On hit, push target 1 space in any direction. |
| 1 | Battering Swing | 1 Action | On hit, apply 1 Force stack. |
| 2 | Home Run | 1 Action, 3 Mana | On hit, push target 3 spaces. Collision with a wall or creature deals 1d8 bonus damage. |
| 2 | Ground Pound | 2 Actions, 3 Mana | Strike the ground. All enemies within 1 space take 1d6 damage and are pushed 1 space away. |
| 3 | Demolition | 2 Actions, 5 Mana | On hit, weapon damage + 1d10. Push target 2 spaces. Wall collision applies Staggered (5 Force stacks). Destroys non-magical terrain in the path. |

#### Greatclub Weapon Augments (Wallbreaker)

Passive. Once learned, these apply to ALL Greatclub Techniques. Each adds its Mana cost to every Greatclub Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Rubble Field | When you destroy terrain with a Greatclub Technique, the area becomes difficult terrain for 2 rounds. | +0 |
| 2 | Follow Through | After pushing a target with a Greatclub Technique, move 1 space toward the target as a Free Action. | +0 |
| 3 | Collateral Damage | When a Greatclub push sends a target into another creature, that creature takes 1d6 damage and gains 1 Force stack. | +1 |

---

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Reach

Extended range (2+ spaces) and zone control. Reach weapons punish movement, lock down areas, and protect allies. They favor kiting, formation fighting, and battlefield control.

### Reach Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Sentinel | Reaction | Enemies entering your reach provoke a free attack. |
| 1 | Sweep | 1 Action | Attack up to two adjacent targets within your reach. One roll vs. both ACs. |
| 2 | Keep at Bay | Free (on hit) | On hit, push target 1 space away from you. |
| 2 | Impale | 1 Action | On hit, target is Restrained until they spend an Action to pull free or you release. You cannot attack other targets while impaling. |
| 3 | Phalanx | Passive | While adjacent to an ally who also wields a Reach weapon, both of you gain +2 AC. |

### Reach Category Technique Augments

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

### Reach Weapons

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

### Reach Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Spear | Bleed | — | Bleed ignores 1 Physical DR. Brace: charging targets take 3 Bleed stacks. |
| Halberd | Force | Bleed | Sweep applies Force on primary target and Bleed on secondary targets. |
| Scythe | Bleed | — | Purge stacks from allies. On kill, transfer stacks to an adjacent enemy. |
| Whip | Bleed | — | Apply Bleed at 3-space range. Rank 3: pull a Bleeding target toward you. |
| Staff | Force | — | Force stacks catalyze elemental stacks (extra tick on hit against targets with active elemental stacks). Gish bridge weapon. |
| Trident | Bleed | — | Impaled targets: Bleed stacks do not decay. |
| Chain | Force | — | Entangled targets gain 1 Force stack per turn (constricting). |

### Spear (Standard, Reach) — 8 Techniques

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

#### Spear Weapon Augments (Deep Pierce)

Passive. Once learned, these apply to ALL Spear Techniques. Each adds its Mana cost to every Spear Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Formation Fighting | While an ally is within 2 spaces, Spear Techniques gain +2 to hit. | +0 |
| 2 | Pin Down | Spear Techniques that apply Bleed also reduce target movement by 1 space per Bleed stack active on them. | +1 |
| 3 | Thrown Mastery | After a thrown Spear Technique, the spear returns immediately (no end-of-turn wait). Thrown range +10 ft. | +1 |
| 4 | Vital Strike | Bleed from Spear Techniques ignores 1 additional Physical DR (2 total with Deep Pierce). | +2 |
| 5 | Lance Charge | If you moved 3+ spaces toward a target before using a Spear Technique, +1d8 Piercing damage. | +2 |

### Halberd (Standard, Reach) — 8 Techniques

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

#### Halberd Weapon Augments (Cleaving Sweep)

Passive. Once learned, these apply to ALL Halberd Techniques. Each adds its Mana cost to every Halberd Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Reach Advantage | Halberd Techniques gain +1 to hit against targets at exactly 2-space reach. | +0 |
| 2 | Splitting Edge | Sweeping Arc and Rending Sweep apply 1 additional Bleed stack to secondary targets. | +1 |
| 3 | Staggering Force | Force stacks from Halberd Techniques reduce target movement by 1 space per stack. | +1 |
| 4 | Dual Condition Mastery | When a Halberd Technique applies both Force and Bleed in one sweep, +1d6 damage to all targets hit. | +2 |
| 5 | Execution Sweep | Halberd Techniques deal +2d10 damage to targets that are Staggered or Shredded. | +2 |

### Scythe (Complex, Reach) — 12 Techniques

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

#### Scythe Weapon Augments (Death's Harvest)

Passive. Once learned, these apply to ALL Scythe Techniques. Each adds its Mana cost to every Scythe Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Lingering Wounds | Bleed from Scythe Techniques lasts 1 additional round before decaying. | +0 |
| 2 | Blood Scent | Scythe Techniques gain +2 to hit against targets with 3+ Bleed stacks. | +1 |
| 3 | Harvest Chain | When Death's Harvest triggers, transfer Bleed to up to 2 enemies within 2 spaces (split stacks as you choose). | +1 |
| 4 | Crimson Mist | Blood Purge range increases to 4 spaces. Heal 2d6 per stack removed instead of 1d6. | +2 |
| 5 | Death's Embrace | Enemies killed by Scythe Techniques cannot be resurrected or healed from Dying for 1 minute. Soul Harvest restores double Mana. | +2 |

### Whip (Standard, Reach) — 8 Techniques

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

#### Whip Weapon Augments (Lashing Reach)

Passive. Once learned, these apply to ALL Whip Techniques. Each adds its Mana cost to every Whip Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Extended Reach | Whip reach increases to 4 spaces. | +0 |
| 2 | Barbed Lash | Whip Techniques apply 1 additional Bleed stack when the target is at maximum reach distance. | +1 |
| 3 | Constricting Wrap | Restrained targets take 1 Bleed stack at the start of each of their turns. | +1 |
| 4 | Savage Crack | Crack deals 1d8 instead of 1d4. Lashing Fury strikes deal 1d6 instead of 1d4. | +2 |
| 5 | Bloodhook | Yank pulls targets 3 spaces instead of 2. Pulled targets take 1d6 Slashing damage on arrival. | +2 |

### Staff (Standard, Reach) — 8 Techniques

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

#### Staff Weapon Augments (Arcane Conduit)

Passive. Once learned, these apply to ALL Staff Techniques. Each adds its Mana cost to every Staff Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Spell Focus | While wielding a Staff, your spells deal +1 damage per die rolled. | +0 |
| 2 | Conduit Mastery | Arcane Conduit elemental ticks deal +1 damage each. | +1 |
| 3 | Mana Flow | When a Staff Technique triggers 3+ elemental ticks in one hit, regain 2 Mana. | +0 |
| 4 | Elemental Infusion | Staff Techniques inherit the element type of the highest active stack on the target. Damage type changes to match. | +2 |
| 5 | Arcane Overcharge | Force stacks from Staff Techniques trigger 1 additional elemental tick beyond normal (Arcane Strike triggers 2, Resonating Blow triggers 3 per stack). | +2 |

### Trident (Standard, Reach) — 8 Techniques

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

#### Trident Weapon Augments (Impaling Tines)

Passive. Once learned, these apply to ALL Trident Techniques. Each adds its Mana cost to every Trident Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Barbed Prongs | Bleed from Trident Techniques requires +2 to the DC to remove via mundane healing. | +0 |
| 2 | Deep Impale | Impaled targets take 1d4 Piercing at the start of each of their turns. | +1 |
| 3 | Trident Recall | Recalling a thrown Trident deals 1d6 Piercing to the target on exit. Apply 1 Bleed stack. | +1 |
| 4 | Relentless Bleed | Bleed from Trident Techniques ignores 2 Magic DR on tick damage. | +2 |
| 5 | Executioner's Pin | Trident Techniques deal +2d10 damage to Impaled targets at or below half HP. | +2 |

### Chain (Complex, Reach) — 12 Techniques

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

#### Chain Weapon Augments (Constriction)

Passive. Once learned, these apply to ALL Chain Techniques. Each adds its Mana cost to every Chain Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Heavy Links | Force stacks from Chain Techniques reduce target movement by 1 space per stack. | +0 |
| 2 | Tightening Grip | Constriction deals 1d4 Bludgeoning per Force stack each time it triggers. | +1 |
| 3 | Chain Web | Entangling a target adjacent to another enemy applies 1 Force stack to that enemy. | +1 |
| 4 | Relentless Bind | Entangled targets cannot use Reactions. Restrained targets cannot use Reactions or Free Actions. | +2 |
| 5 | Shatter Chains | When Cascade Failure triggers, re-Entangle the primary target as a Free Action. Chain fragments deal 1d6 Bludgeoning to all affected enemies. | +2 |

---

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Ranged

Projectile weapons. Ranged favors kiting, precision, and area denial. You attack from safety, but ammunition and Action costs limit sustained fire.

### Ranged Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Aimed Shot | 2 Actions | Spend 1 extra Action aiming. Advantage and +2 to hit. |
| 1 | Quick Shot | 1 Action | Ranged attack at -1 die size on damage. |
| 2 | Suppressing Fire | 2 Actions | Target a 2-space area. All enemies in the area have disadvantage on attacks until your next turn. |
| 2 | Volley | 2 Actions | Attack up to 3 targets. Roll separately for each. |
| 3 | Kill Shot | 2 Actions | If the target hasn't moved since your last turn, double damage. |

### Ranged Category Technique Augments

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

### Ranged Weapons

| # | Weapon | Complexity | Base Damage | Range | Properties |
|---|---|---|---|---|---|
| 26 | Bow | Complex | 1d8 | 60 ft | Two-Handed, Ammunition |
| 27 | Crossbow | Standard | 1d10 | 80 ft | Two-Handed, Ammunition, Loading, Pierce |
| 28 | Hand Crossbow | Standard | 1d6 | 30 ft | Light, Ammunition, Loading |
| 29 | Bomb Flask | Standard | 2d4 | 30 ft | Thrown, AoE (2-space radius), Consumable |

**Crossbow and Loading.** The Crossbow requires 1 Action to reload after each shot. Higher Mastery ranks unlock Techniques that reduce or bypass reload time.

### Ranged Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Bow | Varies | — | Condition changes by Technique. Elemental Arrow: Burn/Chill/Shock/Corrode. Base attacks: Bleed. |
| Crossbow | Bleed | — | Deep Penetration: Bleed ignores 2 Physical DR (Pierce extends to Bleed). |
| Hand Crossbow | Poison | — | Every hit applies 1 Poison. Rapid-fire rushes Venomous. Rank 3: 2 Poison per hit. |
| Bomb Flask | Varies | — | AoE stacks: Fire Flask = Burn, Acid Flask = Acid, Frost Flask = Chill. Area denial condition weapon. |

### Bow (Complex, Ranged) — 12 Techniques

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

#### Bow Weapon Augments (Draw)

Passive. Once learned, these apply to ALL Bow Techniques. Each adds its Mana cost to every Bow Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Power Draw | Full Draw attacks (2+ Actions aiming) deal +2d8 instead of +1d8. Stacks with Perfect Draw passive (+3d8 total). | +2 |
| 2 | Rapid Nock | After using a Bow Technique, your next Bow Technique this turn costs 1 less Action (minimum 1). Once per turn. | +2 |
| 3 | Pinning Shot | Bow Techniques that hit a target within 1 space of a wall or solid object pin them (Restrained until they spend 1 Action to pull the arrow free). | +2 |
| 4 | Windage | Bow Techniques ignore cover penalties (half cover and three-quarter cover). | +1 |
| 5 | Arrow Recovery | After combat, recover 50% of spent ammunition (round down). | +0 |

### Crossbow (Standard, Ranged) — 8 Techniques

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

#### Crossbow Weapon Augments (Deep Penetration)

Passive. Once learned, these apply to ALL Crossbow Techniques. Each adds its Mana cost to every Crossbow Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Heavy Draw | Crossbow Techniques deal +1d10 damage against targets 40 ft or farther away. | +2 |
| 2 | Serrated Bolts | Bleed applied by Crossbow Techniques deals +1 per tick. | +2 |
| 3 | Bipod Rest | While you haven't moved this turn, Crossbow Techniques gain +2 to hit. Stacks with Steady Shot. | +1 |
| 4 | Bleed Through | Deep Penetration ignores 3 Physical DR instead of 2 on Bleed ticks. | +2 |
| 5 | Bolt Recovery | After combat, recover 50% of spent Crossbow ammunition (round down). | +0 |

### Hand Crossbow (Standard, Ranged) — 8 Techniques

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

#### Hand Crossbow Weapon Augments (Toxic Bolts)

Passive. Once learned, these apply to ALL Hand Crossbow Techniques. Each adds its Mana cost to every Hand Crossbow Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Dual Wield | When wielding two Hand Crossbows, fire both with a single Technique. Second shot deals half damage. | +3 |
| 2 | Rapid Toxin | Poison stacks from Hand Crossbow Techniques deal +1 per tick. | +2 |
| 3 | Crippling Venom | Targets with 3+ Poison stacks from your Hand Crossbow have -2 to all attacks. | +2 |
| 4 | Coated Bolts | First Hand Crossbow Technique each combat applies 2 extra Poison stacks. | +0 |
| 5 | Bolt Recovery | After combat, recover 50% of spent Hand Crossbow ammunition (round down). | +0 |

### Bomb Flask (Standard, Ranged) — 8 Techniques

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

#### Bomb Flask Weapon Augments (Volatile Mixture)

Passive. Once learned, these apply to ALL Bomb Flask Techniques. Each adds its Mana cost to every Bomb Flask Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Expanded Blast | Bomb Flask AoE radius increases by 1 space. | +2 |
| 2 | Lingering Residue | Bomb Flask area effects (burning ground, difficult terrain, DR reduction) last 1 additional round. | +2 |
| 3 | Efficient Mixture | Once per combat, a Bomb Flask Technique does not consume a flask. | +0 |
| 4 | Concentrated Formula | Bomb Flask Techniques apply 1 additional stack of their condition type. | +2 |
| 5 | Flask Recovery | After combat, recover 1 flask of each type you used (max 3 total). | +0 |

---

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Firearms

Mechanical ranged weapons. Firearms deal high damage per shot but are limited by ammunition and reload requirements.

### Firearms Category Techniques

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Fan the Hammer | 1 Action | Fire twice in one Action. Half damage each. Revolver and Hand Crossbow only. |
| 1 | Steady Aim | Passive | If you haven't moved this turn, +2 to hit on all ranged attacks. |
| 2 | Covering Fire | 1 Action | Choose an ally. Until your next turn, if an enemy attacks that ally, you may fire at the attacker as a Reaction. |
| 2 | Penetrating Round | 1 Action | Ignores all Physical DR. Costs 2 ammunition. |
| 3 | Dead Eye | 3 Actions | Auto-hit, maximum damage. Once per combat. |

### Firearms Category Technique Augments

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

### Firearms Weapons

| # | Weapon | Complexity | Base Damage | Range | Properties |
|---|---|---|---|---|---|
| 30 | Revolver | Standard | 1d8 | 40 ft | Light, Ammunition (6), Reload |
| 31 | Rifle | Standard | 1d10 | 80 ft | Two-Handed, Ammunition (8), Reload |
| 32 | Shotgun | Standard | 2d6 | 20 ft | Two-Handed, Ammunition (2), Reload, Spread |

### Firearms Condition Signatures

| Weapon | Primary | Secondary | Unique Interaction |
|---|---|---|---|
| Revolver | Force | — | Each shot applies 1 Force stack. Fan the Hammer applies 2 Force in one Action. |
| Rifle | Bleed | Force | Standard shots apply Bleed. Penetrating Round applies Force. Switch by Technique. |
| Shotgun | Force | — | Point-blank: 2 Force stacks. Maximum range: 1 Force stack. Spread: 1 Force to adjacent targets. |

### Revolver (Standard, Firearms) — 8 Techniques

**Unique Mechanic: Six Shooter.** 6-round cylinder. Each Revolver shot expends 1 round and applies 1 Force stack. Light property allows dual-wielding. Fan the Hammer (Category Technique) fires both shots, applying 1 Force per hit (2 Force per Action).

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Quick Draw | Reaction | At combat start, fire 1 shot before initiative resolves. 1d8 Force. Apply 1 Force stack. |
| 1 | Trick Shot | 1 Action, 3 Mana | Ricochet off a surface. Ignores cover. +2 to hit. 1d8 Force. Apply 1 Force stack. |
| 2 | Fanning Barrage | 1 Action, 3 Mana | Fire 3 rounds. 1d4 Force per round. Apply 1 Force stack per hit. Expends 3 ammunition. |
| 2 | Pistol Whip | 1 Action | Melee attack. 1d6 Bludgeon. Apply 1 Force stack. Target loses Reaction until start of its next turn. |
| 3 | Rapid Fan | Passive | Fan the Hammer with a Revolver applies 2 Force stacks per hit instead of 1 (4 Force total per Action). |
| 3 | Staggering Shot | 1 Action, 5 Mana | 2d8 Force. Apply 2 Force stacks. Target rolls `2d10 + Body` vs DC 12 or Prone. |
| 4 | Concussive Impact | 1 Action, 8 Mana | Requires Staggered (5 Force stacks) on target. 2d8 Force. Apply Shattered (T3): Physical DR = 0 for 2 rounds. Physical attacks auto-apply 1 Bleed. |
| 5 | Dead Man's Hand (Capstone) | 1 Action, 15 Mana | Requires Shattered (T3) on target. Spend all 6 rounds. 6d8 Force. Target rolls `2d10 + Body` vs DC 18 or Stunned for 1 round. Reload required. Once per long rest. |

#### Revolver Weapon Augments (Six Shooter)

Passive. Once learned, these apply to ALL Revolver Techniques. Each adds its Mana cost to every Revolver Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Speed Loader | Reload costs 0 Actions once per combat. | +0 |
| 2 | Heavy Rounds | Revolver Techniques deal +1d4 Force damage. | +2 |
| 3 | Gunslinger | When dual-wielding Revolvers, Quick Draw fires both pistols. Second shot deals half damage and applies 1 Force stack. | +2 |
| 4 | Hollow Points | Force stacks from Revolver Techniques deal +1 per tick (+2 total per stack per round instead of +1). | +2 |
| 5 | Showdown | While Shattered (T3) is active on the target, your Revolver Techniques against that target have advantage. | +3 |

### Rifle (Standard, Firearms) — 8 Techniques

**Unique Mechanic: Marksman.** Standard Rifle shots apply Bleed (high-velocity puncture). Techniques marked [Force] apply Force instead (kinetic impact). Choose your condition path by Technique selection.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Long Shot | 1 Action, 2 Mana | +20 ft range. 1d10 Piercing + 1d6 damage. Apply 1 Bleed stack. |
| 1 | Bayonet Strike | 1 Action | Move 2 spaces toward target. Melee attack. 1d8 Piercing. Apply 1 Bleed stack. |
| 2 | Scope In | 2 Actions, 5 Mana | Next Rifle shot auto-hits. +1d10 damage. Apply 2 Bleed stacks. |
| 2 | Suppressing Burst | 1 Action, 5 Mana | [Force] 3-space line. All targets roll `2d10 + Body` vs DC 12 or Prone. Apply 1 Force stack per target. |
| 3 | Armor Piercing Round | 1 Action, 5 Mana | Ignores all Physical DR. 2d10 Piercing. Apply 2 Bleed stacks. |
| 3 | Kinetic Impact | 1 Action, 5 Mana | [Force] 2d10 Force. Apply 2 Force stacks. Push target 2 spaces. |
| 4 | Decisive Shot | 1 Action, 8 Mana | Choose one path. Bleed: requires Shredded (5 Bleed) on target, 2d10 Piercing, apply Hemorrhage (T3): Bleed doubles, healing 50% effective, persists 2 extra rounds. Force: requires Staggered (5 Force) on target, 2d10 Force, apply Shattered (T3): Physical DR = 0 for 2 rounds, physical attacks auto-apply 1 Bleed. |
| 5 | Marksman's Execution (Capstone) | 2 Actions, 15 Mana | Requires Hemorrhage or Shattered (T3) on target. Auto-hit. 4d10 Piercing. If Hemorrhage active: all Bleed stacks tick immediately. If Shattered active: Physical DR permanently reduced by 2 for rest of combat. Once per long rest. |

#### Rifle Weapon Augments (Marksman)

Passive. Once learned, these apply to ALL Rifle Techniques. Each adds its Mana cost to every Rifle Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Extended Magazine | Ammunition increases from 8 to 12 rounds. | +0 |
| 2 | Bipod | While prone or stationary, Rifle Techniques gain +2 to hit. Stacks with Steady Aim. | +1 |
| 3 | Match Rounds | Rifle Techniques deal +1d6 damage at 60 ft or beyond. | +2 |
| 4 | Through-and-Through | Rifle shots that hit continue through the target. One enemy directly behind takes half damage. | +2 |
| 5 | Dual Discipline | When switching between Bleed and Force Techniques in the same turn, the second Technique deals +1d8 damage. | +3 |

### Shotgun (Standard, Firearms) — 8 Techniques

**Unique Mechanic: Buckshot.** Point-blank Shotgun attacks (within 2 spaces) deal +1d6 damage and apply 2 Force stacks instead of 1. Spread property: enemies adjacent to the primary target take half damage and 1 Force stack.

| Rank | Technique | Cost | Effect |
|---|---|---|---|
| 1 | Breaching Entry | 1 Action | Within 2 spaces. 2d6 Force. Apply 2 Force stacks (Buckshot). Push target 2 spaces. |
| 1 | Slug Round | 1 Action, 2 Mana | Single target (no Spread). +1d10 damage. Range increases to 40 ft. Apply 1 Force stack. |
| 2 | Buckshot Sweep | 1 Action, 5 Mana | 2-space cone. 2d6 Force to each target. Apply 1 Force stack per target hit. |
| 2 | Sawed-Off Mode | Free Action | Toggle. Range halved (10 ft). Spread hits all enemies adjacent to you instead of adjacent to the target. |
| 3 | Shrapnel Blast | 1 Action, 7 Mana | Within 2 spaces. 3d6 Force. Apply 2 Force stacks. Spread targets take full damage instead of half. |
| 3 | Staggering Blast | 1 Action, 5 Mana | 2d6 Force. Apply 2 Force stacks. Target rolls `2d10 + Body` vs DC 14 or Prone. Push 2 spaces. |
| 4 | Breaching Shot | 1 Action, 8 Mana | Within 1 space. Requires Staggered (5 Force stacks) on target. 3d6 Force. Apply Shattered (T3): Physical DR = 0 for 2 rounds. Physical attacks auto-apply 1 Bleed. |
| 5 | Demolition Blast (Capstone) | 2 Actions, 15 Mana | Requires Shattered (T3) on target. 6d6 Force. All enemies within 2 spaces take 3d6 Force and 2 Force stacks. Target rolls `2d10 + Body` vs DC 18 or Stunned for 1 round. Once per long rest. |

#### Shotgun Weapon Augments (Buckshot)

Passive. Once learned, these apply to ALL Shotgun Techniques. Each adds its Mana cost to every Shotgun Technique you use.

| # | Augment | Effect | Mana Cost |
|---|---|---|---|
| 1 | Extended Tube | Ammunition increases from 2 to 4 rounds. | +0 |
| 2 | Dragon's Breath | Shotgun Techniques within 2 spaces also apply 1 Burn stack per target hit. | +2 |
| 3 | Knockback | Shotgun Techniques that hit push the target 1 space. Stacks with Push effects from individual Techniques. | +1 |
| 4 | Tight Spread | Spread damage increases from half to three-quarters of the original damage. | +2 |
| 5 | Close Quarters Master | While an enemy is within 2 spaces, Shotgun Techniques against that enemy gain +2 to hit. | +2 |

---

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Condition Escalation and Techniques

Weapon Techniques interact with the condition stack system. Every condition follows the same pipeline: apply stacks → reach 5 stacks → trigger T2 escalation. Weapon Techniques extend this pipeline into T3 and T4.

### Escalation Pipeline

1. **Stacks (T1).** Apply condition stacks through weapon hits and Techniques. Each stack deals +1 damage per round.
2. **T2 Escalation.** At 5 stacks, the condition escalates automatically. Bleed → Shredded. Force → Staggered. Burn → Ignited. Chill → Frozen. Shock → Shocked. Acid → Corroded. Poison → Venomous.
3. **T3 Enhancement.** Requires a T2 escalated condition active on the target. Costs 12 Mana. Accessed through Rank 3–4 Weapon Techniques.
4. **T4 Ultimate.** Requires a T3 enhancement active on the target. Costs 17 Mana. Once per long rest. Accessed through Rank 5 Capstone Weapon Techniques.

### T3 Enhanced Escalations

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

### T4 Ultimate Escalations

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

### Escalation Paths

Three paths reach T3 and T4. They combine freely.

| Path | How T3 | How T4 |
|---|---|---|
| Weapon Techniques | Build stacks over turns → T2 at 5 stacks → T3 Technique enhances | T3 active → T4 capstone Technique (once per long rest) |
| Spellcasting | Pay 12 Mana for T3 spell directly | Pay 17 Mana for T4 spell directly |
| Gish combo | Spells rush to T2 → weapon T3 Technique enhances | Either path to T3 → weapon T4 or spell T4 |

> **Example:** A Staff-wielding Hybrid casts Chill spells to reach Frozen (T2). On the next turn, the Hybrid uses a Staff Technique to apply Permafrost (T3, 12 Mana). The enemy re-freezes each round and takes +1d8 from physical attacks. Two turns later, the Hybrid triggers Absolute Zero (T4, 17 Mana), incapacitating the target for 2 rounds with all damage doubled.

---

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Magic Weapons

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

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Gish Synergies

Spellcasting requires only Mana. No weapon, item, or property gates casting. Any character with Mana can cast any spell with any weapon equipped or empty-handed. Weapons grant bonuses but never act as prerequisites.

Five bridges connect weapon combat and spellcasting.

**Spell Strike.** The Spell Strike Augment bundles a Touch spell with a weapon attack. One roll resolves both. If you miss, the spell is not expended. Mana for the spell is paid separately from the Technique's Mana cost.

**Arcane Infusion.** The Arcane Infusion Augment rewards casting before attacking. After you cast a spell, your next Technique deals +1d8 elemental damage matching the spell's element.

**Stack Exploitation.** Spell stacks and Technique stacks share the same counter per condition type. A Burn spell adds to the same Burn counter as a Condition: Burn Augment or a weapon's innate Burn application. Gish characters cycle stacks faster than pure martials or pure casters.

**Action Economy Weaving.** You have 3 Actions per turn. Split them between Spells and Techniques in any combination. You are never locked into one mode. Cast a spell with Action 1, attack with Action 2, attack with Action 3.

**Mana Reave.** The Mana Reave Augment restores Mana on weapon hits equal to your weapon's base damage die. This enables sustained Technique use for Hybrid builds that would otherwise run dry.

---

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Mana Economy

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

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Build Examples

### The Duelist (Rapier + Shield)

- **Mastery:** Rapier 4, Shield 2. Background: Martial.
- **Role:** Counter-fighting tank.
- **Core loop:** En Garde stance → Parry incoming attacks → generate Openings → Compound Riposte for bonus damage. Shield for Cover Ally and emergency Raise Shield.
- **Key Techniques:** En Garde, Parry (Medium Melee), Compound Riposte, Fleche, Tempo Rubato, Shield Bash, Cover Ally.
- **Weapon Augments (passive):** Riposte Mastery (2 Openings per Parry), Duelist's Grace (+1 AC at 2+ Openings), Tempo Control (-1 to hit per Opening spent).
- **Technique Augments (socketed):** Feint Chain (free Openings on Feinting Thrust hits), Bleeding Riposte (Bleed on Compound Riposte), Rising Thrust (attack after Passata Sotto).
- **Condition path:** Bleed through Rapier → Shredded at 5 stacks. Openings accelerate Bleed application.

### The Berserker (Great Axe)

- **Mastery:** Great Axe 5. Background: Martial.
- **Role:** All offense. Rush in, AoE, execute.
- **Core loop:** Charge in → Power Attack → Cleave on kills → Executioner to finish wounded targets. Double Bleed ticks pressure everything.
- **Key Techniques:** Power Attack, Cleave, Whirlwind, Executioner, Staggering Blow.
- **Category Technique Augments:** Cascading Cleave (chain kills), Brutal Power Attack (+2 dice), Expanding Whirlwind (2-space radius).
- **Condition path:** Bleed at double tick rate → Shredded → Hemorrhage (T3) → Exsanguination (T4 capstone, once per long rest).

### The Sentinel (Spear + Shield)

- **Mastery:** Spear 3, Shield 3. Background: Martial.
- **Role:** Pure tank and controller. Lock down movement, protect allies.
- **Core loop:** Sentinel (Reaction attacks on approach) → Impale to pin targets → Shield Wall with adjacent ally → Raise Shield for durability.
- **Key Techniques:** Sentinel, Sweep, Impale, Keep at Bay, Phalanx, Shield Bash, Raise Shield, Shield Wall.
- **Weapon Augments (passive):** Formation Fighting (+2 to hit near allies), Pin Down (Bleed slows movement), Shield Master (AC bonus to nearby allies).
- **Category Technique Augments:** Threatening Reach (Sentinel triggers within reach), Trip Sweep (prone on Sweep hits).
- **Condition path:** Bleed through Spear (ignores 1 Physical DR). Impaled targets do not lose Bleed to decay. Force through Shield Bash.

### The Hybrid (Staff + Spellcasting)

- **Mastery:** Staff 3. Background: Hybrid (110 HP, 70 Mana, 10 regen).
- **Role:** Gish condition accelerator.
- **Core loop:** Cast Burn/Chill spells → Staff attacks catalyze elemental stacks (extra ticks) → push to T2 escalation → T3 enhancement Technique → T4 if fight goes long.
- **Key Techniques:** Staff weapon Techniques (TODO), Sentinel, Sweep. Spells: Burn/Chill/Shock varieties.
- **Universal Augments (socketed):** Condition: Burn (add stacks to Staff Techniques), Elemental Shift (change damage type on any Technique).
- **Spellblade Augments:** Arcane Infusion (+1d8 elemental after spell), Spell Strike (Touch spell + melee attack), Mana Reave (+3 Mana on Technique kills).
- **Condition path:** Spell stacks + Staff catalysis → Frozen (Chill T2) → Permafrost (T3, 12 Mana) → Absolute Zero (T4 capstone, 17 Mana, once per long rest).

### The Assassin (Dagger + Hand Crossbow)

- **Mastery:** Dagger 4, Hand Crossbow 3. Background: Hybrid or Martial.
- **Role:** Dual-condition poison and bleed specialist. Ambush predator.
- **Core loop:** Open at range with Hand Crossbow → apply Poison stacks (1 per hit, 2 at Rank 3) → close to melee → Dagger Flurry for Bleed + Poison → double escalation (Shredded + Venomous). Against bosses: Neurotoxin (T3) + Hemorrhage (T3) for layered pressure.
- **Key Techniques:** Quick Draw, Flurry, Assassinate, Hand Crossbow Techniques (TODO). Quick Shot for ranged Poison, Flurry for melee combo.
- **Weapon Augments (passive):** Envenomed Blade (+1 Poison tick damage), Arterial Cut (mundane healing can't remove Dagger Bleed), Shadowstep (teleport on kill).
- **Category Technique Augments:** Triple Flurry (3rd attack), Vanishing Strike (stealth after Assassinate), Lethal Ambush (×3 damage).
- **Condition path:** Poison at range → Venomous (T2) → Neurotoxin (T3, movement = 0). Bleed in melee → Shredded (T2) → Hemorrhage (T3). Against bosses: stack both T3s, then Lethal Dose (T4 capstone, once per long rest).

{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}

\page

## Full Augment Catalog

The book includes all Universal Augments and worked examples for Rapier and Katana (Weapon Augments + Technique Augments). The full catalog of all 32 weapons, their Weapon Augments, and all Technique Augments is available through the Solus character builder web app. TODO: web app URL.


{{footnote Weapons, Techniques, and Augments}}
{{pageNumber,auto}}


\page

<!-- CHAPTER 7: MAGIC AND SPELLCASTING -->

# Magic and Spellcasting

{{wide

Solus has no spell list, no grimoire, and no preparation phase. You build every spell by setting ten **parameters**: what tag affinity it belongs to, what it does, how far it reaches, how big the area is, what shape it takes, how long it lasts, how many targets it hits, how it connects with those targets, how much damage it deals, and how powerful its lasting effect is. If you have the mana, you can cast it. Use the tables below as reference during play.

Each parameter has a **mana cost** and an **action cost**. Add up the mana costs of parameters 2 through 10 to get the spell's base mana cost, then multiply by your affinity's cost multiplier for the final mana total. The highest action cost among your parameters sets how many of your 3 turn actions the spell requires.

Your mana pool starts full at the beginning of each encounter. Mana regenerates at the start of your turn each round.

**Sustained spells.** Some parameter options show **S** in the Actions column instead of a number. Picking any S option makes the spell **sustained**: it cannot be cast in a single turn. A sustained spell costs all 3 actions on the turn you begin casting, then 1 action each subsequent turn to maintain. If you skip the maintenance action or get interrupted (knocked unconscious, silenced, stunned), the spell ends and mana already spent is lost. You can release a sustained spell voluntarily at the start of your turn for free.

##### Spell Parameter Table
| Parameter | Option | Actions | Mana | Notes |
|:---|:---|:---:|:---:|:---|
| **Tag Affinity** | Main | — | ×1 | Multiplier applied to the total of all other parameters. See Tag Affinities. |
| | Sub | — | ×2 | |
| | Locked | — | — | Cannot cast from a locked affinity. |
| **Function** | Utility | — | 0 | Dual-function spells add both costs. |
| | Movement | — | 1 | |
| | Defensive | — | 1 | |
| | Offensive | — | 2 | |
| **Range** | Self–25 ft. | 1 | 1 | Contributes 1 damage die. |
| | 30–60 ft. | 2 | 2 | |
| | 65–120 ft. | 3 | 3 | |
| | 125–200 ft. | S | 4 | Sustained. |
| | Sight | S | 5 | Sustained. |
| | Global | S | 6 | Sustained. |
| **Size** | 5–15 ft. | 1 | 1 | Contributes 1 damage die. |
| | 20–30 ft. | 2 | 2 | |
| | 35–60 ft. | 3 | 3 | |
| **Shape** | Point / none | 1 | 1 | |
| | Sphere / Cube / Line / Wall / Cylinder | 2 | 2 | |
| | Freeform / custom | 3 | 3 | |
| **Duration** | Instant | 1 | 1 | If effect outlasts casting, pay the longer duration's cost. |
| | 1 Round | 2 | 2 | |
| | 1 Minute | 3 | 3 | |
| | Hours | S | 4 | Sustained. |
| | Permanent | S | 5 | Sustained. |
| **Target Count** | Single | 1 | 1 | Contributes 1 damage die. |
| | Multi 2+ | 2 | 2 | +1 mana per extra target (max 4). |
| | AOE | 3 | 3 | |
| **Accuracy** | Attack Roll | 1 | 1 | Adds a bonus damage die (sized by Damage parameter). |
| | Save | 1 | 1 | |
| | Auto-Hit | S | 4 | Sustained. |
| **Damage** | None | — | 0 | Non-offensive spells. |
| | d6 per die | — | 1 | Dice count = Range + Size + Target Count (1 each) + Attack Roll bonus (From Accuracy). Magic modifier = flat bonus. |
| | d8 per die | — | 2 | |
| | d10 per die | — | 3 | |
| | d12 per die | — | 5 | |
| **Effect Tier** | T1 | 1 | 3 | Applies the base tag. T2+ applies the escalated condition. Two tags at same tier = pay cost twice. |
| | T2 | 2 | 6 | |
| | T3 | 3 | 12 | |
| | T4 | S | 17 | Sustained. |

**Total mana cost** = (sum of parameters 2–10) × affinity multiplier. 

  **Total action cost** = the highest action value among your parameters.

{{descriptive
**TODO:** Jacob prefers this table grouped by action cost tier (all 1-action options together, all 2-action options together, etc.). Revisit layout once Jacob confirms the grouping he wants.
}}
}}

{{footnote Magic and Spellcasting}}
{{pageNumber,auto}}

\page

{{wide
## Tag Affinities

Your tag affinity determines which **tags** your spell applies on hit. Tags are labels on the source. When a tag lands on a target, it creates **stacks** that build up, deal damage over time, and trigger **escalated conditions** at 5 stacks (see Conditions, Injuries, and Death).

Your affinity also sets the spell's **cost multiplier**. At character creation you pick two tag affinities:

- **Main affinity (×1).** Your primary school. All parameter costs stay at face value.
- **Sub affinity (×2).** Your secondary school. The total mana cost of any spell using this affinity is doubled.

All other affinities are **locked**. You cannot cast spells from a locked affinity.

##### Tag Affinities Table
| Tag Affinity | What It Does | Tag → Escalation |
|:---|:---|:---|
| Elemental | Fire, ice, lightning, water, earth, air, acid, poison. Stack-based damage and control. | [Burn] → [Ignited], [Chilled] → [Frozen], [Volt] → [Shocked] |
| Force | Kinetic impact, barriers, gravity manipulation. | [Force] → [Stunned], [Restrained] → [Crush] |
| Mind | Psychic damage, illusions, charms, fear, sleep. | [Influence] → [Override], [Drowsy] → [Unconscious] |
| Temporal | Speed alteration, time shifts, teleportation. | [Slow] → [Stasis], [Blink] → [Teleport] |
| Creation | Transmutation, shaping matter, size changes. | [Harden] → [Reinforce], [Enlarge] → [Overgrow] |
| Order | Divine strikes, wards, truth compulsion, suppression. | [Strike] → [Judgement], [Suppression] → [Nullify] |
| Summoning | Drawing or binding entities. | [Invite] → [Summon] |
| Life | Healing, revival, radiant damage, purification, light. | [Restore] → [Regenerate], [Rouse] → [Revive], [Radiant] → [Purge], [Illuminate] → [Blind] |
| Death | Necrotic damage, death effects, reanimation, decay. | [Necrosis] → [Necroptosis], [Pyroptosis] → [Apoptosis], [Reanimate] → [Vivify], [Decay] → [Wither] |
| Corruption | Chaotic instability, wild magic. | [Instability] → [Wild Magic] |

#### Mana Pools
| Background | Max Mana | Regen per Round |
|:---|:---:|:---:|
| Caster | 100 | 15 |
| Hybrid | 70 | 10 |
| Martial | 30 | 3 |

}}
{{footnote Magic and Spellcasting}}
{{pageNumber,auto}}

\page
{{wide
## Building a Spell: Fire Bolt

You want a fire attack that hits one enemy at close range. Pick one option for each of the ten parameters, record the mana and action costs, then total them up.

| # | Parameter | Your Pick | Actions | Mana | Why |
|:---:|:---|:---|:---:|:---:|:---|
| 1 | Tag Affinity | Elemental (Main) | — | ×1 | Fire tags. Main = no multiplier penalty. |
| 2 | Function | Offensive | — | 2 | You are attacking. |
| 3 | Range | Self–25 ft. | 1 | 1 | Close range. Contributes 1 damage die. |
| 4 | Size | 20–30 ft. | 2 | 2 | Medium blast. Contributes 1 damage die. |
| 5 | Shape | Point | 1 | 1 | Single impact point. |
| 6 | Duration | Instant | 1 | 1 | Hits and ends. |
| 7 | Target Count | Single | 1 | 1 | One target. Contributes 1 damage die. |
| 8 | Accuracy | Attack Roll | 1 | 1 | Roll to hit. Adds a bonus damage die. |
| 9 | Damage | d6 per die | — | 1 | Sets die size for all 4 damage dice. |
| 10 | Effect Tier | T1 (Burn) | 1 | 3 | Applies 1 Burn stack on hit. |
}}


#### Damage

Range, Size, and Target Count each contribute one die. Attack Roll adds a bonus die. All four use the size from the Damage parameter: d6 in this build. Your Magic modifier applies as a flat bonus.

**Fire Bolt:** 4d6 + Magic modifier

#### Effect

T1 Burn applies 1 Burn stack on hit. Burn stacks deal fire damage equal to the stack count and build toward the Ignited escalated condition at 5 stacks (see Conditions, Injuries, and Death). T2 would skip the buildup and apply Ignited directly.
#### Totals

**Base mana** (parameters 2–10): 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 3 = **13**

**Affinity multiplier:** Elemental is your Main (×1), so the final cost is **13 mana**. As your Sub (×2) the same spell would cost 26.

**Action cost:** The highest action value is 2 (Size). The spell costs **2 of your 3 actions**.

\column

#### Casting Fire Bolt

1. **Check mana.** You need 13 mana in your pool. Mana regenerates at the start of your turn each round.
2. **Spend 2 actions and 13 mana.**
3. **Roll to hit.** Roll 2d10 + Magic against the target's Magical AC.
4. **On hit, roll damage.** Roll 4d6 + Magic modifier. Subtract the target's Magic DR.
5. **Apply the tag.** The target gains 1 Burn stack.

{{note
**Example:** Your Magic is +3. The target has Magical AC 5 (Magic DR 4, Magic +1). You roll 2d10: 7 + 8 = 15, plus 3 = 18. That beats 5. Damage: 4d6 + 3 = 4 + 2 + 5 + 3 + 3 = 17, minus Magic DR 4 = **13 damage**. The target gains 1 Burn stack.
}}

{{wide 
{{descriptive
}}

{{footnote Magic and Spellcasting}}
{{pageNumber,auto}}

\page

{{wide
## More Spell Builds

The spell builder creates anything from a close-range nuke to a sustained healing field. These three builds show the range.

### Disintegration Ray

A single-target Force blast at maximum die size. This is the "kill it now" option. Every caster can build this on day one.

| # | Parameter | Your Pick | Actions | Mana | Why |
|:---:|:---|:---|:---:|:---:|:---|
| 1 | Tag Affinity | Force (Main) | — | ×1 | Force tags. Main = no multiplier penalty. |
| 2 | Function | Offensive | — | 2 | You are attacking. |
| 3 | Range | Self–25 ft. | 1 | 1 | Close range. Contributes 1 damage die. |
| 4 | Size | 5–15 ft. | 1 | 1 | Tight blast. Contributes 1 damage die. |
| 5 | Shape | Point | 1 | 1 | Single impact point. |
| 6 | Duration | Instant | 1 | 1 | Hits and ends. |
| 7 | Target Count | Single | 1 | 1 | One target. Contributes 1 damage die. |
| 8 | Accuracy | Attack Roll | 1 | 1 | Roll to hit. Adds a bonus damage die. |
| 9 | Damage | d12 per die | — | 5 | Maximum die size for all 4 damage dice. |
| 10 | Effect Tier | T2 | 2 | 6 | Skips T1 stacks. Applies Force escalation directly. |

**Damage:** 4d12 + Magic modifier (average ~30 + Magic)

**Base mana:** 2 + 1 + 1 + 1 + 1 + 1 + 1 + 5 + 6 = **19**. Affinity multiplier: ×1. Final cost: **19 mana**.

**Action cost:** Highest action value is 2 (Effect Tier T2). Costs **2 of your 3 actions**.

A Caster (100 mana, 15 regen) can fire this 5 times before running dry. T2 means Physical DR does not reduce the damage. If the target survives, the Force escalation condition is already applied. Pair it with a 1-action follow-up (weapon swing, quick spell) to make full use of your turn.

### Frost Nova

An area burst that locks down a group. Lower damage, high control.

| # | Parameter | Your Pick | Actions | Mana | Why |
|:---:|:---|:---|:---:|:---:|:---|
| 1 | Tag Affinity | Elemental (Main) | — | ×1 | Ice tags. Main = no penalty. |
| 2 | Function | Offensive | — | 2 | Damage + Chilled stacks. |
| 3 | Range | Self–25 ft. | 1 | 1 | Centered on you. Contributes 1 damage die. |
| 4 | Size | 20–30 ft. | 2 | 2 | 30 ft. radius burst. Contributes 1 damage die. |
| 5 | Shape | Sphere | 2 | 2 | Radiates outward from your position. |
| 6 | Duration | Instant | 1 | 1 | One burst. |
| 7 | Target Count | AOE | 3 | 3 | Hits all creatures in the sphere. |
| 8 | Accuracy | Save | 1 | 1 | Targets roll to resist. No bonus die. |
| 9 | Damage | d6 per die | — | 1 | Smaller dice. Control is the point. |
| 10 | Effect Tier | T1 (Chilled) | 1 | 3 | Applies 1 Chilled stack to every target hit. |

**Damage:** 2d6 + Magic modifier per target (Range + Size contribute dice; AOE and Save do not add bonus dice)

**Base mana:** 2 + 1 + 2 + 2 + 1 + 3 + 1 + 1 + 3 = **16**. Affinity multiplier: ×1. Final cost: **16 mana**.

**Action cost:** Highest action value is 3 (AOE). Costs **all 3 actions**.

Every enemy in 30 ft. takes cold damage and gains a Chilled stack. Three hits reach 3 stacks. Two more reach Frozen (movement 0, costs 1 action to break free). This spell sets up the Frozen lockdown. A teammate who follows up with Volt stacks on a Frozen target triggers the Shocked → Stunned combo if the target is also Wet.

### Mending Light (Sustained Healing Field)

A sustained Life spell. Costs all 3 actions on the first turn and 1 action each turn after to maintain.

| # | Parameter | Your Pick | Actions | Mana | Why |
|:---:|:---|:---|:---:|:---:|:---|
| 1 | Tag Affinity | Life (Main) | — | ×1 | Restore tags. Main = no penalty. |
| 2 | Function | Defensive | — | 1 | Healing allies. |
| 3 | Range | Self–25 ft. | 1 | 1 | Centered on you. |
| 4 | Size | 20–30 ft. | 2 | 2 | 30 ft. radius field. |
| 5 | Shape | Sphere | 2 | 2 | Covers the party's position. |
| 6 | Duration | Hours | S | 4 | Sustained. |
| 7 | Target Count | AOE | 3 | 3 | All allies in the sphere. |
| 8 | Accuracy | Auto-Hit | S | 4 | Sustained. No roll required for healing. |
| 9 | Damage | None | — | 0 | Non-offensive. |
| 10 | Effect Tier | T1 (Restore) | 1 | 3 | Applies Restore each round. |

**Base mana:** 1 + 1 + 2 + 2 + 4 + 3 + 4 + 0 + 3 = **20**. Affinity multiplier: ×1. Final cost: **20 mana**.

**Action cost:** Two parameters have **S** (Duration and Accuracy), which makes this a sustained spell. Turn 1: spend all 3 actions and 20 mana to begin casting. Each turn after: spend 1 action to maintain the field. If you skip maintenance, get knocked unconscious, or get stunned, the spell ends and the mana is lost.

While sustained, every ally in 30 ft. gains the Restore tag each round: recent damage is repaired and injuries not yet permanent are stabilized. The field moves with you. Drop it when the party is safe or when you need your actions back.

{{note
**Sustained spells in practice.** Any parameter with an **S** action cost makes the spell sustained. You pay mana up front. On the casting turn, all 3 actions go to the spell. Every turn after, 1 action maintains it. Interruption (unconscious, stunned, silenced, voluntary release) ends the spell immediately. You do not recover the mana.
}}
}}

{{footnote Magic and Spellcasting}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 7: CORE GAMEPLAY LOOP -->

# Core Gameplay Loop

A session of Solus follows a repeating cycle. Every encounter, whether it involves combat, conversation, exploration, or puzzle-solving, passes through the same six steps.

### The Loop

1. **The world presents a problem.** The GM describes a situation that demands a response: a locked door, an ambush, a starving village, a collapsing bridge. The problem can be physical, social, magical, or environmental.
2. **You act.** You use your character's attributes, skills, equipment, and spells to respond. You might fight, negotiate, investigate, sneak, or flee.
3. **The system resolves consequences.** Dice rolls determine uncertain outcomes. Combat Rolls resolve attacks. Proficiency Checks resolve everything else. The GM interprets the results using the Degree of 5 scale (see Running the Game).
4. **Rewards follow.** Successful encounters award XP. Combat encounters pay XP per enemy rank. Exploration and social encounters award XP for engagement, whether you succeed or fail.
5. **Characters adjust between sessions.** You spend XP to raise proficiency ranks or buy new proficiencies. You can swap active proficiencies, change equipment, and update changeable traits with GM confirmation (see Advancement and Between Sessions).
6. **The next problem begins.** The world reacts to what you did. New problems emerge from the consequences of old ones.

\column

### Three Types of Encounters

The GM builds encounters from three modes. Most sessions mix all three.

**Combat encounters** use initiative, turn order, and the action economy from the Combat chapter. Enemies fight using the same rules you do. Rewards scale with enemy rank.

**Social encounters** use Proficiency Checks (Speech, Performance, Insight, Knowledge) against DCs set by the GM. You earn XP for engaging, regardless of outcome. Failing a negotiation still counts as play.

**Exploration encounters** use Proficiency Checks (Survival, Athletics, Investigation, Arcana, Stealth) to navigate terrain, find hidden things, avoid hazards, and solve puzzles. XP is awarded when the group engages with the encounter, not just when they solve it.

{{footnote Core Gameplay Loop}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 8: COMBAT -->

# Combat

Combat begins when negotiation, stealth, or avoidance fails and violence starts. This chapter covers the full sequence: who goes first, what you can do on your turn, how attacks land, and what happens when someone drops.

### Starting Combat

When combat breaks out, every combatant rolls for **initiative**. Roll **1d10** and add either your **Body** or your **Magic** modifier. You choose which modifier to use each time combat starts.

The GM ranks everyone from highest to lowest. That is the turn order for the entire encounter unless a rule changes it.

{{note 
**Tie-breaking.** If two combatants roll the same total:

1. The higher modifier goes first.
2. If still tied, roll another d10 between the tied combatants.
3. Players and their allies may choose to act simultaneously if both are willing. Enemies cannot share a simultaneous turn and must use option 1 or 2.

}}

**Round length.** Each full **round** of combat represents 3 seconds of in-world time. A round includes one **turn** for every combatant. Your turn is the part of the round where you act. When every combatant has taken a turn, the round ends and a new one begins.

### Your Turn

On your turn, you get **3 actions**. Spend them in any order. Finish resolving one action before starting the next. You can repeat an action (attack three times, move three times) unless a specific ability, spell, or item says otherwise.

##### Actions
| Action | What It Does |
|:---|:---|
| Attack | Strike with a weapon. Roll a Combat Roll (see below). |
| Use a Technique | Activate a prepared Technique. Costs 1+ actions and sometimes mana. See Weapons, Techniques, and Augments. |
| Cast a Spell | Cast a spell using 1 or more actions. Multi-action spells can span turns. |
| Move | Move up to your full movement speed. |
| Drink a Potion | Consume a potion or similar item. |
| Interact | Open a door, draw a weapon, pick up an object, pull a lever. |
| Use a Proficiency | Attempt a Proficiency Check during combat (Medicine to stabilize, Athletics to grapple). |

**Multi-action abilities.** Some spells, Techniques, and proficiency uses cost 2 or 3 actions. You can spend those actions on the same turn or split them across consecutive turns. If you are interrupted (stunned, knocked unconscious, forced to move) before completing all required actions, the ability fails and any spent actions are lost. Mana spent on a failed spell or Technique is not refunded.

### Reactions

You get **1 reaction** per round. Your reaction refreshes at the **start of your turn**, not the end.

A reaction is a response to something another creature does. You can use your reaction to:

- Make an **opportunity attack** when an enemy leaves your melee reach.
- **Parry** an incoming attack if you have a parry ability.
- **Counterspell** a spell as it is being cast, if you have a counterspell ability.
- Trigger any other ability, skill, or equipment effect that says "as a reaction."

Reactions can interrupt another creature's action. If a reaction deals damage that drops the acting creature to 0 HP, the interrupted action does not complete.

If you have no reaction available, you cannot respond to triggers until your next turn.

### Movement

Each Move action lets you travel up to your **movement speed** in feet. You can split your movement across multiple Move actions in a turn: Move 10 feet, Attack, Move 15 feet. Conditions that reduce your speed (Frozen, Shocked) apply to each Move action.

**Opportunity attacks.** A creature's **melee reach** is 5 feet unless a weapon or ability says otherwise (Reach-tagged weapons extend this). When you move out of a hostile creature's melee reach, that creature can spend its reaction to make a single melee attack against you. This happens before you leave the threatened space. If you do not leave a creature's reach, no opportunity attack triggers.



### Resolving an Attack

When you attack, follow these steps:

1. **Choose your attack.** Pick a weapon or a spell.
2. **Determine your modifier.** Physical and martial attacks (swords, fists, bows, firearms) use **Body**. Spells use **Magic**.
3. **Roll the Combat Roll.** Roll `2d10 + Body` (physical) or `2d10 + Magic` (spell).
4. **Compare to the target's AC.** Physical attacks compare against **Physical AC**. Spells compare against **Magical AC**. If your result meets or beats the AC, the attack hits. If it falls short, it misses.

{{footnote Combat}}
{{pageNumber,auto}}

\page

5. **Roll damage.** Roll your weapon's damage dice + Body, or your spell's damage dice + Magic. The target's **DR** (Physical DR for weapon hits, Magic DR for spell hits) subtracts from the total. The target takes the remainder as damage. Damage cannot go below 0.
6. **Apply tags and stacks.** If the attack carries a tag that inflicts a condition (Burn, Chilled, Bleed, Force, etc.), apply 1 stack of that condition to the target. Stacks follow the rules in Conditions, Injuries, and Death.
7. **Check for 0 HP.** If the target drops to 0 HP, they are incapacitated (see Conditions, Injuries, and Death: Dropping to 0 HP).

{{note
**Example:** You swing a greathammer at an enemy wearing Light armor (Physical DR 1, Body +2, Physical AC 3). Your Body is +4. You roll 2d10: 5 + 9 = 14, plus 4 = 18. That beats AC 3. You roll damage: 1d8 + 4 = 11. The enemy's Physical DR 1 absorbs 1. They take 10 damage. Your greathammer carries the Force tag, so the enemy gains 1 Force stack.
}}

### Tags in Combat

**Tags** are mechanical labels attached to weapons, spells, terrain, potions, and creature abilities. When an attack lands, its tags determine what conditions apply. A sword tagged with Bleed applies a Bleed stack on hit. A fire spell tagged with Burn applies a Burn stack on hit. Terrain tagged with Acid applies an Acid stack when a creature enters or starts its turn there.

Tags are system-wide. The same Burn stack works the same way whether it came from a spell, a weapon trait, or a pool of lava. See Conditions, Injuries, and Death for full stack rules and condition effects.

**Stack escalation.** Some conditions escalate when they reach 5 stacks. Five Acid stacks trigger Corroded (-2 DR). Five Bleed stacks trigger Shredded. Five Force stacks trigger an escalated condition (see Conditions, Injuries, and Death). Your weapon and spell choices determine which escalation paths you threaten.

## Worked Example

Three combatants: **Jake** (martial, Body +4, greatsword 1d8+Body, Medium armor), **Chris** (hybrid, Body +2, Magic +3, shortsword 1d6+Body, Light armor), and a **Bandit Sergeant** (Enemy rank, Body +3, Magic -1, war hammer 1d8+Body [Force], Medium armor, 100 HP).

**Initiative.** Jake rolls d10: 8, plus Body +4 = 12. Chris rolls d10: 6, plus Magic +3 = 9. Bandit Sergeant rolls d10: 7, plus Body +3 = 10. Turn order: Jake (12), Bandit Sergeant (10), Chris (9).

#### Jake's turn (3 actions)
- Action 1: Move. Jake closes 25 feet to reach the Bandit Sergeant.
- Action 2: Attack with greatsword. Roll `2d10 + 4` = 7 + 6 + 4 = **17**. Bandit's Physical AC = Physical DR 3 + Body 3 = **6**. Hit. Damage: `1d8 + 4` = 5 + 4 = **9**, minus DR 3 = **6 damage**. Bandit is at 94 HP.
- Action 3: Attack again. Roll `2d10 + 4` = 3 + 8 + 4 = **15**. Beats AC 6. Damage: `1d8 + 4` = 7 + 4 = **11**, minus 3 = **8 damage**. Bandit at 86 HP.

#### Bandit Sergeant's turn 
- Action 1: Attack Jake with war hammer (Force tag). Roll `2d10 + 3` = 9 + 4 + 3 = **16**. Jake's Physical AC = DR 3 + Body 4 = **7**. Hit. Damage: `1d8 + 3` = 6 + 3 = **9**, minus 3 DR = **6 damage**. Jake gains 1 Force stack.
- Action 2: Attack again. Roll `2d10 + 3` = 2 + 5 + 3 = **10**. Beats AC 7. Damage: `1d8 + 3` = 3 + 3 = **6**, minus 3 = **3 damage**. Jake gains a second Force stack (now 2 Force, dealing 2 damage at start of his next turn).
- Action 3: Move. The Bandit steps 10 feet to put Jake between himself and Chris.

#### Chris's turn (3 actions)
- Action 1: Move 25 feet to reach the Bandit. This takes her through Jake's space (allies can pass through each other's spaces).
- Action 2: Attack with shortsword. Roll `2d10 + 2` = 8 + 7 + 2 = **17**. Beats Bandit's Physical AC of 6. Damage: `1d6 + 2` = 4 + 2 = **6**, minus 3 DR = **3 damage**. Bandit at 83 HP.
- Action 3: Cast a frost bolt (spell, Chilled tag). Roll `2d10 + 3` (Magic) = 6 + 5 + 3 = **14**. Bandit's Magical AC = Magic DR 1 + Magic -1 = **0**. Hit. Spell damage: `1d6 + 1d8 + 3` = 3 + 6 + 3 = **12**, minus Magic DR 1 = **11 damage**. Bandit at 72 HP and gains 1 Chilled stack.

#### End of Round
 Turn order resets to the top. Jake takes 2 damage from his 2 Force stacks at the start of his next turn. The Bandit's Chilled stack will deal 1 damage at the start of the Bandit's next turn and lasts 2 rounds unless reapplied.

{{footnote Combat}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 9: CONDITIONS, INJURIES, AND DEATH -->
{{wide 

# Conditions, Injuries, and Death

This chapter explains how lasting effects work in Solus: what causes them, how they build, what happens when they get worse, and how to get rid of them. It also covers what happens when a character drops to 0 HP.

Every rule in this chapter applies the same way regardless of where the effect comes from. A Burn stack from a fire spell works the same as a Burn stack from a flaming sword or a pool of lava. The source does not change the rules.

## Tracking Conditions at the Table

The stack and condition system is the densest part of Solus. It has more moving parts than any other chapter. Read it once to understand the logic. You do not need to memorize it. The system caps at 5 stacks per type, and nothing goes past an escalated condition. Once you reach 5 stacks and trigger the escalation, that is the worst it gets. The math stays bounded.

At the table, you have three options for tracking stacks:

- **Paper character sheets.** The Solus character sheet includes a row of five boxes for each stack type. Fill in a box when you gain a stack. Erase it when the stack expires or is removed. Write the round number next to each box so you know when it decays. This works, but it requires attention from every player.

- **Condition Tracker app.** A dedicated Solus Condition Tracker (planned for iOS and Android) handles stack counts, decay timers, escalation triggers, elemental interactions, and damage calculations automatically. If your group plays at a physical table and wants to offload the bookkeeping, this is the recommended tool.

- **Virtual tabletop.** Solus has native support for FoundryVTT. The Foundry module tracks all tag applications, stack counts, decay rounds, escalation thresholds, opposing stack cancellation, and condition damage per round. The GM and players see stack states update in real time. If your group plays online, this is the smoothest way to run the system.

You do not need digital tools to play Solus. The paper sheet works. But the condition system rewards groups that use tracking tools, because those tools let you focus on tactics.

}}

{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}

\page

## Tags and Stacks: The Two-Part System

Solus tracks lasting effects through two linked pieces: **tags** and **stacks**.

A **tag** is a label on an attack, spell, weapon trait, terrain hazard, potion, or creature ability. Tags describe what type of effect the source carries. Common tags include Burn, Bleed, Acid, Chilled, Volt, and Force.

A **stack** is what a tag creates when it lands on a target. Each time a tagged effect hits you, it adds 1 stack of that type to you. Stacks are counters. They build up, deal damage over time, and trigger worse effects if they reach a threshold.

Tags are on the source. Stacks are on the target.

### How Stacks Work

Every stack follows the same four-beat cycle: **Hit → Stack → Hurt → Fade.**

1. **Hit.** A tagged attack lands. The target gains 1 stack of that tag's type.
2. **Stack.** The stack count goes up. Damage dealt by stacks equals the current count.
3. **Hurt.** Stack damage hits twice: once on application, once at the start of the target's next turn.
4. **Fade.** Each stack decays after 2 rounds. Purging, spending, and elemental counters can remove stacks faster. At 5 stacks, an escalated condition triggers.

##### Stack Rules
| Rule | Detail |
|:---|:---|
| Stacks per hit | 1 per hit. Always. |
| One tag per hit (weapons) | Weapon attacks apply one tag per hit. Choose if the weapon has multiple. |
| Multi-tag (magic) | Spells can apply multiple stack types in a single hit if built to do so. |
| Damage per tick | Equal to the current stack count. 3 stacks = 3 damage. |
| Damage timing | On application (immediate) and at the start of the target's next turn. |
| Cap | 5 stacks per type. No exceptions. |
| Independence | Different types stack separately. 3 Burn + 2 Bleed = both tracked, both deal damage. |
| DR | Elemental stacks (Burn, Chilled, Volt, Acid): reduced by Magic DR. Physical stacks (Bleed, Force): reduced by Physical DR. DR reduces stack damage at T1 but does **not** reduce damage from T2 escalated conditions. DR does not prevent stacks from applying or escalating. |

| **Removal** | |
|:---|:---|
| Decay | Each stack type has one shared timer that lasts 2 rounds. A new hit of the same type resets the timer. When the timer expires, all stacks of that type are removed at once. |
| Healing Magic | Healing spells with the appropriate tags can remove stacks. This is the primary way to clear stacks during combat. |
| Counter | Opposing elements cancel 1:1 (Burn ↔ Chilled). See Condition Profiles for each type's counter. Unless a tag says otherwise, countering and healing magic are the only removal methods. |
| Spend | Some abilities consume your stacks to power an effect. Spent stacks do not count toward escalation. |
| Purge (Weapon Trait) | Purge is a weapon-specific trait, not a general action. Only weapons and skills with the Purge trait can remove stacks this way. Full purge (2 actions): remove all elemental stacks from yourself. Partial purge (1 action): remove 1 stack per elemental type. |

{{note
**Example: Tracking stacks across two rounds.**

Round 1, your turn: You hit an enemy with a Bleed-tagged sword. The enemy gains 1 Bleed stack and takes 1 bleed damage. A 2-round Bleed timer starts.

Round 1, enemy's turn: At the start of the enemy's turn, the 1 Bleed stack deals 1 damage.

Round 2, your turn: You hit the enemy again. The enemy gains a second Bleed stack (now at 2). The enemy takes 2 bleed damage. The Bleed timer resets to 2 rounds.

Round 2, enemy's turn: At the start of the enemy's turn, 2 Bleed stacks deal 2 damage.

Round 4, enemy's turn: The Bleed timer expires (2 full rounds since the last Bleed hit). All Bleed stacks are removed.
}}


### Escalation

When a stack type reaches 5, it triggers an **escalated condition** (also called a **Tier 2 condition** or **T2 condition**). This is a stronger, named effect on top of the ongoing stack damage. For the purposes of the playtest, escalation is the ceiling. The stacks stay at 5 and the condition persists until the stacks decay or are removed. T3 and T4 condition effects may be added in a future version.

##### Escalated Conditions at a Glance
| Stack Type | At 5: Escalated Condition | Short Effect |
|:---|:---|:---|
| Burn | Ignited | Burn damage each turn. No healing. |
| Chilled | Frozen | Movement 0. Costs 1 action to break free. |
| Volt | Shocked | Disadvantage on all actions. Half movement. |
| Acid | Corroded | DR reduced by 2. Corrosion countdown on flesh. |
| Poison | Venomous | Lose 1 action. Self-accelerating stacks. |
| Bleed | Shredded | Physical DR reduced by 2. Bleed stacks do not decay. |
| Force | Staggered | Movement halved. Physical attacks deal +1d6 bonus force damage. |
| Necrotic | Necroptosis | Lethal cascade. Target tears itself apart. |
| Decay | Wither | Structural breakdown. Applies Vulnerable. |
| Radiant | Purge | Removes one active biological condition. |

{{note
**Example: Burn to Ignited.** You get hit by a fire spell three rounds in a row. Round 1: 1 Burn stack, 1 fire damage. Round 2: 2 Burn stacks, 2 fire damage. Round 3: 3 stacks, 3 damage. Two more hits and you reach 5 Burn stacks. At 5, you become Ignited: you take Burn damage every turn and cannot receive healing. Your ally hits you with an ice spell (Chilled tag). The Chilled cancels 1 Burn stack, dropping you to 4. Ignited ends. Another ice hit drops you to 3. The fire is coming under control.
}}

{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}

\page

## Condition Profiles

Each profile covers one tag type: what it does on hit, what happens as stacks build, what the T2 condition does at 5, and how to counter or remove it.

#### Fire / Burn

| | |
|:---|:---|
| **Tag** | Fire, Burn |
| **Stack** | Burn. Deals fire damage equal to stack count. |
| **At 5: Ignited** | Burn damage each turn. Cannot receive healing from any source. |
| **Countered by** | Chilled (cancels 1:1). Wet extinguishes fire on terrain and objects. Air/Wind extinguishes open flames. |
| **DR type** | Magic DR reduces Burn stack damage. |

Burn and Chilled are direct opposites. When you would gain a Burn stack, it removes 1 Chilled stack instead (and vice versa). If there is no opposing stack to cancel, the new stack applies normally.

#### Ice / Chilled

| | |
|:---|:---|
| **Tag** | Ice, Chilled |
| **Stack** | Chilled. Deals cold damage equal to stack count. |
| **At 5: Frozen** | Movement becomes 0. Must spend 1 action to break free. |
| **Countered by** | Burn (cancels 1:1). |
| **DR type** | Magic DR reduces Chilled stack damage. |

#### Lightning / Volt

| | |
|:---|:---|
| **Tag** | Electric, Volt |
| **Stack** | Volt. Deals electric damage equal to stack count. |
| **At 5: Shocked** | Disadvantage on all actions. Movement speed halved. |
| **Combo: Shocked + Wet = Stunned** | If a Shocked creature is also Wet, Shocked upgrades to Stunned: disadvantage on all actions and loss of reaction. |
| **Countered by** | Decay (2 rounds) or purging. No direct elemental opposite. |
| **DR type** | Magic DR reduces Volt stack damage. |

Lightning attackers can set up the Stunned combo by applying Wet first (water spell, rain, water terrain) and then building Volt stacks.

{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}


#### Acid

| | |
|:---|:---|
| **Tag** | Acid |
| **Stack** | Acid. Deals acid damage equal to stack count. |
| **At 5: Corroded** | DR reduced by 2. Acid burns through terrain at 5 ft. per round. Direct contact with exposed flesh starts a 3-round corrosion countdown; if not removed, you lose the limb or suffer permanent impairment. |
| **Countered by** | Apply Chilled or Burn (costs 2 actions). Removes Acid stacks and stops corrosion. You take damage from both the Acid and the applied element that round. |
| **DR type** | Magic DR reduces Acid stack damage. |

#### Poison

| | |
|:---|:---|
| **Tag** | Poison |
| **Stack** | Poisoned. Deals poison damage equal to stack count. |
| **At escalation: Venomous** | You lose 1 action. Stacks increase by 1 per round, accelerating to +5 per round at 10 stacks. At 15 stacks, lose a second action. At 20, lose your third. At 35, permanently lose 1 action. |
| **Countered by** | Radiant removes Venomous at 10 or fewer stacks. Purge removes Venomous at 15+. Purge cannot restore an action permanently lost at 35. |
| **DR type** | Magic DR reduces Poison stack damage. |

Poison at T1 has no special effect beyond dealing stack damage. It serves as a primer for the Venomous escalation.


#### Bleed

| | |
|:---|:---|
| **Tag** | Bleed (condition stack, applied by weapon traits and Order/Smite spell tags: [Strike] at T1, [Judgement] at T2) |
| **Stack** | Bleed. Deals physical bleed damage equal to stack count. |
| **At 5: Shredded** | Physical DR reduced by 2. Bleed stacks do not decay while Shredded persists. Healing or purging ends Shredded and allows stacks to decay normally. |
| **Countered by** | Decay (2 rounds) or purging. No direct elemental opposite. |
| **DR type** | Physical DR reduces Bleed stack damage. |

Shredded is the physical mirror of Corroded. Corroded strips Magic DR and eats through material. Shredded strips Physical DR and keeps wounds open. If both are active, the target loses DR on both fronts.

#### Force

| | |
|:---|:---|
| **Tag** | Force (condition stack, applied by weapon traits and Force spell tags: [Impact]/[Blast] at T1, [Slam]/[Repulse] at T2) |
| **Stack** | Force. Deals physical force damage equal to stack count. |
| **At 5: Staggered** | Movement halved. Physical attacks against you deal +1d6 bonus force damage while you remain at 5+ Force stacks. |
| **Countered by** | Decay, purging, or spending. Some weapon traits let you spend Force stacks for bonus damage or special effects before reaching 5. Spent stacks are removed immediately. |
| **DR type** | Physical DR reduces Force stack damage. |

Staggered represents accumulated kinetic trauma. Your body can no longer absorb blunt impacts. The +1d6 bonus applies to melee and ranged physical attacks, not spells. Spending stacks below 5 ends Staggered immediately.

{{note
**Example:** Your unarmed fighting style builds Force stacks on yourself. You have 4. Your next punch lets you spend all 4 for +4 bonus damage. Your count drops to 0, and you avoid triggering Staggered.
}}


#### Reap (Weapon-Specific)

| | |
|:---|:---|
| **Source** | Scythe weapon trait |
| **Stack** | Reap. Unique stack type with its own rules. |
| **Countered by** | Any healing removes all Reap stacks. If the attacker misses the target for 2 consecutive rounds, Reap stacks are removed. |

#### Life: Restoration

| | |
|:---|:---|
| **Tag** | Life, Restoration |
| **T1: Restore** | Repairs recent damage to a living target. Restores lost health. Stabilizes injuries that have not yet become permanent. |
| **T2: Regenerate** | Restores lost body parts and reverses severe physical trauma. Provides ongoing recovery while active. |
| **Countered by** | Necrosis (Death domain). |
| **DR type** | Magic DR reduces Restoration stack damage when used offensively against undead. |

#### Life: Resurrect

| | |
|:---|:---|
| **Tag** | Life, Resurrect |
| **T1: Rouse** | Returns a recently deceased target to life. The body must be intact and death must have occurred within a limited timeframe. |
| **T2: Revive** | Returns a long-dead target to life by reuniting body and soul, even after extended separation or decay. Subject to extreme cost or risk. |

Resurrect tags have no stack escalation. They produce immediate effects.

#### Life: Radiance

| | |
|:---|:---|
| **Tag** | Life, Radiance |
| **T1: Radiant** | Emits concentrated light-infused energy that damages or disrupts organic or corrupted targets. Applies Radiant stacks. Removes Venomous at 10 or fewer stacks. |
| **T2: Purge** | Removes or suppresses one active biological condition or effect within a target or area. Covers Elemental, Mind, and Life domains. The only way to remove Venomous at 15+. Cannot restore an action permanently lost at 35. |
| **Countered by** | Necrosis (Death domain). |
| **DR type** | Magic DR reduces Radiant stack damage. |

#### Life: Light

| | |
|:---|:---|
| **Tag** | Life, Light |
| **T1: Illuminate** | Creates light within a defined area or on a target. Removes darkness and enables normal visual perception. |
| **T2: Blind** | Removes a target's ability to perceive visually while the effect persists. |

Light tags produce binary conditions, not scaling stack damage.

{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}

\page

#### Death: Necrotic

| | |
|:---|:---|
| **Tag** | Death, Necrotic |
| **T1: Necrosis** | Dark energy destabilizes living material and siphons vitality from a target. Applies Necrotic stacks. |
| **T2: Necroptosis** | A lethal internal cascade that forces the body to tear itself apart, fully absorbing the vitality of the target. |
| **Countered by** | Radiant (Life domain). |
| **DR type** | Magic DR reduces Necrotic stack damage. |

#### Death: Death

| | |
|:---|:---|
| **Tag** | Death |
| **T1: Pyroptosis** | The target detonates with necrotic energy in a 5 ft. radius. Creatures in the radius gain Necrotic stacks. |
| **T2: Apoptosis** | A terminal effect. The target dies immediately. |

Death tags produce immediate effects. Pyroptosis has an area component; Apoptosis has no counter once applied.

#### Death: Undeath

| | |
|:---|:---|
| **Tag** | Death, Undeath |
| **T1: Reanimate** | Restores temporary motion to lifeless matter. The target gains no will or awareness. |
| **T2: Vivify** | Forces the tethering of a spirit or essence to a vessel beyond natural death. |

Undeath tags produce immediate effects, not scaling stacks.

#### Death: Rot

| | |
|:---|:---|
| **Tag** | Death, Rot |
| **T1: Decay** | Slow weakening and deterioration of vitality or structure. Applies the Weaken condition. |
| **T2: Wither** | Final failure of integrity resulting in structural or biological breakdown. Applies the Vulnerable condition. |
| **Countered by** | Restore or Regenerate (Life domain). |
| **DR type** | Magic DR reduces Decay stack damage. |



{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}

\page

### Tags on Terrain and Objects

When a spell or effect applies a tag to terrain (a fire patch, an acid pool, a frozen floor), the tagged area persists for the spell's duration. If no duration is specified, T1 effects last 2 rounds and T2 effects last 4 rounds.

A creature that enters tagged terrain or starts its turn there gains 1 stack of the linked type. The same stack rules apply: damage on application, damage at start of turn, 2-round decay, cap at 5.

### Other Tag Conditions

Every effect in Solus works through tags and stacks. The conditions below follow the same system. They are applied by tags carried on spells, abilities, or hazards. The difference is that these tags produce binary conditions instead of scaling numeric damage. A creature either has the condition or does not. Unless a tag's description says otherwise, assume it applies through the stack framework.

##### Tag-Applied Conditions
| Condition | Effect |
|:---|:---|
| Anchored | You cannot move from your current position. You can still take other actions. |
| Blind | You lose visual perception. Attacks against unseen targets are at disadvantage. |
| Charmed | You cannot target the charmer with hostile actions. The charmer gains advantage on social checks against you. |
| Confused | Start of turn, roll: 1-2 move randomly, 3-4 attack nearest creature, 5-6 act normally. No reactions while Confused. |
| Crush | Maintained pressure on a Restrained target. Applies 1 Force stack per round while active. |
| Dominated | The controller chooses your actions each round. You retain awareness but cannot refuse. |
| Drowsy | Perception dulled. You lose your reaction. |
| Frightened | You cannot willingly move closer to the fear source. Disadvantage on attacks and checks against the source. |
| Incapacitated | You cannot take actions, move, or use reactions. You remain on the battlefield. (See Dropping to 0 HP.) |
| Restrained | Your movement is physically limited. You cannot move freely. Some abilities require the target to be Restrained. |
| Shredded | Applied by Bleed at 5 stacks. Physical DR reduced by 2. Bleed stacks do not decay while Shredded persists. |
| Staggered | Applied by Force at 5 stacks. Movement halved. Physical attacks deal +1d6 bonus force damage. |
| Stunned | Disadvantage on all actions. You lose your reaction for the round. (Usually from Shocked + Wet.) |
| Unconscious | You are unresponsive and cannot act until awakened or the effect ends. |
| Weaken | Slow deterioration of vitality or structure. Applied by Decay (Death: Rot). Reduces damage dealt by 1. |
| Vulnerable | Applied by Wither (Death: Rot T2). Incoming damage increased by 2. |
| Wet | No damage. Extinguishes fire on terrain and objects. Enables the Shocked → Stunned upgrade. |
| Drown | Applied by T2 Water spells. You lose your reaction. You must spend 1 action each turn to avoid suffocating. Breath duration depends on Body. |

### Dropping to 0 HP

When your HP reaches 0, you enter the **dying state**. Your **Atraxia Pool** becomes your countdown. When the pool hits 0, you die.

The pool does not reset between encounters or sessions. Whatever your pool reads at the end of a dying incident is your starting value for the next one. The pool tracks your character's total remaining tolerance for near-death across their entire career.

#### While Dying

You remain conscious and can act. The following penalties apply:

- All attack rolls are made with **disadvantage**.
- Movement speed is **halved**.
- Mana regeneration is **halved** (rounded down).

#### Pool Drain on Your Turn

You still get 3 actions per turn. Each action drains your Atraxia Pool:

- Each action you **use** (attack, move, cast, interact): pool **-2**
- Each action you **skip** (do nothing): pool **-1**

You can mix used and skipped actions in any order. A turn where you do nothing costs 3 from the pool. A turn where you use all 3 actions costs 6.

{{note
**Example:** First time dying. Your Atraxia Pool is 45.

Your turn: Action 1, you move behind cover (pool -2 = 43). Action 2, you do nothing (-1 = 42). Action 3, you do nothing (-1 = 41).

You end the turn at 41. If an ally heals you, your pool stays at 41. Next time you hit 0 HP, you resume from 41.
}}

#### Pool Drain from Enemy Attacks

When an enemy hits you while you are dying, the pool drops based on the attack's action cost:

- 1-action attack: pool **-1**
- 2-action attack: pool **-3**
- 3-action attack: pool **-5**

If the pool reaches 0 from any source, you die immediately.

#### Why You Stay Conscious

Dying characters can still act because combat does not pause for you. You choose whether to spend pool faster by acting or conserve it by doing nothing. That choice matters because every point of pool you spend is gone permanently. An aggressive turn while dying costs twice as much pool as a passive one.

Your allies also have a choice: heal you now or finish the fight first. The longer you stay in the dying state, the more pool and Atraxia modifier you lose.

#### Leaving the Dying State

If you receive healing that brings you to **1 HP or more**, you leave the dying state. Leaving the dying state carries three consequences:

- **Atraxia modifier loss.** Your Atraxia modifier permanently drops by 1 for each round you spent dying. Minimum loss is 1, even if you are healed on the same round you go down.
- **Short-term injury.** Roll on the Short-Term Injury Table.
- **Pool carries forward.** Whatever your Atraxia Pool reads when you leave dying is your new starting value for all future dying incidents.

#### Long-Term Impact

Each dying incident costs pool (the immediate countdown) and Atraxia modifier (long-term perception shift). The modifier loss means your character perceives more of the world's hidden layers after each brush with death. Because the modifier also affects future Atraxia Pool rolls if restoration mechanics allow it, repeated dying makes a character both more aware and more fragile.

{{note
**Example:** Your pool was at 41. You drop to 0 HP and spend 2 rounds dying. Between your actions and enemy hits, your pool drops to 29. An ally heals you.

Your Atraxia modifier permanently drops by 2 (one per round in dying). You roll on the Short-Term Injury Table. Next time you hit 0 HP, your pool starts at 29 and your modifier is 2 points lower than at character creation.
}}

{{descriptive
TODO: Short-Term Injury Table needs to be created. TODO: Jacob wants a Shadowdark-inspired survival check where the player can argue which attribute applies. The check mechanic and DC need definition.
}}
<!-- CHAPTER 10: NPCs, ENEMIES, AND ENCOUNTERS -->

# NPCs, Enemies, and Encounters

Every NPC in Solus uses the same action economy, equipment, skills, and spells as player characters. An enemy swings a sword the same way you do, casts spells from the same framework, and takes 3 actions on its turn. The GM does not run NPCs from a separate system. The GM runs them from the same rules you use.

NPCs also have Atraxia Pools. Most commoners, merchants, and low-tier guards rolled theirs from small dice with modest modifiers. A shopkeeper in a quiet town might carry a pool of 8. A veteran city guard might sit around 20. Your player characters, by the time they've survived their first real fight, have already outlasted most people they'll meet on the street. This is not because Solus treats player characters as heroes by default. It is because the kind of person who walks into a dungeon, picks a fight with something that has claws, and walks back out is statistically unusual.

The differences between NPC tiers are stat modifiers, HP, mana pools, and Atraxia Pools. Each tier supports martial, caster, and hybrid variants. An NPC's mana pool and regeneration rate depend on whether the GM builds them as a Martial (30 max, 3 regen), Caster (100 max, 15 regen), or Hybrid (70 max, 10 regen), the same as player backgrounds. Most common NPCs use the Martial pool.

### NPC Tiers

##### NPC Resources by Tier
| Tier | HP | Max Mana / Regen | Atraxia Pool | Example Armor |
|:---|:---:|:---|:---:|:---|
| Minion | 1-5 | 30 / 3 | 4-8 | None (Phys DR 0, Magic DR 0) |
| Regular | 75 | 30 / 3 | 10-20 | Cloth (Phys DR 0, Magic DR 4) or Light |
| Enemy / Ally | 100 | 100 / 15 | 30-50 | Medium (Phys DR 3, Magic DR 1) |
| Mini Boss | 120 | 100 / 15 | 50-70 | Heavy (Phys DR 4, Magic DR 0) |
| Boss | 175 | 100 / 20 | 80+ | Enchanted (Phys DR 3, Magic DR 3) |

##### NPC Attributes by Tier
| Tier | Body | Mind | Social | Magic | Atraxia |
|:---|:---:|:---:|:---:|:---:|:---:|
| Minion | +0 | +0 | +0 | +0 | +0 |
| Regular | +1 | +1 | +1 | +1 | +1 |
| Enemy / Ally | +4 | +1 | +3 | -3 | +0 |
| Mini Boss | +5 | +4 | -3 | +0 | -2 |
| Boss | +5 | +3 | +0 | +5 | -5 |

The attribute spreads for Enemy through Boss tiers are **examples**. Rearrange them to fit the NPC you are building. A scholarly Enemy might swap Body and Mind. A charismatic Mini Boss might lead with Social. The point budget stays the same; the placement should represent the character.

\column

### How Each Tier Works

**Minions** are fodder. They have +0 in every stat, 1-5 HP, and access to the same equipment and spells you do. Their low modifiers mean they miss more often, but they swing the same weapons and cast the same spells. One Minion is a speed bump. Six of them eat your actions, trigger your reactions, and crowd the battlefield until the math catches up with you.

**Regular NPCs** represent ordinary people: shopkeepers, townsfolk, low-ranked guards. They are sturdier than Minions but cannot match a player character in a fight.

**Enemy and Ally NPCs** are the standard challenge tier. They are **on par** with player characters. Same action economy, same equipment access, same spell system. An Enemy can kill you as fast as you can kill it. An Ally fights beside you at the same power level. This is the tier most combat encounters are built around.

**Mini Bosses** outclass a single player character. Higher HP, stronger stats, better equipment. A Mini Boss should require coordination to bring down.

**Bosses** break the standard point-buy rules. A Boss receives one extra +5 attribute beyond what the normal budget allows. That creates a stat line impossible for player characters to replicate. Bosses demand planning, resource management, and the full group's attention.

### Allies and Enemies in the World

NPCs are not only combat pieces. An NPC can create a problem (a corrupt magistrate closes the trade route), sustain a problem (a necromancer keeps raising the dead), appear as a consequence (the bandit you spared returns with reinforcements), or deliver a reward (the merchant pays for the rescued caravan). Allies and enemies follow the same framework. Build them from the tier table, give them a goal, and place them in the scene.

{{descriptive
**TODO:** Jacob, need the encounter-building procedure, XP awards by enemy tier, and guidance for mixing tiers in one encounter.
}}

{{footnote NPCs, Enemies, and Encounters}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 11: ADVANCEMENT AND BETWEEN-SESSION PLAY -->

# Advancement and Between-Session Play

Solus has no character levels. Your character grows by earning **XP** and spending it on skills.

### Earning XP

You earn XP from every type of encounter:

- **Combat:** Each enemy tier awards a set amount of XP when defeated.
- **Exploration:** Engaging with an exploration encounter awards XP, whether you succeed or fail.
- **Social:** Conversation and negotiation encounters award XP for participation.

You do not need to win to earn XP. You need to engage.

### Spending XP

You spend XP **between sessions**. XP is a shared budget across three investment tracks:

- **Proficiency ranks.** Buy new proficiencies or raise existing ones. Each proficiency advances from Rank 1 to Rank 10. Costs rise exponentially.
- **Weapon Mastery ranks.** Buy Mastery Ranks in individual weapons (Rank 1 to 5). Higher ranks unlock more Techniques and Augment Slots.
- **Augments.** Purchase Universal and Category Augments to socket into your prepared Techniques.

Spreading XP gives breadth. Focusing XP gives depth. A character with three weapons at Mastery 2 plays differently from one weapon at Mastery 5.

{{descriptive
**TODO:** Need the full XP cost table (proficiency acquisition + rank 1-10 costs, Weapon Mastery rank 1-5 costs, Augment purchase costs) and XP awards per enemy tier, exploration, and social encounters.
}}

\column

### Between Sessions

Between sessions, you can update any part of your character that the rules mark as changeable (see Character Creation, Step 9). With GM confirmation, you can:

- Swap active proficiencies.
- Change prepared Techniques and re-socket Augments (also available on short/long rests).
- Change weapons and armor from your inventory.
- Spend or gain money and resources.
- Record new languages your character has learned.

Proficiency swaps are also available on **long rests** during a session, so players can adapt tactics between encounters. Technique and Augment changes are available on both **short and long rests**.

{{footnote Advancement and Between Sessions}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 12: RUNNING THE GAME -->

# Running the Game

This chapter is for the GM. It covers how to set difficulty, interpret roll results, and manage the boundary between player and GM control.

### Setting DCs

When a player attempts a Proficiency Check, you set the **Difficulty Class (DC)**. Start with a baseline that reflects the task's inherent difficulty, then adjust it based on the character's circumstances.

##### Difficulty Classes
| Difficulty | Suggested DC |
|:---|:---:|
| Trivial | 5 |
| Easy | 8 |
| Moderate | 12 |
| Hard | 16 |
| Very Hard | 20 |
| Near Impossible | 24 |

Raise the DC if the character lacks relevant context: they have never seen this kind of lock, they are working in the dark, or they are doing it under time pressure. Lower the DC if the character has specific training, preparation, or tools for this task. Most DC adjustments fall between -5 and +5.

These numbers are calibrated to a 2d10 + modifier system where modifiers range from -5 to +10 (two attributes combined). A Moderate DC of 12 gives a character with a +5 modifier about a 70% chance of success. A Hard DC of 16 with the same modifier drops to about 40%. The curve rewards investment without making low-modifier attempts hopeless.

A roll is only needed when the outcome is uncertain. If the task is trivial for the character, describe the success. If the task is impossible, describe the failure.

### The Degree of 5

After a Proficiency Check, read the result using the **Degree of 5** scale. The gap between the result and the DC determines how much the outcome swings beyond a basic success or failure.

##### Degree of 5 Scale
| Gap | Outcome |
|:---|:---|
| Beat DC by 10+ | Strong success with a major bonus. |
| Beat DC by 5-9 | Success with a minor bonus. |
| Within 4 of DC (above or below) | Baseline result. Success if met, failure if missed. No extra swing. |
| Miss DC by 5-9 | Failure with a minor setback. |
| Miss DC by 10+ | Failure with a major setback. |

The Degree of 5 applies to all Proficiency Checks. It does not apply to Combat Rolls (those are binary hit-or-miss against AC).

{{note
**Example:** A player rolls Speech to negotiate a ceasefire. DC 14. They roll 21. That beats the DC by 7, which earns a minor bonus. The enemy agrees to the ceasefire and offers a concession the player did not ask for. If the player had rolled 25, beating by 11, the enemy might surrender entirely.
}}

{{footnote Running the Game}}
{{pageNumber,auto}}


### Player Control vs. GM Control

Keep a clear boundary between what the player decides and what the system or GM decides.

**Players control:** skills, equipment, weapons, spells, money, resources, languages, and which actions to take on their turn.

**The GM or system controls:** status effects, environmental effects, lingering injuries, long-term curses, madness, reputation changes, and NPC behavior.

When a temporary effect changes a character's stats (a spell boosts health, a curse reduces Body), track it as a separate layer on the character sheet. Do not overwrite the character's permanent values. When the effect ends, the original values should be easy to restore.

### Building NPCs

Pick an NPC tier from the table in NPCs, Enemies, and Encounters. Choose martial, caster, or hybrid to set the NPC's background. Assign skills, equipment, and spells from the same lists players use. NPCs follow the same rules in combat, conversation, and exploration.

Use NPCs to drive the gameplay loop. Every NPC should have a goal: protect the gate, steal the shipment, negotiate the treaty, survive the night. The goal tells you how the NPC acts on its turn and what it does between encounters.

{{descriptive
**TODO:** Jacob, need encounter pacing guidance, DC calibration examples across tiers, and adjudication advice for edge cases.
}}

{{footnote Running the Game}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 13: REFERENCE AND PLAYTEST TOOLS -->

# Reference and Playtest Tools

This chapter collects reference tables and playtest materials. Use these at the table when you need to look something up without flipping through the full chapters.

### Core Rolls

| Roll Type | Formula | Compare Against |
|:---|:---|:---|
| Combat Roll (physical) | 2d10 + Body | Target's Physical AC |
| Combat Roll (spell) | 2d10 + Magic | Target's Magical AC |
| Proficiency Check | 2d10 + Proficiency Modifier | DC set by GM |
| Initiative | 1d10 + Body or Magic | Ranked highest to lowest |

### Armor Tiers

| Tier | Physical DR | Magic DR | Total DR |
|:---|:---:|:---:|:---:|
| Cloth | 0 | 4 | 4 |
| Light | 1 | 3 | 4 |
| Medium | 3 | 1 | 4 |
| Heavy | 4 | 0 | 4 |
| Enchanted | 3 | 3 | 6 |

**Physical AC** = Physical DR + Body. **Magical AC** = Magic DR + Magic. Max DR per type: 4. Max AC: 9.

### Backgrounds

| Background | HP | Max Mana | Mana Regen / Round |
|:---|:---:|:---:|:---:|
| Caster | 100 | 100 | 15 |
| Martial | 120 | 30 | 3 |
| Hybrid | 110 | 70 | 10 |

### Atraxia Pool by Campaign Tone

| Tone | Dice | Die Type |
|:---|:---:|:---:|
| Brutal | 4 | d4 |
| Gritty | 6 | d6 |
| Standard | 8 | d6 |
| Heroic | 10 | d8 |

Roll dice = Campaign Tone. Add Atraxia modifier to each die (minimum 1 per die). Total = starting Atraxia Pool.

### Degree of 5

| Gap | Outcome |
|:---|:---|
| Beat DC by 10+ | Strong success, major bonus |
| Beat DC by 5-9 | Success, minor bonus |
| Within 4 | Baseline result |
| Miss DC by 5-9 | Failure, minor setback |
| Miss DC by 10+ | Failure, major setback |

\column

### Actions

| Action | What It Does |
|:---|:---|
| Attack | Strike with a weapon. Roll a Combat Roll. |
| Cast a Spell | Cast a spell using 1+ actions. Multi-action spells can span turns. |
| Move | Move up to your full movement speed. |
| Drink a Potion | Consume a potion or similar item. |
| Interact | Open a door, draw a weapon, pick up an object, pull a lever. |
| Use a Proficiency | Attempt a Proficiency Check during combat. |

3 actions per turn. 1 reaction per round (refreshes at start of your turn).

### Attack Sequence

1. Choose your attack (weapon or spell).
2. Roll `2d10 + Body` (physical) or `2d10 + Magic` (spell).
3. Compare to Physical AC or Magical AC. Meet or beat = hit.
4. Roll damage dice + modifier. Subtract target's DR.
5. Apply tags. 1 stack per hit. Weapons: one tag per hit; spells can apply multiple. 
6. Check for 0 HP.

### NPC Tiers

| Tier | HP | Mana (Max / Regen) | Atraxia Pool |
|:---|:---:|:---|:---:|
| Minion | 1-5 | 30 / 3 | 4-8 |
| Regular | 75 | 30 / 3 | 10-20 |
| Enemy / Ally | 100 | 100 / 15 | 30-50 |
| Mini Boss | 120 | 100 / 15 | 50-70 |
| Boss | 175 | 100 / 20 | 80+ |

### Mana and Damage

| Benchmark | Mana |
|:---|:---:|
| Cheapest spell | 8 |
| Most expensive 1-action spell | 44 |
| Most expensive 3-action spell | 132 |

| Mana Cost | Damage Die |
|:---:|:---:|
| 1 | d6 |
| 2 | d8 |
| 3 | d10 |
| 5 | d12 |

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

### Stack Cycle: Hit → Stack → Hurt → Fade

| Beat | Rule |
|:---|:---|
| Hit | A tagged attack lands. Target gains 1 stack. |
| Stack | Stack count goes up. Damage = current count. |
| Hurt | Damage ticks twice: on application and at start of target's next turn. |
| Fade | One timer per stack type, resets on new hit. When the timer expires (2 rounds), all stacks of that type are removed. At 5 stacks, escalated condition triggers. |

### Escalated Conditions

| Stack Type | At 5 | Short Effect |
|:---|:---|:---|
| Burn | Ignited | Burn damage each turn. No healing. |
| Chilled | Frozen | Movement 0. Costs 1 action to break free. |
| Volt | Shocked | Disadvantage on all actions. Half movement. |
| Acid | Corroded | DR reduced by 2. Corrosion countdown. |
| Poison | Venomous | Lose 1 action. Self-accelerating stacks. |
| Bleed | Shredded | Physical DR reduced by 2. Bleed stacks do not decay. |
| Force | Staggered | Movement halved. Physical attacks deal +1d6 bonus force damage. |
| Necrotic | Necroptosis | Lethal cascade. Target tears itself apart. |
| Decay | Wither | Structural breakdown. Applies Vulnerable. |
| Radiant | Purge | Removes one active biological condition. |

### Stack Removal

| Method | Rule |
|:---|:---|
| Decay | One timer per stack type (2 rounds). Resets on new hit. All stacks removed when timer expires. |
| Healing Magic | Healing spells with appropriate tags remove stacks. Primary removal method. |
| Counter | Opposing elements cancel 1:1 (Burn ↔ Chilled). |
| Spend | Some abilities consume stacks to power effects. |
| Purge (weapon trait) | Full purge (2 actions): remove all elemental stacks. Partial (1 action): remove 1 per type. Weapon-specific. |

\column

### Affinity Multipliers

| Relationship | Mana Multiplier |
|:---|:---:|
| Main Affinity | ×1 |
| Sub Affinity | ×2 |
| Locked Affinity | Cannot cast |

### Character Creation Steps

1. Choose a race.
2. Distribute 5 attribute points (Body, Mind, Social, Magic, Atraxia).
3. Choose a background (Caster, Martial, Hybrid).
4. Choose and configure proficiencies.
5. Choose your initiative modifier (Body or Magic).
6. Choose your tag affinities (Main and Sub).
7. Choose secondary attributes.
8. Equip armor and weapons.
9. Record everything on your character sheet.

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

{{wide
### Spellcasting Quick Reference — By Mana Cost

Look up how much mana each option costs. Add parameters 2–10, then multiply by affinity (Main ×1, Sub ×2).

| Parameter | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 12 | 17 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Function** | Utility | Mvmt / Def | Offensive | — | — | — | — | — | — |
| **Range** | — | Self–25 ft. | 30–60 ft. | 65–120 ft. | 125–200 ft. | Sight | Global | — | — |
| **Size** | — | 5–15 ft. | 20–30 ft. | 35–60 ft. | — | — | — | — | — |
| **Shape** | — | Point | Standard | Freeform | — | — | — | — | — |
| **Duration** | — | Instant | 1 Round | 1 Minute | Hours | Permanent | — | — | — |
| **Target Count** | — | Single | Multi 2+ | AOE | — | — | — | — | — |
| **Accuracy** | — | Roll / Save | — | — | Auto-Hit | — | — | — | — |
| **Damage Die** | None | d6 | d8 | d10 | — | d12 | — | — | — |
| **Effect Tier** | — | — | — | T1 | — | — | T2 | T3 | T4 |

Standard shapes: Sphere, Cube, Line, Wall, Cylinder. Multi targets: +1 mana per extra target after 2 (max 4). Damage dice count = Range + Size + Target Count (1 each) + Attack Roll bonus die. Flat bonus = casting stat modifier.
}}

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

{{wide
### Spellcasting Quick Reference — By Action Cost

Look up how many actions each option costs. The highest action value among your parameters sets the spell's total action cost.

| Parameter | 1 Action | 2 Actions | 3 Actions | Sustained |
|:---|:---|:---|:---|:---|
| **Range** | Self–25 ft. (1) | 30–60 ft. (2) | 65–120 ft. (3) | 125–200 ft. (4), Sight (5), Global (6) |
| **Size** | 5–15 ft. (1) | 20–30 ft. (2) | 35–60 ft. (3) | — |
| **Shape** | Point (1) | Standard (2) | Freeform (3) | — |
| **Duration** | Instant (1) | 1 Round (2) | 1 Minute (3) | Hours (4), Permanent (5) |
| **Target Count** | Single (1) | Multi 2+ (2) | AOE (3) | — |
| **Accuracy** | Roll (1) / Save (1) | — | — | Auto-Hit (4) |
| **Effect Tier** | T1 (3) | T2 (6) | T3 (12) | T4 (17) |

Mana costs in parentheses. Sustained spells cost 3 actions to begin, 1 action per turn to maintain.

**Mana-only parameters** (no action cost): Function (Utility 0, Movement 1, Defensive 1, Offensive 2), Damage Die (d6 = 1, d8 = 2, d10 = 3, d12 = 5), Tag Affinity (Main ×1, Sub ×2).
}}

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

{{wide
## Sample Characters

Nine prebuilt characters covering all three backgrounds. The first seven are balanced builds. The last two are optimized: pushed to the system ceiling on one axis to show what min-maxing looks like. All use Standard Campaign Tone (8d6 Atraxia Pool dice). All weapon damage adds Body.
}}

#### Soridormi — Elf Caster

Elf · Speed 35 ft. · Medium · Caster
100 HP · 100 Mana · 15 Regen

**Body** -1 · **Mind** +2 · **Social** 0 · **Magic** +4 · **Atraxia** 0

**Affinities:** Main Elemental · Sub Temporal
**Armor:** Cloth (Phys DR 0 / Magic DR 4)
**Physical AC** -1 · **Magical AC** 8
**Weapons:** Dagger (1d4), Bow (1d8)

**Racial Traits:** Darkvision 60 ft., Keen Senses, Trance

*Glass cannon. Deep mana pool for sustained elemental bombardment. Strong magical AC, zero physical protection. Stay at range.*

\column

#### Vaelith Sunplume — Gnome Caster

Gnome · Speed 25 ft. · Small · Caster
100 HP · 100 Mana · 15 Regen

**Body** -2 · **Mind** +3 · **Social** 0 · **Magic** +3 · **Atraxia** +1

**Affinities:** Main Mind · Sub Corruption
**Armor:** Cloth (Phys DR 0 / Magic DR 4)
**Physical AC** -2 · **Magical AC** 7
**Weapons:** Dagger (1d4), Bomb Flask (1d6)

**Racial Traits:** Darkvision 60 ft., Small Frame, Arcane Cunning

*Controller. Mind spells for crowd control, Arcane Cunning resists hostile magic, Small Frame slips through enemy lines when positioning breaks down.*

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

#### Gelvas Grimegate — Dwarf Martial

Dwarf · Speed 25 ft. · Medium · Martial
120 HP · 30 Mana · 3 Regen

**Body** +4 · **Mind** 0 · **Social** -1 · **Magic** -1 · **Atraxia** +3

**Affinities:** Main Force · Sub Life
**Armor:** Heavy (Phys DR 4 / Magic DR 0)
**Physical AC** 8 · **Magical AC** -1
**Weapons:** Greathammer (1d8), Short Sword (1d6)

**Racial Traits:** Darkvision 60 ft., Hardy, Stone Steady

*Frontline tank. Physical AC 8 stops most weapon attacks. Hardy blocks Venomous escalation. Stone Steady ignores Heavy armor speed penalties. Vulnerable to all magic.*

\column

#### Terrorfist — Orc Martial

Orc · Speed 30 ft. · Medium · Martial
120 HP · 30 Mana · 3 Regen

**Body** +3 · **Mind** -1 · **Social** +1 · **Magic** -1 · **Atraxia** +3

**Affinities:** Main Force · Sub Death
**Armor:** Medium (Phys DR 3 / Magic DR 1)
**Physical AC** 6 · **Magical AC** 0
**Weapons:** Greatsword (1d8), Bow (1d8)

**Racial Traits:** Powerful Build, Aggressive

*Aggressive brawler. Closes distance fast with Aggressive, controls grapples through Powerful Build. High Atraxia Pool gives a wide death-cheating margin.*

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

#### Astalor Bloodsworn — Half-Breed Martial

Half-Breed (Elf/Orc) · Speed 30 ft. · Medium · Martial
120 HP · 30 Mana · 3 Regen

**Body** +3 · **Mind** +1 · **Social** 0 · **Magic** 0 · **Atraxia** +1

**Affinities:** Main Death · Sub Force
**Armor:** Medium (Phys DR 3 / Magic DR 1)
**Physical AC** 6 · **Magical AC** 1
**Weapons:** Curved Sword (1d8), Bow (1d8)

**Dual Heritage:** Keen Senses (Elf), Powerful Build (Orc)

*Disciplined skirmisher. Keen Senses spots threats at distance, Powerful Build wins contested grapples. Balanced attributes with no deep weaknesses.*

\column

#### Larisse Pembraux — Human Hybrid

Human · Speed 30 ft. · Medium · Hybrid
110 HP · 70 Mana · 10 Regen

**Body** +1 · **Mind** +1 · **Social** +3 · **Magic** +2 · **Atraxia** -2

**Affinities:** Main Mind · Sub Temporal
**Armor:** Light (Phys DR 1 / Magic DR 3)
**Physical AC** 2 · **Magical AC** 5
**Weapons:** Rapier (1d8), Dagger (1d4)

**Racial Traits:** Adaptable (11 proficiency slots), Determined

*Social infiltrator with spell support. High Social dominates conversation. Mind and Temporal spells control the battlefield. Adaptable gives an extra proficiency slot for broader coverage.*

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

#### Caydori Brighstar — Elf Hybrid

Elf · Speed 35 ft. · Medium · Hybrid
110 HP · 70 Mana · 10 Regen

**Body** +2 · **Mind** 0 · **Social** 0 · **Magic** +3 · **Atraxia** 0

**Affinities:** Main Life · Sub Elemental
**Armor:** Light (Phys DR 1 / Magic DR 3)
**Physical AC** 3 · **Magical AC** 6
**Weapons:** Short Sword (1d6), Bow (1d8)

**Racial Traits:** Darkvision 60 ft., Keen Senses, Trance

*Spellblade healer. Life affinity for restoration, Elemental sub for burst damage. Body +2 keeps weapon attacks viable alongside spellcasting. Trance shortens rest downtime.*

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

{{wide
### Optimized Builds

These two characters push a single axis to the system ceiling. They show the tradeoffs of going all-in on one role.
}}

#### Nyx — Gnome Caster (Optimized)

Gnome · Speed 25 ft. · Small · Caster
100 HP · 100 Mana · 15 Regen

**Body** -3 · **Mind** +1 · **Social** 0 · **Magic** +5 · **Atraxia** +2

**Affinities:** Main Elemental · Sub Corruption
**Armor:** Cloth (Phys DR 0 / Magic DR 4)
**Physical AC** -3 · **Magical AC** 9
**Weapons:** Dagger (1d4), Bomb Flask (1d6)

**Racial Traits:** Darkvision 60 ft., Small Frame, Arcane Cunning

*Magical AC 9 is the system ceiling. Arcane Cunning stacks advantage on Mind saves against spells, making Nyx almost untouchable by magic. Physical AC -3 means a stiff breeze deals full damage. Small Frame is the only escape tool when enemies close to melee. Every point went to casting power and magical defense at the cost of all physical survivability.*

\column

#### Dothren Ironfold — Dwarf Martial (Optimized)

Dwarf · Speed 25 ft. · Medium · Martial
120 HP · 30 Mana · 3 Regen

**Body** +5 · **Mind** -1 · **Social** -2 · **Magic** -1 · **Atraxia** +4

**Affinities:** Main Force · Sub Life
**Armor:** Heavy (Phys DR 4 / Magic DR 0)
**Physical AC** 9 · **Magical AC** -1
**Weapons:** Greathammer (1d8), Short Sword (1d6)

**Racial Traits:** Darkvision 60 ft., Hardy, Stone Steady

*Physical AC 9 is the system ceiling. Stone Steady cancels the Heavy armor speed penalty, so Dothren moves at full 25 ft. in plate. Hardy blocks Venomous escalation. Atraxia +4 produces a large death-cheating pool. The tradeoff: Magical AC -1 means every spell lands and hits hard. Social -2 makes negotiation a lost cause. Keep mages away or die.*

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

{{wide
### Systems Reference

A quick-lookup summary of every major mechanic. Each entry names its source chapter.
}}

#### Resolution *(Core Mechanics)*

Roll `2d10`, add together, add modifier. Meet or beat the target number to succeed.

| Roll Type | Formula | Target |
|:---|:---|:---|
| Attack (physical) | 2d10 + Body | Physical AC |
| Attack (spell) | 2d10 + Magic | Magical AC |
| Proficiency Check | 2d10 + Proficiency Modifier | DC set by GM |
| Initiative | 1d10 + Body or Magic | Ranked highest first |

**Critical success:** both dice show 10. **Critical failure:** both dice show 1.

**Degree of 5:** beat by 10+ = major bonus; 5–9 = minor bonus; 0–4 = baseline; miss by 5–9 = minor setback; miss by 10+ = major setback.

\column

#### Attributes and Point Buy *(Character Creation)*

Five attributes: Body, Mind, Social, Magic, Sanity. Range: −5 to +5.

Point buy at creation: **5 points.** Costs: +5 = 6, +4 = 4, +3 = 3, +2 = 2, +1 = 1, 0 = 0. Negative modifiers refund points; refunded points must be spent elsewhere.

**Skill modifier** = primary attribute + one chosen secondary attribute (choose from two options when the check is called).

#### Armor and Defense *(Armor and Defense)*

| Tier | Physical DR | Magic DR |
|:---|:---:|:---:|
| Cloth | 0 | 4 |
| Light | 1 | 3 |
| Medium | 3 | 1 |
| Heavy | 4 | 0 |
| Enchanted | 3 | 3 |

**Physical AC** = Physical DR + Body. **Magical AC** = Magic DR + Magic. DR reduces damage after a hit lands. Magic DR does not block elemental stack application or escalation.

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

#### Action Economy *(Combat)*

3 Actions per turn. 1 Reaction per round (refreshes at start of your turn). Free Actions do not cost from the 3-Action pool.

#### Elemental Stacks *(Conditions, Injuries, and Death)*

Stacks cap at 5 per element. Each active stack deals +1 damage per round (reduced by Magic DR). Stacks last 2 full rounds and reset on reapplication. Burn and Chilled cancel 1:1.

| Tier | Mana | Requirement | Effect |
|:---|:---:|:---|:---|
| T1 | 3 | — | Apply base stacks |
| T2 | 6 | — | Skip to escalation condition |
| T3 | 12 | T2 active, Mastery Rank 3+ | Enhanced escalation |
| T4 | 17 | T3 active, Rank 5 capstone | Ultimate escalation, once per long rest |

Magic DR reduces tick damage but does not block stack application or T3/T4 escalation.

\column

#### Dying *(Conditions, Injuries, and Death)*

At 0 HP, set death counter: `10 + Body modifier` (min 5, max 15). Each turn, the counter drops by active stack damage (after Magic DR) + 1 per unused Action slot or 2 per used Action slot. Healing restores from Dying. Roll `2d10 + Body` vs. DC `(15 − counter value)` for consequences using the Degree of 5 table.

#### Proficiency Checks *(Attributes and Skills)*

11 skills: Athletics, Stealth, Investigation, Knowledge, Medicine, Survival, Animal Handling, Performance, Speech, Arcana, Insight. Used for **non-combat checks only.** No maximum on proficiencies known. Ranks 1–10; higher rank = higher modifier.

#### Spellcasting *(Magic and Spellcasting)*

No spell list. Build each spell from parameters: Category, Function, Range, Size, Shape, Duration, Target Count, Accuracy Type, Effect Tier. No weapon, class, or item requirement. Only mana gates casting.

| Function | Cost |
|:---|:---:|
| Utility | +0 |
| Movement | +1 |
| Defensive | +1 |
| Offensive | +2 |

Multi-function: add both. Die upgrades: d6 = +1, d8 = +2, d10 = +3, d12 = +5. Main category costs normal; Sub costs double.

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

{{wide
#### Weapons, Techniques, and Augments *(Weapons, Techniques, and Augments)*
}}

Three independent layers. Weapon must be equipped to use its Techniques. Spellcasting is fully independent of this system.

**Weapon Mastery (Rank 0–5):** Unlocks higher-rank Techniques and more Augment Slots per Technique. Purchased with XP.

| Mastery Rank | Technique Access | Augment Slots / Technique | Weapon Augments Available |
|:---:|:---|:---:|:---:|
| 0 | Rank 0 (Universal) | 0 | 0 |
| 1 | Rank 1 | 1 | 0 |
| 2 | Rank 2 | 1 | 2 |
| 3 | Rank 3 | 2 | 3 |
| 4 | Rank 4 | 2 | 4 |
| 5 | Rank 5 (Capstone) | 3 | 5 |

**Techniques:** Active combat abilities. Prepare 10 at a time (changeable on rest). Three scopes: Universal (any weapon), Category (any weapon in that category), Weapon-Specific (one weapon only).

**Augments — three layers:**

| Layer | Count | How Equipped | Scope |
|:---|:---:|:---|:---|
| Universal Augments | 22 | Socket into Technique Augment Slots | Any Technique, any weapon |
| Weapon Augments | ~5 per weapon | Passive — always active once learned (10 XP each) | All Techniques from one weapon |
| Technique Augments | ~2–3 per technique | Socket into that Technique's Augment Slots | One specific Technique only |

Universal Augments are known at creation. Weapon Augments add their Mana cost to every Technique from that weapon. Condition Augments (Burn, Chill, Shock, Force, Bleed, Poison) are mutually exclusive on the same Technique.

\column

#### Advancement *(Advancement and Between-Session Play)*

XP earned through combat, exploration, and conversation. Spent between sessions on:

- New proficiency knowledge
- Proficiency rank increases (Rank 1–10, exponential cost)
- Weapon Mastery rank increases
- Weapon Augment purchases (10 XP each)

XP is a shared budget across all categories.

#### NPCs by Rank *(NPCs, Enemies, and Encounters)*

| Rank | HP | Mana | Body | Mind | Magic |
|:---|:---:|:---|:---:|:---:|:---:|
| Minion | 1–5 | 30 / 3 | +0 | +0 | +0 |
| Regular | 75 | 30 / 3 | +1 | +1 | +1 |
| Enemy/Ally | 100 | 100 / 15 | +4 | +1 | −3 |
| Mini Boss | 120 | 100 / 15 | +5 | +4 | +0 |
| Boss | 175 | 100 / 20 | +5 | +3 | +5 |

Bosses use Enchanted armor. Bosses may have one stat at +6 (beyond normal cap).

---

| Term | Definition | Pages |
|:---|:---|:---|
| AC (Armor Class) | The target number an attacker must meet or beat to land a hit. Physical AC = Physical DR + Body. Magical AC = Magic DR + Magic. | 7, 13, 18 |
| Action | One of 3 things you do on your turn: Attack, Cast a Spell, Move, Drink a Potion, Interact, or Use a Proficiency. | 17, 18 |
| Advantage | Roll 3d10 instead of 2d10 and drop the lowest die. | 7 |
| AOE (Area of Effect) | A spell targeting an area rather than specific creatures. All creatures in the area are affected. | 15 |
| Attribute | One of 5 core stats (Body, Mind, Social, Magic, Atraxia) ranging from -5 to +5. | 9, 11 |
| Background | Caster, Martial, or Hybrid. Sets starting HP, max mana, and mana regeneration rate. | 9 |
| Combat Roll | 2d10 + Body (physical/martial) or 2d10 + Magic (spells) compared against the target's AC. | 7, 18 |
| Condition | An ongoing effect applied by tags. Conditions use stacks that build and decay over time. | 20, 21 |
| Counter | Opposing elements cancel stacks 1:1 (Burn ↔ Chilled). See Condition Profiles for each type. | 21, 22 |
| Critical Failure | Both dice show 1 (natural 2). The effect backfires or misfires. | 7 |
| Critical Success | Both dice show 10 (natural 20). The effect lands at its best possible outcome. | 7 |
| DC (Difficulty Class) | The target number for a Proficiency Check, set by the GM based on the task's difficulty. | 7, 8 |
| Decay | One timer per stack type. Lasts 2 rounds, resets on new hit. When it expires, all stacks of that type are removed. | 21 |
| Degree of 5 | The scale measuring how far above or below the DC a Proficiency Check lands. Gaps of 5 or 10 add bonuses or setbacks. | 8 |
| Disadvantage | Roll 3d10 instead of 2d10 and drop the highest die. | 7 |
| Tag Affinity | One of 10 spell schools (Fire, Ice, Lightning, Acid, Poison, Water, Life, Death, Force, Bleed). Determines tags a spell applies. | 10, 15, 16 |
| DR (Damage Reduction) | A flat number subtracted from damage after a hit lands. Physical DR and Magic DR are separate. | 7, 13, 21 |
| Escalated Condition | A stronger effect triggered when a stack type reaches 5 (e.g., 5 Burn = Ignited). Also called a T2 condition. | 21 |
| GM (Game Master) | The player who describes the world, controls NPCs, sets DCs, and adjudicates the rules. | 3 |
| Atraxia Pool | Long-term survival reserve rolled at character creation. Drains during the dying state. At 0, the character is permanently dead. | 11, 23 |
| HP (Hit Points) | How much damage a character can absorb. At 0 HP, the character enters the dying state (see Dropping to 0 HP). | 9, 23 |
| Incapacitated | A character rendered unable to act by a condition or effect. Distinct from the dying state at 0 HP. | 23 |
| Initiative | 1d10 + Body or Magic (chosen each combat). Determines turn order at the start of combat. | 9, 17 |
| Mana | The resource spent to cast spells and use skills. Starts full each encounter. Regenerates at the start of your turn each round. | 9, 15 |
| Mana Regen | Mana recovered per round. Caster: 15. Hybrid: 10. Martial: 3. | 9, 15 |

| Melee Reach | The distance (default 5 feet) within which a creature can make melee attacks and trigger opportunity attacks. | 18 |
| Modifier | A number from -5 to +5 added to a dice roll to produce a result. | 7, 12 |
| NPC (Non-Player Character) | Any character controlled by the GM. Uses the same rules as player characters. Tier determines stats. | 24 |
| Opportunity Attack | A reaction triggered when a creature leaves an enemy's melee reach. | 18 |
| Purge | Full purge (2 actions): remove all elemental stacks from yourself. Partial purge (1 action): remove 1 stack per elemental type from yourself. | 21 |
| Reaction | 1 per round. An action taken in response to another creature's action. Refreshes at the start of your turn. | 18 |
| Round | One full cycle of turns for all combatants. Represents 3 seconds of in-world time. | 17 |
| Secondary Attribute | The second attribute added to a Proficiency Modifier. Chosen per roll from two options listed for each proficiency. | 8, 12 |
| Proficiency | A trained capability (Athletics, Stealth, Speech, etc.) used for non-combat actions. | 12 |
| Proficiency Check | 2d10 + Proficiency Modifier vs. DC. Used when an uncertain non-combat action is attempted. | 8, 12 |
| Proficiency Modifier | Primary attribute + chosen secondary attribute for a given proficiency. Secondary chosen per roll. | 8, 12 |
| Spend | Some abilities consume your stacks to power an effect. Spent stacks do not count toward escalation. | 21 |
| Stack | A condition counter. 1 per hit, damage equals current count, ticks twice per round, 2-round decay, caps at 5. | 20, 21 |
| Augment | A modifier that sockets into a Technique to change its behavior. Universal Augments fit any Technique; Category Augments fit Techniques from that category only. | 6 |
| Category Technique | A Technique shared by all weapons in a category (e.g., all Light Melee weapons share Flurry). Unlocked by Weapon Mastery Rank in any weapon in that category. | 6 |
| Combat Ability | See Technique. Legacy term for active combat abilities. | 6 |
| Sustained | A spell maintained over multiple rounds. 3 actions to begin, 1 action per turn to maintain. Interruption ends it. | 15 |
| Tag | A mechanical label (Burn, Bleed, Force, etc.) on a weapon, spell, terrain, or ability. Tags determine which conditions apply. | 19, 20 |
| Turn | The portion of a round in which one combatant acts. You get 3 actions on your turn. | 17 |
| XP (Experience Points) | Earned from encounters, spent between sessions to buy proficiency ranks, Weapon Mastery ranks, and Augments. | 25 |
| Technique | An active combat ability tied to a specific weapon. 10 slots can be prepared at a time. Costs Actions and sometimes Mana. Three pools: Universal, Category, and Weapon-Specific. | 6 |
| T3 Enhanced Escalation | A powered-up escalation condition requiring T2 active and Weapon Mastery Rank 3+. Costs 12 mana. | 6, 21 |
| T4 Ultimate Escalation | The strongest escalation condition. Requires T3 active and Weapon Mastery Rank 5. Costs 17 mana. Once per long rest. | 6, 21 |
| Universal Technique | A Technique usable with any weapon (Brace, Shove, Taunt, Second Wind). Available at Weapon Mastery Rank 0. | 6 |
| Weapon Mastery | A per-weapon investment track from Rank 0-5. Higher ranks unlock more Techniques and Augment Slots. Purchased with XP. | 6, 25 |
| Weapon-Specific Technique | A Technique unique to one weapon (e.g., Riposte for Rapier, Cyclone Slash for Greatsword). Unlocked by Weapon Mastery Rank in that weapon. | 6 |
}}

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}
