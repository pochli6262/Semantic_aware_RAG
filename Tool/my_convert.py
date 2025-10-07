import pickle, os

with open("Tool/path2Code", "rb") as f:
    data = pickle.load(f)

# 替換所有路徑分隔符
new_data = {}
for k, v in data.items():
    new_data[k] = v.replace("\\", "/")

with open("Tool/path2Code", "wb") as f:
    pickle.dump(new_data, f)

print("Fixed entries:", len(new_data))
