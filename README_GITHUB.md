# PDF 转 Word 工具

一个简单好用的 Windows PDF 转 Word 转换器，完全免费、离线使用、无广告无水印。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)

## ✨ 功能特点

- 🆓 **完全免费** - 不花一分钱，无任何收费项目
- 🔒 **离线使用** - 不需要联网，保护文件隐私
- 📦 **批量转换** - 一次可以转换多个 PDF 文件
- 📄 **保持格式** - 尽量还原原文档排版和格式
- 🇨🇳 **支持中文** - 中文内容完美识别和转换
- 🖱️ **简单易用** - 拖拽文件就能转换，无需学习成本

## 📥 下载安装

### 方式一：直接下载（推荐）
1. 访问 [Releases](https://github.com/sophgotzf/pdf2word-tool/releases) 页面
2. 下载最新版本的 `pdf2word.exe`
3. 双击运行即可使用

### 方式二：自行打包
如果你有 Python 环境，可以自行打包：

```bash
# 1. 克隆仓库
git clone https://github.com/sophgotzf/pdf2word-tool.git
cd pdf2word-tool

# 2. 安装依赖
pip install -r requirements.txt

# 3. 打包成 exe
pyinstaller --onefile --name pdf2word pdf2word.py

# 4. 可执行文件在 dist/pdf2word.exe
```

## 🚀 使用方法

### 方法一：拖拽转换（最简单）
1. 将 PDF 文件拖到 `pdf2word.exe` 上
2. 松开鼠标，自动开始转换
3. 转换完成后，同目录下会生成 `.docx` 文件

### 方法二：命令行
```bash
# 转换单个文件
pdf2word.exe input.pdf
pdf2word.exe input.pdf -o output.docx

# 批量转换目录
pdf2word.exe --batch ./pdf_folder
pdf2word.exe --batch ./pdf_folder --output ./word_folder
```

### 方法三：右键菜单（可选）
1. 以管理员身份运行 `install-context-menu.bat`
2. 右键点击任意 PDF 文件
3. 选择 "ConvertToWord" 即可转换

## 📖 使用示例

### 单个文件转换
```bash
# 基本用法
pdf2word.exe document.pdf

# 指定输出文件名
pdf2word.exe document.pdf -o my_document.docx
```

### 批量转换
```bash
# 转换整个文件夹
pdf2word.exe --batch ./my_pdfs

# 指定输出目录
pdf2word.exe --batch ./my_pdfs --output ./converted_words
```

## ⚠️ 注意事项

- **扫描件/图片型 PDF**：需要 OCR 功能，本工具暂不支持
- **加密的 PDF**：需要先解密才能转换
- **复杂排版**：部分复杂排版的 PDF 可能无法完美还原
- **文件大小**：建议单个文件不超过 100MB

## 🛠️ 技术栈

- **开发语言**：Python 3.8+
- **核心库**：[pdf2docx](https://pypi.org/project/pdf2docx/)
- **打包工具**：[PyInstaller](https://www.pyinstaller.org/)
- **支持系统**：Windows 10/11

## 📝 依赖库

```
pdf2docx>=0.5.0
pyinstaller>=5.0.0
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📬 联系方式

- 问题反馈：请提交 Issue
- 功能建议：欢迎提 Issue 或 Pull Request

---

**觉得好用？欢迎 Star ⭐ 支持一下！**
