import os


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
    # Loop until valid choice is made
    while True:
        # Print animation options
        print("Choose an animation type to add to the file:")
        for index, animation_type in animations.items():
            print(f"{index}: {animation_type}")
        print("0: Exit")
        # Get user input
        choice = int(input())
        # Check if choice is valid
        if choice == 0:
            # Return None if user chooses to exit
            return None
        elif choice in animations:
            # Return animation type if choice is valid
            return animations[choice]
        else:
            # Print error message if choice is invalid
            print("Invalid choice, please enter a valid number.")


def get_seconds():
    # Ask for input of seconds as a string
    seconds_string = input("Enter the seconds separated by commas: ")
    # Verify that input is not empty
    if seconds_string.strip() == "":
        print("Invalid input. Please enter a valid number.")
        return
    # Convert seconds_string to a list of floats
    try:
        seconds = [float(x.strip()) for x in seconds_string.split(",")]
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    # Remove duplicate values and negative values
    seconds = list(set(seconds))
    seconds = [x for x in seconds if x >= 0]
    # check if list is not empty
    if not seconds:
        print("Invalid input. Please enter a valid number.")
        return

    return seconds


def create_another_file():
    return input("Do you want to create another file? (y/n) ").lower() == "y"


def create_animation_file(file_name):
    #create the file in the folder and checks if it exists
    while True:
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        if os.path.isfile(file_name):
            overwrite = input(f"{file_name} already exists, Do you want to overwrite? (y/n) ").lower()
            if overwrite == "n":
                continue
        while True:
            animation_type = get_animation_type(animations)
            if animation_type is None:
                break
            seconds = get_seconds()
            if seconds is None:
                continue
            seconds = [x for x in seconds if x>=0]
            if not seconds:
                print("Invalid input. Please enter a valid number.")
                continue
            create_file(file_name, seconds, animation_type)
            another_animation = input("Do you want to add another animation to the file? (y/n) ").lower()
            if another_animation != "y":
                break
        if not create_another_file():
            return False
    return True

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