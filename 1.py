import os
import shutil

def collect_design_md(src_dir, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.lower() == "design.md":   # ✅ FIXED

                src_path = os.path.join(root, file)

                folder_name = os.path.basename(root)
                base_name = f"{folder_name}_design"
                ext = ".md"

                dest_path = os.path.join(dest_dir, base_name + ext)

                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(
                        dest_dir,
                        f"{base_name}_{counter}{ext}"
                    )
                    counter += 1

                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} → {dest_path}")


# 🔧 paths
source_directory = r"E:\tbwproject"
destination_directory = r"E:\tbwproject\all_md"

collect_design_md(source_directory, destination_directory)