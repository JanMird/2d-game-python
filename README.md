# project

INTRODUCTION
------------

This is a simple example of a 2d game. You are playing as a green tank, white tanks - enemies. Main task - stay alive as long as you can.

Movement:
        To move left press the left arrow key, right - the right arrow key, down - the down arrow key, up - the up arrow key. To shoot press SPACE key.
        
Main manu:
        There are two buttons : start and exit. If a person clicks start button game starts, exit button - exit app.
        
Game:
        Players main task - to live as much as he/she can. Blue square is an destoyable wall, red one is undestroyable. White block is an enemy tank. By shooting and hitting enemies, player makes damage to enemy tanks, by decreasing enemy health. Every 15 seconds new enemies and walls are generated. There are health state of hero and alive time on the tom of the screen.
 
REQUIREMENTS
------------

**This bot requires the following modules:**

python3 (https://www.python.org/downloads/)

pygame (https://www.pygame.org/news)

time (https://docs.python.org/3/library/time.html)

random (https://docs.python.org/3/library/random.html)

RECOMMENDED MODULES
-------------------
 
None
 
INSTALLATION
-------------
 
Enter a directory in wich to download the game (`cd ./mydir`), install as you would normally install git (`sudo apt-get update && install git`), python3 (`sudo apt-get update && install python3`), clone the github repository (`git clone https://github.com/JanMird/project.git`). Enter project directory (`cd project`). If there nothing appeared but README.me, try to switch your branch to dev (`git checkout dev`). Then install requirements (`pip install -r requirements.txt`).
 
 **'you are in desired directory'**
   
     sudo apt-get install git
   
     sudo apt-get install python3
   
     git clone https://github.com/JanMird/project.git
     
     cd project
     
     pip install -r requirements.txt
   
     >git checkout dev (optional)
 
LAUNCH
------
 
 Enter directory with README. Now you are ready to launch game. Use following command : `python3 main.py`
 
 **'you are in the same directory as README.md'**
   
     python3 main.py
 
TROUBLESHOOTING
---------------
 
 If you cloned repository, but script doesnt work:
 
 	- please, check, if there any grammar mistakes or misses in copypaste
 	
 	-try to update python3 using following code:
 	
 	    sudo apt-get update && install python3
 
FAQ
---

    Q: I killed every enemy tanks, but nothing happening. Does that mean that i won?
    
    A: No, it doesent. This game has increasing difficulty level. Every 15 seconds more enemy tanks will be generated.
    
PATTERNS
--------
 **CREATIONAL PATTERNS**
 
 Factory Method
          В библиотеке pygame есть очень удобный класс Sprite. В нём реализованы многие методы, которых почти достаточно для каждого объекта игры. И писать реализацию для каждого класса было бы иррационально.
 
 **STRUCTURAL PATTERNS**
 
 Bridge
         На каждом тике игры требуется обнавлять состояния объектов. Куда удобнее реализовывать обновление параметров, которые имеются у разных классов, в одном цикле. Например метод update класса sprite библиотеки pygame.
 
 **BEHAVIORAL PATTERNS**
 
 Observer
         Есть класс bullet. Для остальных объектов очень важно, где находится объект данного класса каждый тик, а каждый тик он меняет своё местоположение. Так что отлично подойдёт класс observer для прохода по всем спрайтам, кроме пули, и сообщения её нового состояния. Аналогично для сталкивания танков.


