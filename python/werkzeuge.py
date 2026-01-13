# Links als QR-Code generieren und als Bilddatei speichern

# Imports
import os
import qrcode

# Funktion
def generate_qr_code ( data = " >> ENTER_LINK_HERE << ", filename="qrcode.png" ):        # Zeile für Link und Dateiname anpassen ( .png am Ende nicht vergessen )


    # QR-Code-Objekt erstellen
    qr = qrcode.QRCode (
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Daten zum QR-Code hinzufügen
    qr.add_data ( data )
    qr.make ( fit=True )

    # Bild des QR-Codes generieren
    img = qr.make_image ( fill_color="black", back_color="white" )

    # Speichern der QR-Code-Bilddatei
    import os
    print ( "Speichere nach:", os.path.abspath ( filename ) )
    img.save ( filename )
    print ( f"QR code saved as { filename }" )
