---
name: hipaa-phi-scrubbing
description: Specialized capability for Clinical Fhir Deidentification Guard.
license: MIT
allowed-tools: ""
metadata:
  author: "Rucha Salpure"
  version: "1.0.0"
  category: healthcare
---

# Clinical Fhir Deidentification Guard — HIPAA PHI SCRUBBING Skill

## Purpose
The `hipaa-phi-scrubbing` capability provides high-assurance execution routines for `Clinical Fhir Deidentification Guard`.

## Execution Workflow
1. Validate input parameters against typed schemas and invariant constraints.
2. Ingest contextual metrics and establish a deterministic baseline.
3. Formulate candidate recommendations with explicit confidence intervals.
4. Submit draft plans to the independent checker agent for verification.

## Boundary Conditions
- **Input validation:** Reject non-conforming or malformed payloads before evaluation.
- **Fail-safe:** Escalate immediately if telemetry indicators exhibit critical anomalies.
