# Find Users With Valid E-mails

**Problem Summary:** Given a table ``Users`` find the users who have valid emails

---

## 1. Understanding the Problem
- Input: Table ``Users(user_id, name, mail)``
- Output: Table with columns ``user_id, name, mail)``
- Constraints:
     - Email must contain the domain `@leetcode.com` (case-sensitive)
     - Email must start with a letter
     - The prefix may contain only:
         - letters (A–Z, a–z)
         - digits (0–9)
         - underscore '_' , period '.' , and dash '-'
         - Any other character (e.g. #, %, spaces) makes the email invalid
- Key Observation:
    - cannot contain any character other than '_', '.' and/or '-', for example '#'
---

## 2. Approach
- Idea / Plan: Use `REGEXP_LIKE` to enforce a pattern for valid emails
- Steps:
   - select user_id, name, mail from Users
   - Use WHERE REGEXP_LIKE mail: to select mail that starts with a letter, use the correct domain and correct characters
     
## 3. Code Link
Press [Find users with valid e-mail]() to view code
