class LamportsClock:
    def __init__(self, process_id):
        self.process_id = process_id
        self.clock = 0

    def increment(self):
        """Increment the local clock."""
        self.clock += 1

    def send_event(self):
        """Simulate sending an event."""
        self.increment()
        print(f"Process {self.process_id}: Sent event, clock = {self.clock}")
        return self.clock

    def receive_event(self, received_timestamp):
        """Simulate receiving an event."""
        self.increment()
        self.clock = max(self.clock, received_timestamp + 1)
        print(f"Process {self.process_id}: Received event, updated clock = {self.clock}")

    def local_event(self):
        """Simulate a local event."""
        self.increment()
        print(f"Process {self.process_id}: Local event, clock = {self.clock}")


def simulate_lamports_clock():
    # Create processes
    processes = {}
    num_processes = int(input("Enter the number of processes: "))
    for i in range(1, num_processes + 1):
        process_id = f"P{i}"
        processes[process_id] = LamportsClock(process_id)

    while True:
        print("\n--- Lamport's Logical Clock Simulation ---")
        print("1. Local Event")
        print("2. Send Event")
        print("3. Receive Event")
        print("4. Display Clocks")
        print("5. Exit")
        choice = input("Choose an action (1-5): ")

        if choice == "1":
            process_id = input("Enter process ID for local event: ")
            if process_id in processes:
                processes[process_id].local_event()
            else:
                print("Invalid process ID.")
        elif choice == "2":
            sender_id = input("Enter sender process ID: ")
            if sender_id in processes:
                timestamp = processes[sender_id].send_event()
                print(f"Timestamp of message from {sender_id}: {timestamp}")
            else:
                print("Invalid sender ID.")
        elif choice == "3":
            receiver_id = input("Enter receiver process ID: ")
            timestamp = int(input("Enter the received timestamp: "))
            if receiver_id in processes:
                processes[receiver_id].receive_event(timestamp)
            else:
                print("Invalid receiver ID.")
        elif choice == "4":
            print("\nCurrent Clock Values:")
            for process_id, process in processes.items():
                print(f"{process_id}: {process.clock}")
        elif choice == "5":
            print("Exiting simulation.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    simulate_lamports_clock()
