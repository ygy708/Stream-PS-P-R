# -*- coding: utf-8 -*-
import xbmcgui
import xbmcplugin
import xbmc

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

def play_stream(channel_url, channel_name):
    xbmcgui.Dialog().notification('Stream Poslanecké sněmovny ČR', f'Spouštím stream: {channel_name}')
    xbmc.Player().play(channel_url)

def show_menu():
    dialog = xbmcgui.Dialog()
    choice = dialog.select('Vyberte stream:', ['Schůze Poslanecké sněmovny', 'Tiskové konference', 'Výbory a semináře 1', 'Výbory a semináře 2', 'Výbory a semináře 3'])
    
    if choice == 0:
        play_stream('https://pspcr-ott-live.ssl.cdn.cra.cz/channels/ps-stream1/playlist/cze.m3u8', 'Schůze Poslanecké sněmovny')
    elif choice == 1:
        play_stream('https://pspcr-ott-live.ssl.cdn.cra.cz/channels/ps-stream2/playlist/cze.m3u8', 'Tiskové konference')
    elif choice == 2:
        play_stream('https://pspcr-ott-live.ssl.cdn.cra.cz/channels/ps-stream3/playlist/cze.m3u8', 'Výbory a semináře 1')
    elif choice == 3:
        play_stream('https://pspcr-ott-live.ssl.cdn.cra.cz/channels/ps-stream4/playlist/cze.m3u8', 'Výbory a semináře 2')
    elif choice == 4:
        play_stream('https://pspcr-ott-live.ssl.cdn.cra.cz/channels/ps-stream5/playlist/cze.m3u8', 'Výbory a semináře 3')

show_menu()
