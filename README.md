# Vitalizer

A vital preset optimizer

# Processing variables

_file_path_ // __string__ // The file path of the preset

_disabled_prefixes_ // __list__ // A list of the disabled prefixes

_file_data_ // __dict__ // The entire preset file data in dictionary form

# User Input variables

## General

Stick to using these for all user inputs so our programs can work together

_round_amount_ // __int__ // The amount each parameter/knob is rounded too.

_pretty_file_ // __bool__ // Will pretty print the new JSON file for easy reading if true

_round_lfos_ //  __bool__ // Will round LFO's if true

_delete_unused_ // __bool__ // Enables deleting of all unused data from prefixes in _disabled_prefixes_ if true

# Directory Info

## _original_presets_ 

Where you put the presets you want optimized, currently contains the _november 2020 free patch sharing thread_ bank

## _optimized_presets_

Where the presets go after optimization

## _data_

Contains general use data, such as a list of available prefixes
