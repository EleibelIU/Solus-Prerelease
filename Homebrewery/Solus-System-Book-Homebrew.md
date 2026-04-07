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

{{frontCover
![Solus Cover](Homebrewery\Assets\Solus Cover.png) {position:absolute,top:0,left:0,width:100%,height:100%}

}}

\page

<!-- TABLE OF CONTENTS -->

{{toc,wide

# Contents

- ### [{{ Ch. 1: Welcome to Solus}}{{ 3}}](#p3)
  - #### [{{ What You Need}}{{ 3}}](#p3)
  - #### [{{ Roles at the Table}}{{ 3}}](#p3)
  - #### [{{ How a Session Plays}}{{ 4}}](#p4)
  - #### [{{ Where to Find Things}}{{ 7}}](#p7)
- ### [{{ Ch. 2: Core Mechanics}}{{ 8}}](#p8)
  - #### [{{ Key Terms}}{{ 8}}](#p8)
  - #### [{{ How Dice Work}}{{ 8}}](#p8)
  - #### [{{ Critical Results}}{{ 9}}](#p9)
  - #### [{{ Advantage and Disadvantage}}{{ 9}}](#p9)
  - #### [{{ The Two Roll Types}}{{ 9}}](#p9)
- ### [{{ Ch. 3: Character Creation}}{{ 11}}](#p11)
  - #### [{{ Attribute Scores}}{{ 11}}](#p11)
  - #### [{{ Race}}{{ 12}}](#p12)
  - #### [{{ Background}}{{ 12}}](#p12)
  - #### [{{ Skills and Equipment}}{{ 13}}](#p13)
- ### [{{ Ch. 4: Attributes and Skills}}{{ 14}}](#p14)
  - #### [{{ The Five Attributes}}{{ 14}}](#p14)
  - #### [{{ Skill Modifiers}}{{ 15}}](#p15)
  - #### [{{ Skill List}}{{ 16}}](#p16)
- ### [{{ Ch. 5: Equipment, Armor, and Weapons}}{{ 17}}](#p17)
  - #### [{{ How Armor Works}}{{ 17}}](#p17)
  - #### [{{ Weapons}}{{ 19}}](#p19)
- ### [{{ Ch. 6: Magic and Spellcasting}}{{ 20}}](#p20)
  - #### [{{ Building a Spell}}{{ 20}}](#p20)
  - #### [{{ Spell Reference}}{{ 23}}](#p23)
- ### [{{ Ch. 7: Core Gameplay Loop}}{{ 25}}](#p25)
- ### [{{ Ch. 8: Combat}}{{ 26}}](#p26)
  - #### [{{ Initiative}}{{ 26}}](#p26)
  - #### [{{ Actions and Reactions}}{{ 26}}](#p26)
  - #### [{{ Resolving an Attack}}{{ 27}}](#p27)
- ### [{{ Ch. 9: Conditions, Injuries, and Death}}{{ 30}}](#p30)
  - #### [{{ Tags and Stacks}}{{ 30}}](#p30)
  - #### [{{ Element Profiles}}{{ 32}}](#p32)
  - #### [{{ Other Conditions}}{{ 36}}](#p36)
  - #### [{{ Dropping to 0 HP}}{{ 37}}](#p37)
- ### [{{ Ch. 10: NPCs, Enemies, and Encounters}}{{ 38}}](#p38)
- ### [{{ Ch. 11: Advancement and Between Sessions}}{{ 39}}](#p39)
- ### [{{ Ch. 12: Running the Game}}{{ 40}}](#p40)
- ### [{{ Ch. 13: Reference and Playtest Tools}}{{ 41}}](#p41)
  - #### [{{ Quick Reference Tables}}{{ 41}}](#p41)
  - #### [{{ Playtest Checklist}}{{ 43}}](#p43)
  - #### [{{ Glossary}}{{ 43}}](#p43)

}}

<!-- Remove footer on TOC page -->
<style> .page#p2:after {all: unset} </style>

\page

<!-- CHAPTER 1: WELCOME TO SOLUS -->

# Welcome to Solus

Solus is a tabletop roleplaying game for three to six people. One person runs the world as the Game Master. Everyone else plays a character inside it. You describe what your character does, roll dice when the outcome is uncertain, and discover the consequences together. The system rewards tactical choices and punishes carelessness. Your character can grow powerful, but the world grows dangerous to match.

### What You Need

**Two ten-sided dice (2d10).** Each die is numbered 1 through 10. You add the two dice together for a single total. A roll of 7 and 5 gives you 12. Solus does not use percentile dice, twenty-sided dice, or any other die type for core rolls.

**A character sheet.** This records your five attributes (Body, Mind, Social, Magic, Sanity), your skills, your equipment, your health, and your mana. The Character Creation chapter walks you through filling one out.

**Friends.** Solus works best with three to five players and one GM.

**Pencils and scratch paper.** You will track health, mana, conditions, and initiative during play.

\column

### Roles at the Table

**The Game Master (GM)** describes the world, controls all non-player characters (NPCs), sets target numbers for uncertain actions, and adjudicates the rules. The GM does not play against you. The GM plays the world around you.

**Players** each control one character. You decide what your character attempts, roll dice when the rules call for it, and describe how your character reacts to what happens. Your character sheet tells you what your character is good at. The dice tell you whether it works.

### How a Session Plays

The best way to learn Solus is to watch a round of play. The scene below uses real rules. Every roll, modifier, and target number works the way the full chapters describe. You do not need to memorize the math yet. Read it once to see how the pieces fit. Come back after reading the rules to see why each number lands where it does.

Terms used in this scene are defined in the chapters that follow. If you see a bolded term you do not recognize, check the Glossary at the end of this book.

{{footnote Welcome to Solus}}
{{pageNumber,auto}}

\page

#### The Setup

Three players sit at a table with their GM.

**Kael** is a martial fighter. Body +4, Mind +1, Social +0, Magic -2, Sanity +2. He carries a greatsword (2d6 damage, Reach tag) and wears Medium armor (Physical DR 3, Magic DR 1).

**Senna** is a hybrid spellblade. Body +2, Mind +0, Social +1, Magic +3, Sanity -1. She carries a shortsword (1d6 damage) and wears Light armor (Physical DR 1, Magic DR 3).

**Torek** is a social infiltrator. Body +1, Mind +3, Social +4, Magic -1, Sanity -2. He carries a dagger (1d4 damage) and wears Cloth armor (Physical DR 0, Magic DR 0).

#### Scene: The Collapsed Bridge

The GM speaks: *"You've been tracking a stolen shipment through the forest for two days. The trail leads to a stone bridge over a ravine. The bridge is half-collapsed. The far side still holds, but the gap is twelve feet wide. You can hear voices on the other side."*

Torek's player says: "I want to listen and figure out how many people are over there."

The GM calls for a **Skill Check**. The skill is **Perception**. Perception's primary attribute is Mind. Torek chose Body as his secondary attribute for Perception at character creation. His Mind is +3 and his Body is +1, so his Perception modifier is **+4**. The GM sets the **Difficulty Class (DC)** at 14, because the targets are speaking quietly across a ravine with wind.

Torek's player rolls 2d10: **6 + 9 = 15**, plus his modifier of +4 = **19**. He beats the DC of 14 by 5. The GM uses the **Degree of 5** scale: beating a DC by 5 or more earns a bonus.

\column

The GM says: *"You count three distinct voices. One sounds frustrated, barking orders. You also catch the glint of a fourth figure crouched behind a rock. Four enemies total."*

If Torek had rolled a 4 + 3 = 7, plus 4 = 11, he would have missed the DC by 3. The GM might say: *"You hear voices, but the wind carries the words away. At least two people are over there. Maybe more."*

#### Crossing the Gap

Kael's player says: "I want to jump the gap."

Twelve feet is a serious distance. The GM calls for an **Athletics** Skill Check, DC 13. Athletics uses Body as its primary. Kael chose Mind as his secondary. His Body is +4 and Mind is +1, giving him an Athletics modifier of **+5**.

Kael rolls 2d10: **8 + 7 = 15**, plus 5 = **20**. He clears the gap by a wide margin. The GM describes him landing in a crouch on the far side. Because he beat the DC by 7 (more than 5), the GM rules he lands silently and keeps his footing.

Senna follows. Same DC, but her Athletics modifier is lower (Body +2, secondary Mind +0 = **+2**). She rolls: **5 + 6 = 11**, plus 2 = **13**. She meets the DC exactly. She makes it across, but stumbles on the landing. The enemies hear the noise.

{{footnote Welcome to Solus}}
{{pageNumber,auto}}

\page

#### Combat Begins

The GM says: *"A bandit with a crossbow shouts an alarm. Roll initiative."*

**Initiative** uses a d10 (one die, not two) plus Body or Magic, your choice per character.

| Character | Roll | Modifier | Total |
|:---|:---:|:---:|:---:|
| Kael | 7 | +4 (Body) | 11 |
| Senna | 5 | +3 (Magic) | 8 |
| Bandit Leader | 8 | +2 (Body) | 10 |
| Bandit Archer | 4 | +1 (Body) | 5 |

Turn order: Kael (11), Bandit Leader (10), Senna (8), Bandit Archer (5). Ties go to the higher modifier. If still tied, the GM decides.

#### Kael's Turn: Three Actions

Each character gets **3 actions** per turn. Common actions: Move, Attack, Defend, Use Item, Cast Spell.

Kael's player says: "I spend my first action to Move toward the bandit leader. Second action: Attack with my greatsword. Third action: Attack again."

**First Attack.** Kael rolls a **Combat Roll**: `2d10 + Body` because the greatsword is a physical weapon. He rolls **6 + 8 = 14**, plus Body +4 = **18**. The Bandit Leader wears Light armor (Physical DR 1) and has Body +2, giving a **Physical AC of 3** (DR 1 + Body 2). Kael's 18 beats 3, so he hits. He rolls greatsword damage: **2d6 = 4 + 5 = 9**, plus Body +4 = **13**. The bandit's Physical DR of 1 absorbs 1 point. The bandit takes **12 damage**.

\column

**Second Attack.** Kael rolls again: **3 + 4 = 7**, plus 4 = **11**. Still beats the AC of 3. Damage: **2d6 = 2 + 3 = 5**, plus 4 = **9**, minus 1 DR = **8 damage**. The bandit leader is in trouble.

#### Senna's Turn: Sword and Spell

Senna's player says: "First action: Move to flank the archer. Second action: Attack the archer with my shortsword. Third action: Cast a fire bolt at the bandit leader."

**Shortsword Attack.** Physical weapon, so she rolls `2d10 + Body`. Her Body is +2. She rolls **9 + 5 = 14**, plus 2 = **16**. The archer wears Cloth armor (Physical DR 0, Body +1), so Physical AC is **1**. She hits. Shortsword damage: **1d6 = 4**, plus Body +2 = **6**, minus 0 DR = **6 damage**.

**Fire Bolt.** Spell, so she rolls `2d10 + Magic`. Her Magic is +3. She rolls **4 + 7 = 11**, plus 3 = **14**. The bandit leader's **Magical AC** is Magic DR 3 (Light armor) + Magic -1 = **2**. She hits. Spell damage: **1d6 + 1d8 + 3 = 3 + 5 + 3 = 11**, minus Magic DR 3 = **8 damage**. The bandit leader drops to 0 HP.

When a character drops to 0 HP, they are incapacitated (see Conditions, Injuries, and Death).

{{footnote Welcome to Solus}}
{{pageNumber,auto}}

\page

#### What Just Happened

In a few minutes of play, the group used three systems:

**Skill Checks** resolved Torek's Perception (hearing enemies) and Kael's Athletics (jumping the gap). Both used `2d10 + Skill Modifier` against a DC the GM set.

**Combat Rolls** resolved Kael's greatsword swings and Senna's shortsword strike using `2d10 + Body`, and Senna's fire bolt using `2d10 + Magic`. Physical attacks targeted Physical AC. The spell targeted Magical AC.

**Action Economy** gave each character 3 actions per turn, spent on movement, attacks, and spells in any combination.

These three systems carry the game. The chapters that follow teach each one in full.

\column

### Where to Find Things

| If you want to... | Go to... |
|:---|:---|
| Learn how dice, rolls, and target numbers work | Core Mechanics (Ch. 2) |
| Build a character from scratch | Character Creation (Ch. 3) |
| Understand your five attributes and eleven skills | Attributes and Skills (Ch. 4) |
| Choose armor and weapons | Equipment, Armor, and Weapons (Ch. 5) |
| Learn how spells are built and cast | Magic and Spellcasting (Ch. 6) |
| Understand how sessions and encounters flow | Core Gameplay Loop (Ch. 7) |
| Run a full combat encounter | Combat (Ch. 8) |
| Look up a condition or what happens at 0 HP | Conditions, Injuries, and Death (Ch. 9) |
| Build or reference NPCs and encounters | NPCs, Enemies, and Encounters (Ch. 10) |
| Advance your character between sessions | Advancement and Between Sessions (Ch. 11) |
| Run the game as a GM | Running the Game (Ch. 12) |
| Quick-reference tables, playtest checklist, glossary | Reference and Playtest Tools (Ch. 13) |

{{footnote Welcome to Solus}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 2: CORE MECHANICS -->

# Core Mechanics

This chapter covers the rules that every other chapter builds on: how dice work, what the numbers on your sheet mean, and the two types of rolls you will make during play.

### Key Terms

Before you read further, here are four numbers you will see on every character sheet:

**Hit Points (HP)** measure how much damage your character can take. When your HP reaches 0, your character is incapacitated (see Conditions, Injuries, and Death). Your maximum HP is set by your background during character creation and does not change.

**Mana** is the resource you spend to cast spells. Each spell costs a set amount of mana. Your mana regenerates during combat at the start of each of your turns by an amount set by your background (see Character Creation, Step 4). Outside of combat, mana refills between encounters.

**Experience Points (XP)** are the currency of character growth. You earn XP from combat, exploration, and social encounters. You spend XP between sessions to buy new skills and raise existing ones (see Advancement, Mastery, and Between-Session Play).

**Modifiers** are numbers from -5 to +5 that represent how good or bad your character is at something. You add a modifier to your dice roll. Higher is better.

\column

### How Dice Work

Solus uses two ten-sided dice, written as **2d10**. Each die is numbered 1 through 10. Roll both and add the numbers together to get a single total.

After adding the dice, add a number from your character sheet called a **modifier**. Modifiers range from -5 to +5. The final number is your **result**.

{{note
**Example:** You roll a 7 and a 5. That's 12. Your modifier is +3. Your result is 15.
}}

The two dice are added, not read side by side. A roll of 10 and 4 is 14, not 104. Solus does not use percentile dice.

The GM sets a **target number**. If your result meets or beats the target, you succeed. If it falls short, you fail.

### When You Roll

You roll only when the outcome is uncertain. If your character is trained at a task and nothing complicates it, the GM describes the success without dice. If the task is beyond your character entirely, the GM describes the failure. Dice come out when the answer could go either way.

{{footnote Core Mechanics}}
{{pageNumber,auto}}

\page

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

\column

### The Two Roll Types

Solus has two kinds of rolls. Both use 2d10 plus a modifier. The difference is which modifier you add and what target number you compare against.

#### Combat Roll

Roll a Combat Roll when you attack with a weapon or cast an offensive spell.

1. Choose your attack. Physical and martial attacks (a sword swing, a punch, an arrow) add your **Body** modifier. Spells add your **Magic** modifier.
2. Roll `2d10 + Body` or `2d10 + Magic`.
3. Compare your result to the defender's **Armor Class** (AC). Physical attacks target **Physical AC**. Spells target **Magical AC**. (See Equipment, Armor, and Weapons for how AC is calculated.)
4. If your result meets or beats the AC, you hit. Roll damage. The defender's **Damage Reduction** (DR) subtracts from the damage dealt.
5. If your result falls short, you miss.

{{note
**Example:** You swing a greatsword at a bandit. Your Body is +4. You roll 2d10 and get 6 + 8 = 14, plus 4 = 18. The bandit wears Medium armor (Physical DR 3) and has Body +1, so their Physical AC is 4. You beat 4, so you hit. You roll 1d8 + 4 for damage and deal 10. The bandit's Physical DR of 3 absorbs 3 points. The bandit takes 7 damage.
}}

{{footnote Core Mechanics}}
{{pageNumber,auto}}

\page

#### Skill Check

Roll a Skill Check when your character attempts something uncertain that is not a combat attack. Picking a lock, tracking footprints, persuading a guard, recalling a piece of lore, treating a wound: these are Skill Checks.

1. The GM names the relevant skill and sets a **Difficulty Class** (DC), a target number reflecting how hard the task is.
2. Roll `2d10 + your Skill Modifier`.
3. Compare your result to the DC.
4. The GM reads the outcome using the **Degree of 5** scale (see Running the Game). Beating the DC by 5 or more earns a bonus. Missing the DC by 5 or more adds a setback. The wider the gap, the bigger the swing.

Your **Skill Modifier** is the sum of two attributes: a fixed **primary** attribute and a **secondary** attribute you chose at character creation. See Attributes and Skills for the full list and how this math works.

{{note
**Example:** You try to calm a spooked horse. The GM calls for Animal Handling against DC 12. Animal Handling uses Social as its primary. Your secondary choice is Mind. Your Social is +3 and your Mind is +4, so your modifier is +7. You roll 2d10 and get 4 + 5 = 9, plus 7 = 16. You beat DC 12 by 4 and the horse calms down. If you had rolled 3 + 2 = 5, plus 7 = 12, you would meet the DC exactly: a bare success with no bonus or setback.
}}

{{footnote Core Mechanics}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 3: CHARACTER CREATION -->

# Character Creation

Character creation follows seven steps. By the end, you will have a complete character sheet ready for play. You do not need to read the full rulebook first. Each step tells you what to write down and points you to the chapter that explains it.

### Step 1: Build Your Concept

Decide what kind of character you want to play. Ask yourself three questions: How does this character fight? How does this character solve problems outside of combat? What is this character bad at?

Solus does not restrict your choices by class or archetype. A character with high Body and high Magic can swing a greatsword and cast spells in the same turn. A character with high Social and low Body can talk their way past guards but will struggle in a fistfight. The attributes and skills you choose in the next steps define your strengths and weaknesses mechanically.

### Step 2: Distribute Attribute Scores

You have five attributes: Body, Mind, Social, Magic, and Sanity. Each gets a modifier between -5 and +5. The Attributes and Skills chapter describes what each attribute does.

You have **5 points** to spend across all five attributes. Higher modifiers cost more points. Negative modifiers refund points. You must spend all 5 points, with zero remaining.

\column

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
**Example:** You want a melee fighter who can take a hit. You set Body +4 (costs 4), Mind +1 (costs 1), Social +0 (costs 0), Magic -2 (refunds 2), Sanity +2 (costs 2). Total spent: 4 + 1 + 0 - 2 + 2 = **5**. All points used.
}}

Notice that +5 costs 6 points, more than the full budget. You can reach +5 in one attribute, but you will need deep negatives elsewhere to pay for it.

{{footnote Character Creation}}
{{pageNumber,auto}}

\page

### Step 3: Choose Your Race

Your race sets your base movement speed, character size, and one or more racial traits (such as darkvision or a movement bonus). Record these on your sheet.

##### Races
| Race | Notes |
|:---|:---|
| Elves | |
| Dwarves | |
| Orcs | |
| Gnomes | |
| Constructs | |
| Half-Breeds | |
| Humans | |

{{descriptive
**TODO:** Define racial traits for each race (speed, size, unique mechanical trait). A custom race option is under consideration where you select from preset racial trait lists instead of picking a named race.
}}

### Step 4: Choose Your Background

Your background sets your starting hit points (HP), maximum mana pool, and mana regeneration rate. It does not restrict which skills, spells, weapons, or armor you can use. Any background can use any equipment.

The first number after mana is your **maximum mana**. The second is your **mana regeneration per round**.

\column

##### Backgrounds
| Background | HP | Max Mana | Mana Regen / Round |
|:---|:---:|:---:|:---:|
| Caster | 100 | 100 | 15 |
| Martial | 120 | 30 | 3 |
| Hybrid | 110 | 70 | 10 |

A Caster has the deepest mana pool and fastest regeneration but the lowest health. A Martial has the most health but barely enough mana for basic utility spells. A Hybrid splits the difference.

{{descriptive
**TODO:** Confirm Hybrid mana. Jacob believes 70/10 is correct; if 75/10 appears more often in playtest sheets, that is the final number.
}}

### Step 5: Choose Your Skills

Pick skills from the skill list in the Attributes and Skills chapter. For each skill you take, choose its **secondary attribute** from the two options listed. This choice is permanent and determines your skill modifier (see Attributes and Skills: How Skill Modifiers Work).

You start with a limited set of skills and can gain more through play. Only **10 skills** can be active at any time (see Attributes and Skills for full rules on active and inactive skills).

As your skills grow in rank, they unlock **Support Skill Slots**. Support Skills are augments that socket into a skill and change how it works: reduced cooldown, extended range, changed area shape, added effects. Two characters who share the same base skill can play it differently depending on which Support Skills they attach. See Advancement, Mastery, and Between-Session Play for how skills rank up and unlock slots.

{{descriptive
**TODO:** Define when Support Skill slots first become available and the full Support Skill list.
}}

{{footnote Character Creation}}
{{pageNumber,auto}}

\page

### Step 6: Choose Equipment

Pick weapons and armor from the tables in Equipment, Armor, and Weapons. Your background does not restrict your choices. A Caster can wear Heavy armor. A Martial can carry a staff.

Your armor determines your Physical DR, Magic DR, Physical AC, and Magical AC (see Equipment, Armor, and Weapons: How Armor Works). Your weapon determines your damage dice, tags, and traits.

{{descriptive
**TODO:** Add starting equipment budget or package rules.
}}

### Step 7: Review Your Sheet

Check your sheet against this reference. If anything is blank, go back to the step that fills it in.

##### Character Sheet Reference
| Category | What to record | Can it change? |
|:---|:---|:---|
| Name | Character name | Fixed |
| Race | Race, size, speed, racial traits | Fixed |
| Background | Caster, Martial, or Hybrid | Fixed |
| Attributes | Body, Mind, Social, Magic, Sanity | Fixed |
| HP / Mana | Max HP, Max Mana, Mana Regen | Fixed (set by background) |
| Skills | Active skills (up to 10), secondary picks | Skills can be swapped between sessions; secondary picks are permanent |
| Support Skills | Socketed augments per skill | Changeable between sessions |
| Equipment | Weapons, armor, gear | Changeable |
| Masteries | Mastery skills (if any unlocked) | Changeable between sessions |

\column

Solus has no character levels. Your character grows by earning XP and spending it on skill ranks (see Advancement, Mastery, and Between-Session Play). The attributes, race, background, and name you chose in these steps are permanent. Everything else can change between sessions with GM confirmation.

{{footnote Character Creation}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 4: ATTRIBUTES AND SKILLS -->

# Attributes and Skills

Your character has five **attributes**. Each attribute is a number from -5 to +5 that measures a broad area of capability. Attributes feed into combat rolls, Armor Class, initiative, and your skill modifiers. Every attribute matters; there are no dump stats.

### The Five Attributes

#### Body

Body covers all physical capability: strength, speed, endurance, coordination. Whether you swing a hammer, dodge a falling boulder, or sprint across a battlefield, Body is the attribute that matters.

Body is added to physical and martial combat rolls and contributes to **Physical AC** (see Equipment, Armor, and Weapons). Body is one of the two attributes you can choose for **initiative** at the start of combat.

A character with high Body hits hard with weapons, resists physical attacks, and endures punishment. A character with low Body is fragile, inaccurate with weapons, and easy to hit with physical force.

#### Mind

Mind covers intellect, reasoning, perception, and emotional awareness. It governs what you know, what you notice, and how well you process information under pressure.

A character with high Mind spots hidden details, recalls useful lore, and resists tricks that target reasoning. A character with low Mind overlooks clues, forgets critical knowledge, and falls for deceptions.

\column

#### Social

Social covers how you present yourself. It governs persuasion, deception, intimidation, performance, leadership, and your ability to resist social manipulation. Social has no connection to magic.

A character with high Social commands attention, reads a room, and turns conversations in their favor. A character with low Social struggles to lie, inspire, or talk their way past obstacles.

#### Magic

Magic covers all spellcasting. Every spell you cast uses Magic, regardless of its category (elemental, death, summoning, or otherwise). The type of magic you specialize in is handled through Masteries, not through this attribute.

Magic is added to magical combat rolls and contributes to **Magical AC**. Magic is the other attribute you can choose for **initiative**.

A character with high Magic casts powerful spells, resists magical attacks, and reacts quickly in combat. A character with low Magic casts weak spells and is easy to hit with magic.

#### Sanity

Sanity covers mental fortitude and perception of hidden truths. In Solus, lower Sanity does not make you unstable. It opens your eyes. Characters with low Sanity perceive things others cannot: hidden layers of the world, eldritch presences, truths that erode the mind.

Sanity governs fear, stress, madness thresholds, and any corruption mechanics. A character with high Sanity is unshakeable but blind to the world's deeper horrors. A character with low Sanity sees too much and risks breaking under the weight of that knowledge.

{{footnote Attributes and Skills}}
{{pageNumber,auto}}

\page

### Skills

A **skill** is a trained capability your character has. Skills cover everything outside of direct combat attacks: climbing a wall, picking a lock, persuading a merchant, identifying a spell, treating a wound, tracking an animal through snow. When you attempt one of these actions and the outcome is uncertain, the GM calls for a **Skill Check** (see Core Mechanics) using the relevant skill.

Your character does not start with every skill. You choose which skills to take during character creation, and you can gain or swap skills between sessions. You can own as many skills as you can afford, but only 10 can be **active** at any time. Skills you are not carrying cannot be used.

Skills grow through play. As you earn XP and spend it, your skills advance through ranks (Rank 1 to Rank 10), becoming more effective. Higher-ranked skills also unlock **Support Skill Slots**, which let you attach augments that change how the skill behaves (see Advancement and Between Sessions).

### How Skill Modifiers Work

When you make a Skill Check, you roll `2d10` and add your **Skill Modifier**. That modifier comes from two of your attributes added together.

Every skill has a **primary** attribute and a **secondary** attribute.

The **primary** is fixed. It never changes for that skill. Athletics always uses Body. Arcana always uses Magic. The primary represents the core capability the skill draws on.

\column

The **secondary** is your choice. Each skill lists two options. You pick one when you create your character, and that pick is permanent. The secondary represents how your character approaches that skill: do you climb walls through trained technique (Mind) or through sheer refusal to let go (Sanity)?

**Skill Modifier** = primary attribute + secondary attribute.

{{note
**Example:** You are building a character with Body +4, Mind +1, and Sanity -2. You take Athletics, which uses Body as its primary. The secondary options are Mind or Sanity.

If you pick Mind: Athletics = +4 + 1 = **+5**. Your character climbs with practiced efficiency.

If you pick Sanity: Athletics = +4 + (-2) = **+2**. Your character is strong but panics under pressure.

The choice is permanent. Pick the secondary that fits the character you want to play.
}}

This system means every attribute contributes to multiple skills. A character who invests heavily in one attribute will be strong in some skills and dangerously weak in others. Two characters with the same skill can have different modifiers because they chose different secondaries.

{{footnote Attributes and Skills}}
{{pageNumber,auto}}

\page

### Skill List

The table below shows all 11 skills. When you make a Skill Check, find the skill, add the primary and your chosen secondary together, and that is the modifier you roll with.

{{wide

##### Skills
| Skill | Primary | Secondary (pick one) | What it covers |
|:---|:---:|:---:|:---|
| Athletics | Body | Mind or Sanity | Climbing, jumping, sprinting, swimming, feats of strength or endurance |
| Stealth | Body | Mind or Sanity | Moving unseen, hiding, acting without drawing attention |
| Investigation | Mind | Body or Sanity | Searching for clues, analyzing evidence, piecing together hidden details |
| Knowledge | Mind | Social or Sanity | Recalling lore, history, culture, religion, or technical information |
| Medicine | Mind | Body or Sanity | Diagnosing conditions, treating wounds, stabilizing the dying |
| Survival | Mind | Body or Sanity | Tracking, hunting, navigating, enduring harsh environments |
| Animal Handling | Social | Body or Mind | Calming, training, controlling, or reading the behavior of animals |
| Performance | Social | Body or Sanity | Entertaining, inspiring, distracting through art, music, or drama |
| Speech | Social | Body or Mind | Persuading, deceiving, negotiating, intimidating, commanding |
| Arcana | Magic | Mind or Sanity | Identifying, understanding, or manipulating magical and supernatural forces |
| Insight | Sanity | Body or Mind | Perceiving hidden truths, eldritch knowledge, cosmic or occult comprehension |

}}

{{footnote Attributes and Skills}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 5: EQUIPMENT, ARMOR, AND WEAPONS -->

# Equipment, Armor, and Weapons

### How Armor Works

Armor in Solus does two things: it makes you harder to hit, and it absorbs damage when you do get hit. These are two separate systems, and understanding the difference is critical.

#### Armor Class (AC): Can They Hit You?

Every character has two **Armor Class** values:

- **Physical AC** = your armor's Physical DR + your Body modifier
- **Magical AC** = your armor's Magic DR + your Magic modifier

When someone attacks you, they roll `2d10 + their attack modifier` and compare the result to your AC. If they meet or beat your AC, the attack hits. If they fall short, it misses.

Physical attacks (swords, arrows, fists) target your Physical AC. Spells target your Magical AC. Because you have two separate ACs, a character can be tough against swords but vulnerable to spells, or the reverse. Your armor choice and attribute spread determine where your defenses are strong and where they are weak.

\column

#### Damage Reduction (DR): How Much Gets Through?

When an attack lands, your armor's **Damage Reduction** absorbs part of the blow. DR is a flat number subtracted from the damage dealt.

- **Physical DR** reduces damage from weapons, unarmed strikes, falls, and other physical sources.
- **Magic DR** reduces damage from spells and elemental status effects. Magic DR does not stop status effects from applying or escalating; it only reduces the damage those effects deal.

DR is fixed per armor tier. Your attributes do not change it.

##### Armor Tiers
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

\page

#### What Happens When You Get Hit

When an attack targets you, resolve it in two steps:

1. **Compare the attack roll to your AC.** If the attacker's result meets or beats your Physical AC (for weapons) or Magical AC (for spells), the attack lands. Otherwise it misses, and no damage is dealt.
2. **Subtract your DR from the damage.** The attacker rolls damage. Your relevant DR (Physical or Magic) subtracts from the total. You take the remainder.

{{note
**Example:** A mage casts a fire bolt at you. You wear Light Armor (Magic DR 3) and have Magic +2, so your Magical AC is 5. The mage rolls `2d10 + 4` and gets 16. That beats your Magical AC of 5, so the spell hits. The mage rolls 8 damage. Your Magic DR of 3 reduces it to 5. You take 5 damage.
}}

{{note
**Example:** You wear Heavy Armor (Physical DR 4, Magic DR 0) with Body +3 and Magic +0. Your Physical AC is 7. Your Magical AC is 0. A sword fighter rolls 11 against your Physical AC of 7, hits, and deals 9 damage. Your Physical DR of 4 absorbs 4, leaving 5 damage. A caster rolls the same 11 against your Magical AC of 0, also hits, and deals 9 damage. With Magic DR 0, nothing absorbs. You take the full 9. Heavy armor makes you a fortress against blades and a glass window against magic.
}}

\column

### Weapons

All weapon damage adds **Body** as the damage modifier, including ranged weapons and firearms. Weapons are grouped into categories by fighting style.

##### Weapon Categories
| Category | Examples | Damage |
|:---|:---|:---|
| Light Melee | Dagger, Short Sword, Claw Gauntlet, Bare Hands | 1d4 + Body to 1d6 + Body |
| Medium Melee | Rapier, Katana, Curved Sword | 1d8 + Body |
| Heavy Melee | Greatsword, Greathammer, Great Axe | 1d8 + Body |
| Reach | Halberd, Scythe, Whip | 1d6 + Body to 1d10 + Body |
| Ranged / Thrown | Bow, Bomb Flask | 1d6 + Body to 1d8 + Body |
| Firearms | Revolver, Rifle, Shotgun, Sniper Rifle | 1d8 + Body to 1d12 + Body |

Light weapons deal less damage per hit but can be dual-wielded and strike fast. Heavy weapons share a base die with medium weapons but carry traits that offer crowd control, knockback, or finisher effects. Reach weapons let you strike from further away. Firearms deal the highest base damage but carry their own resource costs. The choice between categories is about how you want to fight, not just how hard you want to hit.

#### Weapon Tags

Every weapon carries one or more **tags**: short labels that describe how the weapon behaves. The core tags are Melee, Light, Medium, Heavy, Reach, Thrown, Splash, One-Handed, Two-Handed, Ranged, Firearm, and Unarmed.

Tags matter because other rules reference them. A Support Skill that triggers "on a Heavy weapon hit" only fires when you swing a weapon tagged Heavy. A condition that says "Melee attacks are at disadvantage" applies to any weapon tagged Melee. Tags connect your weapon to the rest of the system.

Many weapons also carry unique **traits**: special effects that apply condition stacks, move targets, alter terrain, or unlock finisher attacks once a target has the right conditions applied to them.

{{descriptive
**TODO:** Insert the full weapon-by-weapon trait list after the equipment chapter is locked.

**TODO:** Confirm whether shields are missing from the equipment list and need to be added.
}}

{{footnote Equipment, Armor, and Weapons}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 6: MAGIC AND SPELLCASTING -->

# Magic and Spellcasting

In many games, you pick spells from a list. Solus works differently. You build every spell yourself by making nine choices about what the magic does. Your choices control how far it reaches, how big it is, how long it lasts, and how hard it hits. Two players who both want to throw fire will end up with different spells depending on the choices they make.

### How Spells Work

To cast a spell, you spend **mana** (magical energy) and **actions** (time on your turn). Every spell is defined by nine choices. Each choice has a mana cost. Several choices also fall into an **action column** (1 Action, 2 Actions, 3 Actions, or 4+). The highest action column among your nine choices sets the spell's total action cost.

##### The Nine Spell Choices
| Choice | What You Are Deciding |
|:---|:---|
| Category | The school of magic (Elemental, Force, Mind, Life, Death, etc.) |
| Function | The spell's purpose: Offensive, Defensive, Movement, or Utility |
| Range | How far the spell can reach |
| Size | How large the affected area is |
| Shape | The geometric form: point, sphere, cube, line, wall, or freeform |
| Duration | How long the effect lasts |
| Target Count | How many creatures or objects it affects |
| Accuracy Type | How the spell determines whether it hits |
| Effect Tier | How powerful the spell's lasting effects are |

The first seven choices are intuitive. You pick a school, a purpose, a range, a size, a shape, a duration, and a target count. The last two need more context, so they are explained inside the walkthrough below when you encounter them.

\column

### Building and Casting Your First Spell

You want to create a fire attack that hits one enemy at close range. Walk through each choice, then cast it.

**Step 1: Category.** Every spell belongs to a school of magic. You are throwing fire: pick **Elemental**. No mana cost. Ten categories exist: Elemental, Force, Mind/Psychological, Temporal, Creation/Transmutation, Order/Binding, Summoning, Life, Death, Corruption/Chaos.

**Step 2: Function.** This spell attacks an enemy: pick **Offensive**. Costs +2 mana. (Defensive and Movement cost +1. Utility costs +0. If a spell serves two functions, add both.)

**Step 3: Range.** Close range: **Self to 15 ft.** Costs +1 mana. Action column 1.

**Step 4: Size.** Medium blast: **20-30 ft.** Costs +2 mana. Action column 2.

**Step 5: Shape.** A bolt hits a single point: **Point**. Costs +1 mana. Column 1.

**Step 6: Duration.** Hits and ends: **Instant**. Costs +1 mana. Column 1.

**Step 7: Target Count.** One target: **Single**. Costs +1 mana. Column 1.

{{footnote Magic and Spellcasting}}
{{pageNumber,auto}}

\page

**Step 8: Accuracy Type.** This choice determines how the spell connects with its target.

- **Attack Roll (1 mana base):** You roll 2d10 + Magic against the target's Magical AC. If you meet or beat the defense, the spell hits. You also get to add a bonus damage die (explained below).
- **Save (1 mana):** The target rolls to resist instead of you rolling to hit. No bonus die.
- **Auto-Hit (4 mana):** The spell connects automatically. No roll. Reliable, but expensive.

You want to roll to hit and deal damage: pick **Attack Roll**. Base cost +1 mana. You also add a d6 bonus damage die (+1 mana). Total for this choice: +2 mana. Column 1.

{{descriptive
**TODO:** Save resolution needs definition now that Resist Rolls have been removed.
}}

**Step 9: Effect Tier.** When a spell hits, it applies a **tag** to the target. Tags are lasting effects like Burn, Chilled, or Acid that create conditions over time (see Conditions, Injuries, and Death). Effect Tier determines which version of the tag your spell applies.

- **Tier 1 (T1, 3 mana):** Applies the foundational tag. A T1 Fire spell applies [Burn], which builds 1 stack per hit. At 5 stacks, it escalates to Ignited. T1 terrain effects last 2 rounds.
- **Tier 2 (T2, 6 mana):** Applies the escalated version directly. A T2 Fire spell applies [Ignited], skipping the stack buildup. T2 terrain effects last 4 rounds.
- **T3 (12 mana) and T4 (17 mana)** exist at higher power.

{{descriptive
**TODO:** Define T3 and T4 mechanically.
}}

You want basic fire: pick **T1 (Burn)**. Costs +3 mana. Column 1. On hit, the target gains 1 Burn stack.

\column

#### The Finished Spell

##### Fire Bolt Breakdown
| Choice | Option | Column | Mana |
|:---|:---|:---:|:---:|
| Category | Elemental | — | 0 |
| Function | Offensive | — | +2 |
| Range | Self to 15 ft. | 1 | +1 |
| Size | 20-30 ft. | 2 | +2 |
| Shape | Point | 1 | +1 |
| Duration | Instant | 1 | +1 |
| Target Count | Single | 1 | +1 |
| Accuracy Type | Attack Roll + d6 bonus | 1 | +2 |
| Effect Tier | T1 (Burn) | 1 | +3 |

**Action cost: 2.** The highest column is 2 (Size). The spell costs 2 of your 3 actions.

**Mana cost: 13.** Add every value: 0 + 2 + 1 + 2 + 1 + 1 + 1 + 2 + 3 = 13.

**Damage.** Three choices (Range, Size, Target Count) each contribute one damage die. The die size scales with how much mana you spent on that choice. Attack Roll adds a bonus die you sized and paid for. Your Magic attribute applies as a flat bonus.

**Fire Bolt damage:** Range (1 mana) d6 + Target Count (1 mana) d6 + Size (2 mana) d8 + Attack Roll bonus d6 + Magic modifier.

{{footnote Magic and Spellcasting}}
{{pageNumber,auto}}

\page

#### Casting It

1. **Check mana.** You need 13 mana in your pool. Mana regenerates at the start of your turn each round.
2. **Spend 2 actions and 13 mana.**
3. **Roll to hit.** Roll 2d10 + Magic against the target's Magical AC (Magic DR + Magic modifier).
4. **On hit, roll damage.** Roll 1d6 + 1d6 + 1d8 + 1d6 + Magic modifier. Subtract the target's Magic DR from the total.
5. **Apply the tag.** The target gains 1 Burn stack.

{{note
**Example:** You cast Fire Bolt. Your Magic is +3. The target has Magical AC 5 (Magic DR 4, Magic +1). You roll 2d10: 7 + 8 = 15, plus 3 = 18. That beats 5. Damage: 1d6 + 1d6 + 1d8 + 1d6 + 3 = 4 + 2 + 6 + 3 + 3 = 18, minus Magic DR 4 = 14 damage. The target gains 1 Burn stack.
}}

\column

### Spell Reference

#### Spell Framework

The number in parentheses is the mana cost for that option.

##### Spell Options by Action Column
| Choice | 1 Action | 2 Actions | 3 Actions | 4+ / Ritual |
|:---|:---|:---|:---|:---|
| Range | Self to 25 ft. (1) | 30-60 ft. (2) | 65-120 ft. (3) | 125-200 ft. (4), Sight (5), Global (6) |
| Size | 5-15 ft. (1) | 20-30 ft. (2) | 35-60 ft. (3) | |
| Shape | Point or none (1) | Sphere / Cube / Line / Wall / Cylinder (2) | Freeform or custom (3) | |
| Duration | Instant (1) | 1 Round (2) | 1 Minute (3) | Hours (4), Permanent (5) |
| Target Count | Single (1) | Multi 2+ (2) | AOE / Area of Effect (3) | |
| Accuracy Type | Attack Roll (1) | Save (1) | | Auto-Hit (4) |
| Effect Tier | T1 (3) | T2 (6) | T3 (12) | T4 (17) |

##### Function Costs
| Function | Mana |
|:---|:---:|
| Utility | +0 |
| Movement | +1 |
| Defensive | +1 |
| Offensive | +2 |

{{footnote Magic and Spellcasting}}
{{pageNumber,auto}}

\page

#### Damage Dice

Range, Size, and Target Count each contribute one die. Attack Roll adds a bonus die (you choose size, pay the mana). A choice's die caps at its maximum mana cost (Size maxes at 3, so its die caps at d10).

##### Damage Die by Mana Spent
| Mana Spent | Die |
|:---:|:---:|
| 1 | d6 |
| 2 | d8 |
| 3 | d10 |
| 5 | d12 |

Your Magic modifier applies as a flat bonus to all offensive spell damage.

#### Mana Pools

| Background | Max Mana | Regen per Round |
|:---|:---:|:---:|
| Caster | 100 | 15 |
| Hybrid | 70 | 10 |
| Martial | 30 | 3 |

The cheapest spell costs 8 mana. The most expensive 1-action spell costs 44. The most expensive 3-action spell costs 132.

#### Main and Sub Categories

At character creation, you choose a **Main** and a **Sub** category. Main costs normal mana. Sub costs double. All other categories are locked unless a Mastery grants access.

{{descriptive
**TODO:** Confirm whether the Main/Sub system should be kept or cut (D-06).
}}

\column

#### Additional Rules

**Duration override.** If the effect outlasts the casting time, pay the higher duration's mana cost.

**Two tags at the same tier.** Pay the tier cost twice. Two T2 tags = 12 mana.

**Multi-target scaling.** Targeting specific creatures (not AOE) adds mana: 2 targets = +2, 3 = +3, 4 = +4. Maximum 4.

**Split casting.** 2- or 3-action spells can split across consecutive turns. Interruption = failure. Mana not refunded.

{{footnote Magic and Spellcasting}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 7: CORE GAMEPLAY LOOP -->

# Core Gameplay Loop

A session of Solus follows a repeating cycle. Every encounter, whether it involves combat, conversation, exploration, or puzzle-solving, passes through the same six steps.

### The Loop

1. **The world presents a problem.** The GM describes a situation that demands a response: a locked door, an ambush, a starving village, a collapsing bridge. The problem can be physical, social, magical, or environmental.
2. **You act.** You use your character's attributes, skills, equipment, and spells to respond. You might fight, negotiate, investigate, sneak, or flee.
3. **The system resolves consequences.** Dice rolls determine uncertain outcomes. Combat Rolls resolve attacks. Skill Checks resolve everything else. The GM interprets the results using the Degree of 5 scale (see Running the Game).
4. **Rewards follow.** Successful encounters award XP. Combat encounters pay XP per enemy rank. Exploration and social encounters award XP for engagement, whether you succeed or fail.
5. **Characters adjust between sessions.** You spend XP to raise skill ranks or buy new skills. You can swap active skills, change equipment, and update changeable traits with GM confirmation (see Advancement and Between Sessions).
6. **The next problem begins.** The world reacts to what you did. New problems emerge from the consequences of old ones.

\column

### Three Types of Encounters

The GM builds encounters from three modes. Most sessions mix all three.

**Combat encounters** use initiative, turn order, and the action economy from the Combat chapter. Enemies fight using the same rules you do. Rewards scale with enemy rank.

**Social encounters** use Skill Checks (Speech, Performance, Insight, Knowledge) against DCs set by the GM. You earn XP for engaging, regardless of outcome. Failing a negotiation still counts as play.

**Exploration encounters** use Skill Checks (Survival, Athletics, Investigation, Arcana, Stealth) to navigate terrain, find hidden things, avoid hazards, and solve puzzles. XP is awarded when the group engages with the encounter, not just when they solve it.

{{footnote Core Gameplay Loop}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 8: COMBAT -->

# Combat

Combat begins when negotiation, stealth, or avoidance fails and violence starts. This chapter covers the full sequence: who goes first, what you can do on your turn, how attacks land, and what happens when someone drops.

### Starting Combat: Initiative

When combat breaks out, every combatant rolls for initiative. Roll **1d10** (one die, not two) and add either your **Body** or your **Magic** modifier. You choose which modifier to use. This choice is per character, not per encounter. A martial fighter adds Body. A caster adds Magic. A hybrid picks whichever is higher.

The GM ranks everyone from highest to lowest. That is the turn order for the entire encounter unless a rule changes it.

**Tie-breaking.** If two combatants roll the same total:

1. The higher modifier goes first.
2. If still tied, roll another d10 between the tied combatants.
3. Players and their allies may choose to act simultaneously if both are willing. Enemies cannot share a simultaneous turn and must use option 1 or 2.

**Round length.** Each full **round** of combat represents 3 seconds of in-world time. A round includes one **turn** for every combatant. Your turn is the part of the round where you act. When every combatant has taken a turn, the round ends and a new one begins.

\column

### Your Turn: Three Actions

On your turn, you get **3 actions**. Spend them in any order. Finish resolving one action before starting the next. You can repeat an action (attack three times, move three times) unless a specific ability, spell, or item says otherwise.

##### Actions
| Action | What It Does |
|:---|:---|
| Attack | Strike with a weapon. Roll a Combat Roll (see below). |
| Cast a Spell | Cast a spell using 1 or more actions. Multi-action spells can span turns. |
| Move | Move up to your full movement speed. |
| Drink a Potion | Consume a potion or similar item. |
| Interact | Open a door, draw a weapon, pick up an object, pull a lever. |
| Use a Skill | Attempt a Skill Check during combat (Medicine to stabilize, Athletics to grapple). |

**Multi-action abilities.** Some spells and skills cost 2 or 3 actions. You can spend those actions on the same turn or split them across consecutive turns. If you are interrupted (stunned, knocked unconscious, forced to move) before completing all required actions, the ability fails and any spent actions are lost. Mana spent on a failed spell is not refunded.

{{footnote Combat}}
{{pageNumber,auto}}

\page

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

\column

### Resolving an Attack

When you attack, follow these steps:

1. **Choose your attack.** Pick a weapon or a spell.
2. **Determine your modifier.** Physical and martial attacks (swords, fists, bows, firearms) use **Body**. Spells use **Magic**.
3. **Roll the Combat Roll.** Roll `2d10 + Body` (physical) or `2d10 + Magic` (spell).
4. **Compare to the target's AC.** Physical attacks compare against **Physical AC**. Spells compare against **Magical AC**. If your result meets or beats the AC, the attack hits. If it falls short, it misses.
5. **Roll damage.** Roll your weapon's damage dice + Body, or your spell's damage dice + Magic. The target's **DR** (Physical DR for weapon hits, Magic DR for spell hits) subtracts from the total. The target takes the remainder as damage. Damage cannot go below 0.
6. **Apply tags and stacks.** If the attack carries a tag that inflicts a condition (Burn, Chilled, Bleed, Force, etc.), apply 1 stack of that condition to the target. Stacks follow the rules in Conditions, Injuries, and Death.
7. **Check for 0 HP.** If the target drops to 0 HP, they are incapacitated (see Conditions, Injuries, and Death: Dropping to 0 HP).

{{note
**Example:** You swing a greathammer at an enemy wearing Light armor (Physical DR 1, Body +2, Physical AC 3). Your Body is +4. You roll 2d10: 5 + 9 = 14, plus 4 = 18. That beats AC 3. You roll damage: 1d8 + 4 = 11. The enemy's Physical DR 1 absorbs 1. They take 10 damage. Your greathammer carries the Force tag, so the enemy gains 1 Force stack.
}}

{{footnote Combat}}
{{pageNumber,auto}}

\page

### Tags in Combat

**Tags** are mechanical labels attached to weapons, spells, terrain, potions, and creature abilities. When an attack lands, its tags determine what conditions apply. A sword tagged with Bleed applies a Bleed stack on hit. A fire spell tagged with Burn applies a Burn stack on hit. Terrain tagged with Acid applies an Acid stack when a creature enters or starts its turn there.

Tags are system-wide. The same Burn stack works the same way whether it came from a spell, a weapon trait, or a pool of lava. See Conditions, Injuries, and Death for full stack rules and condition effects.

**Stack escalation.** Some conditions escalate when they reach 5 stacks. Five Acid stacks trigger Corroded (-2 DR). Five Bleed stacks trigger Shredded. Five Force stacks trigger Concussed. Your weapon and spell choices determine which escalation paths you threaten.

### Worked Example: A Full Round

Three combatants: **Kael** (martial, Body +4, greatsword 1d8+Body, Medium armor), **Senna** (hybrid, Body +2, Magic +3, shortsword 1d6+Body, Light armor), and a **Bandit Sergeant** (Enemy rank, Body +3, Magic -1, mace 1d8+Body, Medium armor, 100 HP).

**Initiative.** Kael rolls d10: 8, plus Body +4 = 12. Senna rolls d10: 6, plus Magic +3 = 9. Bandit Sergeant rolls d10: 7, plus Body +3 = 10. Turn order: Kael (12), Bandit Sergeant (10), Senna (9).

\column

**Kael's turn (3 actions).**
- Action 1: Move. Kael closes 25 feet to reach the Bandit Sergeant.
- Action 2: Attack with greatsword. Roll `2d10 + 4` = 7 + 6 + 4 = **17**. Bandit's Physical AC = Physical DR 3 + Body 3 = **6**. Hit. Damage: `1d8 + 4` = 5 + 4 = **9**, minus DR 3 = **6 damage**. Bandit is at 94 HP.
- Action 3: Attack again. Roll `2d10 + 4` = 3 + 8 + 4 = **15**. Beats AC 6. Damage: `1d8 + 4` = 7 + 4 = **11**, minus 3 = **8 damage**. Bandit at 86 HP.

**Bandit Sergeant's turn (3 actions).**
- Action 1: Attack Kael with mace (Force tag). Roll `2d10 + 3` = 9 + 4 + 3 = **16**. Kael's Physical AC = DR 3 + Body 4 = **7**. Hit. Damage: `1d8 + 3` = 6 + 3 = **9**, minus 3 DR = **6 damage**. Kael gains 1 Force stack.
- Action 2: Attack again. Roll `2d10 + 3` = 2 + 5 + 3 = **10**. Beats AC 7. Damage: `1d8 + 3` = 3 + 3 = **6**, minus 3 = **3 damage**. Kael gains a second Force stack (now 2 Force, dealing 2 damage at start of his next turn).
- Action 3: Move. The Bandit steps 10 feet to put Kael between himself and Senna.

**Senna's turn (3 actions).**
- Action 1: Move 25 feet to reach the Bandit. This takes her through Kael's space (allies can pass through each other's spaces).
- Action 2: Attack with shortsword. Roll `2d10 + 2` = 8 + 7 + 2 = **17**. Beats Bandit's Physical AC of 6. Damage: `1d6 + 2` = 4 + 2 = **6**, minus 3 DR = **3 damage**. Bandit at 83 HP.
- Action 3: Cast a frost bolt (spell, Chilled tag). Roll `2d10 + 3` (Magic) = 6 + 5 + 3 = **14**. Bandit's Magical AC = Magic DR 1 + Magic -1 = **0**. Hit. Spell damage: `1d6 + 1d8 + 3` = 3 + 6 + 3 = **12**, minus Magic DR 1 = **11 damage**. Bandit at 72 HP and gains 1 Chilled stack.

**End of round.** Turn order resets to the top. Kael takes 2 damage from his 2 Force stacks at the start of his next turn. The Bandit's Chilled stack will deal 1 damage at the start of the Bandit's next turn and lasts 2 rounds unless reapplied.

{{footnote Combat}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 9: CONDITIONS, INJURIES, AND DEATH -->

# Conditions, Injuries, and Death

This chapter explains how lasting effects work in Solus: what causes them, how they build, what happens when they get worse, and how to get rid of them. It also covers what happens when a character drops to 0 HP.

Every rule in this chapter applies the same way regardless of where the effect comes from. A Burn stack from a fire spell works the same as a Burn stack from a flaming sword or a pool of lava. The source does not change the rules.

### Before You Read: Tracking Conditions at the Table

The stack and condition system is the densest part of Solus. It has more moving parts than any other chapter. Read it once to understand the logic. You do not need to memorize it. The system caps at 5 stacks per type, and nothing goes past an escalated condition. Once you reach 5 stacks and trigger the escalation, that is the worst it gets. The math stays bounded.

At the table, you have three options for tracking stacks:

**Paper character sheets.** The Solus character sheet includes a row of five boxes for each stack type. Fill in a box when you gain a stack. Erase it when the stack expires or is removed. Write the round number next to each box so you know when it decays. This works, but it requires attention from every player.

**Condition Tracker app.** A dedicated Solus Condition Tracker (planned for iOS and Android) handles stack counts, decay timers, escalation triggers, elemental interactions, and damage calculations automatically. If your group plays at a physical table and wants to offload the bookkeeping, this is the recommended tool.

\column

**Virtual tabletop.** Solus has native support for FoundryVTT. The Foundry module tracks all tag applications, stack counts, decay rounds, escalation thresholds, opposing stack cancellation, and condition damage per round. The GM and players see stack states update in real time. If your group plays online, this is the smoothest way to run the system.

You do not need digital tools to play Solus. The paper sheet works. But the condition system rewards groups that use tracking tools, because those tools let you focus on tactics instead of arithmetic.

### Tags and Stacks: The Two-Part System

Solus tracks lasting effects through two linked pieces: **tags** and **stacks**.

A **tag** is a label on an attack, spell, weapon trait, terrain hazard, potion, or creature ability. Tags describe what type of effect the source carries. Common tags include Burn, Bleed, Acid, Chilled, Volt, and Force.

A **stack** is what a tag creates when it lands on a target. Each time a tagged effect hits you, it adds 1 stack of that type to you. Stacks are counters. They build up, deal damage over time, and trigger worse effects if they reach a threshold.

Tags are on the source. Stacks are on the target.

{{note
**Example:** A mage casts a fire bolt tagged with Burn. The spell hits you. You now have 1 Burn stack. Next round, the mage hits you again. You now have 2 Burn stacks. The tag (Burn) lives on the spell. The stacks (1, then 2) live on you.
}}

{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}

\page

### How Stacks Work

When a tagged effect hits a target, follow these rules:

1. **Apply 1 stack.** Each hit adds exactly 1 stack of the tag's type. A sword tagged with Bleed adds 1 Bleed stack per hit. A spell tagged with Burn adds 1 Burn stack per hit.

2. **One tag per hit.** If an attack carries two tags (a weapon with both Burn and Bleed), you choose which one to apply. A single hit never applies two different stack types.

3. **Stack damage equals the stack count.** A target with 2 Burn stacks takes 2 fire damage. A target with 4 Acid stacks takes 4 acid damage. The more stacks, the more damage.

4. **Stack damage triggers twice.** The target takes stack damage once when the stack is applied (immediately on the hit), and again at the **start of the target's next turn**. This means even if you lose the stacks before your turn, the damage from the initial hit already landed.

5. **Each stack lasts 2 rounds.** Count from the turn the stack was applied. After 2 full rounds pass, that stack expires and is removed.

6. **Reapplying resets the timer.** If a target already has 3 Burn stacks and you hit them with another Burn attack, the new stack resets to a fresh 2-round duration. The older stacks keep their own timers. Track each stack's decay separately.

7. **All stacks cap at 5.** No target can have more than 5 stacks of any single type. No spell, ability, item, or combination of effects can push a stack count above 5.

8. **Different stack types are independent.** A creature can have 3 Burn stacks and 2 Bleed stacks at the same time. Each type tracks its own count, deals its own damage, and decays on its own timers.

\column

{{note
**Example: Tracking stacks across two rounds.**

Round 1, your turn: You hit an enemy with a Bleed-tagged sword. The enemy gains 1 Bleed stack and takes 1 bleed damage immediately.

Round 1, enemy's turn: At the start of the enemy's turn, the 1 Bleed stack deals 1 damage again. The enemy attacks you.

Round 2, your turn: You hit the enemy again. The enemy gains a second Bleed stack (now at 2). The enemy takes 2 bleed damage immediately (the current stack count). The new stack has a fresh 2-round timer. The first stack has 1 round left on its timer.

Round 2, enemy's turn: At the start of the enemy's turn, 2 Bleed stacks deal 2 damage.

Round 3, enemy's turn: The first stack expires (2 rounds have passed since it was applied). The enemy is back to 1 Bleed stack and takes 1 damage.
}}

### Armor and Stack Damage

**Magic DR reduces stack damage** from elemental and magical sources (Burn, Chilled, Volt, Acid). If you have Magic DR 3 and take 4 Burn stack damage, you take 1 damage instead of 4. Magic DR does not prevent the stack from being applied. It does not stop stacks from building toward escalation. It only reduces the damage the stacks deal each round.

Physical DR does not reduce elemental stack damage. Bleed and Force stacks deal physical damage and are reduced by Physical DR.

{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}

\page

### Escalation and Interactions

When a stack type reaches 5, it triggers an **escalated condition**: a stronger, named effect on top of the ongoing stack damage. Escalation is the ceiling. Nothing goes past it. The stacks stay at 5 and the condition persists until the stacks decay or are removed.

The profiles below cover every element and magic type in the game. Each profile tells you four things: what the tag does on hit, what happens as stacks build, what the escalation does at 5, and how to counter or remove it.

{{note
**Example: Burn to Ignited.** You get hit by a fire spell three rounds in a row. Round 1: 1 Burn stack, 1 fire damage. Round 2: 2 Burn stacks, 2 fire damage. Round 3: 3 stacks, 3 damage. Two more hits and you reach 5 Burn stacks. At 5, you become Ignited: you take Burn damage every turn and cannot receive healing. Your ally hits you with an ice spell (Chilled tag). The Chilled cancels 1 Burn stack, dropping you to 4. Ignited ends. Another ice hit drops you to 3. The fire is coming under control.
}}

\column

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

\page

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
| **Stack** | Poisoned. |
| **At escalation: Venomous** | You lose 1 action. Stacks increase by 1 per round, accelerating to +5 per round at 10 stacks. At 15 stacks, lose a second action. At 20, lose your third. At 35, permanently lose 1 action. |
| **Countered by** | Radiant removes Venomous at 10 or fewer stacks. Purge removes Venomous at 15+. Purge cannot restore an action permanently lost at 35. |
| **DR type** | Magic DR reduces Poison stack damage. |

{{descriptive
**TODO:** Define Poisoned mechanical effect (distinct from Venomous).
}}

Venomous is the most dangerous escalation in the game. It accelerates on its own once triggered. Act fast.

\column

#### Bleed

| | |
|:---|:---|
| **Tag** | Bleed (from Smite-type effects and weapon traits) |
| **Stack** | Bleed. Deals physical bleed damage equal to stack count. |
| **At 5: Shredded** | |
| **Countered by** | Decay (2 rounds) or purging. No direct elemental opposite. |
| **DR type** | Physical DR reduces Bleed stack damage. |

{{descriptive
**TODO:** Define Shredded effect.
}}

#### Force

| | |
|:---|:---|
| **Tag** | Force (from Impact, Blast, Slam, Repulse effects) |
| **Stack** | Force. Deals physical force damage equal to stack count. |
| **At 5: Concussed** | |
| **Countered by** | Decay, purging, or spending. Some weapon traits let you spend Force stacks for bonus damage or special effects before reaching 5. Spent stacks are removed immediately. |
| **DR type** | Physical DR reduces Force stack damage. |

{{descriptive
**TODO:** Define Concussed effect.
}}

{{note
**Example:** Your unarmed fighting style builds Force stacks on yourself. You have 4. Your next punch lets you spend all 4 for +4 bonus damage. Your count drops to 0, and you avoid triggering Concussed.
}}

{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}

\page

#### Water / Wet

| | |
|:---|:---|
| **Tag** | Water, Wet |
| **Stack** | Wet is a condition, not a damage stack. It does not deal damage or escalate. |
| **Effect** | Extinguishes fire on terrain and objects. Enables the Shocked to Stunned upgrade. |
| **At Tier 2: Drown** | You lose your reaction. You must spend 1 action each turn to avoid suffocating. Breath duration depends on Body. |

Wet is a setup condition. On its own it does nothing harmful. Combined with Volt stacks, it turns Shocked into Stunned.

#### Life Magic

Life magic tags do not create stacks. They produce immediate effects. These tags appear on spells built from the Life category.

| Tag | What It Does |
|:---|:---|
| Restore | Repairs recent damage. Stabilizes injuries not yet permanent. |
| Regenerate | Restores lost body parts and reverses severe trauma while the spell is active. |
| Radiant | Damages corrupted or organic targets. Removes Venomous at 10 or fewer stacks. |
| Purge | Removes or suppresses one active biological condition. The only way to remove Venomous at 15+. |
| Rouse | Returns a recently deceased target to life (body intact, death recent). |
| Revive | Returns a long-dead target to life at extreme cost or risk. |

Radiant and Purge are the primary healing-side answers to Poison. Restore and Regenerate handle physical damage. Rouse and Revive handle death.

\column

#### Death Magic

Death magic tags do not create stacks. They produce immediate effects. These tags appear on spells built from the Death category.

| Tag | What It Does |
|:---|:---|
| Pyroptosis | Target detonates with necrotic energy in a 5 ft. radius. |
| Apoptosis | Target dies immediately. |
| Reanimate | Restores temporary motion to lifeless matter. |
| Vivify | Tethers a spirit or essence to a vessel beyond natural death. |

#### Reap (Weapon-Specific)

| | |
|:---|:---|
| **Source** | Scythe weapon trait |
| **Stack** | Reap. Unique stack type with its own rules. |
| **Countered by** | Any healing removes all Reap stacks. If the attacker misses the target for 2 consecutive rounds, Reap stacks are removed. |

### General Stack Removal

These removal methods apply to all stack types, not just one element.

**Decay.** Every stack expires 2 rounds after it was applied. Automatic.

**Purging.** A full purge (2 actions) removes all elemental stacks from you. A partial purge (1 action) removes 1 stack of each elemental type. Some purge abilities target a narrower set (Acid and Poison only, for example).

**Spending.** Some weapon traits and abilities let you spend your accumulated stacks to power an effect instead of letting them escalate. Spent stacks are removed immediately and do not count toward escalation. If you lack the required stacks, the ability fails.

{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}

\page

### Tags on Terrain and Objects

When a spell or effect applies a tag to terrain (a fire patch, an acid pool, a frozen floor), the tagged area persists for the spell's duration. If no duration is specified, Tier 1 effects last 2 rounds and Tier 2 effects last 4 rounds.

A creature that enters tagged terrain or starts its turn there gains 1 stack of the linked type. The same stack rules apply: damage on application, damage at start of turn, 2-round decay, cap at 5.

### Other Conditions

These conditions do not come from stacks. They are applied directly by abilities, spells, or hazards.

##### Non-Stack Conditions
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
| Stunned | Disadvantage on all actions. You lose your reaction for the round. (Usually from Shocked + Wet.) |
| Unconscious | You are unresponsive and cannot act until awakened or the effect ends. |
| Weaken | |

\column

{{descriptive
**TODO:** Shredded, Concussed, Poisoned, and Weaken still need full definitions from Jacob.
}}

### Dropping to 0 HP

When your HP reaches 0, you are **incapacitated**. You fall where you stand. You cannot take actions, move, or use reactions. You remain on the battlefield, and other creatures can still target you with attacks, abilities, or healing.

If an ally heals you to 1 HP or more before your next turn ends, you are no longer incapacitated. You can act on your following turn.

If no healing reaches you, your character dies at the end of your next turn.

{{descriptive
**TODO:** The dying system, repeated knockdown rules, and Madness thresholds are under active design review. The final versions will replace this section when approved.
}}

{{footnote Conditions, Injuries, and Death}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 10: NPCs, ENEMIES, AND ENCOUNTERS -->

# NPCs, Enemies, and Encounters

Every NPC in Solus uses the same action economy, equipment, skills, and spells as player characters. An enemy swings a sword the same way you do, casts spells from the same framework, and takes 3 actions on its turn. The GM does not run NPCs from a separate system. The GM runs them from the same rules you use.

The only differences between NPC tiers are stat modifiers, HP, and mana pools. Each tier also supports martial, caster, and hybrid variants.

### NPC Tiers

##### NPC Resources by Tier
| Tier | HP | Max Mana / Regen | Example Armor |
|:---|:---:|:---|:---|
| Minion | 1-5 | 30 / 3 | None (Phys DR 0, Magic DR 0) |
| Regular | 75 | 30 / 3 | Cloth (Phys DR 0, Magic DR 4) or Light |
| Enemy / Ally | 100 | 100 / 15 | Medium (Phys DR 3, Magic DR 1) |
| Mini Boss | 120 | 100 / 15 | Heavy (Phys DR 4, Magic DR 0) |
| Boss | 175 | 100 / 20 | Enchanted (Phys DR 3, Magic DR 3) |

##### NPC Attributes by Tier
| Tier | Body | Mind | Social | Magic | Sanity |
|:---|:---:|:---:|:---:|:---:|:---:|
| Minion | +0 | +0 | +0 | +0 | +0 |
| Regular | +1 | +1 | +1 | +1 | +1 |
| Enemy / Ally | +4 | +1 | +3 | -3 | +0 |
| Mini Boss | +5 | +4 | -3 | +0 | -2 |
| Boss | +5 | +3 | +0 | +5 | -5 |

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
**TODO:** Add encounter-building procedure, XP awards by enemy tier, and guidance for mixing tiers in one encounter.
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

You spend XP **between sessions**. XP buys two things: new skills and skill rank increases.

**Buying a new skill** costs a flat amount. The skill starts at Rank 1.

**Raising a skill's rank** costs XP that increases exponentially from Rank 1 to Rank 10. Early ranks are cheap. Late ranks are expensive. This means spreading XP across many skills gives you breadth, while focusing XP on a few skills gives you depth. Both strategies are viable.

**Support Skill Slots** unlock as a skill's rank increases. A Rank 1 skill has 1 slot. Every other rank after that (Rank 2, 4, 6, 8, 10) opens another, to a maximum of 5 slots per skill.

{{descriptive
**TODO:** Add the full XP cost table (acquisition cost + rank 1-10 costs) and XP awards per enemy tier, exploration, and social encounters.
}}

\column

### Masteries

Masteries are specializations that unlock when your **total lifetime XP** reaches certain thresholds. At each threshold, you gain Mastery points to spend on Mastery Skills. Mastery points are finite. You will have fewer points than available Mastery Skills, so you must choose which Masteries to invest in.

Masteries function like skills, not classes. They define a specialization (a school of magic, a combat discipline, a social archetype) through mechanics, not through role restrictions.

{{descriptive
**TODO:** Add Mastery XP thresholds, Mastery point budget, and the Mastery Skill list.
}}

### Between Sessions

Between sessions, you can update any part of your character that the rules mark as changeable (see Character Creation, Step 7). With GM confirmation, you can:

- Swap active skills (remember: 10 active at a time, see Attributes and Skills).
- Socket or change Support Skills on your active skills.
- Change Masteries using the same rules as skill swaps.
- Change weapons and armor from your inventory.
- Spend or gain money and resources.
- Record new languages your character has learned.

{{footnote Advancement, Mastery, and Between Sessions}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 12: RUNNING THE GAME -->

# Running the Game

This chapter is for the GM. It covers how to set difficulty, interpret roll results, and manage the boundary between player and GM control.

### Setting DCs

When a player attempts a Skill Check, you set the **Difficulty Class (DC)**. Start with a baseline that reflects the task's inherent difficulty, then adjust it based on the character's circumstances.

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

A roll is only needed when the outcome is uncertain. If the task is trivial for the character, describe the success. If the task is impossible, describe the failure.

\column

### The Degree of 5

After a Skill Check, read the result using the **Degree of 5** scale. The gap between the result and the DC determines how much the outcome swings beyond a basic success or failure.

##### Degree of 5 Scale
| Gap | Outcome |
|:---|:---|
| Beat DC by 10+ | Strong success with a major bonus. |
| Beat DC by 5-9 | Success with a minor bonus. |
| Within 4 of DC (above or below) | Baseline result. Success if met, failure if missed. No extra swing. |
| Miss DC by 5-9 | Failure with a minor setback. |
| Miss DC by 10+ | Failure with a major setback. |

The Degree of 5 applies to all Skill Checks. It does not apply to Combat Rolls (those are binary hit-or-miss against AC).

{{note
**Example:** A player rolls Speech to negotiate a ceasefire. DC 14. They roll 21. That beats the DC by 7, which earns a minor bonus. The enemy agrees to the ceasefire and offers a concession the player did not ask for. If the player had rolled 25, beating by 11, the enemy might surrender entirely.
}}

{{footnote Running the Game}}
{{pageNumber,auto}}

\page

### Player Control vs. GM Control

Keep a clear boundary between what the player decides and what the system or GM decides.

**Players control:** skills, Mastery Skills, equipment, weapons, spells, money, resources, languages, and which actions to take on their turn.

**The GM or system controls:** status effects, environmental effects, lingering injuries, long-term curses, madness, reputation changes, and NPC behavior.

When a temporary effect changes a character's stats (a spell boosts health, a curse reduces Body), track it as a separate layer on the character sheet. Do not overwrite the character's permanent values. When the effect ends, the original values should be easy to restore.

### Building NPCs

Pick an NPC tier from the table in NPCs, Enemies, and Encounters. Choose martial, caster, or hybrid to set the NPC's background. Assign skills, equipment, and spells from the same lists players use. NPCs follow the same rules in combat, conversation, and exploration.

Use NPCs to drive the gameplay loop. Every NPC should have a goal: protect the gate, steal the shipment, negotiate the treaty, survive the night. The goal tells you how the NPC acts on its turn and what it does between encounters.

{{descriptive
**TODO:** Add encounter pacing guidance, DC calibration examples across tiers, and adjudication advice for edge cases.
}}

{{footnote Running the Game}}
{{pageNumber,auto}}

\page

<!-- CHAPTER 13: REFERENCE AND PLAYTEST TOOLS -->

# Reference and Playtest Tools

This chapter collects quick-reference tables and playtest materials. Use these at the table when you need to look something up without flipping through the full chapters.

### Quick Reference: Core Rolls

| Roll Type | Formula | Compare Against |
|:---|:---|:---|
| Combat Roll (physical) | 2d10 + Body | Target's Physical AC |
| Combat Roll (spell) | 2d10 + Magic | Target's Magical AC |
| Skill Check | 2d10 + Skill Modifier | DC set by GM |
| Initiative | 1d10 + Body or Magic | Ranked highest to lowest |

### Quick Reference: Armor Tiers

| Tier | Physical DR | Magic DR | Total DR |
|:---|:---:|:---:|:---:|
| Cloth | 0 | 4 | 4 |
| Light | 1 | 3 | 4 |
| Medium | 3 | 1 | 4 |
| Heavy | 4 | 0 | 4 |
| Enchanted | 3 | 3 | 6 |

**Physical AC** = Physical DR + Body. **Magical AC** = Magic DR + Magic. Max DR per type: 4. Max AC: 9.

### Quick Reference: Backgrounds

| Background | HP | Max Mana | Mana Regen / Round |
|:---|:---:|:---:|:---:|
| Caster | 100 | 100 | 15 |
| Martial | 120 | 30 | 3 |
| Hybrid | 110 | 70 | 10 |

\column

### Quick Reference: NPC Tiers

| Tier | HP | Mana (Max / Regen) |
|:---|:---:|:---|
| Minion | 1-5 | 30 / 3 |
| Regular | 75 | 30 / 3 |
| Enemy / Ally | 100 | 100 / 15 |
| Mini Boss | 120 | 100 / 15 |
| Boss | 175 | 100 / 20 |

### Quick Reference: Mana Cost Anchors

| Benchmark | Mana |
|:---|:---:|
| Cheapest spell | 8 |
| Most expensive 1-action spell | 44 |
| Most expensive 3-action spell | 132 |

### Quick Reference: Damage Dice by Mana Cost

| Mana Cost | Die |
|:---:|:---:|
| 1 | d6 |
| 2 | d8 |
| 3 | d10 |
| 5 | d12 |

### Quick Reference: Degree of 5

| Gap | Outcome |
|:---|:---|
| Beat DC by 10+ | Strong success, major bonus |
| Beat DC by 5-9 | Success, minor bonus |
| Within 4 | Baseline result |
| Miss DC by 5-9 | Failure, minor setback |
| Miss DC by 10+ | Failure, major setback |

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

### Playtest Checklist

Use this checklist to verify a session covers the core systems.

**Character creation:**

- Can you assign a race and record racial traits?
- Can you distribute 5 attribute points with zero remaining?
- Can you choose a background and record HP and mana?
- Can you select skills and choose secondary attributes?
- Can you equip armor and weapons?

**Combat:**

- Does initiative produce a clear turn order?
- Can each character take 3 actions per turn?
- Does the attack sequence (roll vs. AC, damage minus DR, apply tags) resolve cleanly?
- Do stacks track, damage, and decay correctly?
- Does the dying system produce the expected tension?

**Spellcasting:**

- Can a caster build a spell by filling all 9 parameters?
- Does the action cost (highest column) calculate correctly?
- Does the total mana cost match the sum of all parameters plus function?
- Do damage dice match the mana-to-die table?

**Social and exploration:**

- Can the GM set a DC and interpret results using the Degree of 5?
- Do exploration and social encounters award XP?

\column

### Glossary of Game Terms

| Term | Definition |
|:---|:---|
| AC (Armor Class) | The target number an attacker must meet or beat to land a hit. Physical AC and Magical AC are calculated separately. |
| Action | One of 3 things you do on your turn: Attack, Cast a Spell, Move, Drink a Potion, Interact, or Use a Skill. |
| Advantage | Roll 3d10 instead of 2d10 and drop the lowest die. |
| AOE (Area of Effect) | A spell targeting an area rather than specific creatures. All creatures in the area are affected. |
| Attribute | One of 5 core stats (Body, Mind, Social, Magic, Sanity) ranging from -5 to +5. |
| Background | Caster, Martial, or Hybrid. Sets starting HP, max mana, and mana regeneration rate. |
| Combat Roll | 2d10 + Body (physical/martial) or 2d10 + Magic (spells) compared against the target's AC. |
| Condition | An ongoing effect applied by tags. Conditions use stacks that build and decay over time. |
| Critical Failure | Both dice show 1 (natural 2). The effect backfires or misfires. |
| Critical Success | Both dice show 10 (natural 20). The effect lands at its best possible outcome. |
| DC (Difficulty Class) | The target number for a Skill Check, set by the GM based on the task's difficulty. |
| Degree of 5 | The scale measuring how far above or below the DC a Skill Check lands. Gaps of 5 or 10 add bonuses or setbacks. |
| Disadvantage | Roll 3d10 instead of 2d10 and drop the highest die. |
| DR (Damage Reduction) | A flat number subtracted from damage after a hit lands. Physical DR and Magic DR are separate. |

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}

\page

##### Glossary (continued)

| Term | Definition |
|:---|:---|
| Escalation | When a stack type reaches 5, it triggers a stronger escalated condition (e.g., 5 Acid stacks trigger Corroded). |
| GM (Game Master) | The player who describes the world, controls NPCs, sets DCs, and adjudicates the rules. |
| HP (Hit Points) | How much damage a character can absorb. At 0 HP, the character is incapacitated. |
| Incapacitated | A character at 0 HP who cannot take actions, move, or use reactions. |
| Initiative | 1d10 + Body or Magic. Determines turn order at the start of combat. |
| Mana | The resource spent to cast spells. Regenerates at the start of your turn each round. |
| Mastery | A specialization unlocked by total XP thresholds. Grants Mastery points spent on Mastery Skills. |
| Melee Reach | The distance (default 5 feet) within which a creature can make melee attacks and trigger opportunity attacks. |
| Modifier | A number from -5 to +5 added to a dice roll to produce a result. |
| NPC (Non-Player Character) | Any character controlled by the GM. Uses the same rules as player characters. |
| Opportunity Attack | A reaction triggered when a creature leaves an enemy's melee reach. |
| Reaction | 1 per round. An action taken in response to another creature's action. Refreshes at the start of your turn. |
| Round | One full cycle of turns for all combatants. Represents 3 seconds of in-world time. |
| Skill | A trained capability (Athletics, Stealth, Speech, etc.) used for non-combat actions. 10 active at a time. |
| Skill Check | 2d10 + Skill Modifier vs. DC. Used when an uncertain non-combat action is attempted. |
| Skill Modifier | Primary attribute + chosen secondary attribute for a given skill. Permanent once set. |
| Stack | A condition counter. 1 per hit, +1 damage per stack per round, 2-round decay, caps at 5. |
| Support Skill | An augment socketed into a skill that modifies its behavior. Slots unlock as skill rank increases. |
| Tag | A mechanical label (Burn, Bleed, Force, etc.) on a weapon, spell, terrain, or ability. Tags determine which conditions apply. |
| Turn | The portion of a round in which one combatant acts. You get 3 actions on your turn. |
| XP (Experience Points) | Earned from encounters, spent between sessions to buy skills and raise skill ranks. |

{{descriptive
**TODO:** Add sample character builds (3 prebuilt characters: martial, caster, hybrid) with full sheets.
}}

{{footnote Reference and Playtest Tools}}
{{pageNumber,auto}}
