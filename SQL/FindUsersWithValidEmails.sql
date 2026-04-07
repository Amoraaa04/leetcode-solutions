SELECT user_id, name, mail
FROM Users
-- Filters valid emails
WHERE REGEXP_LIKE(
    mail, -- checks the mail column
    '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$',
    'c' -- case-sensitive match (ensures '@leetcode.com' is exact)
);
