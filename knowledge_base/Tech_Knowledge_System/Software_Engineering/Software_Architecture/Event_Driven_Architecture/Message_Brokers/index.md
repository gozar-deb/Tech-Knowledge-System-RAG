# Message Brokers

**Path:** Tech_Knowledge_System/Software_Engineering/Software_Architecture/Event_Driven_Architecture/Message_Brokers
**Difficulty:** Intermediate
**Time to Learn:** 2-4 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Message brokers are software intermediaries that enable communication between different applications by managing message queues and topics. They facilitate asynchronous, decoupled communication, enhancing the scalability, reliability, and resilience of distributed systems by ensuring messages are delivered and processed efficiently.

## Key Concepts
- Message Queue → A buffer for messages awaiting processing.
- Publish-Subscribe → A pattern for broadcasting messages to interested subscribers.
- Producer → An application that sends messages.
- Consumer → An application that receives and processes messages.
- Topic → A named channel for message distribution in pub/sub.
- Acknowledgment → Confirmation of successful message processing.
- Dead Letter Queue (DLQ) → Stores messages that failed processing.
- Decoupling → Separating senders and receivers to reduce dependencies.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Apache Kafka | Infrastructure | High-throughput, fault-tolerant event streaming platform |
| RabbitMQ | Infrastructure | Robust, general-purpose message broker supporting various protocols |
| Azure Service Bus | Infrastructure | Cloud-based enterprise messaging as a service |
| Spring Cloud Stream | Framework | Building event-driven microservices with message brokers |
| Pika | Language Library | Python client library for RabbitMQ |
| amqplib | Language Library | Node.js client library for AMQP-based brokers |

## Retrieval Keywords
message broker, message queue, pub/sub, asynchronous communication, distributed systems, event-driven architecture, Kafka, RabbitMQ, ActiveMQ, SQS, SNS, Pub/Sub, decoupling, scalability, reliability, fault tolerance, enterprise integration, event streaming, data pipelines, messaging patterns, producers, consumers, topics, queues, routing, acknowledgments, DLQ

## Related Nodes
- → Tech_Knowledge_System/Software_Engineering/Software_Architecture/Event_Driven_Architecture (parent)
- → Tech_Knowledge_System/Software_Engineering/Software_Architecture/Event_Driven_Architecture/Event_Streaming (sibling)
- → Tech_Knowledge_System/Software_Engineering/Software_Architecture/Microservices (related)

## Fast Queries This Node Should Answer
- "What is a message broker?"
- "How do message queues work?"
- "When should I use a publish-subscribe model?"
- "What are the main tools for message brokering?"
- "What are common failures in message broker systems?"
- "How do message brokers improve system scalability?"
- "What are the security considerations for message brokers?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations