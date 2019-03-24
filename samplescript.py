# just for testing
import os
import sys
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
from io import BytesIO

out = BytesIO()

gTTS(' '.join(sys.argv[1:]), lang='pl', slow=False).write_to_fp(out)
out.seek(0)
play(AudioSegment.from_file(out, format="mp3"))

