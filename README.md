# Deterministic Inventory Models

Inventory simulation for people who like seeing what happens before it happens.

---

## Overview

A deterministic inventory simulation toolkit. Models how different ordering policies and lead times affect inventory levels over time. Code in modules, visuals in notebooks.

## The Setup

- Demand is constant (boring but predictable)
- Orders go out every T days
- Receipts show up after LD days
- Negative inventory = stockout (we keep it simple)

## Parameters

-Parameter | What It Is |

- D | Annual demand |
- D_day | Daily demand |
- T | Order cycle (days) |
- Q | Order quantity |
- LD | Lead time (days) |

## Scenarios

**1. LD = 1 day** — Smooth sawtooth. Inventory hits zero, receipt arrives next day. No drama.

**2. LD = 2 days** — Same policy, longer wait. Inventory goes negative. Timing is the problem.

**3. LD = 2, bigger Q** — Order more to cover the gap. Fixes stockouts, but average inventory climbs. Treats symptom, not cause.

**4. LD = 2, order earlier** — Order when inventory hits ROP = D_day × LD. Clean sawtooth returns. No excess, no stockouts.

**5. EOQ, LD = 1** — Classic formula. Minimizes ordering + holding cost. Average inventory sits at Q*/2.

**6. Stochastic demand, LD = 5** — Demand varies. Fixed cycle alone won't cut it. Safety stock enters the chat.

## Getting Started

```bash
git clone https://github.com/KrrishKoulia/Deterministic-Inventory-Models.git
cd Deterministic-Inventory-Models
pip install -r requirements.txt
jupyter notebook notebooks/inventory_analysis.ipynb
