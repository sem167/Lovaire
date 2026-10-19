from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
F='/usr/share/fonts/truetype/liberation/LiberationSans-'
def font(w,s): return ImageFont.truetype(F+('Bold' if w=='b' else 'Regular')+'.ttf',s)
def fill(im,box,mode='hv'):
    a=np.asarray(im).astype(float); x0,y0,x1,y1=box
    top=a[y0-2,x0:x1]; bot=a[y1+1,x0:x1]
    left=a[y0:y1,x0-2] if x0>=2 else None; right=a[y0:y1,x1+1] if x1+1<a.shape[1] else None
    h=y1-y0; w=x1-x0
    t=np.linspace(0,1,h)[:,None,None]
    v=top[None]*(1-t)+bot[None]*t
    if mode=='hv' and left is not None and right is not None:
        s=np.linspace(0,1,w)[None,:,None]
        hz=left[:,None]*(1-s)+right[:,None]*s
        v=(v+hz)/2
    a[y0:y1,x0:x1]=v
    return Image.fromarray(a.clip(0,255).astype(np.uint8))
def solid(im,box,c):
    d=ImageDraw.Draw(im); d.rectangle(box,fill=c); return im
def text(d,xy,s,f,fill=(17,17,17),anchor='mm',spacing=6,align='center'):
    d.multiline_text(xy,s,font=f,fill=fill,anchor=anchor,spacing=spacing,align=align)
def check(d,x,y,size=34,w=4,c=(17,17,17)):
    d.line([(x,y),(x+size*0.35,y+size*0.4),(x+size,y-size*0.55)],fill=c,width=w,joint='curve')

# --- voor/na ---
im=Image.open('/home/user/Lovaire/fotos/dab-go-3-voor-na.jpg').convert('RGB')
im=fill(im,(0,30,828,210),'v')
im=fill(im,(828,30,990,180),'v')
ImageDraw.Draw(im).ellipse((912-78,267-78,912+78,267+78),fill=(255,255,255))
im=fill(im,(0,1112,990,1262),'v')
# tape labels: cover text with tape colour
for box in [(6,1066,128,1100),(892,1062,982,1096)]:
    im=fill(im,box,'hv')
d=ImageDraw.Draw(im)
text(d,(495,112),"uitgroei weg\nin 5 seconden",font('b',76),spacing=4)
text(d,(910,268),"#1\nconcealer-\nmerk",font('r',24),spacing=2)
text(d,(54,1083),"voor",font('r',30),fill=(60,55,55))
text(d,(938,1080),"na",font('r',30),fill=(60,55,55))
items=[("grijze\nharen",),("dunner\nhaar",),("uitgroei",),("uitgegroeide\nhighlights",)]
fr=font('r',34); xs=[30,255,480,690]
for (s,),x in zip(items,xs):
    check(d,x,1192,36,4)
    d.multiline_text((x+50,1190),s,font=fr,fill=(17,17,17),anchor='lm',spacing=2)
im.save('/home/user/Lovaire/fotos/dab-go-3-voor-na-nl.jpg',quality=92)

# --- sponsje ---
im=Image.open('/home/user/Lovaire/fotos/dab-go-4-sponsje.jpg').convert('RGB')
im=solid(im,(70,100,515,248),(252,252,251))
im=fill(im,(100,272,450,345),'hv')
im=fill(im,(634,668,980,820),'v')
d=ImageDraw.Draw(im)
text(d,(285,175),"precies &\nzonder knoeien",font('b',58),spacing=4)
text(d,(275,310),"aanbrengen",font('r',58))
text(d,(800,745),"het gevulde sponsje\ndoet het werk\nvoor jou",font('r',35),spacing=4)
im.save('/home/user/Lovaire/fotos/dab-go-4-sponsje-nl.jpg',quality=92)
