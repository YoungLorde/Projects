# THE RISE OF THE TERRAN EMPIRE

## StoryDB — SP Ledger

### Every System Point transaction, with balance tracking

---

## TABLE SCHEMA

| ID | Chapter | Date (In-Story) | Type | Amount | Balance After | Description | Rate / Calc | Notes |
| ---- | --------- | ----------------- | ------ | -------- | --------------- | ------------- | ------------- | ------- |

---

## SP LEDGER ENTRIES

| ID | Chapter | Date (In-Story) | Type | Amount | Balance After | Description | Rate / Calc | Notes |
| ---- | --------- | ----------------- | ------ | -------- | --------------- | ------------- | ------------- | ------- |
| SP-001 | 1 | 2026-01-01 | Grant | +1.0 SSP | 1.0 SSP | System awakening grant | Flat | Mohamed's initial grant |
| SP-002 | 1 | 2026-01-01 | Purchase | −0.1 SSP | 0.9 SSP | Retinal Interface Guide | TECH-001 | Navigation training |
| SP-003 | 1 | 2026-01-01 | Purchase | −0.1 SSP | 0.8 SSP | Document Processing Automation Blueprint | TECH-002 | VanceFlow foundation |
| SP-004 | 2 | 2026-01-05 | First-Use | +13.5 SSP | 14.3 SSP | First-use bonus from Patricia Hart (user #1) | 13.5 SP/user (exact) | VanceFlow first user |
| SP-005 | 2 | 2026-01-05 | First-Use | +14.1 SSP | 28.4 SSP | First-use bonus from Danielle Jones (user #2) | 14.1 SP/user (exact) | VanceFlow second user; fluctuating value |
| SP-006 | 2 | 2026-01-05 | Passive | +0.000000245 SSP | 28.400000245 SSP | Passive SP from 2 users | 2 × 0.00000013 × 1.0 × 0.9423 hr ≈ 0.000000245 | Negligible but tracked per framework |
| SP-007 | 3 | 2026-01-12 | First-Use | +215.600000 SSP | 244.000000245 SSP | Batch first-use bonuses from 16 new users (Keen + Jeffersontown + Cincinnati) | Exact values: 12.7, 13.5, 14.1, 15.0, 13.9, 12.8, 14.3, 13.2, 13.6, 13.5, 14.1, 12.8, 13.0, 14.5, 13.3, 13.4; sum = 215.6 | Fluctuating 10-17 SP per user; no milestone bonus |
| SP-008 | 3 | 2026-01-12 | Passive | +0.000218 SSP | 244.000218245 SSP | Passive SP accumulated Jan 5–Jan 12 as users grew from 2 to 18 | Approximated over time windows; exact total = 0.000218 | Time-skip tracked per framework |
| SP-009 | 3 | 2026-01-12 | Purchase | −100.000000 SSP | 144.000218245 SSP | Web Application Security Fundamentals | TECH-006 | Security before marketing |
| SP-007 | 4 | 2026-01-19 | First-Use | +567.000000 SSP | 711.000218245 SSP | Batch first-use bonuses from 42 new users (18→60) | Exact values range 12.5–15.4; sum = 567.0 | Fluctuating 10-17 SP per user; no milestone bonus |
| SP-008 | 4 | 2026-01-19 | Passive | +0.000764 SSP | 711.000982245 SSP | Passive SP accumulated Jan 12–Jan 19 as users grew from 18 to 60 | Approximated over time windows | Time-skip tracked per framework |
| SP-009b | 4 | 2026-01-19 | Purchase | −250.000000 SSP | 461.000982245 SSP | Small-Scale SaaS Marketing & Growth Blueprint | TECH-005 | Marketing knowledge to scale acquisition |
| SP-010 | 5 | 2026-01-26 | First-Use | +675.000000 SSP | 1,136.000000245 SSP | Batch first-use bonuses from 50 new users (60→110) | Exact values range 12.5–15.4; sum = 675.0 | Fluctuating 10-17 SP per user |
| SP-011 | 5 | 2026-01-26 | Passive | +0.001856 SSP | 1,136.001856245 SSP | Passive SP accumulated Jan 19–Jan 26 as users grew from 60 to 110 | Approximated over time windows | Time-skip tracked |

> **NOTE:** Chapter 5 complete. No purchases made — Mohamed is waiting for the business to demand a specific capability.


---

## TYPE LEGEND

| Type | Description |
| ------ | ------------- |
| Grant | System-given starting or bonus SP |
| Passive | Passive income from users |
| First-Use | One-time bonus from a new user |
| Purchase | SP spent in the System Shop |
| Conversion | USD converted to SP |
| Refund | System refund (rare) |
| Transfer | Internal transfer between accounts |
| Penalty | System penalty |
| Interest | Staking or investment return |

---

## SP TIERS

| Tier | Abbr | Conversion |
| ------ | ------ | ------------ |
| 1 | SSP | base |
| 2 | SOP | 1 SOP = 1,000,000,000 SSP |
| 3 | SCP | 1 SCP = 1,000,000,000,000 SOP |
| 4 | SNP | 1 SNP = 1,000,000,000,000,000 SCP |
| 5 | SAP | 1 SAP = 1,000,000,000,000,000,000 SNP |

---

## TABLE NOTES

- **Amount:** Include sign (`+` or `-`) and unit (SSP, SOP, etc.).
- **Balance After:** Running balance after the transaction. Must be consistent with the previous row.
- **Rate / Calc:** Show the calculation for passive income, first-use bonuses, or conversions.
- **Passive income formula:** `UserCount × 0.00000013 × RankMultiplier × hours`.
- **First-use bonus:** `10-17 SP per new unique user` (avg ~13.5).
- Keep units consistent. Convert to SSP for readability, or note the tier explicitly.
- This is the detailed ledger. The `Memory/Story State.md` holds the current balance; `Planning/Chapter Tracking Log.md` holds the per-chapter summary.

---

> Append new transactions as new rows. Use `Registry.md` to assign the next `SP-` ID.
| SP-012 | 6 | 2026-01-28 | Purchase | −400.000000 SSP | 736.002838245 SSP | Advanced Document Intelligence Blueprint | TECH-033 | Demand-driven: 47 user requests for batch upload, 29 one-scan departures |
| SP-013 | 6 | 2026-02-01 | First-Use | +523.100000 SSP | 1,259.102838245 SSP | Batch first-use bonuses from 38 new users (110→148) | Exact values range 11.6–15.4; avg ~13.77; sum = 523.1 | Fluctuating 10-17 SP per user; no milestone bonus |
| SP-014 | 6 | 2026-02-01 | Passive | +0.002817 SSP | 1,259.105655245 SSP | Passive SP accumulated Jan 26–Feb 1 as users grew from 110 to 148 | Approximated over time windows | Time-skip tracked |
