# Scrapy application

Python application to extract data from website with Scrapy module

## Getting Started

Clone the repository using command line

1.Navigate to your repository’s Code tab.

2.Click Clone or download.

3.Copy the URL provided.

4.Open your command line or Terminal application and enter the directory where you would like to copy the repository.

```
cd ~/
```

5.Clone the repository by replacing <URL> with clone URL you copied in the previous step. The repository will be cloned into a new directory in this location.

```
git clone <URL>
```

### Prerequisites

1.Initialize a virtual environment in directory.

```
cd scrapy-spider
virtualenv venv
. venv/bin/activate
```

2.Activate virtual environment

```
source venv/bin/activate
```

2.Install requirements

```
./scripts/bootstap.sh
```

## Building a spider
In the application code `spider.py`

1. Specify the spider name for identifying the spider.

```
name = 'Website'
```

2. Specify the name of json file with urls to initialize `start_urls` variable containing a list of URLs.

```
data.json
```

Inside the file
```
[
  "https://www.url.com",
  "https://www.url1.com",
]
```
3. In `parse` method change the keys and values to your preferences.This method is used to process the webpage to extract what we want.

4. Inspect your URL with the `inspector` in web browser to find the position of the HTML element which you want to capture, and specify the `path` to it.

Example of extracting the title
```
response.xpath('//div[@class="title"]/h1/text()').get()
```

### Running application

1. Run app from root directory, and output a file(.csv, .json) with captured data. 

```
scrapy runspider spider.py -o data.csv
```

### [Scrapy documentation](https://docs.scrapy.org/en/latest/)