SELECT
    ROUND(SUM(payment_value)::numeric, 2) AS total_revenue
FROM final_dataset;

SELECT
    month,
    ROUND(SUM(payment_value)::numeric, 2) AS revenue
FROM final_dataset
GROUP BY month
ORDER BY month;

SELECT
    customer_unique_id,
    ROUND(SUM(payment_value)::numeric, 2) AS total_spending
FROM final_dataset
GROUP BY customer_unique_id
ORDER BY total_spending DESC
LIMIT 10;

SELECT
    product_id,
    ROUND(SUM(payment_value)::numeric, 2) AS revenue
FROM final_dataset
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;

SELECT
    customer_state,
    ROUND(SUM(payment_value)::numeric, 2) AS revenue
FROM final_dataset
GROUP BY customer_state
ORDER BY revenue DESC;

SELECT
    ROUND(AVG(payment_value)::numeric, 2) AS avg_order_value
FROM final_dataset;

SELECT
    COUNT(DISTINCT customer_unique_id) AS total_customers,

    COUNT(
        DISTINCT CASE
            WHEN order_count = 1
            THEN customer_unique_id
        END
    ) AS churned_customers

FROM (
    SELECT
        customer_unique_id,
        COUNT(order_id) AS order_count
    FROM final_dataset
    GROUP BY customer_unique_id
) t;