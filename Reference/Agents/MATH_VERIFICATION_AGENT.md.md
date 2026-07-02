# MATH VERIFICATION AGENT

## SP Economy, Cultivation Progression, and Numerical Consistency

---

## SP ECONOMY FORMULAS (AUTHORITATIVE)

### Base Passive Income

Passive SP/hr = User_Count × 0.00013 × Rank_Multiplier

Rank Multipliers:

- Rank 0: 1.0
- Rank 1: 1.5
- Rank 2: 2.5
- Rank 3: 4.0
- Rank 4: 7.0
- Rank 5: 12.0
- Rank 6: 25.0
- Rank 7: 50.0
- Rank 8: 100.0
- Rank 9: 250.0

### Massive Initial Wave (One-Time Per User)

Massive_Wave = New_Users × 15 SP per user (first activation ONLY)

- Each user triggers ONCE at first interaction with Mohamed's technology
- Cumulative users do NOT trigger again
- Must track which users are "new" per chapter

### SP Balance Formula

Ending_SP = Starting_SP + Massive_Wave + Passive_Accumulated + Mission_Rewards + Daily_Missions - Purchases - Conversions

### Passive Accumulation

Passive_Accumulated = Average_SP_per_hr × Hours_in_Period

Where Average_SP_per_hr = (Starting_User_Count + Ending_User_Count) / 2 × 0.00013 × Rank_Multiplier

### Daily Mission Income

Daily_Mission_Income = Days × 0.03 SP (base rate, may vary by rank)

### Milestone Rewards


| Users         | Reward       |
| ------------- | ------------ |
| 100           | 1.0 SP       |
| 500           | 2.0 SP       |
| 1,000         | 5.0 SP       |
| 2,000         | 10.0 SP      |
| 5,000         | 20.0 SP      |
| 10,000        | 50.0 SP      |
| 25,000        | 100.0 SP     |
| 50,000        | 250.0 SP     |
| 100,000       | 500.0 SP     |
| 500,000       | 1,000.0 SP   |
| 1,000,000     | 2,500.0 SP   |
| 10,000,000    | 10,000.0 SP  |
| 100,000,000   | 50,000.0 SP  |
| 1,000,000,000 | 250,000.0 SP |


---

## CULTIVATION PROGRESSION FORMULAS

### Wisp Capacity by Rank/Level

Rank 0: NO WISPS (physical preparation only)  
Rank 1 Level N: Capacity = N × (N + 1) / 2 (triangular numbers)

- L1: 1, L2: 3, L3: 6, L4: 10, L5: 15, L6: 21, L7: 28, L8: 36, L9: 45, L10: 55  
Rank 2+: Capacity scales geometrically
- Formula: Base_R1_Capacity × (Rank_Multiplier ^ (Rank - 1))

### Level Progression Time (with Pioneer Trait)

Base_Days_Per_Level = 30 days (without Pioneer)  
Pioneer_Multiplier = 0.05 (20x speed)  
Actual_Days_Per_Level = Base_Days × 0.05 = 1.5 days per level (early ranks)

With Concealment Overhead (-15%): 1.725 days per level  
With Combat/Stress Catalyst (-25%): 1.125 days per level  
With Dual Cultivation (+50%): 0.75 days per level (after Ch 300)

### Rank-Up Requirements

Rank 0 → 1: Level 99 + Pioneer Trait + 100 Wisps  
Rank 1 → 2: Level 99 + 1,000 Wisps  
Rank 2 → 3: Level 99 + 10,000 Wisps  
Rank 3 → 4: Level 99 + 100,000 Wisps  
Rank 4 → 5: Level 99 + 1,000,000 Wisps  
...  
(Each rank: 10x previous wisp requirement)

### Lifespan Extensions

Per Wisp Absorbed: +0.1 years (early ranks)  
Per Level Gained: +0.5 years  
Rank Up: +50 years

---

## VERIFICATION CHECKLIST

Before marking chapter COMPLETE:

- Starting SP matches previous chapter's ending EXACTLY
- New users identified and Massive Wave calculated correctly
- Passive income uses AVERAGE user count over time period
- Passive income uses correct hours in period
- All purchases subtracted
- Ending SP = Starting + Income - Expenses (within 0.001 tolerance)
- Cultivation levels progress at plausible rate for time period
- Wisp count matches capacity for current level
- Lifespan extensions consistent with wisps absorbed
- User growth rate plausible for product/market conditions
- Revenue figures consistent with user count and pricing
- No mathematical contradictions in narrative (dates, ages, timelines)

### Known Persistent Checks

- Chapter 1: 0 users, 0 passive, ending 0.3 SP
- Chapter 2: 0 users, 0 passive, ending ~0.12 SP
- Chapter 3: 100 users, +1,500 Massive Wave, ending ~1,501 SP
- Chapter 4: 400 new users, +6,000 Massive Wave, ending ~8,503 SP
- Chapter 5: 500 new users, +7,500 Massive Wave, ending ~16,003 SP
- Chapter 6: 1,000 new users, +15,000 Massive Wave, ending ~29,571 SP
- Chapter 7: 3,000 new users, +45,000 Massive Wave, ending ~73,366 SP
- Chapter 8: 5,000 new users, +75,000 Massive Wave, ending ~147,789 SP
- Chapter 9: 15,000 new users, +225,000 Massive Wave, ending ~372,678 SP
- Chapter 10: 25,000 new users, +375,000 Massive Wave, ending ~751,289 SP

**Agent Interlocks:** SP_CALCULATION_AGENT, CULTIVATION_ACCELERATION_AGENT, CONTINUITY_AGENT