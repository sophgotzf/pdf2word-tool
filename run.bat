@echo off
chcp 65001 >nul
title PDF 转 Word 工具

echo ================================================
echo           PDF 转 Word 工具
echo ================================================
echo.

if "%~1"=="" (
    echo 用法:
    echo   1. 将 PDF 文件拖到此窗口
    echo   2. 或将 PDF 文件拖到 pdf2word.exe 上
    echo   3. 或运行：pdf2word.exe 文件.pdf
    echo.
    echo 按回车键退出...
    pause >nul
    exit /b
)

pdf2word.exe %*
