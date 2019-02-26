# DownStructure
download a structure to server

`!!structget <folder> <name> <url> (-o) (-b64)` - download structure file to server
- Must specify the folder, and it looks like `<folder>:<name>` in minecraft. 
- Only english letters(uppercase and lowercase), numbers and underscores are allowed in folder and file names.
- Use `-o` to overwrite local file when same filename is detected.
- Use `-b64` to open the base64 mode. The file will be downloaded and decoded as base64 data.

`!!structget -l (<foldername>)` - list all structures in server
- Use `<foldername>` to further specify the range
