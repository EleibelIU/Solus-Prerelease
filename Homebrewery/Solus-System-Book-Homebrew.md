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
- ### [{{ Ch. 5: Equipment, Armor, and Weapons}}{{ 13}}](#p13)
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
- ### [{{ Ch. 11: Advancement, Mastery, and Between-Session Play}}{{ 25}}](#p25)
- ### [{{ Ch. 12: Running the Game}}{{ 26}}](#p26)
- ### [{{ Ch. 13: Reference and Playtest Tools}}{{ 27}}](#p27)
  - #### [{{ Reference Tables}}{{ 27}}](#p27)
  - #### [{{ Glossary}}{{ 29}}](#p29)

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
| Choose armor and weapons | Equipment, Armor, and Weapons (Ch. 5) |
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

**Experience Points (XP)** are the currency of character growth. You earn XP from combat, exploration, and social encounters. You spend XP between sessions to buy new skills and raise existing ones (see Advancement, Mastery, and Between-Session Play).

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
3. Compare your result to the defender's **Armor Class** (AC). Physical attacks target **Physical AC**. Spells target **Magical AC**. (See Equipment, Armor, and Weapons for how AC is calculated.)

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

You start with a limited set of proficiencies and can gain more through play. Only **10 proficiencies** can be active at any time (see Attributes and Proficiencies for full rules on active and inactive proficiencies).
{{descriptive
**TODO**: This is accidentally referring to two different systems and needs to be redone. https://poe2db.tw/us/Support_Gems is the actual system this is doing which is similar to Shadowrun's Mods but can be used for anything. This is a fault of naming; Not that I didn't grasp the system. 

This needs to be its own ENTIRE CHAPTER divergent from skills. Let's rename it something that suggests combinatrics. 
}}

As your proficiencies grow in rank, they unlock **Support Skill Slots**. Support Skills are augments that socket into a proficiency and change how it works: reduced cooldown, extended range, changed area shape, added effects. Two characters who share the same base proficiency can play it differently depending on which Support Skills they attach. See Advancement, Mastery, and Between-Session Play for how proficiencies rank up and unlock slots.

{{footnote Character Creation}}
{{pageNumber,auto}}

### Step 8: Choose Equipment

Pick weapons and armor from the tables in Equipment, Armor, and Weapons. Your background does not restrict your choices. A Caster can wear Heavy armor. A Martial can carry a staff.

You begin with **one set of armor** (any tier except Enchanted) and **two weapons**. Choose one melee and one ranged, two melee, or two ranged.

Your armor determines your Physical DR, Magic DR, Physical AC, and Magical AC (see Equipment, Armor, and Weapons: How Armor Works). Your weapon determines your damage dice, tags, and traits.

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
| Proficiencies | Active proficiencies (up to 10) | Proficiencies can be swapped between sessions |
| Support Skills | Socketed augments per proficiency | Changeable between sessions |
| Equipment | Weapons, armor, gear | Changeable |
| Masteries | Mastery skills (if any unlocked) | Changeable between sessions |


Solus has no character levels. Your character grows by earning XP and spending it on proficiency ranks (see Advancement, Mastery, and Between-Session Play). The attributes, race, background, and name you chose in these steps are permanent. Everything else can change between sessions with GM confirmation.

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

- Body is added to physical and martial combat rolls and contributes to **Physical AC** (see Equipment, Armor, and Weapons). Body is one of the two attributes you can choose for **initiative** at the start of combat.

- A character with high Body hits harder with weapons, resists physical attacks, and endures punishment. A character with low Body is fragile, inaccurate with weapons, and easy to hit with physical force.

#### Mind

Mind covers intellect, reasoning, perception, and emotional composure. A character with high Mind spots hidden details, recalls useful lore, resists tricks that target reasoning, and holds steady under fear and stress. A character with low Mind overlooks clues, forgets critical knowledge, falls for deceptions, and panics under pressure.

#### Social

Social covers how you present yourself. It governs persuasion, deception, intimidation, performance, leadership, and your ability to resist social manipulation. A character with high Social commands attention, reads a room, and turns conversations in their favor. A character with low Social struggles to lie, inspire, or talk their way past obstacles.

#### Magic

Magic covers all spellcasting. Every spell you cast uses Magic, regardless of its tag affinity (elemental, death, summoning, or otherwise). 

- Magic is added to magical combat rolls and contributes to **Magical AC**. Magic is the other attribute you can choose for **initiative**.

- The type of magic you specialize in is handled through Masteries, not through this attribute.

- A character with high Magic casts powerful spells, resists magical attacks, and reacts quickly in combat. A character with low Magic casts weak spells and is easy to hit with magic.

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

{{descriptive
**TODO:** Jacob — active combat skills (the mana-costing abilities characters equip and fight with) need their own list or section. The 11 proficiencies below only cover Proficiency Check abilities. Where do combat skills live?
}}

Your character does not start with every proficiency. You choose which proficiencies to take during character creation, and you can gain or swap proficiencies between sessions. You can carry up to 10 **active** proficiencies at any time. Proficiencies you are not carrying cannot be used.

Proficiencies grow through play. As you earn XP and spend it, your proficiencies advance through ranks (Rank 1 to Rank 10), becoming more effective. Higher-ranked proficiencies also unlock **Support Skill Slots**, which let you attach augments that change how the proficiency behaves (see Advancement and Between Sessions).

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

# Equipment, Armor, and Weapons

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

{{footnote Equipment, Armor, and Weapons}}
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

{{footnote Equipment, Armor, and Weapons}}
{{pageNumber,auto}}

\page

## Weapons

All weapon damage adds **Body** as the damage modifier, including ranged weapons and firearms. Weapons are grouped into categories for quick identification:

##### Weapon Categories
| Category | Examples | Damage |
|:---|:---|:---|
| Light Melee | Dagger, Short Sword, Claw Gauntlet, Bare Hands | 1d4 + Body to 1d6 + Body |
| Medium Melee | Rapier, Katana, Curved Sword | 1d8 + Body |
| Heavy Melee | Greatsword, Greathammer, Great Axe | 1d8 + Body |
| Reach | Halberd, Scythe, Whip | 1d6 + Body to 1d10 + Body |
| Ranged / Thrown | Bow, Bomb Flask | 1d6 + Body to 1d8 + Body |
| Firearms | Revolver, Rifle, Shotgun, Sniper Rifle | 1d8 + Body to 1d12 + Body |

No weapon category restricts your playstyle. A caster can swing a greatsword. A martial can throw daggers. Categories exist so you can find a weapon fast and know its base damage. Each weapon's unique traits determine what it does in play, not its category label.

#### Weapon Tags

Every weapon carries one or more **tags**: short labels that describe how the weapon behaves. Tags include Melee, Light, Medium, Heavy, Reach, Thrown, Splash, One-Handed, Two-Handed, Ranged, Firearm, and Unarmed.

Tags matter because other rules reference them. A Support Skill that triggers "on a Heavy weapon hit" only fires when you swing a weapon tagged Heavy. A condition that says "Melee attacks are at disadvantage" applies to any weapon tagged Melee. Tags connect your weapon to the rest of the system.

Many weapons also carry unique **traits**: special effects that apply condition stacks, move targets, alter terrain, or unlock finisher attacks once a target has the right conditions applied to them.

{{descriptive
**TODO:** Jacob, need the full weapon-by-weapon trait list. I'll insert it once the equipment chapter is locked.

**TODO:** Jacob, are shields missing from the equipment list? Do they need to be added?
}}

{{footnote Equipment, Armor, and Weapons}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 6: MAGIC AND SPELLCASTING -->

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
| | Locked | — | — | Cannot cast unless a Mastery grants access. |
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

All other affinities are **locked**. You cannot cast spells from a locked affinity unless a Mastery grants access (see Advancement, Mastery, and Between-Session Play).

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
| Cast a Spell | Cast a spell using 1 or more actions. Multi-action spells can span turns. |
| Move | Move up to your full movement speed. |
| Drink a Potion | Consume a potion or similar item. |
| Interact | Open a door, draw a weapon, pick up an object, pull a lever. |
| Use a Proficiency | Attempt a Proficiency Check during combat (Medicine to stabilize, Athletics to grapple). |

**Multi-action abilities.** Some spells and skills cost 2 or 3 actions. You can spend those actions on the same turn or split them across consecutive turns. If you are interrupted (stunned, knocked unconscious, forced to move) before completing all required actions, the ability fails and any spent actions are lost. Mana spent on a failed spell is not refunded.

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

<!-- CHAPTER 11: ADVANCEMENT, MASTERY, AND BETWEEN-SESSION PLAY -->

# Advancement, Mastery, and Between-Session Play

Solus has no character levels. Your character grows by earning **XP** and spending it on skills.

### Earning XP

You earn XP from every type of encounter:

- **Combat:** Each enemy tier awards a set amount of XP when defeated.
- **Exploration:** Engaging with an exploration encounter awards XP, whether you succeed or fail.
- **Social:** Conversation and negotiation encounters award XP for participation.

You do not need to win to earn XP. You need to engage.

### Spending XP

You spend XP **between sessions**. XP buys two things: new proficiencies and proficiency rank increases.

**Buying a new proficiency** costs a flat amount. The proficiency starts at Rank 1.

**Raising a proficiency's rank** costs XP that increases exponentially from Rank 1 to Rank 10. Early ranks are cheap. Late ranks are expensive. This means spreading XP across many proficiencies gives you breadth, while focusing XP on a few proficiencies gives you depth. Both strategies are viable.

**Support Skill Slots** unlock as a proficiency's rank increases. A Rank 1 proficiency has 1 slot. Every other rank after that (Rank 2, 4, 6, 8, 10) opens another, to a maximum of 5 slots per proficiency.

{{descriptive
**TODO:** Jacob, need the full XP cost table (acquisition cost + rank 1-10 costs) and XP awards per enemy tier, exploration, and social encounters.
}}

\column

### Masteries

Masteries are specializations that unlock when your **total lifetime XP** reaches certain thresholds. At each threshold, you gain Mastery points to spend on Mastery Skills. Mastery points are finite. You will have fewer points than available Mastery Skills, so you must choose which Masteries to invest in.

Masteries function like skills, not classes. They define a specialization (a school of magic, a combat discipline, a social archetype) through mechanics, not through role restrictions.

{{descriptive
**TODO:** Jacob is redesigning Masteries. The current version too closely resembles a class system. Masteries may become regular skills or move into a "special" category with tradeoffs. Waiting on a revised foundation before finalizing this section.
}}

### Between Sessions

Between sessions, you can update any part of your character that the rules mark as changeable (see Character Creation, Step 9). With GM confirmation, you can:

- Swap active proficiencies (remember: 10 active at a time, see Attributes and Proficiencies).
- Socket or change Support Skills on your active proficiencies.
- Change Masteries using the same rules as proficiency swaps.
- Change weapons and armor from your inventory.
- Spend or gain money and resources.
- Record new languages your character has learned.

Proficiency swaps are also available on **long rests** during a session, so players can adapt tactics between encounters. Support Skills can be changed on both **short and long rests**.

{{footnote Advancement, Mastery, and Between Sessions}}
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

**Players control:** skills, Mastery Skills, equipment, weapons, spells, money, resources, languages, and which actions to take on their turn.

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
### Glossary

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
| Mastery | A specialization unlocked by total XP thresholds. Grants Mastery points spent on Mastery Skills. | 25 |
| Melee Reach | The distance (default 5 feet) within which a creature can make melee attacks and trigger opportunity attacks. | 18 |
| Modifier | A number from -5 to +5 added to a dice roll to produce a result. | 7, 12 |
| NPC (Non-Player Character) | Any character controlled by the GM. Uses the same rules as player characters. Tier determines stats. | 24 |
| Opportunity Attack | A reaction triggered when a creature leaves an enemy's melee reach. | 18 |
| Purge | Full purge (2 actions): remove all elemental stacks from yourself. Partial purge (1 action): remove 1 stack per elemental type from yourself. | 21 |
| Reaction | 1 per round. An action taken in response to another creature's action. Refreshes at the start of your turn. | 18 |
| Round | One full cycle of turns for all combatants. Represents 3 seconds of in-world time. | 17 |
| Secondary Attribute | The second attribute added to a Proficiency Modifier. Chosen per roll from two options listed for each proficiency. | 8, 12 |
| Proficiency | A trained capability (Athletics, Stealth, Speech, etc.) used for non-combat actions. 10 active at a time. | 12 |
| Proficiency Check | 2d10 + Proficiency Modifier vs. DC. Used when an uncertain non-combat action is attempted. | 8, 12 |
| Proficiency Modifier | Primary attribute + chosen secondary attribute for a given proficiency. Secondary chosen per roll. | 8, 12 |
| Spend | Some abilities consume your stacks to power an effect. Spent stacks do not count toward escalation. | 21 |
| Stack | A condition counter. 1 per hit, damage equals current count, ticks twice per round, 2-round decay, caps at 5. | 20, 21 |
| Support Skill | An augment socketed into a proficiency that modifies its behavior. Slots unlock as proficiency rank increases. | 12, 25 |
| Sustained | A spell maintained over multiple rounds. 3 actions to begin, 1 action per turn to maintain. Interruption ends it. | 15 |
| Tag | A mechanical label (Burn, Bleed, Force, etc.) on a weapon, spell, terrain, or ability. Tags determine which conditions apply. | 19, 20 |
| Turn | The portion of a round in which one combatant acts. You get 3 actions on your turn. | 17 |
| XP (Experience Points) | Earned from encounters, spent between sessions to buy proficiencies and raise proficiency ranks. | 25 |
}}

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}
