# Shorty

## What this is

`SHORTY` is a simple URL shortener that uses Python and FastAPI for its backend. It generates five random letters, both upper and lower case, for each valid link. The frontend is kept simple on purpose so there is no useless stuff.

---
## How to run it


### With Python

You need Python 3.10 or newer.

```bash

python3 -m venv .venv

source .venv/bin/activate # Windows: .venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload

```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The entries are kept in memory: after a restart the list is empty again.


### With Docker

```bash
docker build -t shorty .

docker run -p 8000:8000 shorty
```

Then open http://127.0.0.1:8000 in your browser.

---
## Team

team members

|      GitHub      |                 Role                  |
| :--------------: | :-----------------------------------: |
| imjusttypingshit |                backend                |
|   BigCheese95    |               frontend                |
|      izqkk       | project manager, supervisor, database |
  
---
## How we work

Each feature has an issue associated with it. For each issue there is a brand new branch created and that that is later merged to main. No direct commits to main are ever done.

We  try to put the team member's name, who does a push at the start of the branch name that gets merged into main.

---
## Sources



|        source         |       for what       |          when           |
| :-------------------: | :------------------: | :---------------------: |
|   www.w3schools.com   | HTTP and CSS styling |       2026.11.16        |
| www.geeksforgeeks.org |       FastAPI        |       2026.11.17        |
|    docs.python.org    |    Python syntax     | through out the project |

---
## Use of AI

|   AI    |                         for what                         |          when           |
| :-----: | :------------------------------------------------------: | :---------------------: |
| Claude  | explaining concepts and providing a better understanding | through out the project |
| ChatGPT | explaining concepts and providing a better understanding | through out the project |
