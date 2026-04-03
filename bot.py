import schedule
import time
from datetime import datetime

def remind(task):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Reminder: {task}")

def main():
    print("📌 Task Scheduler Bot Started")

    while True:
        print("\n1. Add Task")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            seconds = int(input("Remind after how many seconds: "))

            schedule.every(seconds).seconds.do(remind, task)
            print("✅ Task scheduled!")

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

        # Run scheduled tasks
        for _ in range(5):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()