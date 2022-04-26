# MapBoxComposer

This is the home of a small script that will allow you to compose and stick images from
a MapBox created image.

## Running

Edit `GenerateMakefile.py` with the corect endpoints using the variables at the top of the file.

Then use it to generate a Makefile and run it!

```shell
$ ./GenerateMakefile.py > Makefile
$ make -k $NUM_CPU
```
