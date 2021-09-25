# Book Search 


#### The aim of the project is to create an open-source platform
#### that allows you to easily search for books, compare prices between bookstores and write reviews

## Installation 

### With Docker and Docker-Compose
1. Install Docker and Docker-Compose on your system:
Docker https://docs.docker.com/get-docker/
<br><br>Docker-Compose
https://docs.docker.com/compose/install/
<br>
<br>

2. Create .env file inside MainApp folder
   the context of this file should look like this:
      \
      <code>
      POSTGRES_PASSWORD="db_password"\
      POSTGRES_USER="db_user"\
      POSTGRES_DB="db_name"
   </code>
2. Use your terminal to start Docker <code>docker-compose up -d  </code>

3. Open your browser on https://127.0.0.1:8000

## Contribution

Repository is 

Feel free to fork repository, if you want to add new functionality open a new issue
with tag <code>enhancement</code>

### License
Book Search is free and open-source software licensed under the GNU 3.0 License.


