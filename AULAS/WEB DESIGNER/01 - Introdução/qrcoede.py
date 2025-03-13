import qrcode

chave_pix = "lademirvales@hotmail.com"

payload = f"00020126330014BR.GOV.BCB.PIX0117{chave_pix}5204000053039865802BR5920Lademir Vales6009Sao Paulo62070503***6304"

qr = qrcode.make(payload)

qr_code_path = "C:/Users/caiqu/Desktop/qrcode_pix.png"
qr.save(qr_code_path)

qr_code_path