from machine import Pin, SPI
import json
import network, time
import urequests
from epd5in83 import EPD_5in83 # from the demo files at XXX

# Config

SSID = "CHANGE: WIFI NAME (SSID)"
PASSWORD = "CHANGE: WIFI PASSWORD(SSID)"
URL = "CHANGE: URL TO FIND YOUR output.bin FILE" # Github repo to create the output.bin file - https://github.com/karanmhatre1/bvg-weather-e-paper-display
REFRESH_INTERVAL = 120 # How often do you want the e-paper display to refresh

# end Config

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Initialize the library
epd = EPD_5in83()

# Connect to the wifi
def connect_wifi():
  	if not wlan.active():
        wlan.active(True)
        
    if not wlan.isconnected():
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            print('Waiting for connection...')
            time.sleep(1)

    print("WiFi connected")

# Fetch the output.bin file
def fetch_bin():
  resp = urequests.get(URL)
  print("fetching image...")
  with open("output.bin", "wb") as f:
      f.write(resp.content)
  resp.close()
  print("output.bin downloaded")

# Refresh the display
def display_refresh():
    connect_wifi()
    fetch_bin()    
    epd.init()
    
    # You can choose to disconnect the wifi in between refreshes to improve battery life. I've noticed issues with the pico failing to reconnect so I've commented the 2 lines below 

	# wlan.disconnect() 
	# wlan.active(False)
    
    with open("output.bin", "rb") as f:
        buf = bytearray(f.read())
    
    epd.display(buf)
    epd.sleep()

while True:
    display_refresh() # Call display_refresh
    time.sleep(REFRESH_INTERVAL) # sleep from the duration of REFRESH INTERVAL
