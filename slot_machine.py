# slot_machine.py
import random
from typing import Dict, List, Tuple

# --- Game Config ---
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_COUNTS: Dict[str, int] = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

SYMBOL_VALUES: Dict[str, int] = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def compute_payout(reels: List[List[str]], lines: int, bet: int, values: Dict[str, int]) -> Tuple[int, List[int]]:
    """
    Check horizontal lines (top to bottom) for matching symbols across all columns.
    Returns total winnings and list of 1-based winning line indices.
    """
    total = 0
    wins: List[int] = []

    for r in range(lines):
        first = reels[0][r]
        # If every column shows the same symbol on this row, it’s a win
        if all(col[r] == first for col in reels):
            total += values[first] * bet
            wins.append(r + 1)

    return total, wins


def spin_reels(rows: int, cols: int, counts: Dict[str, int]) -> List[List[str]]:
    """
    Build each column by sampling without replacement from the full bag of symbols,
    where multiplicities are given by counts.
    """
    pool: List[str] = [sym for sym, n in counts.items() for _ in range(n)]
    reels: List[List[str]] = []

    for _ in range(cols):
        # sample 'rows' items without replacement from the pool copy
        column = random.sample(pool, rows)
        reels.append(column)

    return reels


def render_reels(reels: List[List[str]]) -> None:
    """
    Print the slot machine in row-major order with separators.
    """
    if not reels:
        return
    rows = len(reels[0])
    for r in range(rows):
        row_symbols = [reels[c][r] for c in range(len(reels))]
        print(" | ".join(row_symbols))


def ask_deposit() -> int:
    while True:
        raw = input("What would you like to deposit? $")
        if raw.isdigit():
            amt = int(raw)
            if amt > 0:
                return amt
            print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")


def ask_lines() -> int:
    while True:
        raw = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if raw.isdigit():
            n = int(raw)
            if 1 <= n <= MAX_LINES:
                return n
            print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")


def ask_bet() -> int:
    while True:
        raw = input("What would you like to bet on each line? $")
        if raw.isdigit():
            amt = int(raw)
            if MIN_BET <= amt <= MAX_BET:
                return amt
            print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")


def play_round(balance: int) -> int:
    """
    Plays a single spin and returns the net change to the balance
    (winnings - total_bet).
    """
    lines = ask_lines()

    while True:
        bet = ask_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    reels = spin_reels(ROWS, COLS, SYMBOL_COUNTS)
    render_reels(reels)

    winnings, winning_lines = compute_payout(reels, lines, bet, SYMBOL_VALUES)
    print(f"You won ${winnings}.")
    if winning_lines:
        print("You won on lines:", *winning_lines)
    else:
        print("No winning lines this time.")

    return winnings - total_bet


def main() -> None:
    balance = ask_deposit()
    while True:
        print(f"Current balance is ${balance}")
        action = input("Press enter to play (q to quit).")
        if action.lower() == "q":
            break
        balance += play_round(balance)

    print(f"You left with ${balance}")


if __name__ == "__main__":
    main()
