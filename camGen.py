import os
import json

def create_file(file_name, seconds, animation_type):
    # initialize with first value
    data = "\"{}\": \"0:(),".format(animation_type)
    for second in seconds:
        data += "{}:(),".format(int(second*12))
    # remove last comma and add closing quotes
    data = data[:-1] + "\",\n"
    with open(file_name, "a") as f:
        f.write(data)
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
                    return animations[choice-1]
                else:
                    print("Invalid choice, please enter a valid number.")
            except ValueError:
                print("Invalid input, please enter a valid number.")

def get_seconds():
    # Ask for input of seconds as a string
    while True:
        seconds_string = input("Enter the seconds separated by commas: ")
        # Verify that input is not empty
        if not seconds_string.strip():
            print("You entered nothing, please enter a valid number.")
            continue
        try:
            seconds = [float(x.strip()) for x in seconds_string.split(",")]
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        # Remove duplicate values and negative values
        seconds = list(set(seconds))
        seconds = [x for x in seconds if x >= 0]
        # check if list is not empty
        if not seconds:
            print("Invalid input. Please enter a valid number.")
            continue
        return seconds

def create_another_file():
    return input("Do you want to create another file? (y/n) ").lower() == "y"

def create_file_loop(file_name):
    # Ensure file has .txt extension
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    while os.path.exists(file_name) or file_name.strip() == "":
        if os.path.exists(file_name):
            print(f"{file_name} already exists.")
        else:
            print("file name is empty, please enter a valid file name")
        file_name = input("Enter a different file name: ")
    # Create directory if it doesn't already exist
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    # Create new file
    open(file_name, 'w')
    return file_name

def add_animations_loop(file_name):
    # Loop until user chooses to exit
    while True:
        # Get animation type from user
        animation_type = get_animation_type(animations)
        # If animation type is None, continue to next iteration
        if animation_type is None:
            continue
        # Get seconds from user
        seconds = get_seconds()
        # If seconds is None, continue to next iteration
        if seconds is None:
            continue
        # Remove negative seconds
        seconds = [x for x in seconds if x>=0]
        # Check if seconds list is not empty
        if not seconds:
            print("Invalid input. Please enter a valid number.")
            continue
        # Create file with animation and seconds
        create_file(file_name, seconds, animation_type)
        # Loop until user enters valid input
        while True:
            # Ask user if they want to add another animation
            another_animation = input("Do you want to add another animation to the file? (y/n) ").lower()
            # Check if input is valid
            if another_animation in ["y", "n"]:
                break
            print("Invalid input. Please enter 'y' or 'n'.")
        # If user doesn't want to add another animation, exit loop
        if another_animation != "y":
            return

def create_animation_file(file_name):
    # Create file and handle errors
    file_name = create_file_loop(file_name)
    # Add animations to file
    add_animations_loop(file_name)
    # Loop until user enters valid input
    while True:
        # Ask user if they want to create another file
        create_another = input("Do you want to create another file? (y/n) ").lower()
        # Check if input is valid
        if create_another in ["y", "n"]:
            break
        print("Invalid input. Please enter 'y' or 'n'.")
    # Return True if user wants to create another file, False otherwise
    return create_another == "y"

animations = {
    1: "translation_x",
    2: "translation_y",
    3: "translation_z",
    4: "rotation_3d_x",
    5: "rotation_3d_y",
    6: "rotation_3d_z",
    7: "noise_schedule",
    8: "strength_schedule",
    9: "contrast_schedule",
    10: "cfg_scale_schedule"
}
while create_animation_file(input("Enter the file name: ") + "Camera"):
    pass

# TODO: Create a file with animations that can be added to and read from, instead of updating this file with numbers
# TODO: Get file to read all animation possibilities from Deforum