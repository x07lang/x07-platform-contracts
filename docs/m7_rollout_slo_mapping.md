# M7 rollout + SLO mapping (runtime ↔ cloud ↔ MCP)

This document defines the canonical mapping and boundary rules for rollout control and SLO evaluation in the X07 PaaS line.

## Responsibilities (Option B boundary)

This contract set assumes **Option B** from the M7 plan:

- **Runtime (`x07-platform`)** executes rollouts and rollbacks and exposes rollout state.
- **Cloud (`x07-platform-cloud`)** evaluates SLOs, stores SLO snapshots, and emits incident triggers / rollback actions.
- **MCP (`x07-mcp`)** consumes these contracts to provide safe read-only visibility and guardrailed actions.

## Correlation fields

All three surfaces should treat these identifiers as canonical:

| Field | Required | Notes |
|---|---:|---|
| `deployment_id` | yes | Primary entity for SLO evaluation and incident correlation. |
| `environment_id` | yes | Required for fleet filtering and safety guardrails. |
| `service_id` | no | Optional; used when a deployment is service-scoped. |
| `rollout_id` | no | Present when an event/snapshot/trigger is tied to a rollout. |
| `request_id` | no | Present when the initiating request is known; used for support pivots. |
| `trace_id` | no | Present when tracing is enabled and correlation is available. |

## Rollout state mapping (`lp.rollout.status@0.1.0`)

The `state` enum is the canonical operator surface and is stable across runtime, cloud, and MCP:

| `state` | UI summary | Notes |
|---|---|---|
| `queued` | pending | Rollout recorded but no shift applied yet. |
| `shifting` | in progress | Traffic/capacity split is moving toward the new revision. |
| `paused` | paused | The split is held steady (manual or policy pause). |
| `promoted` | completed | New revision is fully active. |
| `rolled_back` | rolled back | Previous revision restored as active. |
| `failed` | failed | Rollout terminated without a safe promotion or rollback completion. |

## Incident triggers (`lp.incident.trigger@0.1.0`)

Cloud may emit incident triggers for automated control loops and for audit trails.

### Severity conventions

| `severity` | Operator meaning |
|---|---|
| `info` | informational event |
| `warn` | needs attention soon |
| `page` | on-call action required |

### Signal types

| `signal_type` | Intended source |
|---|---|
| `slo_burn` | SLO evaluator or policy engine |
| `crash_loop` | runtime controller / K8s signal |
| `probe_fail` | readiness/liveness failures |
| `manual` | operator action |

## Redaction rules (`observations`)

The `observations` object in `lp.incident.trigger@0.1.0`:

- **must not contain secrets** (tokens, passwords, API keys, raw headers)
- should prefer **stable identifiers** (snapshot IDs, objective IDs) over raw query strings
- may be stored and displayed in support tooling, so it must be safe-by-default

