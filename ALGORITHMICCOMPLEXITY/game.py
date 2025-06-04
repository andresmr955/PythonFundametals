import time

def linear_search_guess(max_number, target):
    """
    Linear search: Guess sequentially from 1 to max_number.
    This takes O(n) guesses in the worst case.
    """
    guess_count = 0
    for guess in range(1, max_number + 1):
        start_time = time.time()
        guess_count += 1
        print(f"Linear guess #{guess_count}: Is it {guess}?")
        if guess == target:
            print(f"Found the number {target} in {guess_count} guesses (Linear Search).\n")
            end_time = time.time()
            total_time = end_time - start_time
            print(f'Total time: {total_time:.4f}')
            return guess_count
    end_time = time.time()
    print(f'Total time: {total_time:.4f}')
    return guess_count

def binary_search_guess(max_number, target):
    """
    Binary search: Narrow down the range [low, high] by half each step.
    This takes O(log n) guesses in the worst case.
    """
    low, high = 1, max_number
    guess_count = 0
    while low <= high:
        start_time = time.time()
        guess_count += 1
        mid = (low + high) // 2
        print(f"Binary guess #{guess_count}: Is it {mid}?")
        if mid == target:
            print(f"Found the number {target} in {guess_count} guesses (Binary Search).\n")
            end_time = time.time()
            total_time = end_time - start_time
            print(f'Total time: {total_time:.6f}')
            return guess_count
        elif mid < target:
            low = mid + 1
            print("  Too low, adjusting range upward.")
        else:
            high = mid - 1
            print("  Too high, adjusting range downward.")
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Total time: {total_time:.4f}')
    return guess_count

def play_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose a mode:")
    print("1) Linear Search (O(n))")
    print("2) Binary Search (O(log n))")
    
    mode = input("Enter 1 or 2: ").strip()
    max_number = int(input("Set the maximum number (e.g., 100): "))
    target = int(input(f"Think of a number between 1 and {max_number}. Enter it so the computer can guess: "))
    print()
    
    if mode == '1':
        print("You chose Linear Search mode.\n")
        linear_search_guess(max_number, target)
    elif mode == '2':
        print("You chose Binary Search mode.\n")
        binary_search_guess(max_number, target)
    else:
        print("Invalid mode selected. Please restart and choose 1 or 2.")

# Start the game
play_guessing_game()
