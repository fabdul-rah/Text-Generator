import requests
import os
import re
from bs4 import BeautifulSoup

# URL of the Project Gutenberg text file that lists books
main_url = "https://www.gutenberg.org/cache/epub/30000/pg30000.txt"

# Directory to save individual books
save_dir = "gutenberg_books"
os.makedirs(save_dir, exist_ok=True)

# Download the main text file
response = requests.get(main_url)

if response.status_code == 200:
    text_data = response.text
    
    # Extract potential book titles and IDs (Assuming format: "Title — Author [EBook #ID]")
    book_entries = re.findall(r"(.+?) — .+\[EBook #(\d+)\]", text_data)

    for title, book_id in book_entries:
        # Construct the book's page URL
        book_page_url = f"https://www.gutenberg.org/ebooks/{book_id}"

        # Fetch the book's webpage
        book_page_response = requests.get(book_page_url)

        if book_page_response.status_code == 200:
            soup = BeautifulSoup(book_page_response.text, "html.parser")

            # Look for the first plain text file link
            text_link = soup.find("a", href=re.compile(rf"/cache/epub/{book_id}/pg{book_id}.*\.txt"))

            if text_link:
                # Construct full book text URL
                book_url = f"https://www.gutenberg.org{text_link['href']}"

                # Download the book text
                book_response = requests.get(book_url)

                if book_response.status_code == 200:
                    # Clean the book title to be a valid filename
                    safe_title = re.sub(r"[^\w\s-]", "", title).strip().replace(" ", "_")
                    file_path = os.path.join(save_dir, f"{safe_title}.txt")

                    # Save the book text
                    with open(file_path, "w", encoding="utf-8") as book_file:
                        book_file.write(book_response.text)

                    print(f"Saved: {safe_title}.txt")
                else:
                    print(f"Failed to download book: {title} (URL: {book_url})")
            else:
                print(f"No plain text file found for: {title} (ID: {book_id})")
        else:
            print(f"Failed to fetch book page: {book_page_url}")
else:
    print("Failed to download book list. Status code:", response.status_code)
