# Deterministic Inventory Models

This tutorial walks through a simple, deterministic inventory simulation under constant daily demand.  
The goal is to understand how lead time and ordering policy change the shape of inventory on hand (IOH) over time, while keeping the analysis logic in Python modules and the visuals in a Jupyter notebook for teaching.

## Objectives

- Build a clear baseline of fixed-cycle replenishment under constant demand.
- Show how different lead times affect IOH, including stockouts.
- Compare two approaches to dealing with lead time: increasing order quantity versus anticipating orders.
- Keep analysis components packaged in the `inventory` folder while the notebook focuses on storytelling and plots.

## Assumptions

- Demand is deterministic and constant each day.
- Orders are placed on a fixed cycle (every `T` days) unless explicitly stated otherwise.
- Receipts arrive after a fixed lead time (`LD` days).
- No capacity constraints or lost sales modeling in this part (stockouts appear as negative IOH).

## Key Parameters

- `D`: annual demand (units/year)
- `T_total`: number of days in the simulation horizon
- `D_day`: daily demand (`D` divided by `T_total`)
- `T`: cycle length in days (spacing between order placements)
- `Q`: order quantity (often `D_day × T` in the baseline)
- `LD`: lead time in days (order → receipt)
- `initial_ioh`: starting inventory on hand
- Economic parameters defined for later use: unit cost, ordering cost, holding cost rate, selling price, shortage cost

## Scenarios

### Scenario 1 — Lead time = 1 (receive next day)

- `LD = 1` with baseline fixed-cycle ordering.
- Behavior: IOH glides to zero at the cycle boundary; the receipt lands the next day and inventory jumps back up.
- Outcome: no negative IOH; the sawtooth touches zero and then recovers.

### Scenario 2 — Lead time = 2 (receive two days later)

- `LD = 2` baseline fixed-cycle ordering.
- Behavior: the receipt arrives later than needed; IOH becomes negative between the order day and the receipt day.
- Outcome: stockout appears; timing is the root cause.

### Scenario 3 — Keep timing, increase quantity

- `LD = 2` compensate for lead time by increasing `Q = D_day * (T + (LD-1))`
- Behavior: the sawtooth shifts upward; peaks become higher and average IOH rises.
- Outcome: avoids negative IOH but builds excess inventory; higher holding costs and risk of obsolescence.
- Lesson: increasing `Q` treats the symptom (inventory level), not the cause (timing).

### Scenario 4 — Anticipate lead time (lead-time-aware trigger)

- Policy: keep the same cycle length but order earlier so the receipt lands when needed.
- Behavior: the IOH jump realigns with the end of the cycle; the sawtooth stabilizes without excess inventory.
- Interpretation: operationally equivalent to using a reorder point equal to daily demand times lead time (ROP = `D_day × LD`).

### Scenario 5 — EOQ (Economic Order Quantity) with lead time = 1

- Policy: compute the EOQ `Q*` using the classic formula and derive the cycle length `T* = Q* / D_day`.
- Behavior: the sawtooth follows the EOQ cycle — inventory drains from about `Q*` toward zero; with `LD = 1`, IOH touches (or nearly touches) zero at the cycle boundary, then the receipt lands the next day and the level jumps back up.
- Outcome: no negative IOH; average inventory is approximately `Q*/2` (ignoring the one‐day lead‐time dip).
  This setting **minimizes total relevant cost** (ordering + holding) under the deterministic assumptions.

### Scenario 6 — Stochastic demand (Normal) with lead time = 5

- Policy: fixed‐cycle ordering under **random daily demand** (Normal with mean `D_day` and standard deviation `σ = 2.5`)
- Setup (conceptually): keep `Q ≈ D_day × T`, set `LD = 5`, initialize `initial_ioh ≈ Q`. Demand is drawn daily from a Normal distribution and treated as non-negative.
- Outcome: with variability, “timing only” policies are not enough; you need **safety stock** sized for lead-time uncertainty to stabilize service.
