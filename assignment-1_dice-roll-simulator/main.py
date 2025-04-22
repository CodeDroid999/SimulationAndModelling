import random

def roll_dice():
    """Simulates rolling a six-sided die using random.random()."""
    value = random.random()
    
    if 0 <= value < 1/6:
        return 1
    elif 1/6 <= value < 2/6:
        return 2
    elif 2/6 <= value < 3/6:
        return 3
    elif 3/6 <= value < 4/6:
        return 4
    elif 4/6 <= value < 5/6:
        return 5
    else:
        return 6

def main():
    rolls = 1000  # Fixed number of rolls
    face_counts = {i: 0 for i in range(1, 7)}

    # Simulate dice rolls
    for _ in range(rolls):
        face = roll_dice()
        face_counts[face] += 1

    # Print frequency table
    print("Face  Frequency   Percentage")
    for face, count in face_counts.items():
        percentage = (count / rolls) * 100
        print(f"{face:4}   {count:9}   {percentage:.1f}%")

    # Print total
    total_frequency = sum(face_counts.values())
    total_percentage = (total_frequency / rolls) * 100
    print(f"Total  {total_frequency:9}   {total_percentage:.1f}%")

if __name__ == "__main__":
    main()
