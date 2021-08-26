#####################################################################
### Lehmer's Factor Stencils
### August 2021
### by Katherine E. Stange (http://math.katestange.net)
### I release this code into the public domain.
### Although I don't mind attribution. 
### Related YouTube video and project:  
###          https://www.youtube.com/watch?v=QzohwKT6TNA
#####################################################################



import svgwrite
import numpy
import math
from svgwrite import cm, mm

# prime numbers, skipping 2
primelist = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917]

### Number of positions in the stencil
numdots = 512

### List of stencils to create
### Currently all squarefree numbers between -500 and 500 excluding 0, 1
### Then I added 0 back in to indicate the key (unpunched stencil)
stencilslist = [0,-1,2,-2,3,-3,5,-5,6,-6,7,-7,10,-10,11,-11,13,-13,14,-14,15,-15,17,-17,19,-19,21,-21,22,-22,23,-23,26,-26,29,-29,30,-30,31,-31,33,-33,34,-34,35,-35,37,-37,38,-38,39,-39,41,-41,42,-42,43,-43,46,-46,47,-47,51,-51,53,-53,55,-55,57,-57,58,-58,59,-59,61,-61,62,-62,65,-65,66,-66,67,-67,69,-69,70,-70,71,-71,73,-73,74,-74,77,-77,78,-78,79,-79,82,-82,83,-83,85,-85,86,-86,87,-87,89,-89,91,-91,93,-93,94,-94,95,-95,97,-97,101,-101,102,-102,103,-103,105,-105,106,-106,107,-107,109,-109,110,-110,111,-111,113,-113,114,-114,115,-115,118,-118,119,-119,122,-122,123,-123,127,-127,129,-129,130,-130,131,-131,133,-133,134,-134,137,-137,138,-138,139,-139,141,-141,142,-142,143,-143,145,-145,146,-146,149,-149,151,-151,154,-154,155,-155,157,-157,158,-158,159,-159,161,-161,163,-163,165,-165,166,-166,167,-167,170,-170,173,-173,174,-174,177,-177,178,-178,179,-179,181,-181,182,-182,183,-183,185,-185,186,-186,187,-187,190,-190,191,-191,193,-193,194,-194,195,-195,197,-197,199,-199,201,-201,202,-202,203,-203,205,-205,206,-206,209,-209,210,-210,211,-211,213,-213,214,-214,215,-215,217,-217,218,-218,219,-219,221,-221,222,-222,223,-223,226,-226,227,-227,229,-229,230,-230,231,-231,233,-233,235,-235,237,-237,238,-238,239,-239,241,-241,246,-246,247,-247,249,-249,251,-251,253,-253,254,-254,255,-255,257,-257,258,-258,259,-259,262,-262,263,-263,265,-265,266,-266,267,-267,269,-269,271,-271,273,-273,274,-274,277,-277,278,-278,281,-281,282,-282,283,-283,285,-285,286,-286,287,-287,290,-290,291,-291,293,-293,295,-295,298,-298,299,-299,301,-301,302,-302,303,-303,305,-305,307,-307,309,-309,310,-310,311,-311,313,-313,314,-314,317,-317,318,-318,319,-319,321,-321,322,-322,323,-323,326,-326,327,-327,329,-329,330,-330,331,-331,334,-334,335,-335,337,-337,339,-339,341,-341,345,-345,346,-346,347,-347,349,-349,353,-353,354,-354,355,-355,357,-357,358,-358,359,-359,362,-362,365,-365,366,-366,367,-367,370,-370,371,-371,373,-373,374,-374,377,-377,379,-379,381,-381,382,-382,383,-383,385,-385,386,-386,389,-389,390,-390,391,-391,393,-393,394,-394,395,-395,397,-397,398,-398,399,-399,401,-401,402,-402,403,-403,406,-406,407,-407,409,-409,410,-410,411,-411,413,-413,415,-415,417,-417,418,-418,419,-419,421,-421,422,-422,426,-426,427,-427,429,-429,430,-430,431,-431,433,-433,434,-434,435,-435,437,-437,438,-438,439,-439,442,-442,443,-443,445,-445,446,-446,447,-447,449,-449,451,-451,453,-453,454,-454,455,-455,457,-457,458,-458,461,-461,462,-462,463,-463,465,-465,466,-466,467,-467,469,-469,470,-470,471,-471,473,-473,474,-474,478,-478,479,-479,481,-481,482,-482,483,-483,485,-485,487,-487,489,-489,491,-491,493,-493,494,-494,497,-497,498,-498,499,-499]

##############################################################################
### Setup parameters controlling punch size, overall size, etc.  
### The defaults work well for me with 12x12 cardstock
### Change things here to adjust stencils
##############################################################################

phi = (1 + numpy.sqrt(5))/2 # golden ratio

fsize = '5px' # base font size

# parameters to set stencil size 
myr = 1.55 # hole punch radius
xoff = 60 # offset of centre -- x
yoff = 60 # offset of centre -- y 
bigr = 59 # radius of stencil itself

# global scale factor
scalefac = 0.9
# scaling of inside of stencil within outside
insidescalefac = 2.385

#########################################################################
### Changing parameters above into actual sizes in pts
### Don't change things here, use the stuff above/previous
#########################################################################

# stencil outline coordinates/radius
mmsub = scalefac*2.83465 # first factor is a scale factor; second is ratio mm to pt
stenx = xoff*mmsub
steny = yoff*mmsub
stenrad = bigr*mmsub # slightly smaller than the actual stencil

# radius and degree range of arc where text label should appear
arcrad = 0.945*stenrad # slightly smaller than the actual stencil
degree0 = -80 # where to start writing
degree1 = 260 # where to end writing

#########################################################################
### Jacobi function
### adapted from https://www.johndcook.com/blog/2019/02/12/computing-jacobi-symbols/
### tested in SageMath
#########################################################################
def jacobi(a, n):
    if a == 0:
        return 0
    if n == 2:
        if a%2 == 0:
            return 0
        else:
            return 1
    assert(n > a > 0 and n%2 == 1)
    t = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0


#########################################################################
### Jacobi function
### Label creator for stencils (not used in video)
### Includes stencil number, and the congruence condition 
###              dictating inclusion of a prime in a stencil
### tested in SageMath
#########################################################################

## Use this version only if you want the stencil label
def get_text(x):
    return "X = " + str(x)

## rename to use this version if you want the full congruence condition
def get_text_verbose(x):
    if x == -1:
        resList = [1]
        modulus = 4
    if x == 2:
        resList = [1,7]
        modulus = 8
    if x % 2 == 1:
        resList = []
        modulus = x
        if x % 4 == 3: 
            modulus = modulus*4
            for y in range(1,modulus):
                ymod = y % x
                if y % 4 == 3 and jacobi(ymod,x) == -1:
                    resList.append(y)
                if y % 4 == 1 and jacobi(ymod,x) == 1:
                    resList.append(y)
        if x % 4 == 1:
            for y in range(1,x):
                if jacobi(y,x) == 1:
                    resList.append(y)
    myString = str(x)+" RES "
    for y in resList:
        myString += str(y)+", "
    myString = myString[:-2]
    myString += " MOD "+str(modulus)
    return myString


#########################################################################
### Now make the stencils!
#########################################################################

for n in stencilslist:

    # Create filename
    filename = "stencil"+str(n)+".svg"
    dwg = svgwrite.Drawing(filename, size=(500*mm, 500*mm), viewBox=('0 0 500 500'), debug=True)

    # embed some single line fonts (these are free fonts I found online)
    dwg.embed_font(name="Slim Extreme", filename='SlimExtreme.ttf')
    dwg.embed_stylesheet("""
    .slimextreme {
        font-family: "Slim Extreme";
    }
    """)
    dwg.embed_font(name="Stymie Hairline Regular", filename='Stymie Hairline Regular.ttf')
    dwg.embed_stylesheet("""
    .hairline {
        font-family: "Stymie Hairline Regular";
    }
    """)
    dwg.embed_font(name="Flamenco Regular", filename='Flamenco-Regular.ttf')
    dwg.embed_stylesheet("""
    .flamenco {
        font-family: "Flamenco Regular";
    }
    """)
    dwg.embed_font(name="Machine Tool Gothic", filename='machtgth.ttf')
    dwg.embed_stylesheet("""
    .mtgothic {
        font-family: "Machine Tool Gothic";
    }
    """)

    # Create the outer circle and notches
    outline = dwg.circle(center=(stenx,steny), r=stenrad, stroke='green', fill='white', stroke_width=1)
    dwg.add(outline)
    notch1 = dwg.circle(center=(stenx,scalefac*(-1.8)*mmsub), r=5*mmsub, stroke='purple', fill='white', stroke_width=1)
    notch2 = dwg.circle(center=((1.86)*(1.01)*stenx,((1.5)*(1.04))*steny), r=5*mmsub, stroke='purple', fill='white', stroke_width=1)
    notch3 = dwg.circle(center=((1-0.86)*(0.99)*stenx,((1.5)*(1.06))*steny), r=5*mmsub, stroke='purple', fill='white', stroke_width=1)
    dwg.add(notch1)
    dwg.add(notch2)
    dwg.add(notch3)


    # a list of dots/primes to punch out
    primesyes = []

    # for each prime, make a dot and text (later we include only one or other)
    for i in range(1,numdots+1):

        # get the prime corresponding to a location
        p = primelist[i-1]

        # determine position in spiral
        insidescale = insidescalefac*numpy.sqrt(i)
        ang = 2*numpy.pi*i/(phi*phi)
        xpos = (xoff+insidescale*numpy.cos(ang))
        ypos = (yoff+insidescale*numpy.sin(ang))

        # create circle element
        circle = dwg.circle(center=(xpos*mmsub,ypos*mmsub), r=myr*mmsub, stroke='blue', stroke_width=1, fill='white')

        # determine font size and text offset based on the number of digits
        pStr0 = str(p)
        pStr1 = ""
        if (p < 10):
            fsize = '10px'
            xadj = -0.53*myr
            yadj = 0.6*myr
        if (p > 9 and p < 100 ):
            fsize = '8px'
            xadj = -0.75*myr
            yadj = 0.50*myr
        if (p > 99 and p < 1000 ):
            fsize = '5px'
            xadj = -0.73*myr
            yadj = 0.39*myr
        if (p > 999 ):
            fsize = '4px'
            pStr0, pStr1, pStr2, pStr3 = pStr0[0], pStr0[1], pStr0[2], pStr0[3]
            xadj = -0.40*myr
            yadj = 0.03*myr
            xextra = 0.5*myr
            yextra = 0.7*myr

        # create the text element
        text = dwg.text(pStr0, insert=((xpos+xadj)*mmsub,(ypos+yadj)*mmsub), stroke='black',stroke_width=0.1, fill=svgwrite.rgb(0,0,0,'%'),font_size=fsize)
        if (p > 999): # for 4-digit primes, create each digit separately in a square
            text1 = dwg.text(pStr1, insert=((xpos+xadj+xextra)*mmsub,(ypos+yadj)*mmsub), stroke='black',stroke_width=0.1, fill=svgwrite.rgb(0,0,0,'%'),font_size=fsize)
            text2 = dwg.text(pStr2, insert=((xpos+xadj)*mmsub,(ypos+yadj+yextra)*mmsub), stroke='black',stroke_width=0.1, fill=svgwrite.rgb(0,0,0,'%'),font_size=fsize)
            text3 = dwg.text(pStr3, insert=((xpos+xadj+xextra)*mmsub,(ypos+yadj+yextra)*mmsub), stroke='black',stroke_width=0.1, fill=svgwrite.rgb(0,0,0,'%'),font_size=fsize)

        # based on stencil number and jacobi value, include circle or not
        nmod = n % p
        if n != 0 and (jacobi(nmod,p) == 1 or jacobi(nmod,p) == 0):
            dwg.add(circle)
            primesyes.append(p)
        else:
            pass

        # Create a textgroup for the numbers and label
        textgroup = dwg.add(dwg.g(class_="slimextreme", ))

        # based on stencil number and jacobi value, include text or not
        nmod = n % p
        if n != 0 and (jacobi(nmod,p) == 1 or jacobi(nmod,p) == 0):
            pass
        else:
            textgroup.add(text)
            if (p > 999):
                textgroup.add(text1)
                textgroup.add(text2)
                textgroup.add(text3)


    # create a label for the stencil that is curved around the outside of the stencil
    # some helpful background:  https://stackoverflow.com/questions/42004408/textpath-with-svgwrite-valueerror-invalid-children-textpath-for-svg-element

    # angles and (x,y) coordinates of beginning of writing and end of writing
    angle0 = math.radians(degree0)
    angle1 = math.radians(degree1)
    ax0 = stenx + arcrad*(math.cos(angle0)) # absolute coordinates
    ay0 = steny + arcrad*(math.sin(angle0))
    ax1 = arcrad*(math.cos(angle1)) - ax0 + stenx # difference from previous (relative) coordinates
    ay1 = arcrad*(math.sin(angle1)) - ay0 + steny

    # create the arc path for the writing
    # {0},{1} is start position
    # {3},{4} is end position
    # {2} is radius
    pathString = "M {0},{1} a {2},{2} 0 1,1 {3},{4}".format(ax0,ay0,arcrad,ax1,ay1)
    print(pathString)
    labelPath = dwg.path(d=pathString, fill="none", stroke_width=0, stroke="orange")#, stroke-width="5")
    dwg.add(labelPath)

    # Create a label element with the text around the path
    labelString = get_text(n)

    # Here I add the label to the picture
    textgrouplabel = dwg.add(dwg.g(class_="slimextreme", ))
    text = textgrouplabel.add(svgwrite.text.Text("")) 
    text.add(svgwrite.text.TextPath(path=labelPath, text=labelString, font_size='5px', startOffset=None, method='align', spacing='exact'))

    # save the result and finish
    dwg.save(pretty=True)

    # print out the prime holes for the stencil (for debugging)
    print(n, primesyes)
