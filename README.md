# MapBoxComposer

This is the home of a small script that will allow you to compose and stick images from
a MapBox created image.

## Running

Edit `GenerateMakefile.py` with the correct endpoints using the variables at the top of the file.

Then use it to generate a Makefile and run it!

```shell
./GenerateMakefile.py > Makefile
make -j NUM_CPU
```

## resource limits errors

edit (or temporary remove) `/etc/ImageMagick-6/policy.xml` 

or set env `MAGICK_CONFIGURE_PATH` to `/dev/null`
