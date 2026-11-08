
import random
import os
import matplotlib.pyplot as plt


def simulate_dice_rolls(number_of_sides, number_of_rolls=100_000):
    """Simulate rolling two dice and return the sum of each roll."""
    generator = random.Random(42)
    sums = []

    for _ in range(number_of_rolls):
        first_die = generator.randint(1, number_of_sides)
        second_die = generator.randint(1, number_of_sides)
        sums.append(first_die + second_die)

    return sums


def create_histogram(sums, number_of_sides, number_of_rolls):
    """Create and save a histogram of the dice-roll sums."""
    possible_sums = range(2, (2 * number_of_sides) + 1)
    bin_edges = [value - 0.5 for value in range(2, (2 * number_of_sides) + 2)]

    plt.figure(figsize=(10, 6))
    plt.hist(sums, bins=bin_edges, edgecolor="black")

    plt.title(
        f"Distribution of Two {number_of_sides}-Sided Dice "
        f"({number_of_rolls:,} Rolls)"
    )
    plt.xlabel("Sum of Both Dice")
    plt.ylabel("Frequency")
    plt.xticks(possible_sums)
    plt.grid(axis="y", alpha=0.3)

    filename = f"images/{number_of_sides}_sided_dice_histogram.png"
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

    print(f"Histogram saved: {filename}")


def main():
    """Run both dice simulations and create their histograms."""
    os.makedirs("images", exist_ok=True)

    number_of_rolls = 100_000

    for sides in (6, 8):
        results = simulate_dice_rolls(sides, number_of_rolls)
        create_histogram(results, sides, number_of_rolls)

        print(f"\nResults for two {sides}-sided dice:")
        for total in range(2, (2 * sides) + 1):
            frequency = results.count(total)
            print(f"Sum {total}: {frequency:,}")


if __name__ == "__main__":
    main()
