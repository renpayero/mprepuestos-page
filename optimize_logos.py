import os
from PIL import Image

def resize_images(directory, max_width=300):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.webp', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    if width > max_width:
                        # Calculate new height to maintain aspect ratio
                        new_height = int((max_width / width) * height)
                        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                        
                        # Save as WebP
                        target_path = os.path.splitext(filepath)[0] + ".webp"
                        img.save(target_path, "WEBP", quality=90)
                        print(f"Resized and saved: {target_path} ({max_width}x{new_height})")
                    else:
                        print(f"Skipped (already small enough): {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    resize_images("/root/webs/mp-repuestos/assets/Logos")
