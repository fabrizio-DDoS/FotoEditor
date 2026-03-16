from PIL import Image, ImageFilter
Xasa = 1
img = Image.open('tralalero.jpeg')
while (Xasa < 100):
    peb = input('Quer a foto em prero e branco? Y ou N  ')

    tamanho  = int(input('Que a foto de que tamanho?'))

    resized_img = img.resize((tamanho, tamanho))
    if peb == 'Y':
        filtered_img = resized_img.convert("L")
        filtered_img.show(filtered_img)
    else:
        resized_img.show(resized_img)

    print('Imagem Pronta!') 
    Xasa += 1