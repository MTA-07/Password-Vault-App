FILE_NAME = "valut.txt"

def save_entry(site, username, encrypted_password):
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{site}|{username}|{encrypted_password}\n")
    print(f"[DEBUG] {site} successfully saved to file ")

def load_entries():
    entries = []

    try:
        with open(FILE_NAME, "r", encoding= "utf-8") as file:
            data = file.read()
            lines = data.split("\n")

            for line in lines:
                if line.strip():
                    parts = line.split("|")
                    if len(parts)==3:
                        entries.append({
                            "site": parts[0],
                            "username": parts[1],
                            "encrypted": parts[2]
                        })
    except FileNotFoundError:
        print("[DEBUG] vault.txt not found yet, returning empty list")

    return entries


#TEST

if __name__ == "__main__":
    save_entry("github", "mehmet", "INeedToForget1221511")

    saved_entries = load_entries()
    print('Entries in file:', saved_entries)


def delete_entry(site_to_delete):
    entries = load_entries()

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for entry in entries:
            if entry["site"] != site_to_delete:
                file.write(f"{entry["site"]}|{entry["username"]}|{entry["encrypted"]}\n")

    print(f"[DEBUG]{site_to_delete} deleted from file")
    



