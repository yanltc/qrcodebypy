import qrcode

data = input("Entrez un texte ou un lien : ")
img = qrcode.make(data)
img.save("qrcode.png")
img.show()
print("QR code généré et enregistré sous le nom 'qrcode.png'.")
