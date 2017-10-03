# Utilities

Automation, setup and other useful scripts along with system tweaks.
Some tweaks might only be applicable to Ubuntu.


## Contents
* **Bash configuration** : bashrc file having some aliases and functions
* **Filename modifier** : Scripts to rename video playlist/series files in a consistent format
* **Git configuration** : Configuration to get an improved git log
* **Setup scripts** : Common installations on a new machine/server
* **Sublime Text Tweaks** : Packages and themes for Sublime Text editor
* **Ubuntu Tweaks** : Extensions and themes for Ubuntu
* **Vim configuration** : Some plugins, color scheme and keyboard mappings to improve vim


## Extra

#### Changing extension name of files
Run command in below format in terminal :  
```
rename "s/<old extension>/<new extension>/" *.<old extension>
```  
Example : ```rename "s/css/scss/" *.css``` will rename all .css files to .scss

#### Settings to control mouse cursor using keyboard
1. Open 'Settings' -> 'Universal Access' -> 'Pointing and clicking' -> 'Mouse keys'
2. Turn that option ON (Try Alt-m to toggle if spacebar doesn't work)
3. Now you will be able to move cursor with numpad but the speed will be extremely slow.
4. Run the following commands in terminal to set a good to do speed :  
  ```sudo apt-get install xkbset```  
  ```xkbset ma 60 10 10 5 2```

#### Merge and compress PDF
1. Install ghostscript using ```sudo apt-get install ghostscript```
2. Use the command:  
  ```gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf```  
  This command will compress input.pdf to output.pdf
3. Give multiple files at end of command to merge files in same order like:
  ```gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input1.pdf input2.pdf```  
4. ```PDFSETTINGS``` parameter can be given these values:  
  - screen (low-size)
  - ebook (medium-size)
  - default (large-size)
  - printer (print optimized)
  - prepress (prepress optimized)

#### Compress images
* JPG/JPEG :  
  ```sudo apt-get install jpegoptim```  
  ```sudo find . -type f -name "*.jpg" -exec jpegoptim {} \;```
* PNG :  
  ```sudo apt-get install optipng```  
  ```sudo find . -type f -name "*.png" -exec optipng {} \;```
