# About blackcar-mirror
### An unexpected archive
![](https://marcdacosta.github.io/storage/blackcarslice.jpg)

Ridesharing apps have seen a meteoric rise in recent years. In many ways, they seek to absorb the labor of their drivers behind APIs, using exploitative psychological tactics to keep them on the road long enough to generate the training data that will power their self-driving replacements. Black Car Mirror extracts the driver profile photos that are living in the email box of any Uber customer. 

The output is a video like [this one](https://vimeo.com/212105348)

# How to run

* Update Gmail username/password and run `python harvest.py > images.txt`
* Download image list: `wget -i images.txt`
* Generate video of images: `mogrify -resize 300x300 -format jpg *.*
cat *.* | ffmpeg -f image2pipe -r 3 -vcodec mjpeg -i - -vcodec libx264 out.mp4`
