# python projects
* pygame - Snake Game
* scrapy - Web Crawler

## pygame
pygame (the library) is a Free and Open Source python programming language library for making multimedia applications like games built on top of the excellent SDL library. 

**Project Name：snake game**

The player controls a square on a bordered plane. As it moves forward, it leaves a trail behind, resembling a moving sname. The player attempts to eat items by running into them with the head of the snake. Each item eaten makes the snake longer.

------------------------------------------------------
## scrapy

scrapy is an open source and collaborative framework for extracting the data you need from websites.

**Project Name: Web Crawler**

a web crawler for the FDA drug data from https://www.biopharmcatalyst.com/

**run web crawler and generate report file** 

direct to the root file "biopharm", and execute the command line as below.

For CSV file

```
scrapy crawler fda -o ./reports/xpt_mm_dd_YY.csv
```

For JSON file

```
scrapy crawler fda -o ./reports/xpt_mm_dd_YY.json
```