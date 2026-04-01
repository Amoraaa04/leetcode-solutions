# Average Selling Price
---

**Problem Summary:**  Given two tables ``Prices`` and ``UnitsSold``, return the average selling price for each product.
- average price should be rounded to 2 decimal places
- If a product does not have any sold units (NULL), its average selling price is assumed to be 0

---

## 2. Understanding the Problem
- Input: Tables ``Prices(product_id, price, start_date, end_date)`` and ``UnitsSold(units, purchase_date)``
- Output: Table with columns ``product_id`` and ``average_price``
- Constraints:
    - UnitsSold can be NULL
    - average_price must be rounded to two decimal places
- Key Observation:
    -  Use LEFT JOIN to handle products with no sales
    -   Match purchase_date between start_date and end_date


---

## 3. Approach
- Idea / Plan: Use aggregate SUM(p.price * u.units) / SUM(u.units)to find average_price
- Steps:
    - Create logic to calculate the average selling price and handle NULL values using COALESCE
    - LEFT JOIN on product.id
    - Ensure purchase_date is between start_date and end_date 
    - ORDER BY product_id
      
--

## Code link

Press [AverageSellingPrice.sql](https://github.com/Amoraaa04/leetcode-solutions/blob/ec28f90a87827973664bb5f6f9a976a8dadf3362/SQL/AverageSellingPrice.sql) to view code
