import os
from subprocess import call
def upload(fileArgs):
    """
    --file="/tmp/test_video_file.flv"
                       --title="Summer vacation in California"
                       --description="Had fun surfing in Santa Cruz"
                       --keywords="surfing,Santa Cruz"
                       --category="22"
                       --privacyStatus="private"
    """

    os.system('python YouTubeAPI.py ' + '--file="' + fileArgs['fileName'] + \
              '" --title="' + fileArgs['title'] + \
              '" --description="' + fileArgs['description'] + '" --keywords="' + \
              fileArgs['keywords'] + '" --category="22" --privacyStatus="unlisted"')