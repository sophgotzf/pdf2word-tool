@echo off
chcp 65001 >nul
echo ================================================
echo PDF 转 Word 工具 - 打包脚本
echo ================================================
echo.

echo [1/3] 安装依赖...
pip install -r requirements.txt
if errorlevel 1 (
    echo 错误：依赖安装失败
    pause
    exit /b 1
)
echo.

echo [2/3] 打包为可执行文件...
pyinstaller --onefile --name pdf2word --icon=NONE --console pdf2word.py
if errorlevel 1 (
    echo 错误：打包失败
    pause
    exit /b 1
)
echo.

echo [3/3] 清理临时文件...
if exist build rmdir /s /q build
if exist pdf2word.spec del pdf2word.spec
echo.

echo ================================================
echo 打包完成！
echo 可执行文件位置：dist\pdf2word.exe
echo ================================================
echo.
pause
