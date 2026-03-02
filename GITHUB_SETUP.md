# 🚀 GitHub 托管快速指南

## 第一步：添加 SSH Key 到 GitHub（2 分钟）

### 1.1 复制 SSH 公钥
已为你生成好 SSH key，复制以下内容：

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINsDi+vJfzvdZJVPap0qyd1ix4XelMmHlYBTatrpxPPh zhifei.tang@sophgo.com
```

### 1.2 添加到 GitHub
1. 登录 https://github.com
2. 点击右上角头像 → **Settings**
3. 左侧菜单 → **SSH and GPG keys**
4. 点击 **New SSH key**
5. Title: `sophon-workstation`
6. Key type: 选 **Authentication Key**
7. 粘贴上面的公钥
8. 点击 **Add SSH key**

---

## 第二步：创建 GitHub 仓库（1 分钟）

### 方式 A：手动创建（推荐）
1. 访问 https://github.com/new
2. Repository name: `pdf2word-tool`
3. Description: `PDF 转 Word 工具 - 免费、离线、批量转换`
4. **Public** (公开)
5. **不要** 勾选 "Add a README file"
6. 点击 **Create repository**

### 方式 B：使用 API（需要 Token）
如果你有 GitHub Personal Access Token，告诉我，我可以自动创建。

---

## 第三步：推送代码（1 分钟）

创建仓库后，在本地执行：

```bash
cd /home/linaro/.openclaw/workspace/pdf2word-tool

# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin git@github.com:YOUR_USERNAME/pdf2word-tool.git

# 推送代码
git push -u origin main
```

---

## 第四步：发布 Release（上传 exe）

### 4.1 在 Windows 上打包
```
1. 将 pdf2word-tool 文件夹复制到 Windows
2. 安装 Python 3.8+ (https://python.org)
3. 双击运行 build.bat
4. 得到 dist/pdf2word.exe
```

### 4.2 上传到 GitHub Releases
1. 访问你的仓库 → **Releases** → **Create a new release**
2. Tag version: `v1.0.0`
3. Release title: `PDF 转 Word 工具 v1.0`
4. 上传 `pdf2word.exe`
5. 勾选 **Set as the latest release**
6. 点击 **Publish release**

---

## 第五步：获取下载链接

发布后，下载链接：
```
https://github.com/YOUR_USERNAME/pdf2word-tool/releases/latest/download/pdf2word.exe
```

---

## ✅ 完成检查清单

- [ ] SSH Key 已添加到 GitHub
- [ ] 仓库已创建（pdf2word-tool）
- [ ] 代码已推送（git push）
- [ ] Windows 上已打包 exe
- [ ] Release 已发布
- [ ] 下载链接已获取

---

## 📮 下一步

拿到下载链接后，告诉我，我帮你：
1. 更新公众号文章中的下载链接
2. 生成二维码图片
3. 优化文章排版

---

**需要我帮你做什么？**
- 如果卡在某一步，告诉我
- 如果有 GitHub Token，我可以自动创建仓库
- 如果需要修改任何文件，随时说
