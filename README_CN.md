# DownStructure
下载并管理结构文件
### 本程序遵循以下协议 [GPL-3.0 License](https://github.com/TISUnion/DownStructure/blob/master/LICENSE)
---
## Guide
`!!structget <folder> <name> <url> (-o) (-b64)` - 下载结构文件到本地的文件夹中
- 必须在 `<folder>` 指定文件夹，下载的文件在minecraft中显示为 `<folder>:<name>`。
- 文件夹和文件名只兼容英文小写字母、数字、短划线和下划线。
- 使用 `-o` 在重名时覆盖
- 使用 `-b64` 打开base64模式，将会作为base64编码的文件被下载和解码

`!!structget -l(:<page>) (<key>)` - 列出服务器的结构文件，最多一页20个
- 指定关键字 `<key>` 进一步定位
- 使用如 `-l:2` 的格式来翻页

`!!structget -d <folder> <name>` - 删除结构文件
- 在文件名处使用星号 `*` 时删除整个文件夹，**谨慎操作！**
