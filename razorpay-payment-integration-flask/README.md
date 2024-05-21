# Razorpay Integration with Flask

This project demonstrates how to integrate Razorpay payment gateway with a Flask application. It allows users to make
payments and captures payments through a webhook.

## Getting Started

Follow these steps to set up and run the project:

### Prerequisites

- Python 3.9 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/shahdeep1908-tech/Razorpay-Payment-Integration.git
   cd razorpay-payment-integration-flask
   ```
2. Create a virtual environment (optional but recommended):
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install project dependencies:
   ```shell
   pip install -r requirements.txt
   ```

### Configuration

Configure Razorpay API Keys:

Create .env file and update "RAZORPAY_CLIENT_KEY" and "RAZORPAY_CLIENT_SECRET" with your actual Razorpay API
credentials.

## Usage

1. Start the Flask application:
   ```shell
   python app.py
   ```

2. Access the payment initiation page:

   Open your web browser and visit http://localhost:8000/ to access the Razorpay payment page.

### Webhooks

To handle Razorpay webhooks, configure your Razorpay dashboard to send webhook events to your Flask application's
/webhook/razorpay endpoint. Ensure that you've set up the webhook secret in your .env.

## Project Workflow Diagram

*Figure 1: Razorpay Payment Dashboard*
![dashboard.png](images%2Fdashboard.png)

*Figure 2: Razorpay Payment Options*
![razorpay_payment_options.png](images%2Frazorpay_payment_options.png)

*Figure 3: Razorpay Payment OTP Verification*
![OTP_verification.png](images%2FOTP_verification.png)

*Figure 4: Razorpay Success Page*
![payment_success.png](images%2Fpayment_success.png)

*Figure 5: Razorpay Success Page Redirect
![success_redirect.png](images%2Fsuccess_redirect.png)