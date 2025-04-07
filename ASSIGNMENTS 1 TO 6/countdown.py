import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{mins:02}:{secs:02}", end="")
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")

time_in_seconds = int(input("Enter time in seconds: "))
countdown_timer(time_in_seconds)