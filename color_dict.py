

def colors():
    color={
    'blue':(255,0,0),
    'green':(0,255,0),
    'red':(0,0,255),
    'yellow':(0,255,255),
    'magenta':(255,0,255),
        'cyan':(255,255,0),
        'white':(255,255,255),
        'black':(0,0,0),
        'gray':(125,125,125),
        'dark_gray':(50,50,50),
        'ligth_gray':(220,220,200)
    }
    return color

if __name__ == '__main__':
   color= colors()
   print(color.get('green'))
   print(color['cyan'])
