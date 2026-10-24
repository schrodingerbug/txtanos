import os

print("I am Txtanos, the Mad Eraser.")
original_file = input("Which file do you want to reduce to atoms?").strip()

if not os.path.exists(original_file):
    print("File does not exist. Perhaps it is not in the current folder?")
else:
    name_part, ext_part = os.path.splitext(original_file)
    copied_half_file = f"{name_part}_blipped{ext_part}"

    with open(original_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    halfway_index = len(lines) // 2
    first_half = lines[:halfway_index]

    with open(copied_half_file, "w", encoding="utf-8") as file:
        file.writelines(first_half)

    print("Perfectly balanced, as all files should be.")
    print("I can finally rest. And watch the sun rise on a grateful folder.")
    print("I am inevitable.")
    #And I...am...Iron Man.
