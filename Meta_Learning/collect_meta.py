import os

# --- 設定路徑 (請根據你的 Ubuntu 路徑修改) ---
SOURCE_DIR = os.path.expanduser("~/桌面/Notes/Daily")
TARGET_FILE = os.path.expanduser("~/桌面/Notes/Meta_Learning/log.md")
START_MARKER = "## [Meta-Learning]"

def collect_meta():
    all_meta_entries = []

    # 取得所有 .md 檔案並排序
    if not os.path.exists(SOURCE_DIR):
        print(f"錯誤：找不到路徑 {SOURCE_DIR}")
        return

    files = sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')])

    for filename in files:
        file_path = os.path.join(SOURCE_DIR, filename)
        date = filename.replace('.md', '')
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        is_collecting = False
        current_block = []

        for line in lines:
            # 當偵測到 ## [Meta] 時，開始收集
            if line.strip().startswith(START_MARKER):
                is_collecting = True
                continue
            
            # 當開始收集後，如果遇到另一個 ## 開頭的行，就停止收集
            if is_collecting and line.strip().startswith("## "):
                is_collecting = False
                # 將收集到的內容存入清單
                if current_block:
                    content = "".join(current_block).strip()
                    all_meta_entries.append(f"### 來源：{date}\n{content}\n\n---\n")
                current_block = [] # 重置區塊內容內容
                continue

            # 如果正在收集狀態，就把行加入當前區塊
            if is_collecting:
                current_block.append(line)

        # 處理特殊情況：如果檔案結束了但還在收集狀態 (即後面沒有下一個 ##)
        if is_collecting and current_block:
            content = "".join(current_block).strip()
            all_meta_entries.append(f"### 來源：{date}\n{content}\n\n---\n")

    # 寫入目標檔案
    os.makedirs(os.path.dirname(TARGET_FILE), exist_ok=True)
    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write(f"# 元學習紀錄匯總\n生成時間：{os.popen('date').read()}\n\n")
        f.writelines(all_meta_entries)

    print(f"完成！已從 {len(files)} 個檔案中提取內容。")

if __name__ == "__main__":
    collect_meta()