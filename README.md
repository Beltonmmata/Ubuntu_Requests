# Ubuntu_Requests

# 🐧 Ubuntu Image Fetcher

> **"I am because we are" — Ubuntu Philosophy**  
> A mindful Python script that connects to the wider web community, fetches images respectfully, and organizes them for later appreciation.

---

## 📖 Description

This project demonstrates the power of Python libraries (specifically `requests`) to fetch images from the internet while following the Ubuntu principles of **community, respect, sharing, and practicality**.

The script:

- Prompts the user for one or more image URLs
- Creates a directory `Fetched_Images` if it doesn’t exist
- Downloads and saves the image(s) locally
- Handles errors gracefully (e.g., bad URLs, connection issues)
- Avoids duplicates using hashing
- Ensures files are actually images by checking HTTP headers

---

## 🚀 Features

- ✅ Multiple URL support (comma separated input)
- ✅ Graceful error handling (network failures, invalid URLs, etc.)
- ✅ Duplicate detection using MD5 hashing
- ✅ Content-Type check (ensures only images are saved)
- ✅ Organized saving into `Fetched_Images/` directory

---

## 🛠️ Requirements

- Python 3.7+
- `requests` library

Install dependencies:

```bash
pip install requests
```
