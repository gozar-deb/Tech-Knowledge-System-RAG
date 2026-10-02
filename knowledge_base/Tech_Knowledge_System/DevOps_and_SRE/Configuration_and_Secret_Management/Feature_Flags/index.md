# Feature Flags

**Path:** Tech_Knowledge_System/DevOps_and_SRE/Configuration_and_Secret_Management/Feature_Flags
**Difficulty:** Intermediate
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Feature flags are a software development practice that allows developers to enable or disable specific functionalities in an application remotely, without requiring a new code deployment. This technique facilitates controlled feature rollouts, A/B testing, and rapid incident response by providing dynamic control over application behavior.

## Key Concepts
- Feature Toggle → A conditional switch that controls the visibility or behavior of a feature.
- Targeting Rules → Logic that determines which users or segments see a particular feature.
- Progressive Delivery → Gradually releasing new features to a growing audience.
- Kill Switch → An immediate mechanism to turn off a feature in case of issues.
- A/B Testing → Comparing two versions of a feature to determine user preference or impact.
- Configuration Management → The process of maintaining system settings and application behavior.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| LaunchDarkly | SaaS Platform | Comprehensive feature flag management with advanced targeting. |
| Unleash | Open Source | Self-hosted feature toggles with client SDKs for various languages. |
| Split.io | SaaS Platform | Feature experimentation and rollout platform with data integration. |
| Flagsmith | Open Source / SaaS | Feature flags, remote config, and A/B testing for web, mobile, and backend. |

## Retrieval Keywords
feature flags, feature toggles, A/B testing, canary releases, dark launching, progressive delivery, configuration management, remote configuration, software development, DevOps, SRE, continuous delivery, release management, experimentation, dynamic configuration, toggle router, flag configuration, context attributes, rollout strategy, kill switch, feature management

## Related Nodes
- → Tech_Knowledge_System/DevOps_and_SRE/Configuration_and_Secret_Management (parent)
- → Tech_Knowledge_System/DevOps_and_SRE/CI_CD/Deployment_Strategies (related)
- → Tech_Knowledge_System/Software_Engineering/Software_Testing/A_B_Testing (related)

## Fast Queries This Node Should Answer
- "What is a feature flag?"
- "How do feature flags work?"
- "When should I use feature flags?"
- "What are the main tools for feature flags?"
- "What are common failures in feature flag implementations?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations