
db = db.getSiblingDB("bookstore");

// Load authors
db.authors.drop();
let authors = JSON.parse(
  fs.readFileSync("/Users/graciehughes/ds2022-fall-2026/lab-05-nosql/authors.json", "utf8")
);
db.authors.insertMany(authors);

// Load books
db.books.drop();
let books = JSON.parse(
  fs.readFileSync("/Users/graciehughes/ds2022-fall-2026/lab-05-nosql/books.json", "utf8")
);
db.books.insertMany(books);

// Display all authors and books
db.authors.find();
db.books.find();

// Insert two new books
db.books.insertMany([
  {
    title: "The Hobbit",
    published_year: 1937,
    author_ids: ["author_004"]
  },
  {
    title: "The Lord of the Rings",
    published_year: 1954,
    author_ids: ["author_004"]
  }
]);

// Insert the missing author
db.authors.insertOne({
  _id: "author_004",
  name: "J.R.R. Tolkien",
  nationality: "British",
  bio: {
    short: "Author of The Hobbit and The Lord of the Rings.",
    long: "J.R.R. Tolkien was a British writer and scholar best known for creating Middle-earth and writing The Hobbit and The Lord of the Rings."
  }
});

// Find books by either author
db.books.find({
  author_ids: { $in: ["author_001", "author_004"] }
});
