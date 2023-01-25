# Don't reinvent the wheel

import click


# Flow
# Main to encompass the whole program, do you want to create a file or exit
# Creating the file name
# Select frame rate
# Select time
# Select from list of animation types
# If we're doing all of them then different types require different amounts of input and types
# Figure out different types of data needed, T/F, string, lists of samplers, min/max settings, etc...
# maybe look at the scripts in Deforum for some of these answers?
# Add all data to file in a structured way
# set default values

# Larger goal
# Allow input to the data created IE, at frame X in type Y would you like to frame X, blank for nothing at frame but move to next



fps = None

@click.command()
def main():
    global fps
    create_file()
    fps = click.prompt("Enter the frames per second", type=int)
    click.echo("Frames per second: {}".format(fps))

def create_file():
    file_name = click.prompt("Enter the name of the output file", default="output.txt")
    with open(file_name, "w") as f:
        f.write("")
    click.echo("File {} created.".format(file_name))

def select_parameter():
    # enter number from list, or list items





if __name__ == '__main__':
    main()
