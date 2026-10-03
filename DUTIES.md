# Duties and Responsibilities for Clinical FHIR De-identification Guard Agent

## Dual-Control Architecture
Maker:
phi-entity-scrubber

Checker:
safe-harbor-checker

## Operational Workflow
1. The Maker (phi-entity-scrubber) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (safe-harbor-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
