#import os,sys
from tinytag import TinyTag

def buscatag(song):
    tag = TinyTag.get(song)
    print(tag)
    artista = tag.artist
    if artista is None:
        artista = "desconocido"
        print(artista)
    #print(tag.artist + "_" + tag.album)
    return;

song_path = "/home/mario/Music/_/previewbn.mp3"
a = buscatag(song_path)
#os.path.join(sys.argv[1]) # With sys.argv[1] the path to a mp3 file containing a picture
#import mutagen
#from mutagen.mp3 import MP3
#from mutagen.easyid3 import EasyID3
#from mutagen.id3 import ID3
#track = MP3(song_path, ID3=EasyID3)
#print(track)
#print(track.get('title')[0])
#print(track.get('album')[0])
#print(track.get('artist')[0])
#audio = ID3(song_path)
#print(audio)
#print ("Artist: %s" % audio['TPE1'].text[0])
#print ("Track: %s" % audio["TIT2"].text[0])
#print ("Album: %s" % audio["TALB"].text[0])
#print ("Release Year: %s" % audio["TDRC"].text[0])
#print('Artista:' % tag.artist)
#print('Album:  ' % tag.album)
#print(tag.artist)
#print(tag.album)
