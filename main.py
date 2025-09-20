def gps_tracker():
    x, y = 0, 0  # starting position
    print("Starting at position (0, 0)")
    print("Enter directions: N (North), S (South), E (East), W (West)")
    print("Type STOP to end the session.\n")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "stop":
            break
        elif command in ["n", "north"]:
            y += 1
        elif command in ["s", "south"]:
            y -= 1
        elif command in ["e", "east"]:
            x += 1
        elif command in ["w", "west"]:
            x -= 1
        else:
            print("Invalid input. Please enter N, S, E, W, or STOP.")
            continue

        print(f"Current position: ({x}, {y})")

    print("\nSession ended.")
    print(f"Final position: ({x}, {y})")

    if (x, y) == (0, 0):
        print("You returned to the origin (0, 0).")
    else:
        print("You did not return to the origin.")


# Run the program
if __name__ == "__main__":
    gps_tracker()
