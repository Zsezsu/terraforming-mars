# Terraforming Mars


## About 🚀🪐

This application is based on the famous board game **Terraforming Mars**.

In **Terraforming Mars**, you play a 🌐 corporation in the 2400s, racing to make Mars habitable:
heat up the planet 🔥, boost oxygen 🌿, create oceans 🌊, plant forests 🌳, and build cities 🏙️.
Compete against rival corporations to contribute the most and **win the race to terraform**! 🏆

> Play. Score. Compare. Conquer Mars. ❤️‍🔥

---

## Tech Stack

<p align="left">
  <a href="https://www.python.org/">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">
  </a>
  <a href="https://flask.palletsprojects.com/">
    <img alt="Flask" src="https://img.shields.io/badge/Flask-2.x-000000?logo=flask&logoColor=white">
  </a>
  <a href="https://jinja.palletsprojects.com/">
    <img alt="Jinja2" src="https://img.shields.io/badge/Jinja2-Templates-B41717?logo=jinja&logoColor=white">
  </a>
  <a href="https://gunicorn.org/">
    <img alt="Gunicorn" src="https://img.shields.io/badge/Gunicorn-20.x-499848?logo=gunicorn&logoColor=white">
  </a>
  <a href="https://www.postgresql.org/">
    <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-15-4169E1?logo=postgresql&logoColor=white">
  </a>
  <a href="https://www.psycopg.org/">
    <img alt="psycopg2" src="https://img.shields.io/badge/psycopg2-2.9-2F6792?logo=postgresql&logoColor=white">
  </a>
  <a href="https://www.docker.com/">
    <img alt="Docker" src="https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white">
  </a>
  <a href="https://developer.mozilla.org/docs/Web/HTML">
    <img alt="HTML5" src="https://img.shields.io/badge/HTML5-e34f26?logo=html5&logoColor=white">
  </a>
  <a href="https://developer.mozilla.org/docs/Web/CSS">
    <img alt="CSS3" src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white">
  </a>
  <a href="https://developer.mozilla.org/docs/Web/JavaScript">
    <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?logo=javascript&logoColor=000">
  </a>
  <a href="https://pypi.org/project/bcrypt/">
    <img alt="bcrypt" src="https://img.shields.io/badge/bcrypt-4.x-33858D?logo=lock&logoColor=white">
  </a>
</p>

---

## How to Setup (Dockerized)

### Prerequisites

- **Windows/macOS:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker & Docker Compose)
- **Linux:** [Docker Engine](https://docs.docker.com/engine/) and [Docker Compose](https://docs.docker.com/compose/)

### 1. Clone the repository

```bash
git clone git@github.com:Zsezsu/terraforming-mars.git
cd issue-tracker
```

### 2. Configure Environment Variables

- Copy the example environment file and edit as needed:

```bash
cp .env.example .env
```

Edit `.env` to set your database credentials (defaults are provided):

```
FLASK_ENV=development
SECRET_KEY=dev-secret-change-me
DATABASE_URL=postgresql://tmars:tmars@db:5432/tmars
PORT=5000
```

> The Docker Compose setup will automatically use these variables for all services.




### 3. Start All Services (Database, Server, Client)

```bash
docker compose up --build
```

This will start:

App: http://localhost:5000


---


## Contribution - GIT Guidelines

### Commits

**Commit frequently.**
Don't worry about whether your change will go into the final branch version or not, you can manipulate commits with
several git rebase methods (such as squash). The important thing here is to commit very often.

Commit message examples:

`Add login system`

`Fix input bug`

`Update tiles`

### Branching

Don't commit directly to the development branch. Create **[ feature | enhancement | fix ]** branches to record your
changes.

Name the branches as the following:

`git branch <github-username>_<branch-type>_<branch-name>`

### Rebase

Do the following when rebasing a branch to the development.

1. On **development** branch `git pull`
2. On **custom branch**
    - `git pull`
    - `git rebase -i development`
3. Finish rebase by resolving merge conflicts if necessary.
    1. After resolving conflicts, `git rebase --continue`
4. Check if the application works as it should
5. Complete rebase by `git push -f`

## SQL Guidelines

### SQL Format Example

```sql
SELECT 
    <column_name_1>,
    <column_name_2>,
    <column_name_3>,
    CASE
        WHEN <statement>
            THEN <column_name>
        WHEN <another_statement>
            THEN <value>
    END
        AS <name>
FROM
    <table_name>
 WHERE
    <where_clause_1>,
    <where_clause_2>,
    <where_clause_3>,
 GROUP BY
    <group_by_statement>
```
