

## API ENDPOINTS! json objects returned

### ALPHABET ENDPOINTS

- **GET url/alphabet**
    - list of JSONified alphabet objects from DB with all their properties 
- **POST url/alphabet**
    - generate new alphabet
- **GET url/alphabet/a.name**
    - return alphabet properties/data
- **DELETE url/alphabet/a.name**
    - NOT IMPLEMENTED

### CHARACTER ENDPOINTS ***nested***
- **GET url/alphabet/a.name/char/c.unicode**
    - return character color properties from specific alphabet
- **PUT url/alphabet/a.name/char/c.unicode**
    - add custom character to existing alphabet
- **DELETE url/alphabet/a.name/char/c.unicode**
    - delete custom chars ONLY

## TO DO:
- no duplicate letters for each alphabet
- custom letters created in post/custom letters altered in put
  
## API -- receives JSON from front-end logic

## INPUT
- Str: Char from Personal Name(s)
- Click: LOAD Alphabet
- Click: SAVE Alphabet


## PROCESSING -- API/backend
1. when user starts typing, create a new alphabet if not loaded; give it a name
2. for each letter in a user's name, create a new COLORFUL LETTER OBJECT and, if the color is not in the alphabet already, commit the letter to the alphabet
    - else: generate a new colorful letter



TO DO:
- no duplicate letters for each alphabet
- custom letters created in post/custom letters altered in put










## ALPHABET CLASS / db.Model
- unique rgb combination for each unicodepoint
- must contain 0-256 codepoints fo ASCII characters
- user can add to an alphabet, save and return/share that alphabet
    - **others can load and update this alphabet**
-

## API ENDPOINTS
- post: create new alphabet ... with 201 status code "Created"
- get: load alphabet (from db)
- post: add codepoint ... with 201 status code "Created"
    - *1 at a time or ...*
- get: individual rgb values for a letter/letter data

