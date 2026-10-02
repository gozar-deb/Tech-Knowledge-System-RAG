# Contract Testing

**Path:** Tech_Knowledge_System/Software_Engineering/Testing_and_Quality/Contract_Testing
**Difficulty:** Advanced
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Contract testing is a method for verifying that interactions between two separate services conform to a shared agreement, known as a contract. It ensures compatibility and prevents breaking changes in distributed systems, particularly microservices, by testing consumer expectations against provider implementations.

## Key Concepts
- Consumer → The service making a request to another service.
- Provider → The service fulfilling requests from a consumer.
- Contract → A document or agreement detailing the expected interaction between consumer and provider.
- Consumer-Driven Contracts (CDC) → Consumers define the contract, and providers validate their implementation against it.
- Pact → A widely used framework for implementing consumer-driven contract testing.
- Schema Validation → Verifying that data structures exchanged between services match predefined specifications.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Pact | Framework | Consumer-driven contract testing |
| Spring Cloud Contract | Framework | Contract testing for Spring-based applications |
| OpenAPI/Swagger | Specification | Defining and documenting API contracts |
| Postman | API Platform | API development, testing, and contract validation |

## Retrieval Keywords
contract testing, API testing, microservices, integration testing, consumer-driven contracts, provider-driven contracts, Pact, Spring Cloud Contract, OpenAPI, Swagger, schema validation, service virtualization, distributed systems, software quality, CI/CD, interface testing, compatibility testing, consumer, provider, contract

## Related Nodes
- → Tech_Knowledge_System/Software_Engineering/Testing_and_Quality/Integration_Testing (parent concept)
- → Tech_Knowledge_System/Software_Engineering/Microservices_Architecture (dependency)
- → Tech_Knowledge_System/Software_Engineering/API_Design (related concept)

## Fast Queries This Node Should Answer
- "What is contract testing?"
- "How does contract testing work?"
- "When should I use contract testing?"
- "What are the main tools for contract testing?"
- "What are common failures in contract testing?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations