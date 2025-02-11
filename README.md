# Lottery Scheduling Program

## Introduction
This program simulates lottery scheduling, a process scheduling algorithm used in operating systems. It is implemented in Python and demonstrates how processes can be allocated CPU time based on a random lottery system. The scheduler:
- Generates a random number of processes, each with a unique ID.
- Allocates a random number of tickets to each process.
- Draws random tickets to determine the winning process for execution.

## Prerequisites
- **Python 3.10 or above**: The program was written in Python 3.12.1, but it is compatible with Python 3.10 or newer.
- No additional libraries are required as it uses Python's built-in functionality.

## Installation
1. Clone the repository to your local machine:
   
   ```bash
   git clone https://github.com/Nemesis-12/lottery-scheduling.git
   ```
   
2. Navigate to the directory containing the script:

   ```console
   cd lottery-scheduling
   ```

## Usage
Run the program in the terminal or an IDE:

```console
python process.py
```

## Example

The program does not require any user input

### Initialization

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

### Lottery Winners

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
This project is an educational tool and welcomes contributions. To contribute:
- Fork the repository.
- Make your changes.
- Submit a pull request with a description of your updates.

Feel free to open an issue for suggestions or bugs.

## License
This project is licensed under the [MIT License](LICENSE).
