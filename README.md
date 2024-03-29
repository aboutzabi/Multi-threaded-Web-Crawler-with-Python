# Multi-threaded-Web-Crawler-with-Python

# Multi-threaded Web Crawler with Python

This Python script provides a simple multi-threaded web crawler capable of making HTTP and HTTPS GET requests. It can be used to concurrently fetch web content from different hosts and save the responses to individual files.

## Features
- Multi-threaded design for concurrent web crawling.
- Supports both HTTP and HTTPS connections.
- Saves fetched content to specified file paths.

## Getting Started
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Run the script:
    ```bash
    python script_name.py
    ```
    Follow the prompts to input host, scheme (http/https), output file paths, and whether to add another.

3. View the results:
    The fetched content will be saved to the specified file paths, and a list of executed crawlers will be displayed.

## Usage
- Input the host, scheme, and output file path for each crawler.
- Specify whether to add another crawler.
- The script will launch multiple threads, each responsible for a specific web crawler.
- Executed crawlers will be listed after all threads have finished.

## Note
- This script uses a simple approach for HTTPS connections and ignores SSL certificate verification for simplicity. In a production environment, proper SSL certificate handling should be implemented.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
