import Ta5k

myshelf = Ta5k.Ta5k()

myshelf.connectTelnet('bbdlc_cot','10.13.138.101','ADMIN','PASSWORD')
myshelf.connectTelnet(bbdlc_cot, 10.13.138.101, ADMIN, PASSWORD)
auto = myshelf.command("show auto shelf")

print auto
