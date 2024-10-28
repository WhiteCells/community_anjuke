import os


def delete_files_containing_string(folder_path, target_string):
    with open("delete_list.txt", "a", encoding="utf-8") as f:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()

                    if target_string in content:
                        f.write(filename)
                        print(f"Deleting file: {file_path}")
                        os.remove(file_path)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")


folder_to_check = "wuhan_community"
string_to_search = "xxzlGatewayUrl"
delete_files_containing_string(folder_to_check, string_to_search)
