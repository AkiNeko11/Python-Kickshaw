import os
import re
from pathlib import Path


def rename_pictures(folder_path, start_number):
    # 支持的图片扩展名
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    # 获取文件夹中的所有图片文件
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]

    # 如果文件夹为空，直接返回
    if not files:
        print("文件夹中没有找到图片文件！")
        return

    # 对文件按名称排序（可选，按需取消注释）
    # files.sort()

    # 开始计数，从用户输入的数字开始
    counter = start_number

    # 重命名所有文件
    for filename in files:
        # 获取文件扩展名
        ext = os.path.splitext(filename)[1]

        # 生成新文件名
        new_name = f"{counter}{ext}"

        # 检查是否已存在同名文件
        while os.path.exists(os.path.join(folder_path, new_name)):
            counter += 1
            new_name = f"{counter}{ext}"

        # 执行重命名
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"重命名: {filename} -> {new_name}")
        counter += 1

    print("重命名完成！")


if __name__ == "__main__":
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取用户输入的起始数字
    while True:
        try:
            start_num = int(input("请输入开始的数字 n: "))
            if start_num >= 0:
                break
            print("请输入一个非负整数！")
        except ValueError:
            print("请输入有效的数字！")

    rename_pictures(current_dir, start_num)