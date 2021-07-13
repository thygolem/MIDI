import usb.util
import usb.core

dev = usb.core.find(idVendor=0x0944, idProduct=0x0115)
ep=dev[0].interfaces()[0].endpoints()[0]
i=dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)

dev.set_configuration()
eaddr=ep.bEndpointAddress

r=dev.read(eaddr,299264) 
# Para saber qué valor tiene tu controlador, sube el valor exageradamente y ejecuta el programa 

print(len(r))