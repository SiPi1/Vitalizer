# Vitalizer

A vital preset optimizer

# Process

1. _main.py_ is launched.
2. _main.py_ calls _gui.py_
3. _gui.py_ finishes and returns the **User Input variables** to _main.py_
4. _main.py_ loops through all the files in _original_presets_ and extracts the **Processing variables**
5. _main.py_ either sends a dictionary (https://pastebin.com/czG8igxq) for all of the files, or sends them one at a time, containing both **User Input variables** and **Processing variables** to _processing.py_
6. _processing.py_ processes the files and either returns the to _main.py_ or sends them off to _optimized_presets_

# Processing variables

_file_path_ // __string__ // The file path of the preset

_disabled_prefixes_ // __list__ // A list of the disabled prefixes

_file_data_ // __dict__ // The entire preset file data in dictionary form

# User Input variables

Stick to using these for all user inputs so our programs can work together

_round_amount_ // __int__ // The amount each parameter/knob is rounded too.

_pretty_file_ // __bool__ // Will pretty print the new JSON file for easy reading if true

_round_lfos_ //  __bool__ // Will round LFO's if true

_delete_unused_ // __bool__ // Enables deleting of all unused data from prefixes in _disabled_prefixes_ if true

# Directory Info

## Folders

### _original_presets_ 

Where you put the presets you want optimized, currently contains the _april 2021 free patch sharing thread_ bank

### _optimized_presets_

Where the presets go after optimization

### _data_

Contains general use data, such as a list of available prefixes

## Files

### _main.py_

The heart of the opperation

### _gui.py_

Contains the GUI of the program and is the only part that the user ineracts with

### _processing.py_

Contains the guts and actual functionality of the program.
