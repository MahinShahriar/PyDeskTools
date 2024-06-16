import pyautogui
import time

def autoscroller(speed):
    # Adjust the speed of scrolling
    scroll_pause_time = speed  # Adjust the speed of scrolling

    scroll_counter = 0  # Counter to track the number of scrolls

    try:
        while True:
            # Check if the scroll counter has reached the threshold (e.g., 5 scrolls)
            if scroll_counter >= 3:
                print("Auto-scrolling initiated...")
                # Start auto-scrolling
                while True:
                    pyautogui.scroll(-1)  # Scrolls down
                    time.sleep(scroll_pause_time)  # Wait for the specified time before the next scroll

            # Simulate mouse wheel movement for smooth scrolling
            # pyautogui.scroll(1)  # Scrolls up
            time.sleep(scroll_pause_time)  # Wait for the specified time before the next scroll
            scroll_counter += 1  # Increment the scroll counter

    except KeyboardInterrupt:
        pass  # Catch KeyboardInterrupt to stop the scrolling when Ctrl+C is pressed

# Example usage
speed = 6  # Adjust the speed of scrolling (in seconds)
autoscroller(speed)
