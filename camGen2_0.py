# Don't recreate the wheel, learn this library
import os
import re
import sys
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

# Larger goal
# Allow input to the data created IE, at frame X in type Y would you like to frame X, blank for nothing at frame but move to next


# Names

# main
# file_create
# animation_type
# data_copy
# data_save
# Create a file yes/no > name file > enter frame rate > enter seconds
# ask for what to add
# list parameters to add, do it three per line
# variables: seconds,

import click

@click.command()
def main():
    # Ask the user if they want to create a file or exit
    choice = click.confirm("Do you want to create a file?", default=True)
    if choice:
        # If they choose to create a file, ask for the file name
        file_name = click.prompt("Enter the file name")
        # Create the file and handle errors
        create_output_file(file_name)
        # Add animations to file
        add_animations_to_file(file_name)
    else:
        sys.exit()





if __name__ == '__main__':
    main()










