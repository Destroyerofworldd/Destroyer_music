from FADEDMUSIC.core.bot import PURVI
from FADEDMUSIC.core.dir import dirr
from FADEDMUSIC.core.git import git
from FADEDMUSIC.core.userbot import Userbot
from FADEDMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PURVI()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
