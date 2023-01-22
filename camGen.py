import os
import re
import sys

def create_file(file_name, seconds, animation_type):
    # initialize with first value
    data = "\"{}\": \"0:(),".format(animation_type)
    for second in seconds:
        data += "{}:(),".format(int(second*12))
    # remove last comma and add closing quotes
    data = data[:-1] + "\",\n"
    with open(file_name, "a") as f:
        print(file_name)
        print(seconds)
        print(animation_type)
        print(data)
        f.write(data)
        f.close()
    print(f"{animation_type} added to {file_name}.")



def get_animation_type(animations):
    while True:
        # Print animation options
        print("Choose an animation type to add to the file:")
        for index, animation_type in enumerate(animations):
            print(f"{index+1}: {animation_type}")
        print("0: Exit")
        while True:
            try:
                # Ask user to enter animation type choice
                choice = int(input())
                # Check if choice is 0, if so return None
                if choice == 0:
                    return None
                # Check if choice is a valid animation type
                elif choice in range(1, len(animations)+1):
                    return choice-1
                else:
                    print("Invalid choice, please enter a valid number.")
            except ValueError:
                print("Invalid input, please enter a valid number.")

def get_seconds():
    # Loop until user enters valid input
    while True:
        # Ask user for seconds input
        seconds_string = input("Enter the seconds separated by commas: ")
        # Check if input is empty
        if not seconds_string.strip():
            print("You entered nothing, please enter a valid number.")
            continue
        # Extract seconds from input
        seconds = re.findall(r"[-+]?\d*\.\d+|\d+", seconds_string)
        # Check if seconds were extracted
        if not seconds:
            print("Invalid input. Please enter a valid number.")
            continue
        # Convert seconds to float and return
        return [float(x) for x in seconds]


def create_file_loop(file_name):
    # Ensure file has .txt extension
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    dir_name = 'output'
    # Create directory if it doesn't already exist and dir_name is not empty
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    while True:
        if os.path.exists(os.path.join(dir_name, file_name)):
            # Ask user to enter different file name if file already exists
            create_another = input(f"{file_name} already exists, enter a different file name or 'n' to exit: ").lower()
            if create_another == "n":
                sys.exit()
            file_name = create_another
        else:
            # Create new file
            with open(os.path.join(dir_name, file_name), 'w') as f:
                f.write('')
            break
    # Note to self, don't forget to do this ever again, join the dir and file name
    return os.path.join(dir_name, file_name)




def add_animations_loop(file_name):
    # Load animation types from file
    with open('animation_types.txt', 'r') as f:
        animations = f.readlines()
    animations = [x.strip() for x in animations]
    while True:
        # Print animation options
        print("Choose an animation type to add to the file:")
        for index, animation_type in enumerate(animations):
            print(f"{index+1}: {animation_type}")
        print("0: Exit")
        # Ask user to enter animation type choice
        choice = input()
        if not choice:
            print("Invalid input. Please enter a valid number.")
            continue
        choice = int(choice)
        # Check if choice is 0, if so return None
        if choice == 0:
            return None
        # Check if choice is a valid animation type
        elif choice in range(1, len(animations)+1):
            animation_type = animations[choice-1]
            # Get seconds from user
            seconds = get_seconds()
            # Create file
            create_file(file_name, seconds, animation_type)




def create_animation_file(file_name):
    # Create file and handle errors
    file_name = create_file_loop(file_name)
    # Add animations to file
    add_animations_loop(file_name)
    while True:
        # Ask user if they want to create another file
        create_another = input("Do you want to create another file? (y/n) ").lower()
        if create_another in ["y", "n"]:
            break
        print("Invalid input. Please enter 'y' or 'n'.")
    if create_another == "n":
        sys.exit()
    else:
        return True


def main():
    file_name = input("Enter the file name: ") + "Camera"
    while True:
        create_animation_file(file_name)

if __name__ == "__main__":
    main()