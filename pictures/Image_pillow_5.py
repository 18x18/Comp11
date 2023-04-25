import os,PIL
from PIL import Image, ImageFilter
from time import sleep

#im = Image.open('city.jpg')
#im.save('pngs/cities.png')
##i.save('700/{}_700{}'.format(fn, fext))



def image_editor():
#How would you select the pictures? And how would you edit it.
#For now there are 2 option: Amongus and city.
    shade = 'shade'

#user input and pictures
#Could do automatic check of .jpg files.
#They did it in the video, I'm not going to do that lol

    pics = []

    for f in os.listdir('.'):
        if f.endswith('.jpg'):
            i = Image.open(f)
            fn, fext = os.path.splitext(f)
            pics.append(fn)
            

    pic = input(pics 

).lower()
    
#Checks if user input = valid
    if pic not in pics:
        print('No spaces or other strange characters, now pick one of the available options.')
        sleep(1)
        image_editor()

#Magic
    im = Image.open(pic + '.jpg')
    im.show()
    
#Now we got to make it so that one can edit the picture chosen.
#I have an idea using ifs and elifs

#just some comfirmation 
    choice = 0
    while choice != 2:
        choice = input('''Is this the image you want to use? (y) (n)
''').lower()
        sleep(1)
        if choice == 'y': 
            print('ok')
            choice = 2
            sleep(1)
        elif choice == 'n':
            image_editor()
        else:
            print('What?')
            choice = 1
            sleep(1)

#Now for the idea
    while True:
        save = 0
        print(f"How would you like to edit {pic}?")
        sleep(1)
        decide = str(input("""
        1. Rotate
        2. Size
        3. Blur
        4. Shade (black and white)

        (q) to quit
Decide by typing in the number (1) (2) etc...
"""))

#Rotate option
        if decide == '1' or decide == 'one':
            imro = im
            while save == 0:
                print("How would you like to rotate it?")
                ro = input("""
                Pick a degree.
                For example 90 or 45.
""")
                if ro.isdecimal():
                    ro = int(ro)
                    imro = imro.rotate(ro)
                    imro.show()
                    print('Would you like to save this image?')
                    save = input('''(y) or (n)
''').lower()
#Escape the LOOP
                    if save == 'y' or save == 'yes':

                        imro.save(f'pngs/{pic}_rotate_{ro}.png')
                        sleep(1)
                        print('saved')
                        hmm = input("""(y) or (n) 
""").lower()
                    elif save == 'n' or save == 'no':
                        print('ok')
                        save = 'no'
                        sleep(1)
                        print('Would you still like to edit this pic? (replace old pic)')
                        hmm = input("""(y) or (n) 
""").lower()
                    else:
                        print("You don't want to save? Whatever man.")
#Continue? Continue? Continue?
                    if hmm == 'y' or hmm == 'yes':
                        im = imro
                        pic = pic + '_rotate_' + str(ro)
                        continue
                    
                    elif hmm == 'n' or hmm == 'no':
                        print('ok')
                        continue

                    else:
                        print("Don't want to edit this pic? Whatever")
                        continue
                else:
                    print("That is not an integer.")
                    continue

#Resize option
        if decide == '2' or decide == 'two':
            imsize = im
            while save == 0:
                print('How many pixels would you like your image to have?')
                print('''
                For reference: There are hundreds of pixels in pictures. 
                300 x 300 = three hundred by three hundred pixels
''')
                sleep(1)
                si1 = input('Enter the first dimension (x): ')
                si2 = input('Enter the second dimension (y): ')
                if si1.isdecimal() and si2.isdecimal():
                    si1 = int(si1)
                    si2 = int(si2)
                    si = (si1, si2)
#I have been using .thubnail() What the heck 
#WAIT WHAT????????????????? I dont get it. I'll have to watch the video again '-'
                    imsize = imsize.resize([si1,si2],PIL.Image.ANTIALIAS)
                    imsize.show()
                    print('Would you like to save this image?')
                    save = input('''(y) or (n)
''').lower()
#Escape the LOOP

#I HAVE NO IDEA HOW TO FUNCTION THIS :(
                    if save == 'y' or save == 'yes':

                        imsize.save(f'pngs/{pic}_size_{si1},{si2}.png')
                        sleep(1)
                        print('saved')
                        print("would you like to keep editing this pic?")
                        hmm = input("""(y) or (n) 
""").lower()
                        
                    elif save == 'n' or save == 'no':
                        print('ok')
                        save = 'no'
                        sleep(1)
                        print('Would you still like to edit this pic? (replace old pic)')
                        hmm = input("""(y) or (n) 
""").lower()
                    else:
                        print("You don't want to save? Whatever man.")
                        sleep(1)
                        print("Well do you want to keep editing this image?")
                        hmm = input("""(y) or (n) 
""").lower()
#Continue? Continue? Continue?
                    if hmm == 'y' or hmm == 'yes':
                        im = imsize
                        pic = pic + '_size_' + str(si1, si2)
                        continue
                    
                    elif hmm == 'n' or hmm == 'no':
                        print('ok')
                        continue

                    else:
                        print("Don't want to edit this pic? Whatever")
                        continue
                else:
                    print("That is not an integer.")
                    continue


#Blur Option
        if decide == '3' or decide == 'three':
            imblur = im
            while save == 0:
                print("How much blur would you like to add?")
                sleep(1)
                print("15 is already a lot.")
                blur = input("Amount of blur: ")
                if blur.isdecimal():
                    blur = int(blur)
                    imblur = imblur.filter(ImageFilter.GaussianBlur(blur))
                    imblur.show()
                    print("would you like to save this image?")
                    save = input('''(y) or (n)
''').lower()
#Escape the LOOP

#I HAVE NO IDEA HOW TO FUNCTION THIS :(
                    if save == 'y' or save == 'yes':

                        imblur.save(f'pngs/{pic}_blur_{blur}.png')
                        sleep(1)
                        print('saved')
                        print("would you like to keep editing this pic?")
                        hmm = input("""(y) or (n) 
""").lower()
                        

                    elif save == 'n' or save == 'no':
                        print('ok')
                        save = 'no'
                        sleep(1)
                        print('Would you still like to edit this pic? (replace old pic)')
                        hmm = input("""(y) or (n) 
""").lower()
                    else:
                        print("You don't want to save? Whatever man.")
                        sleep(1)
                        print("Well do you want to keep editing this image?")
                        hmm = input("""(y) or (n) 
""").lower()
#Continue? Continue? Continue?
                    if hmm == 'y' or hmm == 'yes':
                        im = imblur
                        pic = pic + '_blur_' + str(blur)
                        continue
                    
                    elif hmm == 'n' or hmm == 'no':
                        print('ok')
                        continue

                    else:
                        print("Don't want to edit this pic? Whatever")
                        continue
                else:
                    print("That is not an integer.")
                    continue


#shade option
        if decide == '4' or decide == 'four':
            imsh = im
            while save == 0:
                print("Would you like the picture black and white?")
                sh = input('(y) or (n) ').lower()
                if sh == 'y' or sh == 'yes':
                    imsh = imsh.convert('L')
                    imsh.show()
                    print("would you like to save this image?")
                    save = input('''(y) or (n)
''').lower()
#Escape the LOOP

#I HAVE NO IDEA HOW TO FUNCTION THIS :(
                    if save == 'y' or save == 'yes':

                        imsh.save(f'pngs/{pic}_{shade}.png')
                        sleep(1)
                        print('saved')
                        print("would you like to continue editing this pic?")
                        hmm = input("""(y) or (n) 
""").lower()

                    elif save == 'n' or save == 'no':
                        print('ok')
                        save = 'no'
                        sleep(1)
                        print('Would you still like to edit this pic? (replace old pic)')
                        hmm = input("""(y) or (n) 
""").lower()
                    else:
                        print("You don't want to save? Whatever man.")
                        sleep(1)
                        print("Well do you want to keep editing this image?")
                        hmm = input("""(y) or (n) 
""").lower()
                        
                    #Continue? Continue? Continue?
                    if hmm == 'y' or hmm == 'yes':
                        im = imsh
                        pic = pic + '_' + shade 
                        continue
                    
                    elif hmm == 'n' or hmm == 'no':
                        print('ok')
                        continue

                    else:
                        print("Don't want to edit this pic? Whatever")
                        continue

                elif sh == 'n' or sh == 'no':
                    print('Oh, ah, ok.')
                    sleep(1)
                    continue
                else:
                    print("What?")
                    sleep(1)
                    continue

#quit opTion
        elif decide == 'q' or decide == 'quit':
            print("do you want to quit?")
            choose = input('(y) or (n)').lower()
            if choose == 'y' or choose == 'yes':
                print('ok, bye!')
                quit()
            if choose == 'n' or choose =='no':
                print('ok')
                continue
        
#Just some stuff
        else:
            continue

image_editor()


















# I dont really get it...
def save(imsh, shade, amount1, amount2, ): # an attempy to automate

    print("would you like to save this image?")
    save = input('''(y) or (n)
    ''').lower()
    #Escape the LOOP

    #I HAVE NO IDEA HOW TO FUNCTION THIS :(
    if save == 'y' or save == 'yes':
    #FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER
    #FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER
    #FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER FOLDER
        imsh.save(f'{pic}_{shade}_{amount1}{amount2}.png')
        sleep(1)
        print('saved')
        print("would you like to continue editing this pic?")
        hmm = input("""(y) or (n) 
        """).lower()

    elif save == 'n' or save == 'no':
        print('ok')
        save = 'no'
        sleep(1)
        print('Would you still like to edit this pic? (replace old pic)')
        hmm = input("""(y) or (n) 
    """).lower()
    else:
        print("You don't want to save? Whatever man.")
        sleep(1)
        print("Well do you want to keep editing this image?")
        hmm = input("""(y) or (n) 
    """).lower()
        
    #Continue? Continue? Continue?
    if hmm == 'y' or hmm == 'yes':
        im = imsh
        pic = pic + '_' + shade + '_' + amount1 + amount2 + '_'
        return pic, im, save
    
    elif hmm == 'n' or hmm == 'no':
        print('ok')
        return save

    else:
        print("Don't want to edit this pic? Whatever")
        return save
        







































































































#
#pick a picture:
#
#'Amongus'
#'City'
#'Cat'
#'Dog'
#'Elephant'
#'Flower'
#'Funny'
#'Game'
#'Letters'
#'People'
#'Tree'























































































































































































































































































































































































































































































































































































































def test():
    im = Image.open('city.jpg')
    im.filter(ImageFilter.GaussianBlur(15)).save('city_mod3.jpg')
    im.convert(mode='L').save('city_mod2.jpg')
    im.rotate(90).save('city_mod.jpg')


    size_300 = (300, 300)
    size_700 = (700, 700)

    for f in os.listdir('.'):
        if f.endswith('.jpg'):
            i = Image.open(f)
            fn, fext = os.path.splitext(f)

            i.thumbnail(size_700)
            i.save('700/{}_700{}'.format(fn, fext))

            i.thumbnail(size_300)
            i.save('300/{}_300{}'.format(fn, fext))

    im = Image.open('city.jpg')
    im.show()
    im.save('city.png')

