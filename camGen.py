import os

def create_file(file_name, seconds, animation_type):
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

animations = {
    1: "translation_x",
    2: "translation_y",
    3: "translation_z",
    4: "rotation_3d_x",
    5: "rotation_3d_y",
    6: "rotation_3d_z"
}

def create_animation_file(file_name):
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
            create_file(file_name, seconds, animation_type)
            another_animation = input("Do you want to add another animation to the file? (y/n) ").lower()
            if another_animation != "y":
                break
        if not create_another_file():
            return False
    return True

while create_animation_file(input("Enter the file name: ") + "Camera"):
    pass
