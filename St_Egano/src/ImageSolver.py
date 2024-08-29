from PIL import Image
def ReadMessageFromImage(pathToImage: str) -> str: 
    im = Image.open(pathToImage).convert("RGB")
    #print(im.mode);
    sizeX = im.width;
    sizeY = im.height;
    message = "";
    x = 0;
    y = 0;
    # Die relativen Koordinaten, die vom aktuellen Pixel zum nächsten führen
    diffX = 0;
    diffY = 0;
    # Initielle Pixel Werte werden aus den Koordinaten  0,0 gelesen
    (r,g,b) = im.getpixel((0,0));
    # Hier wird der erste "Schritt" mit dem Weg zum nächsten Buchstaben initialisiert
    diffX = g;
    diffY = b;
    message += chr(r);      
    #print(str(g % sizeX),str( b % sizeY))       
    # Abbruchbedingung: Falls die neuen relative Koordianten 0 0 sein sollten terminiert der Algorithmus
    while(diffX != 0 and diffY !=0):
        # Die neuen Koordianten für die nächste Iteration berechnen:
        # Überprüfung ob die relative Koordianten außerhalb des Bildes gehen
        if (x + (diffX % sizeX ) > sizeX):
            ## Falls ja, dann setze die x-Koordinate auf den Rest von dem was übrig bleibt, wenn man gegen den Rand läuft
            x = x + (diffX % sizeX ) - sizeX;
        else: 
            # Sonst erhöhe die neue x-Koordinate auf
            x += (diffX % sizeX);
        if (y + (diffY % sizeY ) > sizeY):
            y = y + (diffY % sizeY ) - sizeY;        
        else: 
            y += (diffY % sizeY);
        # Final out of bounds check, falls x = sizeX ist und somit an den Anfang gesetzt werden muss
        if x == sizeX:
            x = 0;
        # Final out of bounds check, falls y = sizeY ist und somit an den Anfang gesetzt werden muss
        if y == sizeY:
            y = 0;
            
        (r,g,b) = im.getpixel((x,y));
        diffX = g;
        diffY = b;
        message += chr(r);
        # print(x, y);
        #print(chr(r));      
    print(message); 
    return message;
