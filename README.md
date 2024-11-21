
# Lamport's Logical Clock Simulator

This project implements **Lamport's Logical Clock**, a mechanism to order events in a distributed system. The Python-based simulator allows interactive simulation of local events, message sending, and receiving across multiple processes.

---

## Features

- Simulate **Local Events** for any process.
- Simulate **Send Events** with timestamp generation.
- Simulate **Receive Events** with logical clock updates.
- **Dynamic Number of Processes** for flexibility.
- **Interactive Menu** for user control.
- Display the current state of all processes' clocks.

---

## Getting Started

### Prerequisites

- Python 3.6 or higher.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bhaskarjyotikaushik/lamport-logical-clock.git
   cd lamport-logical-clock
   ```

2. Run the script:
   ```bash
   python lamport_clock.py
   ```

---

## Usage

1. **Start the Simulation:**
   Enter the number of processes when prompted.
   ```text
   Enter the number of processes: 2
   ```

2. **Interactive Menu Options:**
   - **Local Event:** Simulate an event for a process:
     ```text
     Enter process ID for local event: P1
     ```
   - **Send Event:** Simulate sending a message:
     ```text
     Enter sender process ID: P1
     ```
   - **Receive Event:** Simulate receiving a message:
     ```text
     Enter receiver process ID: P2
     Enter the received timestamp: 2
     ```
   - **Display Clocks:** View the current state of all processes' clocks.
   - **Exit:** End the simulation.

---

## Example Output

```text
Enter the number of processes: 2

--- Lamport's Logical Clock Simulation ---
1. Local Event
2. Send Event
3. Receive Event
4. Display Clocks
5. Exit
Choose an action (1-5): 1
Enter process ID for local event: P1
Process P1: Local event, clock = 1

Choose an action (1-5): 2
Enter sender process ID: P1
Process P1: Sent event, clock = 2
Timestamp of message from P1: 2

Choose an action (1-5): 3
Enter receiver process ID: P2
Enter the received timestamp: 2
Process P2: Received event, updated clock = 3
```

---

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

- **Your Name**  
  [GitHub](https://github.com/bhaskarjyotikaushik) | [LinkedIn](https://www.linkedin.com/in/bhaskar-jyoti-kaushik-100085248/)

---

## Acknowledgments

- The concept of **Lamport's Logical Clock** from [Distributed Systems Theory](https://en.wikipedia.org/wiki/Lamport_timestamps).
