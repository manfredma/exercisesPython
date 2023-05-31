import pandas as pd
import random

from IPython.display import Markdown, display
from faker import Faker

fake = Faker(locale="zh_CN")

data = {'Name': ['Apple', 'Banana', 'Orange', 'Grape', 'Watermelon'],
        'Size': ['Small', 'Medium', 'Small', 'Small', 'Large'],
        'IsYellow': [False, True, True, False, False],
        'Level': [1, 2, 1, 3, 2],
        'Dimension': [(1, 2, 3), (2, 3, 4), (1, 2, 2), (3, 4, 5), (4, 5, 6)],
        'Grade': ['A', 'A', 'A', 'C', 'B'],
        'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit']}

df = pd.DataFrame(data)
brands = ['红富士', '多乐', '美味佳', '鲜美', '天香', '国光']

df['Brand'] = [random.choice(brands) for _ in range(len(df))]
df['Barcode'] = [fake.ean(length=13) for _ in range(len(df))]

pd.set_option('expand_frame_repr', False)
print(df)

new_df = df[['Barcode', 'Size', 'IsYellow', 'Brand']].copy()
new_df['Brand Group'] = new_df['Brand'].map({'红富士': '红富士', '国光': '红富士'}).fillna('其他')


def level_grade(x):
    level = x["Level"]
    grade = x["Grade"]
    if level == 1 or (level == 2 and grade == "A"):
        return "优质"
    if level == 2:
        return "普通"
    return "差 (DE)"


new_df['品级'] = df.apply(level_grade, axis=1)

print(f"\n{new_df}")

keys = ['IsYellow', 'Brand Group']
grouped = new_df.groupby(keys)


def group_title(keys_, group_key_list_):
    l = list(zip(keys_, group_key_list_))
    return ", ".join([str(t[0]) + "=" + str(t[1]) for t in l])


for key, item in grouped:
    group_key_list = list(key)  # tuple
    # group title
    display(Markdown("#### " + group_title(keys, group_key_list)))
    print(grouped.get_group(key), "\n\n")


def print_markdown_table(headers, table_data):
    """
    Renders table given headers and data
    """
    md = ''

    for h in headers:
        md += '|' + h

    md += '|\n'

    for r in range(len(headers)):
        md += '|---'

    md += '|\n'

    for row in table_data:
        for element in row:
            md += '|' + str(element)
        md += '|\n'

    display(Markdown(md))


headers = ["name", "age"]
table_data = [["ma", "18"], ["xu", "17"]]
print_markdown_table(headers, table_data)
