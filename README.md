# web2pdf
A python app to read a bookmark.html file and fetch PDF versions of all links within.

# Installation

```
# Clone the repo
git clone git@github.com:IndelibleStamp/web2pdf.git

# Install wkhtmltopdf. See https://wkhtmltopdf.org/ for other ways
sudo dnf install wkhtmltopdf # For Fedora. 

# Install the python dependencies
cd web2pdf
pip install -r requirements.txt
```

# Usage

Check `web2pdf/web2pdf/conf.py` and edit it. Mainly the `INPUT` varialble needs 
to be set with the path to the bookmarks.html file. Then run as follows:

```
(pdf) bash-4.3 ~/code/web2pdf/web2pdf$ ./web2pdf.py 
Found 2599 links in the bookmark file
Found 2599 rows in the bookmark db
..of which 81 links are already saved
..and 2506 are pending
Hit enter to start downloading pending PDFs
Downloading https://www.quantamagazine.org/20170207-bell-test-quantum-loophole/ | experiment-reaffirms-quantum-weirdness
<snipped>
```

# TODO

This is a weekend project. There is quite a bit more to do :)

- Make it async. Too slow right now.
- Log to file instead of stdout.
- Add tests.
- Support additional bookmark formats?
