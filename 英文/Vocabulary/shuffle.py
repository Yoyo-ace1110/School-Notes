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
            if line.startswith('#') or not line.strip():
                flush_buffer()
                final_output.append(line)
            elif line.startswith('  '):
                if current_shuffle_buffer:
                    current_shuffle_buffer[-1] += line
                else:
                    current_shuffle_buffer.append(line)
            else:
                current_shuffle_buffer.append(line)
        flush_buffer()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(final_output)
        print(f"成功！已處理：{input_path} -> {output_path}")
    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    parent_folder = r"G10-5_Exam\英文"
    target_file =   parent_folder + r"\單字書11-3.md"
    save_file =     parent_folder + r"\單字書11-3.md"
    shuffle_file(target_file, save_file)
