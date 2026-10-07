import os
import zipfile

DATA_FILE = "students.txt"
ARCHIVE_FILE = "students.dat"


def decompress_and_load_data():
    """Checks for existing archive, decompresses, and loads stored student data."""
    if os.path.exists(ARCHIVE_FILE):
        print(f"Found existing data archive: {ARCHIVE_FILE}. Decompressing...")

     
        with zipfile.ZipFile(ARCHIVE_FILE, "r") as zipf:
            zipf.extractall()

       
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                content = f.read()
            print("Loaded Data:\n" + content)
    else:
        print(
            f"No existing '{ARCHIVE_FILE}' archive found. Initializing new session."
        )


def save_and_compress_data():
    """Saves current student data to file and compresses it into archive format."""
    sample_data = "Student ID: 101, Name: Alice\nStudent ID: 102, Name: Bob"

    
    with open(DATA_FILE, "w") as f:
        f.write(sample_data)

    
    with zipfile.ZipFile(
        ARCHIVE_FILE, "w", compression=zipfile.ZIP_DEFLATED
    ) as zipf:
        zipf.write(DATA_FILE)

    print(f"Successfully compressed and saved data to {ARCHIVE_FILE}")


def main():
    decompress_and_load_data()

   
    print("\n--- Program running ---")

   
    save_and_compress_data()


if __name__ == "__main__":
    main()