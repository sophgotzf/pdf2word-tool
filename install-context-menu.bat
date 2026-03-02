@echo off
chcp 65001 >nul
echo ================================================
echo 注册右键菜单 - PDF 转 Word
echo ================================================
echo.

set "EXE_PATH=%~dp0pdf2word.exe"

echo 正在添加右键菜单项...
reg add "HKCR\pdf_auto_file\shell\ConvertToWord\command" /ve /d "\"%EXE_PATH%\" \"%%1\"" /f >nul 2>&1
reg add "HKCR\.pdf" /ve /t REG_SZ /d "pdf_auto_file" /f >nul 2>&1

if %errorlevel% equ 0 (
    echo ✓ 右键菜单注册成功！
    echo.
    echo 现在你可以右键点击 PDF 文件，选择 "ConvertToWord" 进行转换
) else (
    echo ✗ 注册失败，请以管理员身份运行此脚本
)

echo.
pause
