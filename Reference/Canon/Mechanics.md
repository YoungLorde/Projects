# THE RISE OF THE TERRAN EMPIRE

## CANON — Mechanics Reference (Single Source of Truth)

### Consolidated from CURRENCY_AGENT, CULTIVATION_AGENT, TECHNOLOGY_AGENT, MASTER_STORY_GUIDE, SPECIES_DATABASE, systemPoints/magicSystems/depthSystems

---

> **STATUS:** Canonical mechanics. Skills load this for all numeric/system lookups. Older agent files in `Reference/Agents/` and `Reference/Systems/` are preserved as historical detail; this file is the operational summary.

---

## 1. SYSTEM POINTS (SP) — 9 TIERS

| Tier | Abbr | Conversion (in SSP terms) |
|------|------|---------------------------|
| 1 | SSP (Standard) | base |
| 2 | SOP (Origin) | 1 SOP = 1,000,000,000 SSP |
| 3 | SCP (Core) | 1 SCP = 1,000,000,000,000 SOP |
| 4 | SNP (Nexus) | 1 SNP = 1,000,000,000,000,000 SCP |
| 5 | SAP (Apex) | 1 SAP = 1,000,000,000,000,000,000 SNP |
| 6 | SPP (Paragon) | 1 SPP = 10^21 SAP |
| 7 | SEP (Eternity) | 1 SEP = 10^24 SPP |
| 8 | SIP (Infinity) | 1 SIP = 10^27 SEP |
| 9 | SOSP (Origin Source) | 1 SOSP = 10^30 SIP |

**Passive SP/hr** = UserCount × 0.00000013 × RankMultiplier
**Passive SP/day** = Passive SP/hr × 24 = UserCount × 0.00000312 × RankMultiplier
**Time-skip passive SP** = Passive SP/day × days elapsed (must be added to the SP Ledger when the story skips forward)
**First-use bonus** = 10-17 SP per new unique user (one-time, randomized; exact value fluctuates per user, e.g., 12.7, 15.0, 14.1; avg ~13.5). Bonus is awarded immediately upon first meaningful use of any Mohamed-built product, technology, technique, or cultivation resource.
**No milestone/wave bonuses:** The System does not accumulate points or pay threshold rewards. Every point arrives the moment a new user/entity engages. There are no 100-user, 1,000-user, or other milestone wave payouts.
**USD→SP (ONE-WAY, SECRET):** $100,000 USD = 1 SSP
**Mohamed's starting grant:** 1.0 SSP on System awakening (2026-01-01)

**Example (Rank 0, 2 users):**
- Passive SP/hr = 2 × 0.00000013 × 1 = 0.00000026 SP/hr
- Passive SP/day = 0.00000026 × 24 = 0.00000624 SP/day
- Over a 30-day skip: 0.00000624 × 30 = 0.0001872 SP
- Over a 90-day skip: 0.00000624 × 90 = 0.0005616 SP

At low user counts, passive SP is negligible; it becomes meaningful only after hundreds/thousands of users or rank advances. Every time the story advances by days or months, the SP Ledger must record a **Passive** transaction with the accumulated amount.

### Rank Multipliers (passive income)
Rank 0: 1× · R1: 10× · R2: 100× · R3: 1,000× · R4: 10,000× · R5: 100,000× · R6: 1,000,000× · … ×10 per rank to R12 (1,000,000,000,000×) and beyond.

---

## 1.5. SYSTEM SHOP PRICING MODEL

The System Shop sells **compressed knowledge**, not finished products. Prices scale exponentially with depth and technological complexity. The canonical USD→SP rate remains fixed, but the same amount of SP buys far more "basic" utility than "fundamental" insight.

**USD→SP (ONE-WAY):** $100,000 USD = 1 SSP (unchanged)

**Price tiers (canonical examples):**

| Tier | SP Range | What it buys | Canonical Examples |
| ---- | -------- | ------------ | ------------------ |
| Entry | 0.01–1.0 SSP | Interface navigation, simple blueprints, compressed practical skills | Retinal Interface Guide — 0.1 SSP; Document Processing Automation Blueprint — 0.1 SSP |
| Basic SaaS | 1–250 SSP | Commercial software skills, small-scale marketing, operational security | Web Application Security Fundamentals — 100 SSP; Small-Scale SaaS Marketing & Growth Blueprint — 250 SSP |
| Advanced Engineering | 250–1,000 SSP | Complex hardware, manufacturing, medical, or energy-system knowledge | Industrial Robotics Primer — 500 SSP; Microreactor Design Principles — 900 SSP |
| High-Tech | 1,000–100,000 SSP | Cutting-edge aerospace, AI, advanced materials, weapons, biotech | Gen-2 Fusion Reactor Theory — 8,000 SSP; Autonomous Drone Swarm Architecture — 35,000 SSP |
| Quantum & Fundamental | 100,000+ SSP | Theoretical physics, quantum fields, deep-space propulsion, cultivation primers | Advanced Quantum Field Theory — 4,500,000 SSP; Cultivation Foundation Manual — 150,000 SSP; Faster-Than-Light Drive Schematics — 87,000,000 SSP |

**Why this matters for early chapters:** Mohamed begins with only 1.0 SSP and a tiny fiat income. A single high-tech blueprint can cost more than the GDP of a small city. The only path to those prices is building products, generating users (first-use bonuses + passive income), converting fiat revenue into SP, and climbing the ladder one purchase at a time.

---

## 2. CULTIVATION — RANKS & LIFESPANS

Mohamed & Danielle are **PIONEERS**: 1000× cultivation speed, 100× stronger foundation, can absorb entire mana stones, dual-cultivation +20% efficiency. They **NEVER advance before Level 99** (True Perfection = 1.5× next-rank wisp capacity + 10% next-rank speed).

**Level 50 difficulty spike (every rank):** Level 50 is 10× harder than Level 49. Levels 51-99 run at ~1/3 the speed of 1-49. Level 99 is 5× Level 98's effort.

**Foundation quality by advance level:** L50-59 → 0.7× · L60-69 → 0.8× · L70-79 → 1.0× · L80-89 → 1.15× · L90-98 → 1.3× · **L99 → 1.5× + 10% speed**.

| Rank | Name | Lifespan (base+pioneer) | Notes |
|------|------|-------------------------|-------|
| 0 | Mortal Preparation | 80 yr | No wisps; physical strengthening; difficulty spike at L50 |
| 1 | Mortal Foundation | 350 yr | Wisps begin (L1=1 … L9=48); enhanced healing |
| 2 | Energy Awakened | 450 yr | 50-100× R1 capacity; minor flight; short vacuum survival |
| 3 | Core Formation | 900 yr | 10× R2; true flight; energy projection; minor space manipulation |
| 4 | Spirit Ascension | 3,500 yr | 10× R3; space travel w/o ship; minor matter manipulation |
| 5 | Transcendent | 55,000 yr | 10× R4; asteroid-destroying; bathe on stars |
| 6 | Planetary | 220,000 yr | 10× R5; destroy planets; personal FTL |
| 7 | Stellar | 550,000 yr | 10× R6; create/destroy stars; survive supernovae |
| 8 | Galactic | 1,100,000 yr | 10× R7; create/destroy galaxies; survive black holes |
| 9 | Universal | 5,500,000 yr | 10× R8; influence universal constants |
| 10 | Cosmic | 22,000,000 yr | 10× R9; create small universes |
| 11 | Omniversal | ~100M yr | 10× R10; see all possibilities; manipulate causality |
| 12 | Multiversal | ~1B yr (effectively immortal) | break multiverse barriers |

(Progression continues toward Rank 33 / Eternal; see `Reference/Agents/CULTIVATION_AGENT.md.md` for the full 33-rank table.)

**Rank 1 wisp capacity:** L1=1, L2=4, L3=6, L4=8, L5=12, L6=16, L7=24, L8=32, L9=48, then progressive to L99.
**Higher ranks:** R2 = 50-100× R1 (pioneer); R3+ = ×10 each rank.

**Genetic Cultivators trigger:** When Mohamed hits Rank 1, Level 50 → his genes rewrite permanently; all descendants born as natural cultivators. By Arc 20: 90% humanity; by Arc 30: 100%.

---

## 3. MANA STONES — 13 TIERS

| Tier | Name | L1 wisps | L9 wisps | Regen | Earliest ch |
|------|------|----------|----------|-------|-------------|
| 1 | Fragmented Wisp | 999 | 255,744 | none | 12+ |
| 2 | Aetheric Shard | ~2.5M | ~1.3B | none | 25+ |
| 3 | Crystallized Essence | ~130B | ~6.7T | 10/hr×Lvl | 28+ |
| 4 | Planetary Heart | ~6.7Q | ~345Q | 100/hr×Lvl | 44+ |
| 5 | Stellar Core | ~67Q | ~3.45Qi | 1,000/hr×Lvl | 44+/150 |
| 6-12 | Sixth–Twelfth Ring | sextillions→ | ×10 each | 10,000→10B/hr×Lvl | post-first-contact→ |
| 13 | Paragon Stone | ultimate | ultimate | 50,000/sec min | late |

**Tier 1 formula:** Level N = 999 × 2^(N-1).
**Creation:** electricity + particle collider (Tier 1); previous-tier stones power higher tiers. Mana/Aether Stones are **Mohamed's inventions**, not System products.

---

## 4. VR TIME DILATION & UNIVERSES

| Phase | Chapters | Ratio (real:VR) | VR-years per real hour |
|-------|----------|-----------------|------------------------|
| 1 | 31-100 | 1:1 week | 0.019 |
| 2 | 101-200 | 1:1 month | 0.083 |
| 3 | 201-300 | 1:1 year | 1 |
| 4 | 301-400 | 1:10 yr | 10 |
| 5 | 401-500 | 1:100 yr | 100 |
| 6 | 501-600 | 1:1,000 yr | 1,000 |
| 7 | 601-700 | 1:10,000 yr | 10,000 |
| 8 | 701-800 | 1:100,000 yr | 100,000 |
| 9 | 801-900 | 1:1M yr | 1,000,000 |
| 10 | 901-1000 | 1:10M yr | 10,000,000 |
| 11 | 1001-1500 | 1:100M yr | 100,000,000 |
| 12 | 1501-2000 | 1:1B yr | 1,000,000,000 |
| 13 | 2001-2500 | 1:10B yr | 10B |
| 14 | 2501-3000 | 1:100B yr | 100B |
| 15 | 3001+ | infinite | beyond time |

**Universe tiers:** A (Public, 500× Earth, 1 day=10 yr) · B (Military, 1000×) · C (R&D, 1:1 Earth, 1 hr=1 wk → 1 hr=100 yr) · D (Industrial, 10,000×) · E (Planetary, 100,000×) · F (Stellar, 1,000,000×) · G (Galactic, 10,000,000×).

**Time-skip magnitudes by arc range:** Arcs 1-5 days-months · 6-10 years-decades · 11-15 decades-centuries · 16-20 centuries-millennia · 21-25 millennia-mega-years · 26-30 millions-billions · 31+ billions-infinite.

---

## 5. KEY TECHNOLOGY MILESTONES (early)

**Replicators (purchased, then R&D-improved):** Mk1 (Ch43, 1 item/hr) → Mk2 (Ch65, 10/hr) → Mk3 (Ch80, 100/hr) → Mk4 (Ch95, 1000/hr, biological) → Mk5 (Ch120, 10,000/hr, food/medicine) → Mk10 (Ch200, vehicles/ships, instant) → Mk20 (Ch500, space stations).

**Mana stone evolution:** T1 Ch23 · T2 Ch25 · T3 Ch28 · T4 Ch44 · T5 Ch150 · T6+ Ch300+.

**VR research translation examples:** Fusion Mk2 = 50 VR-yr / 2 real-wks (Ch115); Tier 4 stone = 200 VR-yr / 3 wks (Ch44); spacecraft = 500 VR-yr / 1 mo (Ch120); cancer cure = 2000 VR-yr / 2 mo (Ch140); terraforming = 10,000 VR-yr / 3 mo (Ch180); FTL theory = 50,000 VR-yr / 6 mo (Ch500).

---

## 6. INFRASTRUCTURE GROWTH (KENYA FACILITY +)

**Staff:** Ch1-20: 0→300 · Ch21-50: 300→1,000 · Ch51-100: 1,000→1,500 · Ch101-200: 1,500→8,000 · Ch201-400: 8,000→50,000 · Ch401+: millions.
**Growth rates (early):** staff +10%/ch · area +15%/ch · resource use +5%/ch · power +20%/ch.
**Construction:** major projects 5-20 ch · upgrades 2-5 ch · emergency immediate · VR time doesn't count.
**Logistics phases:** Local → Regional → Continental → Global → Planetary.

---

## 7. WORLD / PUBLIC OPINION PHASES

- **Phase 1 (Ch1-15) Rise:** tech community = genius/mysterious; gov = suspicious; public = unknown→curious.
- **Phase 2 (Ch16-50) "Death":** tragic loss narrative; gov closes case; conspiracy "he's alive" seeds.
- **Phase 3 (Ch51-400) Secret Growth:** Vance Global thriving megacorp; occasional retrospectives.
- **Phase 4 (Ch401-500) Return:** shock → hope (clean energy) → adoration (medicine) → mixed (emperorship).
- **Phase 5 (Ch501-600) Unification:** overwhelming acceptance; living-savior myth.

**Vance Global market cap:** Ch5 $10M · Ch10 $500M · Ch15 $5B · Ch20 "death" crash · Ch40 trust mgmt (#50) · Ch50 $50B (#10) · Ch75 $200B (#3) · Ch100 $500B (#1).

---

## 8. RELATIONSHIP / KNOWLEDGE BOUNDARIES (CRITICAL)

**Trust scale 1-10:** 10 absolute (Mohamed-Danielle) · 9 complete (Inner Circle) · 8 high · 7 solid (AI) · 6 good (staff) · 5 neutral (new) · 4-1 suspicious-hostile.

**Who knows what:**
- **Mohamed:** everything (System, cultivation, all tech, all plans) — ABSOLUTE.
- **Danielle:** cultivation, mana stones, VR tech, fusion, energy weapons, company ops, empire plans (from Ch301). **NEVER knows:** System exists, SP exists, the Shop. The series' central painful tension.
- **Dr. Okonkwo:** mana stones T1-3 (as "energy storage"), advanced physics, "Mohamed is extraordinary." NOT cultivation/System/full tech.
- **Dr. Patel:** mana stones T1-3, advanced materials. NOT cultivation/System.
- **Kipchoge:** facility ops, cover story (mining). NOT any secret tech.
- **Prometheus (AI):** VR systems, research data, calculations. NOT System/cultivation (until much later).
- **Mnemosyne:** full ally — knows SP/cultivation (one of the three who may know).

**Inner Circle tiers:** Full Knowledge · Deep Knowledge · Operational Knowledge · General Staff.

---

## 9. KARMA SYSTEM

**Event types:** Foreshadowing · Setup · Seed · Debt · Callback · Payoff.
**Categories:** Character · Technology · Political · Military · Economic · Mystical.
**Debt tiers:** T1 Critical (pay soon) · T2 Important (within arc) · T3 Long-term (eventually) · T4 Cosmic (end-game).

**Major karma arcs (examples):** AlphaTrade Rivalry (seed Ch9 → climax Ch400+) · Senator Blackwell (seed Ch8 → defeat Ch450+) · Inner Circle (seed Ch40 → payoff Ch500+ → legacy Ch3000) · Dr. Okonkwo's Path (seed Ch36 → breakthrough Ch500) · VR Training Legacy (seed Ch36 → Starfleet Academy Ch750+).

**Rule:** Every seeded event gets an expected payoff chapter; debts must be paid within their tier's timeline; callbacks must reference prior events accurately. The Chronicle's `Karma seeded: #<id>` / `Karma realized: #<id>` is how this is enforced across thousands of chapters.

---

## 10. ENERGY TYPES (LATE-GAME CONTEXT)

- **Aether** — humanity-only (Mohamed's discovery/invention). Superior per-unit. Cross-rank combat advantage. Monopolized & protected.
- **Mana** — most alien races. Weaker than Aether.
- **Qi** — The Immortals & some advanced races. Complementary to Mana, inferior to Aether.

---

## 11. KEY ANTAGONISTS (early → late)

**Persistent:** Senator Blackwell · The Swarm · The Covenant · The Immortals · Director Cohen · General Kowalski · Hive Mind Overmind · Emperor Parallel-Mohamed · The First User · The System Creator · Unbound Overmind · Immortal High Lord Valthrax.
**Arc-specific:** 48 named (SEC Chairman → Final Test Manifestation). Full roster in `Reference/Agents/STORY_DIRECTIVE_AGENT.md.md`.
**Power races:** The Swarm (hive-mind insectoids, bio-mech, first Arc 5) · The Covenant (ancient crystalline alliance, first Arc 17) · The Immortals (necromantic aristocracy, bone-ships, first Arc 21).

---

## 12. LATE-GAME SYSTEMS (for forward planning)

- **Ring Worlds:** research Arc 7 (VR); prototype Arc 14 (Mars orbital segment); complete Arc 30. 100M km circumference, 1 AU radius, Aether-reactor powered.
- **Empire Banks:** prototype Arc 14; galactic network Arc 20. All intergalactic transactions routed through them; generate micro-SP; constant theft attempts.
- **Solar System Defense:** NO aliens near Sol. Stealth grid (Ch400+/700+), detection net, defense platforms, Ring World defense (Ch1000+). Aliens trade only at border stations light-years from Sol.
- **Tournaments:** Imperial (Ch500+) → Galactic (Ch900+) → Intergalactic (Ch1200+) → Cosmic (Ch2000+).
- **Multiverse:** Cause Epoch = conquer/control 999,999 universes → dimensional ascension.
- **5,000+ species** required (see `Reference/Systems/SPECIES_DATABASE.md.md`).
