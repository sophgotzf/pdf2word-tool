# PDF 转 Word 工具

一个简单的 Windows 工具，用于将 PDF 文件转换为 Word (.docx) 格式。

## 功能特点

- ✅ 支持单个 PDF 文件转换
- ✅ 支持批量转换整个目录
- ✅ 保持原文档格式和布局
- ✅ 支持中文内容
- ✅ 可拖拽文件直接转换
- ✅ 命令行界面，简单易懂

## 使用方法

### 方法一：直接拖拽（最简单）
1. 将 PDF 文件拖到 `pdf2word.exe` 上
2. 程序会自动在同目录下生成 `.docx` 文件

### 方法二：命令行单个文件
```cmd
pdf2word.exe input.pdf
pdf2word.exe input.pdf -o output.docx
```

### 方法三：批量转换
```cmd
pdf2word.exe --batch ./pdf_folder
pdf2word.exe --batch ./pdf_folder --output ./word_folder
```

### 方法四：右键菜单（可选）
将 `pdf2word.exe` 复制到任意位置，右键 PDF 文件 → 打开方式 → 选择 `pdf2word.exe`

## 打包说明

如果你需要重新打包或修改源码：

### 环境要求
- Python 3.8+
- Windows 10/11

### 打包步骤
1. 安装 Python（确保勾选"Add Python to PATH"）
2. 双击运行 `build.bat`
3. 等待打包完成，可执行文件在 `dist\pdf2word.exe`

或者手动执行：
```cmd
pip install -r requirements.txt
pyinstaller --onefile --name pdf2word pdf2word.py
```

## 依赖库

- **pdf2docx**: PDF 解析和转换核心库
- **pyinstaller**: Python 打包工具

## 注意事项

- 复杂排版的 PDF 可能无法完美转换
- 扫描件/图片型 PDF 需要 OCR 功能（本工具不支持）
- 加密的 PDF 需要先解密
- 转换速度取决于 PDF 文件大小和复杂度

## 常见问题

**Q: 转换后格式错乱？**
A: 复杂排版的 PDF 可能无法完美还原，这是正常现象。

**Q: 程序闪退？**
A: 确保 PDF 文件没有损坏或加密。

**Q: 转换速度慢？**
A: 大文件需要更长时间，请耐心等待。

## 技术原理

使用 `pdf2docx` 库解析 PDF 的文本、表格、图片等元素，然后重建为 Word 文档格式。

## License

MIT License
