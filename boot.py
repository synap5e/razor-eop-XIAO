import usb_hid

devices = [
    usb_hid.Device.MOUSE,
    usb_hid.Device.MOUSE,
    usb_hid.Device.MOUSE,
]
usb_hid.enable(devices)
