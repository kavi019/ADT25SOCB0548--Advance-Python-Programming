import re

REGEX_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

def search_emails(source_text):
    return re.findall(REGEX_PATTERN, source_text)

def verify_email(candidate_str):
    return re.fullmatch(REGEX_PATTERN, candidate_str) is not None

if __name__ == "__main__":
    test_paragraph = """
    Please contact us for support:
    - General queries: support@examplecorp.com
    - Sales team: sales.team@business-hub.co.in
    - Personal note from Rahul (rahul_23@gmail.com) sent yesterday.
    - Invalid mentions: not-an-email, @missing-local.com, plain.text@
    - Newsletter sign-up: newsletter+promo@my-site.org
    """

    print("Original text:")
    print(test_paragraph)

    matches_found = search_emails(test_paragraph)
    print(f"Found {len(matches_found)} email address(es) in the text:")
    for email_match in matches_found:
        print(f"  - {email_match}")

    print("\nValidating individual strings with verify_email():")
    cases = [
        "john.doe@example.com",
        "invalid-email",
        "user@site",
        "user@site.com",
        "plain.text@",
        "a.b-c_d+e@sub.domain.co.in",
    ]
    for case in cases:
        validation_status = "VALID" if verify_email(case) else "INVALID"
        print(f"  {case:30s} -> {validation_status}")