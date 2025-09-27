# zach api

written in go :D

## installation

```bash
go install
go run main .
```

set the $PORT env variable to change the port (default is 3000)

## usage

```bash
curl http://localhost:3000/quotes/random
```

```json
{
  "quote": "Databases are amazing. I can't believe how awesome Postgres is",
  "index": 1
}
```

## endpoints

/quotes/random - returns a random quote \
/quotes/{index} - returns the quote at the given index \
\
/photos/random - returns a random photo \
/photos/{title} - returns the photo with the given title \
\
/health - returns 200 OK if the server is running \
