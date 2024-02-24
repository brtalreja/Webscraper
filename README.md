# Web Scraper

A Python script to scrape and display blog post dates and titles from a website.

## Overview

This web scraper uses the BeautifulSoup library to extract information from a specified URL. It fetches the content, extracts blog post dates and titles, and prints them in a user-friendly format.

## Features

- Random user-agent headers for each request.
- Fetches content from a specified URL.
- Parses and formats blog post dates.
- Prints blog post dates and titles.
- More details can be scraped based on requirements.

## Prerequisites

- Python 3.x
- Required libraries: `requests`, `random`, `datetime`, `bs4` (BeautifulSoup)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/brtalreja/Webscraper.git
    cd Webscraper
    ```

2. Run the script:

    ```bash
    python Webscraper.py
    ```

3. The scrapper is built for `https://pixelford.com/blog/` webpage.

## Functions

### `get_content(url)`

This function fetches the content from a given URL and handles exceptions.

### `format_date(date_string)`

This function formats the date in the required format while handling exceptions.

### `print_blogs_date_title(blogs)`

This function performs the scraping task, extracting and printing blog post dates and titles.

### `main()`

The main function calls all helper functions to complete the web scraping task.

## References

This project was created following the guidance of the LinkedIn Learning course:

- **Instructor:** Nick Walter
