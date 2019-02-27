# DownStructure
download a structure to server and manage structures

[中文文档](./README_CN.md)
### This program follows [GPL-3.0 License](https://github.com/TISUnion/DownStructure/blob/master/LICENSE)
---
## Guide
`!!structget <folder> <name> <url> (-o) (-b64)` - download structure file to server
- Must specify the folder, and it looks like `<folder>:<name>` in minecraft. 
- Only lowercase english letters, numbers and underscores are allowed in folder and file names.
- Use `-o` to overwrite local file when same filename is detected.
- Use `-b64` to open the base64 mode. The file will be downloaded and decoded as base64 data.

`!!structget -l(:<page>) (<key>)` - list all structures in server, 20 entries in a page
- Use `<key>` to further specify the range with keyword
- Use `-l:<page>` to see other pages 

`!!structget -d <folder> <name>` - delete the structure file
- Use `*` in `<name>` to delete the folder, **BE CAREFUL**
