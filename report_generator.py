from datetime import datetime


def generate_report(url, headers, risk):

    with open("security_report.txt", "w") as file:

        file.write("=" * 60 + "\n")
        file.write("Website Security Header Analysis Report\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Website : {url}\n")
        file.write(f"Date    : {datetime.now()}\n\n")

        file.write("Security Headers\n")
        file.write("-" * 60 + "\n")

        for header, status in headers.items():

            if status:
                file.write(f"[Present] {header}\n")
            else:
                file.write(f"[Missing] {header}\n")

        file.write("\n")
        file.write("-" * 60 + "\n")
        file.write(f"Overall Risk Level : {risk}\n")
        file.write("-" * 60 + "\n\n")

        file.write("Recommendations\n")
        file.write("-" * 60 + "\n")

        recommendations = {
            "Content-Security-Policy":
                "Implement a strong Content Security Policy.",

            "X-Frame-Options":
                "Use DENY or SAMEORIGIN to prevent clickjacking.",

            "X-Content-Type-Options":
                "Set X-Content-Type-Options to nosniff.",

            "Strict-Transport-Security":
                "Enable HSTS to enforce HTTPS.",

            "Referrer-Policy":
                "Configure Referrer-Policy to reduce information leakage.",

            "Permissions-Policy":
                "Restrict browser features using Permissions Policy.",

            "Cache-Control":
                "Disable caching for sensitive pages."
        }

        for header, status in headers.items():

            if not status:
                file.write(f"- {recommendations[header]}\n")

        file.write("\n")
        file.write("=" * 60)