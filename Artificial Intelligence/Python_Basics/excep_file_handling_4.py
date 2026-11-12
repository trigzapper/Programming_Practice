from pathlib import Path

# Define a directory path

data_dir = Path("data/raw_images")

# Create directory automatically if it doesn't exist

data_dir.mkdir(parents = True , exist_ok = True )

# Build a file path securely ( handles slashes automatically regardless of OS )

image_path = data_dir / "cat_01.jpg"
print(image_path)

#check if file exists

if image_path.exists:
    print("Found")
else:
    print("Not Found")