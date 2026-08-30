# FROGE Architecture

## System Model

FROGE is a control-plane architecture for coordinating AI models, providers, MCP servers, tools, skills, memory, sessions, and verification.

```text
User / Agent Request
        │
        ▼
┌────────────────────┐
│ FROGE Orchestrator │
└─────────┬──────────┘
          │
   ┌──────┼───────────────┐
   ▼      ▼               ▼
 Planner  Policy       Session
   │      Engine        Manager
   └──────┬───────────────┘
          ▼
┌──────────────────────────┐
│ Capability / MCP Control  │
│ Plane                     │
└────────────┬─────────────┘
             │
   ┌─────────┼──────────┐
   ▼         ▼          ▼
Providers  Tools      Skills
Models     Runtimes   Agents
   │         │          │
   └─────────┼──────────┘
             ▼
       Execution Layer
             │
       ┌─────┴─────┐
       ▼           ▼
   Verification  Recovery
       │           │
       └─────┬─────┘
             ▼
       Memory / Evidence
```

## Core Layers

### 1. Orchestration
Owns intent normalization, planning, routing, execution coordination, and result handling.

### 2. Provider and Model Layer
Abstracts provider-specific APIs and model identifiers. Provider health and model health are tracked independently.

### 3. MCP Control Plane
Provides a consistent interface for discovering, invoking, monitoring, and governing external/local tools.

### 4. Skill Layer
Contains reusable workflows with explicit inputs, outputs, permissions, and verification requirements.

### 5. Context and Memory
Maintains active session state and durable operational knowledge. Memory should be selective and evidence-oriented.

### 6. Recovery
Classifies failures, retries boundedly, applies cooldowns, selects verified fallbacks, and records successful recovery paths.

### 7. Verification
Tests capabilities before trusting them and validates important results after execution.

## Design Boundary

The orchestrator coordinates these layers; it should not become a monolithic implementation of every provider, tool, or skill.

## Local System Integration

FROGE is intended to control approved software and runtimes installed on the user's computer through the MCP/control-plane layer. Local configuration may describe executable paths and capabilities, but secrets must remain outside Git.
