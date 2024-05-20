import qrcode
img = qrcode.make("https://portal.int.mynavi.jp/cgi-bin/login.cgi?reload=1")
img.save("qrcode-test.png")
