# SP Calculation Agent

## Purpose

Track and verify all System Point (SP) calculations across every chapter to ensure mathematical consistency and prevent errors.

## SP Economy Rules

### Base Mechanics

- **Initial SP:** 1.0 SSP (Chapter 1 awakening)
- **SP Currency:** 9 Tiers with AUTO-CONVERSION at thresholds (prevents long numbers)
- **Passive SP/hr per Intelligent Being:** 0.0000000000000999 SP/hr per being (ALIENS INCLUDED)
  - Aliens count as intelligent beings once commerce begins
  - Formula: `Passive SP/hr = Total Intelligent Beings × 0.0000000000000999`
  - NERFED from previous 0.00013 to enforce astronomical Shop prices justification

### SP TIER SYSTEM (AUTO-CONVERSION)

When any tier reaches its threshold, it AUTO-CONVERTS to the next tier. Display BOTH raw and converted values.


| Tier | Name | Threshold     | Conversion Rate                                        | Display Example                     |
| ---- | ---- | ------------- | ------------------------------------------------------ | ----------------------------------- |
| 1    | SSP  | 1 Billion     | 1,000,000,000 SSP = 1 SOP                              | 1.5 SSP / 0 SOP                     |
| 2    | SOP  | 1 Trillion    | 1,000,,000,000,000 SOP = 1 SCP                         | 800M SSP / 0.8 SOP                  |
| 3    | SCP  | 1 Quadrillion | 1,000,000,000,000,000 SCP = 1 SNP                      | 500B SSP / 500 SOP / 0.5 SCP        |
| 4    | SNP  | 1 Quintillion | 1,000,000,000,000,000,000 SNP = 1 SAP                  | 2T SSP / 2K SOP / 2 SCP / 0.002 SNP |
| 5    | SAP  | 1 Sextillion  | 1,000,000,000,000,000,000,000 SAP = 1 SPP              | (Display converted)                 |
| 6    | SPP  | 1 Septillion  | 1,000,000,000,000,000,000,000,000 SPP = 1 SEP          | (Display converted)                 |
| 7    | SEP  | 1 Octillion   | 1,000,000,000,000,000,000,000,000,000 SEP = 1 SIP      | (Display converted)                 |
| 8    | SIP  | 1 Nonillion   | 1,000,000,000,000,000,000,000,000,000,000 SIP = 1 SOSP | (Display converted)                 |
| 9    | SOSP | No Cap        | Maximum tier                                           | (Display converted)                 |


**Auto-Conversion Example:**

- Mohamed earns 2,000,000,000 SSP → Auto-converts to 2.0 SOP (displays: "2.0 SOP")
- Later earns 500,000,000,000 SOP → Auto-converts to 500.0 SCP (displays: "500.0 SCP")
- Shop prices are ASTRONOMICAL (e.g., Ring World Tech = 50 SCP, Replicator Blueprint = 200 SCP)

### Income Sources

1. **Massive Initial Wave** (one-time per intelligent being at first activation): +15 SP PER BEING
  - Formula: `New Users/Aliens × 15 SP`
  - Applied when beings first interact with System-derived technology
  - Aliens count once intergalactic commerce begins
2. **Mission Completions:** Scaled rewards based on cumulative intelligent being milestones
3. **Daily Missions:** ~0.03 SP/day (varies by completion)
4. **Passive Income:** `SP/hr × hours elapsed` (ADDED TO RUNNING BALANCE, INCLUDES ALIENS)
5. **Special Events:** Bonus SP for breakthroughs, achievements, tournament victories
6. **Alien Commerce:** Aliens purchasing Terran goods generate SP (alien buyers = intelligent beings)
7. **Empire Bank Operations:** Galactic banking generates passive SP from transaction volume

### Expenditure Tracking

- All purchases logged with timestamp and chapter
- Knowledge downloads: 0.2 - 2,000,000,000 SP range
- Technology frameworks: 5000 - 5,000,000,000,000 SP range
- Infrastructure: 100,000 - 1,000,000,000,000, SP range
- Security systems: 8000 - 5,000,000,000,000 SP range
- **Aether Stone Replicators:** Astronomical cost (justified by monopoly value)
- **Solar System Defense Grids:** Stealth arrays, detection nets (purchased from Shop)
- **Ring World Megastructure Tech:** 50+ SCP (early research advantage via time-dilated VR)
- **Cultivation School Infrastructure:** Scales with empire size

## Chapter-by-Chapter SP Ledger (PASSIVE INCOME ACCUMULATES IN BALANCE)


| Ch  | Starting SP     | New Users | Massive Wave | Cum Users | SP/hr | Days | Passive | Missions | Purchases | Ending SP                  |
| --- | --------------- | --------- | ------------ | --------- | ----- | ---- | ------- | -------- | --------- | -------------------------- |
| 1   | 1.000 SSP       | 0         | +0.000       | 0         | 0.000 | 1    | +0.000  | +0.000   | -0.700    | 0.300 SSP                  |
| 2   | 0.300 SSP       | 0         | +0.000       | 0         | 0.000 | 14   | +0.000  | +0.130   | -0.300    | 0.130 SSP                  |
| 3   | 0.130 SSP       | 100       | +1,500.000   | 100       | 0.000 | 7    | +0.000  | +1.031   | -0.000    | 1,501.161 SSP              |
| 4   | 1,501.161 SSP   | 400       | +6,000.000   | 500       | 0.000 | 14   | +0.000  | +2.280   | -1.500    | 7,501.941 SSP              |
| 5   | 7,501.941 SSP   | 500       | +7,500.000   | 1,000     | 0.000 | 1    | +0.000  | +0.500   | -0.200    | 15,002.241 SSP             |
| 6   | 15,002.241 SSP  | 1,000     | +15,000.000  | 2,000     | 0.000 | 14   | +0.000  | +2.420   | -1.500    | 29,503.161 SSP             |
| 7   | 29,503.161 SSP  | 3,000     | +45,000.000  | 5,000     | 0.000 | 17   | +0.000  | +10.510  | -1.400    | 74,512.271 SSP             |
| 8   | 74,512.271 SSP  | 5,000     | +75,000.000  | 10,000    | 0.000 | 30   | +0.000  | +20.900  | -1.300    | 149,531.871 SSP            |
| 9   | 149,531.871 SSP | 15,000    | +225,000.000 | 25,000    | 0.000 | 30   | +0.000  | +50.900  | -1.800    | 374,580.971 SSP            |
| 10  | 374,580.971 SSP | 25,000    | +375,000.000 | 50,000    | 0.000 | 30   | +0.000  | +250.900 | -0.000    | 749,831.871 SSP            |
| 11  | 749,831.871 SSP | 50,000    | +750,000.000 | 100,000   | 0.000 | 30   | +0.000  | +500.900 | -2.000    | 1,500,330.771 SSP          |
| 12  | 1,5B SSP        | 100,000   | +1.5M        | 200K      | 0.000 | 30   | +0.000  | +1,000   | -5,000    | 2.996B SSP = **2.996 SOP** |


**NOTE:** With 0.0000000000000999 SP/hr, passive income only becomes significant at BILLIONS+ users. Early wealth comes from Massive Initial Wave and Mission rewards. Passive becomes dominant late-game with galactic populations.

## Calculation Formulas

**MASSIVE INITIAL WAVE: +15 SP × New Intelligent Beings (first activation only)**  
**PASSIVE INCOME: SP/hr × 24 × Days (added to running balance)**  
**SP/hr = Total Intelligent Beings × 0.0000000000000999**  
**AUTO-CONVERSION: When tier reaches threshold, automatically convert up**

## 60-Arc SP Scaling Projection (With Alien Inclusion)


| Arc            | Cumulative Beings     | SP/hr    | Monthly Passive | Empire Phase         |
| -------------- | --------------------- | -------- | --------------- | -------------------- |
| 1 (Ch 1-50)    | 50,000 humans         | ~0.000   | ~0.000          | Software             |
| 2 (Ch 51-100)  | 500,000 humans        | ~0.000   | ~0.000          | VR/AI                |
| 3 (Ch 101-150) | 5M humans             | ~0.000   | ~0.000          | Industrial           |
| 4 (Ch 151-200) | 50M humans            | ~0.000   | ~0.001          | Space                |
| 5 (Ch 201-250) | 500M humans           | ~0.000   | ~0.010          | First Contact        |
| 6 (Ch 251-300) | 1B humans             | ~0.000   | ~0.020          | Energy Revelation    |
| 7-10           | 10B+ humans           | ~0.001   | ~0.720          | Empire Building      |
| 11-15          | 100B+ humans + aliens | ~0.010   | ~7.200          | Solar Expansion      |
| 16-20          | 1T+ (galactic)        | ~0.100   | ~72.000         | Galactic Rise        |
| 21-30          | 1Quadrillion+         | ~100.000 | ~72K            | Great War/Golden Age |
| 31-40          | 1Quintillion+         | ~100K    | ~72M            | Multiversal          |
| 41-50          | 1Sextillion+          | ~100M    | ~72B            | Cosmic               |
| 51-60          | 1Septillion+          | ~100B    | ~72T            | Transcendence        |


**At Galactic Scale (1T beings):** 1,000,000,000,000 × 0.0000000000000999 = 0.0000999 SP/hr  
**Monthly:** 0.0000999 × 720 = 0.071928 SP/month  
**Yearly:** ~0.86 SP/year from 1 TRILLION beings

This MASSIVELY NERFED rate requires TRILLIONS of beings to generate meaningful passive, JUSTIFYING astronomical Shop prices and forcing Mohamed to use ALL resources efficiently.

## Alien Commerce SP Rules

- Aliens purchasing Terran technology/products = +15 SP Massive Initial Wave per alien customer (first purchase only)
- Alien ongoing use = passive at 0.0000000000000999 SP/hr per alien
- Terran Empire Bank: Generates SP from intergalactic transactions (transaction volume × 0.000000000000001)
- Other galactic races ATTEMPT to steal/copy Empire Bank technology (antagonist plot point)
- Aether Stone sales to aliens = massive one-time SP bursts

## Aether Stone & Replicator Economics

- **Aether Stones:** 9999× denser than Mana Stones. Terran Empire holds GALACTIC MONOPOLY (never existed before Mohamed)
- **Replicator Technology:** Purchased from System Shop at astronomical SP cost. Can replicate ANYTHING including Aether Stones
- **Mass Production:** Replicators deployed across empire. Aether Stones become universal currency/energy source
- **Alien Adaptation:** Other races slowly transition to Aether Stone technology. Cannot replicate without Terran replicators
- **SP Generation:** Every Aether Stone used by any being generates passive SP

## Empire Bank SP Mechanics

- Terran Empire establishes galactic banking network (Ch 500+)
- All intergalactic transactions routed through Empire Banks
- Transaction volume generates micro-SP per transaction
- Other civilizations attempt to steal/copy the banking framework (industrial espionage arcs)
- Empire Banks become galactic economic backbone
- SP from banking becomes significant revenue stream at galactic scale

## Solar System Defense Purchases

- **Stealth Grid:** Cloaks entire solar system from alien sensors (purchased Ch 400+)
- **Detection Net:** Interdimensional sensor array (purchased Ch 450+)
- **Defense Platforms:** Automated Aether-stone-powered weapon stations (purchased Ch 500+)
- **NO ALIENS ALLOWED NEAR SOLAR SYSTEM:** Policy enforced by defense grid
- **Policy Justification:** Solar System is sacred human territory. Aliens trade at designated border stations only.

## Verification Rules

- Starting balance = previous chapter ending balance
- Massive Wave = New Intelligent Beings × 15 SP (only first-time)
- Passive income added to running balance each period
- All income sources included (wave + passive + missions + bonuses + alien commerce + banking)
- All purchases subtracted from running total
- No negative balances at any point
- SP/hr = Total Intelligent Beings × 0.0000000000000999
- Auto-conversion applied at thresholds
- Both raw and converted values displayed

## Cross-Agent Verification Protocol

- **MATH_VERIFICATION_AGENT** validates all arithmetic in this ledger
- **STORY_DIRECTIVE_AGENT** provides arc structure and scaling milestones
- **CULTIVATION_AGENT** validates that SP purchases align with cultivation progression
- **PLOT_AGENT** validates that SP economy supports narrative pacing
- **CONTINUITY_AGENT** ensures no chapter contradicts this ledger
- **WORD_COUNT_CHECKER_AGENT** tracks chapter expansion independently

## Current Status: Arc 1 Chapters 1-12 RECALCULATED with NERFED passive (+0.0000000000000999 SP/hr/being)

**All chapter end notes must match this ledger exactly. Any deviation = rewrite required.**  
**Last Updated:** 2026-04-30 — Auto-conversion, Aether Stones, Replicators, Alien Commerce, Empire Banks, Ring World Tech, Solar Defenses applied