# FileSorter
Python automated script which sorts downloaded files and files in desktop into appropriate folders according to their names/types. Uses the watchdog library to monitor
the source folders (downloads and desktop). When a file is added to either folder an event is triggered which scans the folder for any file which should be relocated.

# Usage
This script can be run on any computer. The source and destination paths would need to be changed according to the users directory layout and file names.

# Citations
  * Watchdog, Yesudeep Mangalapilly 2023
