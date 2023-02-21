from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys
import json
import webbrowser
import colorama
from pypresence.presence import Presence

hostName = "localhost"
serverPort = 8080
now = time.time()

if __name__ == "__main__":
    input(colorama.Fore.RED + 'IMPORTANT!\nCreate an app on Discord: https://discord.com/developers/applications\nIn "Rich presence" and then in "Art assets", upload 2 files named "big" and "small" for the big and small image\nIn "General informations", the "name" is the name of your Rich Presence, and copy the "APPLICATION ID".\n\nPress Enter to continue' + colorama.Fore.WHITE)

    configFile = open('config.json', 'r', encoding='utf-8')
    config = json.load(configFile)
    configFile.close()

    class Server(BaseHTTPRequestHandler):
        def do_GET(self):
            configFile = open('config.json', 'r', encoding='utf-8')
            config = json.load(configFile)
            configFile.close()

            show1 = ''
            show2 = ''

            if config['start'] == True: show1 = 'checked'
            else: show2 = 'checked'

            btn1_text = ''
            btn1_url = ''
            btn2_text = ''
            btn2_url = ''
            if len(config.get('buttons', [])) >= 1:
                button1 = config['buttons'][0]
                btn1_text = button1['label'] if 'label' in button1 else ''
                btn1_url = button1['url'] if 'url' in button1 else ''
            if len(config.get('buttons', [])) == 2:
                button2 = config['buttons'][1]
                btn2_text = button2['label'] if 'label' in button2 else ''
                btn2_url = button2['url'] if 'url' in button2 else ''

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes('<!DOCTYPE html><html><head><meta charset="utf-8"><title>Configure Discord RPC online</title><link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet"><link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous"><style>', "utf-8"))
            self.wfile.write(bytes('html,body {min-height: 100%; }body, div, form, input, select, textarea, p {padding: 0; margin: 0; outline: none; font-family: Roboto, Arial, sans-serif; font-size: 14px; color: #666; line-height: 22px; }h1 {position: absolute; margin: 0; font-size: 36px; color: #fff; z-index: 2; }.testbox { display: flex; justify-content: center; align-items: center; height: inherit; padding: 20px; }form { width: 100%; padding: 20px; border-radius: 6px; background: #fff; box-shadow: 0 0 20px 0 #333; }.banner { position: relative; height: 210px; display: flex; justify-content: center; align-items: center; text-align: center; }.banner::after { content: ""; background-color: rgba(0, 0, 0, 0.4); position: absolute; width: 100%; height: 100%; }input, textarea, select { margin-bottom: 10px; border: 1px solid #ccc; border-radius: 3px; }input { width: calc(100% - 10px); padding: 5px; }select { width: 100%; padding: 7px 0; background: transparent; }textarea { width: calc(100% - 12px); padding: 5px; }.item:hover p, .item:hover i, .question:hover p, .question label:hover, input:hover::placeholder { color: #333; }.item input:hover, .item select:hover, .item textarea:hover { border: 1px solid transparent; box-shadow: 0 0 6px 0 #333; color: #333; }.item { position: relative; margin: 10px 0; }input[type=radio], input.other { display: none; }label.radio { position: relative; display: inline-block; margin: 5px 20px 10px 0; cursor: pointer; }.question span { margin-left: 30px; }label.radio:before { content: ""; position: absolute; top: 2px; left: 0; width: 15px; height: 15px; border-radius: 50%; border: 2px solid #ccc; }#radio_5:checked~input.other { display: block; }input[type=radio]:checked+label.radio:before { border: 2px solid #444; background: #444; }label.radio:after { content: ""; position: absolute; top: 7px; left: 5px; width: 7px; height: 4px; border: 3px solid #fff; border-top: none; border-right: none; transform: rotate(-45deg); opacity: 0; }input[type=radio]:checked+label:after { opacity: 1; }.btn-block { margin-top: 10px; text-align: center; }button { width: 150px; padding: 10px; border: none; border-radius: 5px; background: #444; font-size: 16px; color: #fff; cursor: pointer; } button:hover { background: #666; }@media (min-width: 568px) { .name-item, .city-item { display: flex; flex-wrap: wrap; justify-content: space-between; } .name-item input, .city-item input { width: calc(50% - 20px); } .city-item select { width: calc(50% - 8px); } }', "utf-8"))
            self.wfile.write(bytes('</style></head><body><div class="testbox"><form onsubmit="event.preventDefault(); event.stopPropagation(); save()"><div class="banner"><h1>Configure your Discord</h1><h1 style="padding-top: 70px;">RPC online!</h1></div>', "utf-8"))
            self.wfile.write(bytes('<div class="item"><p>First line</p><input type="text" placeholder="The first line of the RPC" maxlength="128" value="%s" id="details" /></div>' % config['details'], "utf-8"))
            self.wfile.write(bytes('<div class="item"><p>Second line</p><input type="text" placeholder="The second line of the RPC" maxlength="128" value="%s" id="state" /></div>' % config['state'], "utf-8"))
            self.wfile.write(bytes('<div class="item"><p>Text on the big image</p><input type="text" maxlength="128" value="%s" id="large_text" /></div>' % config['large_text'], "utf-8"))
            self.wfile.write(bytes('<div class="item"><p>Text on the small image</p><input type="text" maxlength="128" value="%s" id="small_text" /></div>' % config['small_text'], "utf-8"))
            self.wfile.write(bytes('<div class="question"><p>Show time elapsed</p><div class="question-answer"><div><input type="radio" value="none" id="start_yes" name="starttime" %s/><label for="start_yes" class="radio"><span>Yes</span></label></div><div><input type="radio" value="none" id="start_no" name="starttime" %s/><label for="start_no" class="radio"><span>No</span></label></div></div></div>' % (show1, show2), "utf-8"))
            self.wfile.write(bytes('<div class="item"><p>Button 1</p><div class="name-item"><input type="text" id="button1-label" placeholder="Button text" maxlength="32" value="%s" /><input type="text" id="button1-url" placeholder="Button URL" value="%s" /></div></div>' % (btn1_text, btn1_url), "utf-8"))
            self.wfile.write(bytes('<div class="item"><p>Button 2</p><div class="name-item"><input type="text" id="button2-label" placeholder="Button text" maxlength="32" value="%s" /><input type="text" id="button2-url" placeholder="Button URL" value="%s" /></div></div>' % (btn2_text, btn2_url), "utf-8"))
            self.wfile.write(bytes('<div class="btn-block"> <button onclick="event.preventDefault(); event.stopPropagation(); save()">Save</button> </div></form></div><script>async function save() { let button1 = { label: document.getElementById("button1-label").value, url: document.getElementById("button1-url").value };  if (!button1.label || !button1.url) return alert("RPC needs at least one button!"); let button2 = { label: document.getElementById("button2-label").value, url: document.getElementById("button2-url").value }; let buttons = []; if (button1.label && button1.url) buttons.push(button1); if (button2.label && button2.url) buttons.push(button2); let json = {details: document.getElementById("details").value, state: document.getElementById("state").value, large_text: document.getElementById("large_text").value, small_text: document.getElementById("small_text").value, start: document.getElementById("start_yes").checked, buttons: buttons, }; let res = await fetch("/", { method: "POST", body: JSON.stringify(json), headers: { "Content-Type": "application/json" } }); if (res.status == 200) alert("RPC saved!"); if (res.status != 200) { let error = await res.text(); alert(`An error occured: \n${error}`) }}</script></body></html>', "utf-8"))
        
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()
            json_data = json.loads(post_data)
            print(json_data['start'])

            print('Saved new data, updating RPC in a few seconds...')
            save(json_data)

            self.send_response(200)
            self.end_headers()


    print('Config file parsed, checking fields...')
    if config['app_id'] == 'undefined':
        AppIdToReset = False
    else:
        AppIdToReset = input('Tap "Enter" to launch or type something to change the App ID: ')

    if AppIdToReset:
        config['app_id'] = 'undefined'

    try:
        Presence(config['app_id']).connect()
    except:
        inputAppID = input('App id not found in config, please paste it here: ')
        try:
            Presence(inputAppID).connect()
            config['app_id'] = inputAppID

            fp = open('config.json', 'w', encoding='utf-8')
            json.dump(config, fp)
            fp.close()
        except:
            sys.exit('[Stopping] Invalid app id')

    RPC = Presence(config['app_id'])
    RPC.connect()

    def save(newconfig, save=True):
        if save:
            newconfig['app_id'] = config['app_id']
            fp = open('config.json', 'w', encoding='utf-8')
            json.dump(newconfig, fp)
            fp.close()

        time.sleep(2)

        starttime = None
        if newconfig['start'] == True:
            starttime = now

        buttons = []
        if len(newconfig.get('buttons', [])) >= 1:
            button1 = newconfig['buttons'][0]
            label1 = button1['label'] if 'label' in button1 else None
            url1 = button1['url'] if 'url' in button1 else None
            if label1 and url1:
                buttons.append({ "label": label1, "url": url1 })
        if len(newconfig.get('buttons', [])) == 2:
            button2 = newconfig['buttons'][1]
            label2 = button2['label'] if 'label' in button2 else None
            url2 = button2['url'] if 'url' in button2 else None
            if label2 and url2:
                buttons.append({ "label": label2, "url": url2 })


        details = newconfig.get('details', None) 
        if details == '': details = None

        state = newconfig.get('state', None) 
        if state == '': state = None

        large_text = newconfig.get('large_text', None) 
        if large_text == '': large_text = None

        small_text = newconfig.get('small_text', None) 
        if small_text == '': small_text = None

        RPC.update(
            details=details, # Max: 128
            state=state, # Max: 128
            large_image='big',
            large_text=large_text, # Max: 128
            small_image='small',
            small_text=small_text, # Max: 128
            buttons=buttons,
            start=starttime
        )

        print('Rich Presence updated!')
        
    save(config, False)


    webServer = HTTPServer((hostName, serverPort), Server)
    print("\nOpen the Web configuration here: http://%s:%s" % (hostName, serverPort))
    print('============= LOGS =============')
    webbrowser.open("http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('\n')
    print('================================')
    print("\nRPC closed, goodbye!")
