import subprocess

def run_simulation():
    # Run the simulation scripts
    subprocess.run(["python", "simulate.py"])
    subprocess.run(["python", "receive.py"])
    subprocess.run(["python", "app.py"])

def run_execution():
    # Run the execution scripts
    subprocess.run(["python", "receive.py"])
    subprocess.run(["python", "app.py"])

def main():
    # Ask user whether to simulate or execute
    user_choice = input("Do you want to simulate the process? (yes/no): ").lower()
    
    if user_choice == "yes":
        run_simulation()
    elif user_choice == "no":
        run_execution()
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
