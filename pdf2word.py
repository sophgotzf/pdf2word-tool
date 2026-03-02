#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF 转 Word 工具
支持批量转换 PDF 文件为 Word (.docx) 格式
"""

import sys
import os
import argparse
from pathlib import Path

try:
    from pdf2docx import Converter
except ImportError:
    print("错误：缺少 pdf2docx 库")
    print("请运行：pip install pdf2docx")
    sys.exit(1)


def convert_pdf_to_word(pdf_path, output_path=None):
    """
    转换单个 PDF 文件为 Word 格式
    
    Args:
        pdf_path: PDF 文件路径
        output_path: 输出文件路径（可选，默认为同目录下的.docx 文件）
    
    Returns:
        bool: 转换是否成功
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        print(f"错误：文件不存在 - {pdf_path}")
        return False
    
    if not pdf_path.suffix.lower() == '.pdf':
        print(f"错误：不是 PDF 文件 - {pdf_path}")
        return False
    
    # 确定输出路径
    if output_path is None:
        output_path = pdf_path.with_suffix('.docx')
    else:
        output_path = Path(output_path)
    
    print(f"正在转换：{pdf_path.name}")
    print(f"输出文件：{output_path.name}")
    
    try:
        cv = Converter(pdf_path)
        cv.convert(output_path)
        cv.close()
        print(f"✓ 转换成功：{output_path}")
        return True
    except Exception as e:
        print(f"✗ 转换失败：{e}")
        return False


def batch_convert(input_dir, output_dir=None):
    """
    批量转换目录下的所有 PDF 文件
    
    Args:
        input_dir: 输入目录
        output_dir: 输出目录（可选，默认为输入目录）
    """
    input_dir = Path(input_dir)
    
    if not input_dir.exists():
        print(f"错误：目录不存在 - {input_dir}")
        return
    
    if output_dir is None:
        output_dir = input_dir
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    pdf_files = list(input_dir.glob('*.pdf')) + list(input_dir.glob('*.PDF'))
    
    if not pdf_files:
        print(f"目录中没有找到 PDF 文件：{input_dir}")
        return
    
    print(f"找到 {len(pdf_files)} 个 PDF 文件")
    print("-" * 50)
    
    success_count = 0
    for pdf_file in pdf_files:
        output_path = output_dir / pdf_file.with_suffix('.docx').name
        if convert_pdf_to_word(pdf_file, output_path):
            success_count += 1
        print()
    
    print("-" * 50)
    print(f"转换完成：{success_count}/{len(pdf_files)} 个文件成功")


def main():
    parser = argparse.ArgumentParser(
        description='PDF 转 Word 工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  # 转换单个文件
  pdf2word.exe input.pdf
  pdf2word.exe input.pdf -o output.docx
  
  # 批量转换目录
  pdf2word.exe --batch ./pdf_folder
  pdf2word.exe --batch ./pdf_folder --output ./word_folder
  
  # 拖拽文件到 exe 上
  直接将 PDF 文件拖到 pdf2word.exe 上即可转换
        """
    )
    
    parser.add_argument('input', nargs='?', help='PDF 文件或目录路径')
    parser.add_argument('-o', '--output', help='输出文件路径（单个文件）或输出目录（批量）')
    parser.add_argument('--batch', action='store_true', help='批量转换模式（输入为目录）')
    parser.add_argument('-v', '--version', action='version', version='PDF2Word v1.0')
    
    args = parser.parse_args()
    
    print("=" * 50)
    print("PDF 转 Word 工具 v1.0")
    print("=" * 50)
    print()
    
    # 如果没有提供参数，显示帮助
    if not args.input:
        parser.print_help()
        print("\n提示：你也可以直接将 PDF 文件拖到此程序上")
        input("\n按回车键退出...")
        return
    
    input_path = Path(args.input)
    
    # 处理拖拽文件的情况（Windows）
    if input_path.suffix.lower() == '.pdf' and not args.batch:
        convert_pdf_to_word(input_path, args.output)
    elif args.batch or input_path.is_dir():
        batch_convert(input_path, args.output)
    else:
        print(f"错误：请提供有效的 PDF 文件或目录")
        parser.print_help()
    
    print()
    input("按回车键退出...")


if __name__ == '__main__':
    main()
