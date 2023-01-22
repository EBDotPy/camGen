import os


def create_file(file_name, seconds, animation_type):
    data = "\"{}\": \"0:(),".format(animation_type) # initialize with first value
    for second in seconds:
        data += "{}:(),".format(int(second*12))
    data = data[:-1] + "\",\n" # remove last comma and add closing quotes
    with open(file_name, "a") as f:
        f.write(data)
    print(f"{animation_type} added to {file_name}.")


def get_animation_type(animations):
    # Checks list of animation types and displays them by number
    while True:
        print("Choose an animation type to add to the file:")
        for index, animation_type in animations.items():
            print(f"{index}: {animation_type}")
        print("0: Exit")
        choice = int(input())
        if choice == 0:
            return None
        elif choice in animations:
            return animations[choice]
        else:
            print("Invalid choice, please enter a valid number.")

def get_seconds():
    #handles the seconds calculation and checks for errors
    while True:
        seconds_string = input("Enter the seconds separated by commas: ")
        if seconds_string.strip() == "":
            print("Invalid input. Please enter a valid number.")
            continue
        try:
            seconds = [float(x.strip()) for x in seconds_string.split(",")]
            seconds = list(set(seconds))
            seconds = [x for x in seconds if x>=0]
            if not seconds:
                print("Invalid input. Please enter a valid number.")
                continue
            return seconds
        except ValueError:
            print("Invalid input. Please enter a valid number.")


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