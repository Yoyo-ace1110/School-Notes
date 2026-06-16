import random

def shuffle_file(file_path):
    try:
        # 讀取所有行
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # 打亂行序
        random.shuffle(lines)
        # 寫回原文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"成功！檔案已打亂: {file_path}")
    except Exception as e:
        print(f"錯誤: {e}")

if __name__ == "__main__": shuffle_file(r"G10-4_Exam\英文\單字書.md")
