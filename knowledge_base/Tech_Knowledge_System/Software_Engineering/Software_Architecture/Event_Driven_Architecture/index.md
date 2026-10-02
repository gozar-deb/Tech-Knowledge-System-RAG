# Event Driven Architecture

**Path:** Tech_Knowledge_System/Software_Engineering/Software_Architecture/Event_Driven_Architecture
**Difficulty:** Advanced
**Time to Learn:** 3-6 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Event-Driven Architecture (EDA) is a paradigm where services communicate asynchronously by producing and consuming events. This promotes loose coupling, high scalability, and resilience, making systems more responsive to changes and failures.

## Key Concepts
- Event → An immutable record of a significant state change that occurred in the past.
- Event Producer → A component that publishes events without knowledge of their consumers.
- Event Consumer → A component that subscribes to and processes specific types of events.
- Event Broker → An intermediary system responsible for routing events between producers and consumers.
- Asynchronous Communication → Non-blocking interactions where components don't wait for immediate responses.
- Loose Coupling → Reduced dependencies between services, allowing independent development and deployment.
- Event Sourcing → Storing all application state changes as a chronological sequence of events.
- Saga Pattern → A distributed transaction managed by a sequence of local transactions, coordinated via events.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Apache Kafka | Event Streaming Platform | High-throughput, fault-tolerant event streaming |
| RabbitMQ | Message Broker | General-purpose message queuing and routing |
| AWS Kinesis | Managed Streaming Service | Real-time data streaming and processing in AWS |
| Apache Pulsar | Distributed Messaging & Streaming | Unified messaging and streaming platform |

## Retrieval Keywords
event-driven, architecture, EDA, asynchronous, events, producers, consumers, brokers, message queues, stream processing, microservices, distributed systems, reactive, scalability, resilience, loose coupling, event sourcing, saga, CQRS, pub/sub, real-time, system design, enterprise integration patterns

## Related Nodes
- → Tech_Knowledge_System/Software_Engineering/Software_Architecture/Microservices (common implementation style)
- → Tech_Knowledge_System/Software_Engineering/Software_Architecture/Message_Queues (core technology)
- → Tech_Knowledge_System/Software_Engineering/Software_Architecture/Distributed_Systems (foundational pattern)

## Fast Queries This Node Should Answer
- "What is Event-Driven Architecture?"
- "How does Event-Driven Architecture work?"
- "When should I use Event-Driven Architecture?"
- "What are the main tools for Event-Driven Architecture?"
- "What are common failures in Event-Driven Architecture?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations