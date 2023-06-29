# DiscordWebRPC
Manage an RPC on Discord on a website!

## How to run?
**YOU NEED TO HAVE PYTHON3 INSTALLED!**

> If you are on Mac or Linux, do like on Windows OR run the start.sh file by using the following:
```
bash start.sh
# Or
sh start.sh
```

> If you are on Windows, use the following:

Then install the dependencies:
```
pip3 install pypresence
```
and run the script:
```
python3 index.py
```

## Preparation
**Please read the red message before. You need to create an app on the Discord developper page:**
https://discord.com/developers/applications/
**And in Rich presence then in "Art assets" you need to upload 2 images. One called big and one small (minimum 512x512). (Just upload them one time, Discord don't refresh very quickly but its uploaded so you can run the script)**
**Then just go in "General Informations" and copy the APP ID and paste it in the code when it is asked**

### If you want to run directly without anything to type in the terminal (the App id must be saved in the config.json), use something like that :
```
python3 index.py --no-validation
```

## Screens
<div align="center">
<h4>Run the script and you will have an output like this:</h4>
<img src="/assets/console.png" width="80%">
<h4>It will then open your webbrowser on "localhost:8080"</h4>
<img src="/assets/web.png" width="80%">
<h4>And you can then fill some fields (only one button is required (at least))</h4>
<img src="/assets/web2.png" width="80%">
<h4>Click on save and wait a little bit (can take some time)</h4>
<img src="/assets/webcomplete.png" width="80%">
<h4>And on your Discord profile it will show :)</h4>
<img src="/assets/discordRPC.png" width="80%">
</div>
