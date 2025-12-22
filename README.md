# Crawlers

A comprehensive collection of web scrapers and automation scripts built with Python, designed to extract data from various platforms including e-commerce sites, social media, job boards, and more.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)

## Features

This repository contains multiple scraping modules for different websites and services:

- **Amazon Scrapers**: Extract product data using ASINs with varying complexity levels (basic, intermediate, advanced Scrapy-based)
- **Automation Scripts**: Automate daily tasks like Excel manipulation, email sending, PDF processing, and more
- **Booking Scrapers**: Scrape hotel booking data
- **Indeed Job Scrapers**: Extract job listings and details
- **Instagram Scrapers**: Collect profile and post data from Instagram
- **TikTok Scrapers**: Scrape video and user data from TikTok
- **YouTube Scrapers**: Extract channel, video, and category information
- **REI Scrapers**: Scrape product data from Recreational Equipment Inc.
- **AliExpress Scrapers**: Extract product listings and details
- **Selenium Scripts**: Various browser automation scripts for dynamic content
- **Whisky Scrapers**: Specialized scrapers for whisky-related data

## Technologies Used

- **Python**: Core programming language
- **Scrapy**: Web crawling framework
- **Selenium**: Browser automation for JavaScript-heavy sites
- **BeautifulSoup**: HTML parsing
- **Django**: Web framework for Instagram scraper
- **Requests**: HTTP library
- **Google API Client**: For YouTube API integration
- **OpenPyXL**: Excel file manipulation
- **Pandas**: Data processing (implied in automation scripts)

## Project Structure

```
Crawlers/
├── project.py              # Main project file with scraping examples
├── requirements.txt        # Python dependencies
├── SECURITY.md            # Security policy
├── amazon/                # Amazon product scrapers
│   ├── basic/            # Simple Amazon scraper
│   ├── intermediate/     # Medium complexity scraper
│   └── amzscrapy/        # Advanced Scrapy-based scraper
├── automation/            # Life automation scripts
│   ├── Excel Automation - Medium.ipynb
│   ├── Send Emails.py
│   └── various subfolders for different automations
├── booking/               # Hotel booking scraper
├── indeed/                # Job search scraper
├── insta/                 # Instagram scraper
├── instagram/             # Django-based Instagram scraper
├── rei/                   # REI product scraper
├── scrapy_ali/            # AliExpress Scrapy project
├── scrapone/              # Additional Scrapy project
├── seleniums/             # Selenium automation scripts
├── tiktok/                # TikTok scraper
├── wisky/                 # Whisky data scraper
├── youtube/               # YouTube scraper
└── youtube_api/           # YouTube API integration
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/alphaoumardev/Crawlers.git
cd Crawlers
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. For Selenium-based scrapers, ensure you have the appropriate web drivers installed (ChromeDriver, GeckoDriver, etc.)

4. For Django-based modules (like instagram/), run migrations if needed:
```bash
cd instagram
python manage.py migrate
```

## Usage

Each scraper module has its own usage instructions. Generally:

### Running Scrapy-based crawlers:
```bash
cd <module_directory>
scrapy crawl <spider_name>
```

### Running Python scripts:
```bash
python <script_name>.py
```

### Running Django applications:
```bash
cd instagram
python manage.py runserver
```

**Note**: Always respect website terms of service and robots.txt when scraping. Use appropriate delays and consider the legal implications of web scraping in your jurisdiction.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security

Please see [SECURITY.md](SECURITY.md) for information about reporting security vulnerabilities.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This repository is for educational purposes only. Web scraping may violate the terms of service of websites. Always ensure you have permission to scrape data and comply with applicable laws and regulations.</content>
<parameter name="filePath">/workspaces/Crawlers/README.md