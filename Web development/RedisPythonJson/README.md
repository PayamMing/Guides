# What is this:
Vi vet att vi har en redis server och vi ska läsa variabler från databasen. Låt oss säga att det finns en Hash i Redis. Vi använder Redis Desktop Manager och vi skriver data där istället för enkelhetens skull. Googla och ladda ner Redis Desktop Manager.

# Steg 1: Starta Redis (Linux)
Testat på Ubuntu
`redis-server`
Om redis vägrar starta ska du döda den. Det kan man göra via Task Manager eller enligt följande: 
`sudo /etc/init.d/redis-server stop`
Att döda processen med Task Manager är att föredra

# Steg 2: Starta Flask
För att köra `.py` coden skall du först installera Flask och Redis för Python enligt nedan:

```
sudo apt install python-pip
pip install redis
pip install Flask
```
Om du startar Redis med RDM så har du möjlighet att välja address. annars kör vi med 127.0.0.1 port 6379.

Flask vanligt vist kör med 127.0.0.0 port 5000 men det kan man ändra på.

# Glöm ej:
I koden ändra bara på app.route områdena och låt resten stå kvar.
