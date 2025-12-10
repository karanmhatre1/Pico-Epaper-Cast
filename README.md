# Pico-Epaper-Cast
Cast remotely generated .bin images to a Waveshare E-Paper display using a Raspberry Pi Pico W / Pico 2 W.

## Installation
1. Flash MicroPython to your Pico W ([Instructions on the Raspberry Pi website](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html))
2. Copy these files to the Pico (Using [Thonny](https://thonny.org/))
3. Run the files on Pico (Using [Thonny](https://thonny.org/))

## Configuration
Edit the top of main.py:

```
SSID = "CHANGE: WIFI NAME (SSID)"
PASSWORD = "CHANGE: WIFI PASSWORD (SSID)"
URL = "CHANGE: URL TO FIND YOUR output.bin FILE"
REFRESH_INTERVAL = 120    # seconds
```

Your URL should point to a hosted output.bin. You can use the code here to generate the .bin file: [BVG/Weather E-paper display](https://github.com/karanmhatre1/bvg-weather-e-paper-display)

# How It Works
Every refresh cycle:
1. Connect to Wi-Fi
2. Download output.bin using urequests
3. Display the image on the epaper display
4. Sleep for the duration specified in the REFRESH_INTERVAL

# Battery Notes
E-paper only draws power during refresh. The Pico W uses most of the energy on Wi-Fi connection. 
To extend battery life:
- Increase REFRESH_INTERVAL
- Disconnect the Wi-Fi between refreshes
