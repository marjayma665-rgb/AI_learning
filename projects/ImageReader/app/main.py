from pathlib import Path

folder = Path("data/input")
img_list = []

for item in folder.iterdir():
    if item.suffix.lower() in [".jpg",".jpeg",".png",".webp"]:
        img_list.append(item)
        
img_list.sort()

print("文件夹内所有图片：")
for path in img_list:
    print(path.name)
   