# Error Budgets and SLOs

**Path:** Tech_Knowledge_System/DevOps_and_SRE/Site_Reliability_Engineering/Error_Budgets_and_SLOs
**Difficulty:** Advanced
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Error Budgets define the acceptable failure rate for a service, derived from Service Level Objectives (SLOs). SLOs are measurable targets for service performance, crucial for balancing reliability with feature development and ensuring user satisfaction.

## Key Concepts
- Error Budget → The maximum allowable unreliability for a service over a period.
- SLO (Service Level Objective) → A specific, measurable target for a service's performance or reliability.
- SLI (Service Level Indicator) → A quantitative measure of a service's performance, used to track SLOs.
- Burn Rate → The speed at which the error budget is being consumed.
- Reliability → The probability of a system performing its intended function without failure.
- Availability → The proportion of time a system is functional and accessible.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Prometheus | Monitoring | Time-series data collection and alerting |
| Grafana | Visualization | Dashboarding and data visualization |
| OpenTelemetry | Observability | Standardized telemetry data collection |
| PagerDuty | Incident Management | On-call scheduling and incident alerting |

## Retrieval Keywords
error budget, SLO, SLI, SRE, service level objective, service level indicator, reliability engineering, site reliability, performance, availability, latency, throughput, error rate, monitoring, alerting, incident response, operational excellence, system health, burn rate, toil, reliability metrics, business impact, customer experience

## Related Nodes
- → Tech_Knowledge_System/DevOps_and_SRE/Site_Reliability_Engineering/SLIs_and_SLAs (related_concept)
- → Tech_Knowledge_System/DevOps_and_SRE/Site_Reliability_Engineering/Monitoring_and_Alerting (prerequisite)

## Fast Queries This Node Should Answer
- "What is an error budget in SRE?"
- "How do SLOs relate to error budgets?"
- "When should I use error budgets and SLOs?"
- "What are the main tools for managing error budgets?"
- "What are common failures in error budget implementation?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations