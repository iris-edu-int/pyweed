# Support

## Common problems

Far and away the most common problem is library mismatches -- some of the libraries that PyWEED uses (ObsPy and Qt most notably) bring in a wide mix of their own dependencies, resulting in a complex mix of library versions.

This can be addressed by specifying PyWEED's direct dependencies in more granularity (eg. require matplotlib=3.1 rather than matplotlib=3) but this increases the likelihood that something will be entirely unavailable on some platform (or at some point in time, since the 

### matplotlib / basemap

#### ImportError: cannot import name 'dedent' from 'matplotlib.cbook'

See #119, in an existing environment running
```
conda install matplotlib=3.2
```
should install the correct package.

## Contact

If you see a problem, send an email to pyweed@iris.washington.edu, or file a ticket at https://github.com/iris-edu/pyweed/issues.