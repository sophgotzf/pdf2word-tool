# GitHub 发布指南

## 📦 第一步：创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角 **+** → **New repository**
3. 填写信息：
   - **Repository name**: `pdf2word-tool`
   - **Description**: `PDF 转 Word 工具 - 免费、离线、批量转换`
   - **Public** (公开仓库)
   - **不要** 勾选 "Initialize this repository with a README"
4. 点击 **Create repository**

## 🚀 第二步：推送代码到 GitHub

在仓库页面，你会看到推送指令。或者在本地执行：

```bash
# 进入工具目录
cd /home/linaro/.openclaw/workspace/pdf2word-tool

# 替换 YOUR_USERNAME 为你的 GitHub 用户名
git remote add origin https://github.com/YOUR_USERNAME/pdf2word-tool.git

# 推送代码
git push -u origin main
```

**如果提示需要认证：**
- 使用 GitHub Personal Access Token
- 或在 GitHub 设置中启用 SSH

## 🏷️ 第三步：创建 Release（发布可执行文件）

### 3.1 在 Windows 上打包 exe
1. 将代码复制到 Windows 电脑
2. 安装 Python 3.8+
3. 运行 `build.bat`
4. 得到 `dist/pdf2word.exe`

### 3.2 上传到 GitHub Releases
1. 在 GitHub 仓库页面，点击 **Releases** → **Create a new release**
2. 填写：
   - **Tag version**: `v1.0.0`
   - **Release title**: `PDF 转 Word 工具 v1.0`
   - **Description**: 
     ```
     🎉 第一个正式版本！
     
     功能：
     - PDF 转 Word 转换器
     - 支持单个/批量转换
     - 拖拽文件即可使用
     - 完全免费、离线使用
     
     使用：
     1. 下载 pdf2word.exe
     2. 拖拽 PDF 文件到 exe 上
     3. 完成！
     ```
3. 点击 **Attach binaries by dropping or uploading files**
4. 上传 `pdf2word.exe`
5. 勾选 **Set as the latest release**
6. 点击 **Publish release**

## 📝 第四步：更新 README

将 `README_GITHUB.md` 的内容复制为 `README.md`，并修改：
- 将 `YOUR_USERNAME` 替换为你的 GitHub 用户名
- 更新下载链接

```bash
# 在本地
cp README_GITHUB.md README.md
# 编辑 README.md，替换 YOUR_USERNAME
git add README.md
git commit -m "Update README with download links"
git push
```

## 🔗 第五步：获取下载链接

发布后，下载链接格式：
```
https://github.com/YOUR_USERNAME/pdf2word-tool/releases/latest/download/pdf2word.exe
```

这个链接可以直接放在公众号文章里！

## ✅ 检查清单

- [ ] 创建 GitHub 仓库
- [ ] 推送代码
- [ ] Windows 上打包 exe
- [ ] 创建 Release 并上传 exe
- [ ] 更新 README
- [ ] 获取下载链接
- [ ] 更新公众号文章中的下载链接

---

## 📮 公众号文章更新

拿到下载链接后，更新 `wechat-article.md` 中的下载方式部分：

```markdown
**GitHub 下载地址：**
https://github.com/YOUR_USERNAME/pdf2word-tool/releases/latest/download/pdf2word.exe

**或者扫码获取：**
[生成二维码图片]
```

需要我帮你生成二维码吗？
