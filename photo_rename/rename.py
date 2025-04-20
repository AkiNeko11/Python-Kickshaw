import os
import re
from pathlib import Path


def rename_pictures(folder_path):
    # 支持的图片扩展名
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

    # 获取文件夹中的所有文件
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]

    # 找出当前最大的数字编号
    max_number = 0
    for filename in files:
        # 提取文件名中的数字
        match = re.match(r'(\d+)\..*', filename)
        if match:
            num = int(match.group(1))
            max_number = max(max_number, num)

    # 开始计数，从最大数字+1开始
    counter = max_number + 1

    # 重命名所有非数字命名的文件
    for filename in files:
        # 如果文件名已经是数字开头，跳过
        if re.match(r'^\d+\..*', filename):
            continue

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
    rename_pictures(current_dir)