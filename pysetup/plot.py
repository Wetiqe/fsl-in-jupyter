from matplotlib import pyplot as plt
from matplotlib.font_manager import FontManager
import subprocess

def check_fonts(order=2):
    """
    check the fonts that is avaliable in matplotlib
    args: 
        order: show what kind of funcs
            1 represents avaliable chinese fonts in system
            2 represents avaliable chinese fonts  
            3 represents all fonts??
    """
    fm = FontManager()
    mat_fonts = set(f.name for f in fm.ttflist)
    all_ava = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
    if order == 1:
        print( '*' * 10, '系统可用的中文字体', '*' * 10)
        print (all_ava)
    elif order == 2:
        zh_fonts = set(f.split(',', 1)[0] for f in all_ava.decode('utf-8').split('\n'))
        available = mat_fonts & zh_fonts
        print ('*' * 10, '可用的中文字体', '*' * 10)
    elif order == 3:
        print(mat_fonts)

        
def get_sig_symbol(sig):
    symbol = ''
    if  0.01 < sig < 0.05:
        symbol = '*'
    elif 0.001< sig <=0.01:
        symbol = '**'
    elif sig <=0.001:
        symbol = '***'
    elif 0.05 <= sig <0.10:
        symbol = '^'
        
    return symbol


def save_fig(name):
    plt.savefig('figure/{}.svg'.format(name))
