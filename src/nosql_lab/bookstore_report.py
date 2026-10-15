
"""Generate a report about the bookstore MongoDB database."""

import logging
import os

from pymongo import MongoClient


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def main():
    """Connect to MongoDB and print a report about authors and books."""
    client = None

    try:
        # Read MongoDB connection settings from environment variables.
        url = os.environ["MONGODB_ATLAS_URL"]
        username = os.environ["MONGODB_ATLAS_USER"]
        password = os.environ["MONGODB_ATLAS_PWD"]

        # Connect to MongoDB Atlas.
        client = MongoClient(
            url,
            username=username,
            password=password,
            serverSelectionTimeoutMS=5000
        )

        # Check that the connection works.
        client.admin.command("ping")
        logging.info("Connected to MongoDB Atlas.")

        # Select the bookstore database.
        db = client["bookstore"]

        # Retrieve all authors and books.
        authors = list(db.authors.find())
        books = list(db.books.find())

        # Print the report.
        print("\nBOOKSTORE REPORT")
        print("================")
        print(f"Total authors: {len(authors)}")
        print(f"Total books: {len(books)}")

        print("\nAUTHORS")
        for author in authors:
            print(f"- {author['name']}")

        print("\nBOOKS")
        for book in books:
            print(f"- {book['title']}")

        logging.info("Bookstore report completed.")

    except Exception:
        logging.exception("Could not generate the bookstore report.")

    finally:
        # Close the connection when finished.
        if client is not None:
            client.close()
            logging.info("MongoDB connection closed.")


if __name__ == "__main__":
    main()
