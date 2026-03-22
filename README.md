# Deterministic Inventory Models

Inventory simulation for people who like seeing what happens before it happens.

---

## Overview

A deterministic inventory simulation toolkit. Models how different ordering policies and lead times affect inventory levels over time. Code in modules, visuals in notebooks. Nothing fancy, just works.

## What's Inside

- Fixed-cycle ordering with configurable lead times
- Baseline, EOQ, and lead-time-aware policies
- Clean separation between simulation logic and visualization
- Metrics for average inventory, stockout days, and cost

## Getting Started

```bash
git clone https://github.com/KrrishKoulia/Deterministic-Inventory-Models.git
cd Deterministic-Inventory-Models
pip install -r requirements.txt
jupyter notebook notebooks/inventory_analysis.ipynb
