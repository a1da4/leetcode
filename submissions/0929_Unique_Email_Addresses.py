class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        vocab = set()
        for email in emails:
            local, domain = email.split("@")
            local = "".join(local.split("."))
            local = local.split("+")[0]
            vocab.add(f"{local}@{domain}")
        
        return len(vocab)
