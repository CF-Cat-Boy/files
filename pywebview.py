import webview

def thing():
    while True:
        if not wind in webview.windows:
            sponge.destroy()

wind = webview.create_window("","https://raw.githubusercontent.com/CF-Cat-Boy/images/main/helpful-image.png",width=20,height=255)
wind.frameless = True
wind.transparent = True
wind.on_top = True
wind.focus = False
wind.draggable = False
wind.text_select = False
wind.min_size = (0,0)
#wind.confirm_close = True

sponge = webview.create_window("","http://localhost:8888")
sponge.zoomable = True
sponge.on_top = True
sponge.frameless = True

webview.start(func=thing)