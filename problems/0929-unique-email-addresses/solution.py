class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split("@")

            # canonize local
            local = local.replace(".", "")
            local, *_ = local.partition("+")

            # concat them and add to set
            unique_emails.add(local+"@"+domain)

        return len(unique_emails)