"""
Advent of Code 2025: Day 1
Secret Entrance
"""
import time

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

# Now run and time both parts (hope it works lol)
start_time = time.perf_counter()
part1_result = part_1(commands)
part1_time = time.perf_counter() - start_time

start_time = time.perf_counter()
part2_result = part_2(commands)
part2_time = time.perf_counter() - start_time

print(f"Part 1 answer: {part1_result} (took {part1_time*1000:.3f}ms)") # Output: Part 1 answer: 1052 (took 1.034ms)
print(f"Part 2 answer: {part2_result} (took {part2_time*1000:.3f}ms)") # Output: Part 2 answer: 6295 (took 39.304ms)