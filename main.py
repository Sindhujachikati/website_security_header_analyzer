from header_checker import check_security_headers
from risk_calculator import calculate_risk
from report_generator import generate_report

def main():
    print("=" * 50)
    print(" Website Security Header Analyzer ")
    print("=" * 50)

    url = input("Enter Website URL (https://example.com): ").strip()

    try:
        headers_status = check_security_headers(url)

        print("\nSecurity Header Analysis")
        print("-" * 50)

        for header, status in headers_status.items():
            if status:
                print(f"✔ {header}")
            else:
                print(f"✘ {header}")

        risk = calculate_risk(headers_status)

        print("\nRisk Level:", risk)

        generate_report(url, headers_status, risk)

        print("\nReport generated successfully!")
        print("File: security_report.txt")

    except Exception as e:
        print("\nError:", e)


if __name__ == "__main__":
    main()