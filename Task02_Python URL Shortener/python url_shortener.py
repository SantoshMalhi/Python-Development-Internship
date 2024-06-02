import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten_url(self, long_url):
        """Generate a shortened URL for the given long URL."""
        hash_code = hashlib.sha256(long_url.encode()).hexdigest()[:8]
        short_url = f"http://short.url/{hash_code}"
        self.url_map[short_url] = long_url
        return short_url

    def expand_url(self, short_url):
        """Expand a shortened URL to its original long URL."""
        if short_url in self.url_map:
            return self.url_map[short_url]
        else:
            return "Short URL not found."

def main():
    shortener = URLShortener()
    while True:
        print("\nSelect option:")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")

        choice = input("Enter choice(1/2/3): ")

        if choice == '3':
            print("Exiting the URL shortener. Goodbye!")
            break

        if choice == '1':
            long_url = input("Enter long URL to shorten: ")
            short_url = shortener.shorten_url(long_url)
            print(f"Shortened URL: {short_url}")

        elif choice == '2':
            short_url = input("Enter shortened URL to expand: ")
            long_url = shortener.expand_url(short_url)
            print(f"Expanded URL: {long_url}")

        else:
            print("Invalid input! Please select a valid option.")

if __name__ == "__main__":
    main()
