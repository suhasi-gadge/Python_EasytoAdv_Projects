import time  # For creating delays in the countdown
import sys   # For handling system operations

def countdown_timer(seconds):
    """Runs a countdown timer for the given number of seconds."""
    try:
        while seconds >= 0:
            mins, secs = divmod(seconds, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            print(timer_display, end='\r')  # Overwrites the previous line
            time.sleep(1)
            seconds -= 1
        print("\n⏰ Time's up! ⏰")
    except KeyboardInterrupt:
        print("\n⏸ Countdown interrupted!")

def get_user_time():
    """Prompts the user to enter time in minutes or seconds."""
    while True:
        try:
            user_input = input("Enter time (e.g., '2m' for 2 minutes or '30s' for 30 seconds): ").strip().lower()
            if user_input.endswith('m'):
                return int(user_input[:-1]) * 60  # Convert minutes to seconds
            elif user_input.endswith('s'):
                return int(user_input[:-1])
            else:
                print("⚠️ Invalid format! Use 'Xm' for minutes or 'Ys' for seconds.")
        except ValueError:
            print("⚠️ Please enter a valid number followed by 'm' or 's'.")

def alert_user():
    """Alerts the user when the timer ends."""
    print("\n⏰ Time's up! ⏰")
    try:
        # Works on most systems
        for _ in range(3):
            print("\a", end='')  # Terminal beep sound
            time.sleep(0.5)
    except:
        pass  # Ignore errors if sound doesn't play

if __name__ == "__main__":
    print("===== ⏳ Countdown Timer ⏳ =====")
    user_seconds = get_user_time()
    countdown_timer(user_seconds)
    alert_user()