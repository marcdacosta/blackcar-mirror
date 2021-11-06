# About Black Car Mirror
![](https://marcdacosta.github.io/storage/blackcarslice.jpg)

### An unexpected archive
Ridesharing apps have imposed themselves on the nature of work in recent years. In many ways, they seek to absorb the labor of their drivers behind APIs, using exploitative psychological tactics to keep them on the road long enough to generate the training data that--it is presumed--will power their self-driving replacements. I was surprised to learn that each time one takes an Uber ride a full sized picture of the driver is attached to the email receipt. Black Car Mirror is a utility for making a video of all those images. 

The output is a video like [this one](https://vimeo.com/212105348)

# How to run

* Update Gmail username/password and run `python harvest.py > images.txt`
* Download image list: `wget -i images.txt`
* Generate video of images: `mogrify -resize 300x300 -format jpg *.*
cat *.* | ffmpeg -f image2pipe -r 3 -vcodec mjpeg -i - -vcodec libx264 out.mp4`
