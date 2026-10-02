# SPI I2C UART

**Path:** Tech_Knowledge_System/Embedded_Systems_and_IoT/Hardware_Interfacing/SPI_I2C_UART
**Difficulty:** Intermediate
**Time to Learn:** 1-2 weeks
**Version:** 2.0 | **Last Updated:** 2026-10-02
**Confidence:** 0.88

## Quick Definition
SPI, I2C, and UART are essential serial communication protocols for embedded systems, enabling microcontrollers to exchange data with various peripherals. They offer distinct advantages in speed, wiring complexity, and multi-device support, forming the foundation for hardware interfacing.

## Key Concepts
- SPI → Synchronous, high-speed, 4-wire, master-slave communication.
- I2C → Synchronous, medium-speed, 2-wire, multi-master/slave with addressing.
- UART → Asynchronous, simple, 2-wire, point-to-point communication.
- Master-Slave → A device hierarchy where one controls communication flow.
- Baud Rate → Data transfer speed, critical for asynchronous protocols.
- Data Integrity → Ensuring data accuracy during transmission via error checking.

## Tools

| Tool | Type | Purpose |
|------|------|---------|
| Logic Analyzer | Hardware | Debugging serial bus signals and timing |
| Oscilloscope | Hardware | Visualizing electrical signals and identifying noise |
| Arduino IDE | Software | Programming microcontrollers with built-in libraries |
| STM32CubeMX | Software | Configuring STM32 microcontrollers and generating HAL code |
| Python (PySerial) | Software | Interacting with UART devices from a host PC |

## Retrieval Keywords
SPI, I2C, UART, serial communication, embedded systems, hardware interfacing, microcontroller, peripheral, data transfer, synchronous, asynchronous, master-slave, bus protocol, IoT, digital communication, signal integrity, baud rate, addressing, full-duplex, half-duplex

## Related Nodes
- → Tech_Knowledge_System/Embedded_Systems_and_IoT/Hardware_Interfacing (parent)
- → Tech_Knowledge_System/Embedded_Systems_and_IoT/Microcontrollers (related concept)
- → Tech_Knowledge_System/Embedded_Systems_and_IoT/Sensors_and_Actuators (related application)

## Fast Queries This Node Should Answer
- "What is the difference between SPI, I2C, and UART?"
- "How does SPI communication work?"
- "When should I use I2C instead of UART?"
- "What are the main tools for debugging serial communication?"
- "What are common failures in SPI, I2C, or UART communication?"
- "How to optimize serial communication in embedded systems?"

## Common Misconceptions
- See the corresponding overview.txt for detailed misconceptions.

## Implementation Checklist
1. Study definition and core concepts
2. Experiment with basic examples
3. Review failure modes and apply mitigations