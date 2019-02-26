# DownStructure
download a structure to server

`!!structget <folder> <name> <url> (-o) (-b64)` - download structure file to server
- Must specify the folder, and it looks like `<folder>:<name>` in minecraft. 
- Only lowercase english letters, numbers and underscores are allowed in folder and file names.
- Use `-o` to overwrite local file when same filename is detected.
- Use `-b64` to open the base64 mode. The file will be downloaded and decoded as base64 data.

`!!structget -l (<key>)` - list all structures in server
- Use `<key>` to further specify the range with keyword

`!!structget -d <folder> <name>` - delete the structure file
- Use `*` in `<name>` to delete the folder, **BE CAREFUL**
