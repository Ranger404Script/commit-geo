
import datetime

def greet():
    print("Hello from your simple Python script!")
    now = datetime.datetime.now()
    print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    greet()
