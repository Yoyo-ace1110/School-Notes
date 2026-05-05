import random

def shuffle_file(input_path: str, output_path: str) -> None:
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        final_output = []
        current_shuffle_buffer = []

        def flush_buffer():
            """將目前收集到的可打亂 Token 打亂並存入最終結果"""
            if current_shuffle_buffer:
                random.shuffle(current_shuffle_buffer)
                final_output.extend(current_shuffle_buffer)
                current_shuffle_buffer.clear()

        for line in lines:
            # 判斷是否為「不要動」的行：# 開頭 或 純空行
            if line.startswith('#') or not line.strip():
                flush_buffer()   # 先把之前的打亂
                final_output.append(line) # 原封不動放入特殊行
            
            # 判斷是否為 Token 的續行 (開頭至少 2 個空格)
            elif line.startswith('  '):
                if current_shuffle_buffer:
                    current_shuffle_buffer[-1] += line
                else:
                    # 如果第一行就是空格，當作一般行處理
                    current_shuffle_buffer.append(line)
            
            # 普通可打亂的行
            else:
                current_shuffle_buffer.append(line)

        # 最後處理剩餘的 buffer
        flush_buffer()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(final_output)
            
        print(f"成功！已處理：{input_path} -> {output_path}")

    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    parent_folder = r"G10-5_Exam\英文"
    target_file =   parent_folder + r"\雜誌.md"
    # save_file =     parent_folder + r"\單字書11-3.md"
    save_file = target_file
    shuffle_file(target_file, save_file)
