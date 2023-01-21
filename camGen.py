import os

def create_file(file_name, seconds, animation_type, initial_value):
    data = "\"{}\": \"".format(animation_type)
    for i, second in enumerate(seconds):
        if i == 0:
            data += "0:(), "
        data += "{}:(), ".format(int(second*12), initial_value)
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
    seconds_string = input("Enter the seconds separated by commas: ")
    return [float(x) for x in seconds_string.split(",")]

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

while True:
    file_name = input("Enter the file name: ")
    file_name += "Camera"
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    if os.path.isfile(file_name):
        overwrite = input(f"{file_name} already exists, Do you want to overwrite? (y/n) ").lower()
        if overwrite == "n":
            continue
    animation_type = get_animation_type(animations)
    if animation_type is None:
        break
    seconds = get_seconds()
    create_file(file_name, seconds, animation_type, animations[animation_type])
    if not create_another_file():
        break
