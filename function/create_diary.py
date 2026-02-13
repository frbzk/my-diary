import os
from datetime import datetime
from pathlib import Path

def create_daily_note():
    # 1. 取得當前日期
    today_str = datetime.now().strftime('%Y-%m-%d')
    filename = f"{today_str}.md"
    
    # 2. 設定目標路徑 (腳本所在位置的上一層的 Daily 資料夾)
    # 使用 .resolve() 確保路徑處理更準確
    base_path = Path(__file__).resolve().parent.parent
    target_dir = base_path / "Daily"
    file_path = target_dir / filename

    # 3. 檢查資料夾是否存在：不存在則不執行
    if not target_dir.is_dir():
        print(f"提示：資料夾 '{target_dir}' 不存在，程式已終止。")
        return

    # 4. 檢查檔案是否已存在：存在則不執行
    if file_path.exists():
        print(f"提示：檔案 '{filename}' 已存在，跳過執行。")
        return

    # 5. 定義內文範本
    content = f"""# {today_str} 雜記

## [TODO]
* 
* 
* 

## [Meta-Learning]
* 
* 
* 
"""

    # 6. 寫入檔案
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"成功創建檔案：{file_path}")
    except Exception as e:
        print(f"寫入檔案時發生錯誤: {e}")

if __name__ == "__main__":
    create_daily_note()