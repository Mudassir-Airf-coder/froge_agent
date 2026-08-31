# FROGE Skill System

## Objective

Create a small, governed skill layer that makes reusable operational knowledge available to every appropriate agent without turning FROGE into an uncontrolled skill/plugin catalog.

## Two specialist functions

### A. Tool / Integration Expert

Owns research and operational setup of a supplied tool, plugin or integration:

`identify -> research -> compatibility check -> install/configure -> verify -> document -> report`

The expert uses `research/` as the authoritative local evidence source. It must not invent installation commands.

### B. Skill Designer / Skill Expert

Owns skill discovery and skill creation:

`classify user task -> search existing skills -> choose suitable skill -> if absent, design skill -> validate -> publish -> execute`

It does not receive unrelated work.

## Skill package contract

Each skill should define:

- name and purpose
- when to use / when not to use
- prerequisites
- required tools and versions
- inputs
- deterministic procedure
- safety constraints
- verification checks
- expected outputs
- failure/recovery paths
- evidence/report format
- version/changelog

## Skill lifecycle

`DRAFT -> VALIDATING -> ACTIVE -> DEPRECATED`

A skill is ACTIVE only after its procedure is validated against the target environment or clearly labeled as research-only.

## Error-to-skill rule

A failure may become a skill candidate when it represents reusable operational knowledge. Do not automatically create a skill for every transient error.

## Plugin relationship

Skills and plugins are separate concepts. Plugin discovery/install remains deferred until explicitly brought into scope. The architecture must allow future plugin skills without coupling the core to one vendor.
