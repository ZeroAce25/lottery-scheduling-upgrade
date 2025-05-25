'''
This is a program that simulates a lottery scheduling algorithm. The
program creates a process, after which the scheduler handles operations such as
adding processes to the scheduler, allocating tickets, starting the scheduler,
and so on.
'''

import random

# Create Process class to handle creating processes
class Process:
    def __init__(self, id) -> None:
        self.uuid = id
        self.tickets = []
        self.burst_time = random.randint(1, 5) 
        self.wins = 0

# Create a Scheduler class that can add process, allocate tickets, etc. 
class Scheduler:
    def __init__(self) -> None:
        self.processes = []

    # Add all processes to a list
    def add(self, process):
        self.processes.append(process)

    # Show the current state of the scheduler
    def state(self, process):
        print(f"Process ID: {process.uuid}, Tickets: {process.tickets}")

    # Allocate a certain number of ticket to each process
    def allocate_tickets(self):
        init_tickets = 1

        # For every process in a list of processes, assign a certain 
        # number of tickets. After that, increase the initial number of
        # tickets so that we have a fresh and unique batch of tickets
        for process in self.processes:
            rand_assign = random.randint(1, 10)
            process.tickets = list(range(init_tickets, init_tickets + rand_assign))
            self.state(process)
            init_tickets += rand_assign
        print('\n')

    # Start the scheduling process and pick a random process as winner
    def start(self):
        # Store every single ticket in a list
        tot_tickets = []
        for process in self.processes:
            for tickets in process.tickets:
                tot_tickets.append(tickets)

        # Now we can make use of the list to pick a random ticket and check
        # which process it belongs to
        lottery_winner = random.choice(tot_tickets)
        for process in self.processes:
            if lottery_winner in process.tickets:      
                print(f"Process {process.uuid} wins the lottery!")
                break
    def summary(self):
        print("\n=== Simulation Summary ===")
        for process in self.processes:
            print(f"Process {process.uuid} | Burst Time: {process.burst_time} | Total Wins: {process.wins}")
# Define main function of the program
def main():
    random_process = random.randint(3, 6)
    scheduler = Scheduler()

    print("Adding processes to scheduler...\n")
    for i in range(1, random_process + 1):
        scheduler.add(Process(i))

    total_cycles = 5
    for cycle in range(1, total_cycles + 1):
        print(f"\n=== Cycle {cycle} ===")
        print("Assigning tickets...")
        scheduler.allocate_tickets()

        print("Starting scheduling...")
        scheduler.start()

    scheduler.summary()

if __name__ == '__main__':
    main()