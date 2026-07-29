# website_security_header_analyzer

# 🛡️ Website Security Header Analyzer

A simple Python-based cybersecurity tool that analyzes the HTTP response headers of a website and checks whether important security headers are present. The application identifies missing security headers, calculates an overall risk level, and generates a security report with remediation recommendations.

---

## 📌 Features

- Analyze HTTP response security headers
- Detect missing security headers
- Calculate overall website risk level
- Generate a detailed security report
- Beginner-friendly and lightweight
- Command-line interface

---

## 🔒 Security Headers Checked

- Content-Security-Policy (CSP)
- X-Frame-Options
- X-Content-Type-Options
- Strict-Transport-Security (HSTS)
- Referrer-Policy
- Permissions-Policy
- Cache-Control

---

## 🛠️ Technologies Used

- Python 3
- Requests Library
- HTTP Protocol
- Cybersecurity Fundamentals

---

## 📂 Project Structure

```
Website-Security-Header-Analyzer/
│
├── main.py
├── header_checker.py
├── risk_calculator.py
├── report_generator.py
├── requirements.txt
├── README.me
├── sample_output
└── screenshots

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Website-Security-Header-Analyzer.git
```

### Navigate to the Project Folder

```bash
cd Website-Security-Header-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python main.py
```

Enter a website URL when prompted.

Example:

```
https://example.com
```

---

## 💻 Sample Output

```
==================================================
Website Security Header Analyzer
==================================================

Website:
https://example.com

✔ Content-Security-Policy
✘ X-Frame-Options
✔ X-Content-Type-Options
✘ Strict-Transport-Security
✔ Referrer-Policy
✘ Permissions-Policy
✔ Cache-Control

Risk Level : Medium

Report generated successfully!
```

---

## 📄 Generated Report

The application automatically creates a file named:

```
security_report.txt
```

The report includes:

- Website URL
- Scan Date & Time
- Security Header Status
- Overall Risk Level
- Security Recommendations

---



## 🚀 Future Enhancements

- GUI using Tkinter
- PDF Report Generation
- HTML Report Export
- SSL Certificate Analysis
- HTTPS Enforcement Check
- Cookie Security Analysis
- Security Score (0–100)
- Scan Multiple Websites
- Export Results to CSV
- Logging Support

---

## 🎓 Learning Outcomes

This project helped in understanding:

- Importance of HTTP Security Headers
- Common Web Security Best Practices
- Risk Assessment
- Secure Website Configuration
- Python Requests Library
- HTTP Response Analysis

---



---

⭐ If you found this project useful, consider giving it a star!
