# DownStructure
下载并管理结构文件
### 本程序遵循以下协议 [GPL-3.0 License](https://github.com/TISUnion/DownStructure/blob/master/LICENSE)
---
## Guide
`!!struct get <folder> <name> <url> (-o) (-b64)` - 下载结构文件到本地的文件夹中
- 必须在 `<folder>` 指定文件夹，下载的文件在minecraft中显示为 `<folder>:<name>`。
- 文件夹和文件名只兼容英文小写字母、数字、短划线和下划线。
- 使用 `-o` 在重名时覆盖
- 使用 `-b64` 打开base64模式，将会作为base64编码的文件被下载和解码

`!!struct list(:<page>) (<key>)` - 列出服务器的结构文件，最多一页20个
- 指定关键字 `<key>` 进一步定位
- 使用如 `-l:2` 的格式来翻页

`!!struct del <folder> <name>` - 删除结构文件
- 在文件名处使用星号 `*` 时删除整个文件夹，**谨慎操作！**

`!!struct paste <folder> <name> (-d:<N|10M|1H|1D|1W|2W|1M|6M|1Y>)` -将结构文件以base64编码上传到pastebin
- 采用base64编码，下载时记得使用 `-b64`
- 使用 `<-d>` 设置保存时长；不使用 `<-d>` 时默认无限保存
- 冒号后分别是：无限、十天、一小时、一天、一周、两周、一个月、两个月和一年