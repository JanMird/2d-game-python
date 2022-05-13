# general

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# game parameters

WIDTH = 800
HEIGHT = 650
FPS = 30

SMALLTEXTSIZE = 34
BIGTEXTSIZE = 68
DEFAULINTERX = 350
DEFAULINTERY = 30
DEFAULINTERCOL = RED
INTERSPACE = 30

STARTBLOCKEM = 200
BLOCKGENCOOLDOWN = FPS * 15
BLOCKGENINCR = 1
STARTENEMYEM = 3
ENEMYGENCOOLDOWN = FPS * 15

#endscreen

ENDSCREENSCX = WIDTH // 2
ENDSCREENSCY = HEIGHT // 2
PRESSANYBUTX = WIDTH // 2
PRESSANYBUTY = HEIGHT // 2 + BIGTEXTSIZE * 2

# block parameters

BLWIDTH = 30
BLOCKCOL = BLUE
BLDEFAULTRECTX = 0
BLDEFAULTRECTY = 0
BLDEFAULTHEALTH = 1

BORDERWIDTH = 10
BORDERHEIGHT = HEIGHT - BLWIDTH
BORDCOL=RED

# bullet parameters

BUWIDTH = 5
BULCOL = RED
BULDEFAULTRECTX = 0
BULDEFAULTRECTY = 0
BULDEFAULTSPEED = 9
BULDEFAULTDAMAGE = 1
BULDEFAULTDIR = 'right'

# button parameters

BUTTON_WIDTH = 350
BUTTON_HEIGHT = 65
TSIZE = 50
BACKGCOL = GREEN
BUTTCOL = BLUE
UPDBUTTCOL = GREEN
UPDBUTBGCOL = BLUE

# enemy parameters

ENTWIDTH = 30
ENDEFAULTSPEED = 5
ENDEFAULTRECTX = 100
ENDEFAULTRECTY = 100
ENDEFAULTHEALTH = 3
ENDEFAULTDIR = 'right'
ENBULGEN = 5
ENEMYCOL = WHITE
TURNFREQ = FPS
SHOOTFREQ = 15

# tank parameters

HTANKWIDTH = 30
HTANKCOL = GREEN
HTANKSPEED = 5
HTANKDX = 100
HTANKDY = 100
HTANKDHEALTH = 3
HTANKDDIR = 'right'
HEROX = 100
HEROY = 200
TBULGEN = 5
