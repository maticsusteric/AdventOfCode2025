"""
Advent of Code 2025: Day 1
Secret Entrance
"""
file = "input.txt"

lock_combinations = list(range(100))


commands_from_file = []

with open(file, "r") as f:
    commands_from_file = f.readlines()

commands = [command.strip() for command in commands_from_file]

def part_1(commands: list[str]) -> int:
    """
    Count how many times on each command the step_cal will recah 0

    Args:
        commands : List of commands to process
    Returns:
        int: Number of times step_calc reaches 0
    """
    times_on_zero = 0
    step_calc = 50
    for comm in commands:
        if 'R' in comm:
            # Wrap around with % (if reaches 100 goes back to 0 etc
            step_calc = (step_calc + int(comm[1:])) % 100
            if step_calc == 0:
                times_on_zero += 1
        else:
            step_calc = (step_calc - int(comm[1:])) % 100
            if step_calc == 0:
                times_on_zero += 1
    return times_on_zero

def part_2(commands: list[str]) -> int:
    """
    This one is similar to part 1 but now counts every step.
    Args:
        commands: List of commands to process (like before duh :D)

    Returns:
        int: Number of times step_calc reaches 0 (am I going crazy or am I repeating myself? :P)
    """

    times_on_zero = 0
    step_calc = 50
    for comm in commands:
        if 'R' in comm:
            for _ in range(int(comm[1:])):
                step_calc = (step_calc + 1) % 100
                if step_calc == 0:
                    times_on_zero += 1
        else:
            for _ in range(int(comm[1:])):
                step_calc = (step_calc - 1) % 100
                if step_calc == 0:
                    times_on_zero += 1
    return times_on_zero


print(f"Part 1 answer: {part_1(commands)}")
print(f"Part 2 answer: {part_2(commands)}")