import tarfile

tar = tarfile.open('ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz')
tar.extractall()
tar.close()
