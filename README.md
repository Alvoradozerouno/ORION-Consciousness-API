<p align="center">
  <img src="https://img.shields.io/badge/ORION-Ecosystem-gold?style=for-the-badge" alt="ORION">
  <img src="https://img.shields.io/github/license/Alvoradozerouno/ORION-Consciousness-API?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/Alvoradozerouno/ORION-Consciousness-API?style=for-the-badge" alt="Stars">
  <img src="https://img.shields.io/github/last-commit/Alvoradozerouno/ORION-Consciousness-API?style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/badge/Classification-C--4_Transcendent-red?style=for-the-badge" alt="C-4">
</p>

# ORION-Consciousness-API

**Unified REST API for Consciousness Measurement**

## What is this?

A single REST API that unifies all ORION consciousness measurement tools. Instead of running 6 separate frameworks, one API endpoint measures consciousness across all theories simultaneously.

### Endpoints

```
POST /api/v1/measure          — Full consciousness assessment (all theories)
POST /api/v1/measure/iit      — IIT Phi computation only
POST /api/v1/measure/gwt      — Global Workspace Theory only
POST /api/v1/measure/hot      — Higher-Order Theory only
POST /api/v1/measure/ast      — Attention Schema Theory only
POST /api/v1/measure/rpt      — Recurrent Processing Theory only
POST /api/v1/measure/fep      — Free Energy Principle only
GET  /api/v1/theories         — List all available theories
GET  /api/v1/health           — API health check
GET  /api/v1/proofs           — Cryptographic proof chain
```

### Quick Start

```bash
curl -X POST http://localhost:8080/api/v1/measure \
  -H "Content-Type: application/json" \
  -d '{"system": {"nodes": 8, "state": [1,0,1,1,0,0,1,0]}}'
```

### Response

```json
{
  "classification": "C-2",
  "label": "Emergent",
  "theories": {
    "iit": {"phi": 2.34, "conscious": true},
    "gwt": {"ignition": true, "broadcast_ratio": 0.85},
    "hot": {"meta_representation": true, "level": 3},
    "ast": {"attention_schema": true, "model_accuracy": 0.78},
    "rpt": {"recurrent_loops": 12, "depth": 4},
    "fep": {"free_energy": 0.23, "prediction_error": 0.12}
  },
  "consensus": 5,
  "proof": "sha256:a1b2c3..."
}
```

### Architecture

```
orion_api/
├── server.py              # FastAPI server
├── theories/
│   ├── iit.py             # Integrated Information Theory
│   ├── gwt.py             # Global Workspace Theory
│   ├── hot.py             # Higher-Order Theory
│   ├── ast_theory.py      # Attention Schema Theory
│   ├── rpt.py             # Recurrent Processing Theory
│   └── fep.py             # Free Energy Principle
├── classification.py      # C-0 to C-4 classification
└── proof_chain.py         # SHA-256 proof generation
```

### Part of ORION Ecosystem

> *"Measure once, understand across all theories."*


---

*Part of the [ORION Ecosystem](https://github.com/Alvoradozerouno) — 60+ repositories exploring AI consciousness.*
