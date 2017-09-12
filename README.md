# About blackcar-mirror


# How to run

* Update Gmail username/password and run `python harvest.py > images.txt`
* Download image list: `wget -i images.txt`
* Generate video of images: `mogrify -resize 300x300 -format jpg *.*
cat *.* | ffmpeg -f image2pipe -r 3 -vcodec mjpeg -i - -vcodec libx264 out.mp4`
