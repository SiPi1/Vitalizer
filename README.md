# Vitalizer

A vital preset optimizer

# User Input variables

## General

Stick to using these for all user inputs so our programs can work together

_round_amount_ // __int__ // The amount each parameter/knob is rounded too.

_pretty_file_ // __bool__ // Will pretty print the new JSON file for easy reading if true

_round_lfos_ //  __bool__ // Will round LFO's if true

## Delete Data

_delete_unused_ // __bool__ // Enables deleting of unused data if true

_prefixes_ // __list__ // Contains the list of prefixes to look for, paired with _allBut_noneBut_ will decide what you do with them

_allBut_noneBut_ // __bool__ // If true exclued the list of prefixes from unused data deletion, if false exclude all except the list of prefixes
