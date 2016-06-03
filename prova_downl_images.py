from download import *
# PROVA DOWNLOAD IMAGES

urlimagesProva = ("""http://i.hizliresim.com/G5z1J7.png
http://i.hizliresim.com/vL0dBp.png
https://ip1.anime-pictures.net/jvwall_images/d8e/d8e5bd7fb9cd1f12bf5212eec2c285b3_bp.jpg
http://mmii.info/icons/The_Solid_Ninja/babes_babyVeganBooty.png
Matrix:
https://i.gyazo.com/9a99d66c347f7dbe7c370c808e0178ac.jpg
http://image.happyfor.me/img/d8d3e2a8e944a72aea7c3b7a5dd24792@256h_20-49-331-331a
http://i.imgur.com/b2znhqo.jpg
http://i.imgur.com/J9LWHdy.jpg
Proclaim:
http://i.imgur.com/JKU6Qvr.png
http://i.imgur.com/6lrsHdw.png
http://i.imgur.com/YH737kj.png
http://i.imgur.com/EMtPLD8.png
http://i.imgur.com/bHTqIMT.png

DjDamage:
http://www.vector-eps.com/wp-content/gallery/dj-posters-vector-templates/dj-posters-vector-templates6.jpg
http://i.imgur.com/HxAYFGd.png
http://i.imgur.com/15NVElo.jpg
Machine:
http://i.imgur.com/y2myHY3.png
http://i.imgur.com/eVci2tb.png
http://i.imgur.com/15NVElo.jpg
Cold Shadow:
http://pm.odaii.com/galeri/images/2015/05/05/1835/dovme-cilginligi-dovme-seksi-1361038.jpg
http://i.hizliresim.com/XoVgEj.jpg
http://i.hizliresim.com/l9Np5Q.jpg
Regrow:
https://ip1.anime-pictures.net/jvwall_images/34b/34b234e6ef13036a65f74ccac9be5861_bp.jpg
http://www.hdwallpaperscool.com/wp-content/uploads/2014/04/awesome-hd-wallpaper-of-anime-girl.jpg
http://s693.photobucket.com/user/TasteInMusic1245/media/wendy22222222222222222222.jpg.html
http://cdn.mysitemyway.com/etc-mysitemyway/icons/legacy-previews/icons-256/3d-transparent-glass-icons-culture/022152-3d-transparent-glass-icon-culture-heart-solid-sc44.png
http://www.jarodsafehouse.com/_wp/wp-content/uploads/2015/02/3d-glass-heart-2-300x224.png
http://cdn.mysitemyway.com/etc-mysitemyway/icons/legacy-previews/icons/glowing-green-neon-icons-culture/111434-glowing-green-neon-icon-culture-heart-triple.png
http://www.yoanu.com/wp-content/uploads/2015/03/anime-girls-wallpaper-latest-awesome-i0eok2jx.png
http://fr.tinypic.com/useralbum.php?ua=XUB4Q66sLwEyi26E5Kfs9A
http://fr.tinypic.com/useralbum.php?ua=XUB4Q66sLwEqaaucy%2FVNIg
""").split('\n')

# print(url) for url in urlimagesProva
p = re.compile(r'\.(?:jpg|gif|png)')
urlimagesProva = [x for x in urlimagesProva if re.search(p, x)]

filenames = [x.split('/')[-1] for x in urlimagesProva]
# print('\n'.join(urlimagesProva))
imagesProva = dict(zip(filenames, urlimagesProva))
# print('\n'.join(filenames))
downloadVideos(imagesProva)

# extract correct filenames to download
# correctfilenames = [x.split('.')[-1] for x in filenames if "." in x]
# print('\n'.join(correctfilenames))
