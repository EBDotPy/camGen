import os


def create_file(file_name, seconds, animation_type):
    # Creates output for file
    data = "\"{}\": \"".format(animation_type)
    for i, second in enumerate(seconds):
        if i == 0:
            data += "0:(), "
        data += "{}:(), ".format(int(second*12))
    data = data[:-2] + "\",\n"
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
    while True:
        file_name = add_txt_ext(file_name)
        if file_exists(file_name):
            continue
        if not create_another():
            return

def add_txt_ext(file_name):
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    return file_name

def file_exists(file_name):
    if os.path.isfile(file_name):
        overwrite = input(f"{file_name} already exists, overwrite? (y/n) ").lower()
        if overwrite == "n":
            return True
    return False

def create_another():
    another_file = input("Create another file? (y/n) ").lower()
    if another_file != "y":
        return False
    return True

animations = {
    1: "translation_x",
    2: "translation_y",
    3: "translation_z",
    4: "rotation_3d_x",
    5: "rotation_3d_y",
    6: "rotation_3d_z"
}

while create_animation_file(input("Enter the file name: ") + "Camera"):
    pass
