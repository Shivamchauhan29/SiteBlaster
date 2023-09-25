# SiteBlaster

SiteBlaster is a Python script designed for sending payloads to a website's contact form multiple times with randomized data. It is a useful tool for testing the robustness of a website's contact form and assessing how well it handles various types of input. Please use this tool responsibly and only on websites that you have permission to test.

## Features

- Send payloads to a website's contact form with randomized data.
- Multithreading for faster requests.
- Customizable payload options.

## Prerequisites

Before using SiteBlaster, make sure you have the following prerequisites installed:

- Python 3
- Requests library (`pip install requests`)
- Requests-Toolbelt library (`pip install requests-toolbelt`)

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/SiteBlaster.git
## 1. Navigate to the project directory:

```bash
cd SiteBlaster
```
## 2. Edit the script (site_blaster.py) to configure the payload data as needed:

- Modify the **`education_words`** list to include keywords relevant to your testing.
- Customize the **`menu_options`** list with options specific to the website you're testing.
- Adjust the **`url`** variable to point to the target website's contact form.

## 3. Run the script to send payloads:

```bash
python site_blaster.py
```
- Monitor the script's progress as it sends payloads to the specified URL.
## Customization
- You can customize the payload data in the **`send_post_request function`** to match the expected fields of the contact form on the target website.
- Adjust the **`num_requests`** variable to specify the number of requests you want to send.

## Responsoble Use

Please use SiteBlaster responsibly and in accordance with ethical guidelines. Ensure that you have proper authorization to test the website's contact form. Unauthorized and excessive use of this tool may result in legal consequences.

## Disclaimer

This tool is provided for educational and testing purposes only. The developers and maintainers of SiteBlaster are not responsible for any misuse or unlawful activity conducted with this tool. Use it at your own discretion.
