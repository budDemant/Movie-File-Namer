# Movie File Namer

A simple tool that helps label and re-direct movie files. The main movie file will be renamed to the parent folder name (which should already be the movie name and year released), and the other files will be moved to an Extras sub-directory. This is the format that is required for a media server like Jellyfin.

## Project Overview
- **Input:**
  - Directory that contains a movie file and its extras (if any)
- **Output:**
  - Movie file name will match the directory name
  - Other files moved to sub-directory labeled "Extras"

## How It Works
1. **List Directory Contents**
   - Each file is put in a dictionary, which lists each file's name and corresponding file size.
2. **Identify Main Movie File**
   - The file with the largest size is identified: largest_file.
3. **Label Main Movie File**
   - largest_file is renamed to that of its parent folder.
4. **Re-direct Extras**
   - The lesser-sized files are put in a sub-directory called "Extras" (created if it doesn't already exist).

## Technologies Used
- Python 3
- OS

## Getting Started
1. Copy the path to the movie's files (ex: C:\Users\anthd\Videos\The_Matrix_1999).
2. Run the program.
3. Paste the path in the terminal (Right-click or Ctrl+Shift+V).


## Potential Extensions
- GUI for path selection
- Requirements for proper initial file structure
- Error handling for invalid file path
- Reverting file path to original state

## License
MIT License

---
