# DownStructure
download a structure to server and manage structures

[中文文档](./README_CN.md)
### This program follows [GPL-3.0 License](https://github.com/TISUnion/DownStructure/blob/master/LICENSE)
---
## Guide
`!!struct get <folder> <name> <url> (-o) (-b64)` - download structure file to server
- Must specify the folder, and it looks like `<folder>:<name>` in minecraft. 
- Only lowercase english letters, numbers and underscores are allowed in folder and file names.
- Use `-o` to overwrite local file when same filename is detected.
- Use `-b64` to open the base64 mode. The file will be downloaded and decoded as base64 data.

`!!struct list(:<page>) (<key>)` - list all structures in server, 20 entries in a page
- Use `<key>` to further specify the range with keyword
- Use `-list:<page>` to see other pages 

`!!struct del <folder> <name>` - delete the structure file
- Use `*` in `<name>` to delete the folder, **BE CAREFUL**

`!!struct paste <folder> <name> (-d:<N|10M|1H|1D|1W|2W|1M|6M|1Y>)` -upload base64 encoded file to pastebin
- Base64 format is used, don't forget to use `-b64` when download
- Use `<-d>` to set expire date; default to `N` 
- Times available are: never, 10 minutes, 1 hour, 1 day, 1 week, 2 weeks, 1 month, 6 months and 1 year
