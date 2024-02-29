# Lottery Scheduling Program

## Getting Started
This program is a simple lottery scheduling program written in Python, which generates a random number of processes assigned with an id. The scheduler then adds all processes to its list, allocates a random number of tickets to each process, selects a random ticket based on lottery and then displays the process corresponding to the ticket. The following document will help you get started on setting up the program.

## Prerequisites
This program requires Python 3.10 to run and was written in 3.12.1. To download, go to python.org and download Python 3.10.x or above. You will not be required to install any additional libraries as we are using default libraries.

## Installation
Clone the repository or download the source code onto your local machine. Navigate to the directory of the script and run it through the terminal or an IDE.

## Usage
Run the following program on the terminal:

```console
python process.py
```

When the program starts, you will not need to enter any values or data. The program itself generates a random number of processes using the random modules function random.randint(). 

```python
# Pick a random number to generate the number of processes
    random_process = random.randint(2, 6)
    scheduler = Scheduler()

    # Generate a random number of processes to the scheduler
    print("Adding processes to scheduler...")
    for i in range(1, random_process + 1):
        scheduler.add(Process(i))
```

The processes are then added to a scheduler through a loop that adds the processes using the Scheduler().add() function.  The scheduler then allocates a random number of tickets to each process using Scheduler().allocate_tickets().

```python
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
```

This is the output generated when the above code is run:

```console
Adding processes to scheduler...
Assigning tickets...
Process ID: 1, Tickets: [1, 2, 3, 4, 5]
Process ID: 2, Tickets: [6, 7, 8, 9, 10, 11, 12]
Process ID: 3, Tickets: [13, 14, 15]
Process ID: 4, Tickets: [16, 17, 18, 19, 20, 21, 22, 23, 24]
Process ID: 5, Tickets: [25, 26, 27, 28, 29, 30, 31, 32]
Process ID: 6, Tickets: [33, 34, 35, 36]
```

After this, the program starts the scheduling process and displays the winning processes up to the number of tickets that were generated. The output of the winning processes is shown below: 

```console
Starting scheduling...
Process 2 wins the lottery!
Process 4 wins the lottery!
Process 2 wins the lottery!
Process 2 wins the lottery!
Process 1 wins the lottery!
Process 1 wins the lottery!
```

## Contributing
This project is an educational tool and is open to contributions. If you have suggestions or improvements, create a pull request by forking the repository.
