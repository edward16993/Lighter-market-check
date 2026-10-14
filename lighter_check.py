
import requests

URL = "https://mainnet.zklighter.elliot.ai/api/v1/orderBooks"

def main():
    response = requests.get(URL, timeout=20)
    response.raise_for_status()
    data = response.json()

    books = data.get("order_books", data.get("orderBooks", []))

    if not books:
        print("No order_books list found.")
        print("Response keys:", list(data.keys()))
        print(data)
        return

    print("Lighter markets returned:", len(books))

    for book in sorted(books, key=lambda item: str(item.get("symbol", ""))):
        print(
            f"Symbol={book.get('symbol')} | "
            f"Market ID={book.get('market_id')} | "
            f"Type={book.get('market_type')} | "
            f"Status={book.get('status')}"
        )

if __name__ == "__main__":
    main()
