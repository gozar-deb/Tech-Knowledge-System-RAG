# Mocking and Stubbing

**Path:** Tech_Knowledge_System/Software_Engineering/Testing_and_Quality/Unit_and_Integration_Testing/Mocking_and_Stubbing
**Difficulty:** Advanced
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
Mocking creates simulated objects to verify interactions and behavior of a unit under test, while stubbing provides pre-programmed responses to dependency calls. Both are test doubles used to isolate code, making tests deterministic and faster by controlling external dependencies.

## Key Concepts
- Mock → A configurable object that records calls and allows behavior verification.
- Stub → An object that provides predefined data or responses to method calls.
- Test Double → A general term for objects used in place of real dependencies for testing.
- Dependency Injection → A technique to supply dependencies to a class, aiding testability.
- Test Isolation → Ensuring a test runs independently without side effects from other tests or external systems.
- Behavior-Driven Development (BDD) → A development methodology that often leverages mocks for specifying behavior.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Mockito | Library | Java mocking framework for unit tests |
| Moq | Library | Popular C# mocking framework |
| unittest.mock | Built-in Module | Python's standard library for mocking and patching |
| Jest | Framework | JavaScript testing framework with built-in mocking capabilities |
| Sinon.js | Library | Standalone test spies, stubs, and mocks for JavaScript |

## Retrieval Keywords
Mocking, Stubbing, Test Doubles, Unit Testing, Integration Testing, Test Isolation, Dependency Injection, TDD, BDD, Test Automation, Software Testing, Quality Assurance, Mock Objects, Stub Objects, Fakes, Spies, Verification, Testability, Design Patterns, Software Engineering, Testing Strategies

## Related Nodes
- → Tech_Knowledge_System/Software_Engineering/Testing_and_Quality/Unit_and_Integration_Testing (Parent)
- → Tech_Knowledge_System/Software_Engineering/Design_Patterns (Related Concept)
- → Tech_Knowledge_System/Software_Engineering/Testing_and_Quality/Test_Automation (Related Practice)

## Fast Queries This Node Should Answer
- "What is the difference between a mock and a stub?"
- "How do mocking and stubbing improve unit testing?"
- "When should I use mocks versus stubs?"
- "What are the main tools for mocking in Java/Python/C#?"
- "What are common pitfalls when using test doubles?"
- "How does dependency injection relate to mocking?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations