class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails = []
        for email in emails:
            res = email.partition("@")
            local = res[0]
            seperator = res[1]
            domain = res[2]
            if "." in local:
                local = local.replace(".", "")
            if "+" in local:
                index = local.index("+")
                local = local[:index]
            mail = "" + local + seperator + domain
            if not mail in mails:
                mails.append(mail)

        return len(mails)