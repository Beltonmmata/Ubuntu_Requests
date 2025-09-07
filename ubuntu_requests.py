import requests
import os
import hashlib
from urllib.parse import urlparse

def get_filename_from_url(url):
    """Extracts a filename from URL or generates one if not present."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:  # If URL doesn't end with a file name
        filename = "downloaded_image.jpg"
    return filename

def is_duplicate(content, save_dir):
    """Check if an image with same hash already exists in directory."""
    file_hash = hashlib.md5(content).hexdigest()
    for existing_file in os.listdir(save_dir):
        with open(os.path.join(save_dir, existing_file), "rb") as f:
            if hashlib.md5(f.read()).hexdigest() == file_hash:
                return True
    return False

def fetch_image(url, save_dir="Fetched_Images"):
    """Fetch an image from a given URL and save it locally."""
    try:
        # Make sure directory exists
        os.makedirs(save_dir, exist_ok=True)

        # Request the image with precautions
        headers = {"User-Agent": "UbuntuFetcher/1.0"}
        response = requests.get(url, timeout=10, headers=headers, stream=True)
        response.raise_for_status()

        # Security precaution: check content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipping {url} (Not an image, got {content_type})")
            return

        # Extract filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(save_dir, filename)

        # Check duplicates
        content = response.content
        if is_duplicate(content, save_dir):
            print(f"⚠ Duplicate detected: {filename}, skipping save.")
            return

        # Save image
        with open(filepath, "wb") as f:
            f.write(content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ Unexpected error for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter one or more image URLs (comma separated): ")
    url_list = [url.strip() for url in urls.split(",") if url.strip()]

    for url in url_list:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
