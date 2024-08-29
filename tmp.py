import json

# 读取现有的JSON文件
with open('dataset/AMchat_dataset.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 多个增强后的数据条目，确保数学逻辑正确
new_entries = [
    {
        "conversation": [
            {
                "input": "将平面任意分成4个部分, 请证明一定存在一条直线通过其中至少三个部分.",
                "output": "证明: 我们采用反证法, 即假设任意一条直线最多通过其中两个部分. 我们在4个不同部分中的每个部分都挑选一个点, 不妨设 A, B, C, D, 请注意显然直线对 (AB, CD), (AC, BD), (AD, BC) 中必有一个不是平行的, 从而会有交点, 该交点无论是属于哪个部分都会导致矛盾。"
            }
        ]
    },
    {
        "conversation": [
            {
                "input": "平面被任意划分为四个区域，证明：必定存在一条直线，使得该直线至少穿过其中三个区域。",
                "output": "证明：\n1. 反证法：假设不存在穿过至少三个区域的直线。 在四个区域中各取一点，记为W、X、Y、Z, 显然它们一定会产生六条不重合的直线。考虑以下直线对：(WX,YZ)、(WY,XZ)、(WZ,XY)。每条直线最多穿过两个区域，因此这三组直线必须两两平行。 然而通过某个有并且仅有一条直线与已知直线平行, 从而导致矛盾。"
            }
        ]
    }
]

# 将新的数据条目添加到现有数据中
data.extend(new_entries)

# 将更新后的数据写回JSON文件
with open('dataset/AMchat_dataset_new.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"已成功添加 {len(new_entries)} 个新的数据条目到JSON文件中。")