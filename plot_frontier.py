{
  "name": "invoice_extraction",
  "task_type": "extraction",
  "prompt_template": "Extract these fields from the invoice text as JSON with keys invoice_number, vendor, quantity, total_usd. quantity and total_usd must be strings with no units or currency symbols. Respond with only the JSON object.\nText: {input}\nJSON:",
  "subset_match": false,
  "examples": [
    {
      "input": "Invoice INV-1994 from Globex Ltd, dated 2025-08-10. Line item: 50 units of floor mats at a total of USD 1986.71. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-1994",
        "vendor": "Globex Ltd",
        "quantity": "50",
        "total_usd": "1986.71"
      }
    },
    {
      "input": "Invoice INV-3645 from Umbrella Inc, dated 2025-07-07. Line item: 144 units of USB hubs at a total of USD 2454.72. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-3645",
        "vendor": "Umbrella Inc",
        "quantity": "144",
        "total_usd": "2454.72"
      }
    },
    {
      "input": "Invoice INV-8474 from Cyberdyne, dated 2025-08-23. Line item: 10 units of copier toner at a total of USD 378.70. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8474",
        "vendor": "Cyberdyne",
        "quantity": "10",
        "total_usd": "378.70"
      }
    },
    {
      "input": "Invoice INV-6957 from Globex Ltd, dated 2025-10-13. Line item: 5 units of copier toner at a total of USD 175.81. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-6957",
        "vendor": "Globex Ltd",
        "quantity": "5",
        "total_usd": "175.81"
      }
    },
    {
      "input": "Invoice INV-1965 from Hooli, dated 2025-04-13. Line item: 24 units of safety gloves at a total of USD 155.51. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-1965",
        "vendor": "Hooli",
        "quantity": "24",
        "total_usd": "155.51"
      }
    },
    {
      "input": "Invoice INV-8327 from Stark Industries, dated 2025-02-08. Line item: 100 units of cable reels at a total of USD 460.07. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8327",
        "vendor": "Stark Industries",
        "quantity": "100",
        "total_usd": "460.07"
      }
    },
    {
      "input": "Invoice INV-3401 from Stark Industries, dated 2025-11-28. Line item: 5 units of USB hubs at a total of USD 64.88. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-3401",
        "vendor": "Stark Industries",
        "quantity": "5",
        "total_usd": "64.88"
      }
    },
    {
      "input": "Invoice INV-3472 from Umbrella Inc, dated 2025-11-08. Line item: 10 units of office chairs at a total of USD 73.25. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-3472",
        "vendor": "Umbrella Inc",
        "quantity": "10",
        "total_usd": "73.25"
      }
    },
    {
      "input": "Invoice INV-3530 from Globex Ltd, dated 2025-03-15. Line item: 100 units of office chairs at a total of USD 1124.47. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-3530",
        "vendor": "Globex Ltd",
        "quantity": "100",
        "total_usd": "1124.47"
      }
    },
    {
      "input": "Invoice INV-8588 from Wonka Co, dated 2025-03-05. Line item: 144 units of copier toner at a total of USD 4234.28. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8588",
        "vendor": "Wonka Co",
        "quantity": "144",
        "total_usd": "4234.28"
      }
    },
    {
      "input": "Invoice INV-6571 from Globex Ltd, dated 2025-03-18. Line item: 5 units of copier toner at a total of USD 7.54. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-6571",
        "vendor": "Globex Ltd",
        "quantity": "5",
        "total_usd": "7.54"
      }
    },
    {
      "input": "Invoice INV-1458 from Umbrella Inc, dated 2025-04-25. Line item: 50 units of laptop docks at a total of USD 638.96. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-1458",
        "vendor": "Umbrella Inc",
        "quantity": "50",
        "total_usd": "638.96"
      }
    },
    {
      "input": "Invoice INV-7564 from Umbrella Inc, dated 2025-06-24. Line item: 24 units of laptop docks at a total of USD 514.30. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-7564",
        "vendor": "Umbrella Inc",
        "quantity": "24",
        "total_usd": "514.30"
      }
    },
    {
      "input": "Invoice INV-7850 from Pied Piper, dated 2025-08-14. Line item: 12 units of cable reels at a total of USD 88.22. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-7850",
        "vendor": "Pied Piper",
        "quantity": "12",
        "total_usd": "88.22"
      }
    },
    {
      "input": "Invoice INV-5132 from Initech, dated 2025-02-04. Line item: 100 units of floor mats at a total of USD 1552.03. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-5132",
        "vendor": "Initech",
        "quantity": "100",
        "total_usd": "1552.03"
      }
    },
    {
      "input": "Invoice INV-6341 from Cyberdyne, dated 2025-03-02. Line item: 50 units of USB hubs at a total of USD 881.60. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-6341",
        "vendor": "Cyberdyne",
        "quantity": "50",
        "total_usd": "881.60"
      }
    },
    {
      "input": "Invoice INV-8945 from Acme Corp, dated 2025-03-14. Line item: 12 units of safety gloves at a total of USD 148.25. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8945",
        "vendor": "Acme Corp",
        "quantity": "12",
        "total_usd": "148.25"
      }
    },
    {
      "input": "Invoice INV-8506 from Stark Industries, dated 2025-03-17. Line item: 144 units of USB hubs at a total of USD 940.95. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8506",
        "vendor": "Stark Industries",
        "quantity": "144",
        "total_usd": "940.95"
      }
    },
    {
      "input": "Invoice INV-9236 from Pied Piper, dated 2025-04-26. Line item: 100 units of laptop docks at a total of USD 2510.93. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-9236",
        "vendor": "Pied Piper",
        "quantity": "100",
        "total_usd": "2510.93"
      }
    },
    {
      "input": "Invoice INV-8832 from Umbrella Inc, dated 2025-06-03. Line item: 12 units of ink cartridges at a total of USD 382.58. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8832",
        "vendor": "Umbrella Inc",
        "quantity": "12",
        "total_usd": "382.58"
      }
    },
    {
      "input": "Invoice INV-5430 from Initech, dated 2025-11-27. Line item: 12 units of ink cartridges at a total of USD 410.51. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-5430",
        "vendor": "Initech",
        "quantity": "12",
        "total_usd": "410.51"
      }
    },
    {
      "input": "Invoice INV-6627 from Hooli, dated 2025-02-04. Line item: 200 units of safety gloves at a total of USD 4988.98. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-6627",
        "vendor": "Hooli",
        "quantity": "200",
        "total_usd": "4988.98"
      }
    },
    {
      "input": "Invoice INV-9974 from Globex Ltd, dated 2025-04-16. Line item: 10 units of floor mats at a total of USD 37.95. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-9974",
        "vendor": "Globex Ltd",
        "quantity": "10",
        "total_usd": "37.95"
      }
    },
    {
      "input": "Invoice INV-4222 from Hooli, dated 2025-10-27. Line item: 100 units of laptop docks at a total of USD 2008.22. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-4222",
        "vendor": "Hooli",
        "quantity": "100",
        "total_usd": "2008.22"
      }
    },
    {
      "input": "Invoice INV-9282 from Stark Industries, dated 2025-09-26. Line item: 24 units of safety gloves at a total of USD 453.97. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-9282",
        "vendor": "Stark Industries",
        "quantity": "24",
        "total_usd": "453.97"
      }
    },
    {
      "input": "Invoice INV-1457 from Acme Corp, dated 2025-12-20. Line item: 50 units of desk lamps at a total of USD 573.91. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-1457",
        "vendor": "Acme Corp",
        "quantity": "50",
        "total_usd": "573.91"
      }
    },
    {
      "input": "Invoice INV-2542 from Umbrella Inc, dated 2025-11-27. Line item: 144 units of desk lamps at a total of USD 1118.54. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-2542",
        "vendor": "Umbrella Inc",
        "quantity": "144",
        "total_usd": "1118.54"
      }
    },
    {
      "input": "Invoice INV-6218 from Stark Industries, dated 2025-09-15. Line item: 10 units of cable reels at a total of USD 22.50. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-6218",
        "vendor": "Stark Industries",
        "quantity": "10",
        "total_usd": "22.50"
      }
    },
    {
      "input": "Invoice INV-3554 from Stark Industries, dated 2025-12-21. Line item: 12 units of steel bolts at a total of USD 24.58. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-3554",
        "vendor": "Stark Industries",
        "quantity": "12",
        "total_usd": "24.58"
      }
    },
    {
      "input": "Invoice INV-2019 from Wonka Co, dated 2025-08-06. Line item: 24 units of copier toner at a total of USD 945.83. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-2019",
        "vendor": "Wonka Co",
        "quantity": "24",
        "total_usd": "945.83"
      }
    },
    {
      "input": "Invoice INV-2601 from Acme Corp, dated 2025-02-15. Line item: 200 units of USB hubs at a total of USD 514.57. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-2601",
        "vendor": "Acme Corp",
        "quantity": "200",
        "total_usd": "514.57"
      }
    },
    {
      "input": "Invoice INV-2486 from Umbrella Inc, dated 2025-02-08. Line item: 144 units of steel bolts at a total of USD 4800.07. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-2486",
        "vendor": "Umbrella Inc",
        "quantity": "144",
        "total_usd": "4800.07"
      }
    },
    {
      "input": "Invoice INV-5070 from Wayne Supplies, dated 2025-05-17. Line item: 12 units of laptop docks at a total of USD 55.82. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-5070",
        "vendor": "Wayne Supplies",
        "quantity": "12",
        "total_usd": "55.82"
      }
    },
    {
      "input": "Invoice INV-9319 from Hooli, dated 2025-05-18. Line item: 24 units of USB hubs at a total of USD 845.92. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-9319",
        "vendor": "Hooli",
        "quantity": "24",
        "total_usd": "845.92"
      }
    },
    {
      "input": "Invoice INV-8634 from Hooli, dated 2025-03-04. Line item: 200 units of desk lamps at a total of USD 2701.26. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8634",
        "vendor": "Hooli",
        "quantity": "200",
        "total_usd": "2701.26"
      }
    },
    {
      "input": "Invoice INV-8855 from Acme Corp, dated 2025-02-13. Line item: 100 units of copier toner at a total of USD 3363.40. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8855",
        "vendor": "Acme Corp",
        "quantity": "100",
        "total_usd": "3363.40"
      }
    },
    {
      "input": "Invoice INV-8481 from Acme Corp, dated 2025-02-16. Line item: 144 units of ink cartridges at a total of USD 2427.94. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8481",
        "vendor": "Acme Corp",
        "quantity": "144",
        "total_usd": "2427.94"
      }
    },
    {
      "input": "Invoice INV-3471 from Stark Industries, dated 2025-09-04. Line item: 144 units of steel bolts at a total of USD 617.59. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-3471",
        "vendor": "Stark Industries",
        "quantity": "144",
        "total_usd": "617.59"
      }
    },
    {
      "input": "Invoice INV-5278 from Globex Ltd, dated 2025-04-18. Line item: 100 units of office chairs at a total of USD 1519.43. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-5278",
        "vendor": "Globex Ltd",
        "quantity": "100",
        "total_usd": "1519.43"
      }
    },
    {
      "input": "Invoice INV-8005 from Pied Piper, dated 2025-08-12. Line item: 100 units of desk lamps at a total of USD 2404.41. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8005",
        "vendor": "Pied Piper",
        "quantity": "100",
        "total_usd": "2404.41"
      }
    },
    {
      "input": "Invoice INV-8757 from Initech, dated 2025-11-17. Line item: 10 units of USB hubs at a total of USD 38.78. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8757",
        "vendor": "Initech",
        "quantity": "10",
        "total_usd": "38.78"
      }
    },
    {
      "input": "Invoice INV-8332 from Umbrella Inc, dated 2025-08-11. Line item: 12 units of ink cartridges at a total of USD 74.19. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8332",
        "vendor": "Umbrella Inc",
        "quantity": "12",
        "total_usd": "74.19"
      }
    },
    {
      "input": "Invoice INV-6685 from Wonka Co, dated 2025-10-04. Line item: 5 units of desk lamps at a total of USD 75.93. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-6685",
        "vendor": "Wonka Co",
        "quantity": "5",
        "total_usd": "75.93"
      }
    },
    {
      "input": "Invoice INV-3476 from Acme Corp, dated 2025-10-16. Line item: 200 units of office chairs at a total of USD 5009.11. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-3476",
        "vendor": "Acme Corp",
        "quantity": "200",
        "total_usd": "5009.11"
      }
    },
    {
      "input": "Invoice INV-8905 from Pied Piper, dated 2025-04-09. Line item: 10 units of USB hubs at a total of USD 36.88. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8905",
        "vendor": "Pied Piper",
        "quantity": "10",
        "total_usd": "36.88"
      }
    },
    {
      "input": "Invoice INV-9134 from Wonka Co, dated 2025-09-09. Line item: 10 units of office chairs at a total of USD 187.94. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-9134",
        "vendor": "Wonka Co",
        "quantity": "10",
        "total_usd": "187.94"
      }
    },
    {
      "input": "Invoice INV-2848 from Globex Ltd, dated 2025-05-02. Line item: 24 units of copier toner at a total of USD 113.67. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-2848",
        "vendor": "Globex Ltd",
        "quantity": "24",
        "total_usd": "113.67"
      }
    },
    {
      "input": "Invoice INV-9627 from Globex Ltd, dated 2025-04-27. Line item: 12 units of ink cartridges at a total of USD 473.79. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-9627",
        "vendor": "Globex Ltd",
        "quantity": "12",
        "total_usd": "473.79"
      }
    },
    {
      "input": "Invoice INV-1950 from Stark Industries, dated 2025-07-03. Line item: 24 units of steel bolts at a total of USD 115.42. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-1950",
        "vendor": "Stark Industries",
        "quantity": "24",
        "total_usd": "115.42"
      }
    },
    {
      "input": "Invoice INV-1296 from Hooli, dated 2025-05-17. Line item: 144 units of cable reels at a total of USD 3084.65. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-1296",
        "vendor": "Hooli",
        "quantity": "144",
        "total_usd": "3084.65"
      }
    },
    {
      "input": "Invoice INV-5744 from Initech, dated 2025-10-10. Line item: 144 units of office chairs at a total of USD 3213.56. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-5744",
        "vendor": "Initech",
        "quantity": "144",
        "total_usd": "3213.56"
      }
    },
    {
      "input": "Invoice INV-5337 from Stark Industries, dated 2025-04-17. Line item: 200 units of office chairs at a total of USD 4275.78. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-5337",
        "vendor": "Stark Industries",
        "quantity": "200",
        "total_usd": "4275.78"
      }
    },
    {
      "input": "Invoice INV-2271 from Acme Corp, dated 2025-10-16. Line item: 100 units of cable reels at a total of USD 2826.89. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-2271",
        "vendor": "Acme Corp",
        "quantity": "100",
        "total_usd": "2826.89"
      }
    },
    {
      "input": "Invoice INV-7651 from Wayne Supplies, dated 2025-10-16. Line item: 12 units of USB hubs at a total of USD 442.66. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-7651",
        "vendor": "Wayne Supplies",
        "quantity": "12",
        "total_usd": "442.66"
      }
    },
    {
      "input": "Invoice INV-4942 from Globex Ltd, dated 2025-05-26. Line item: 144 units of copier toner at a total of USD 1395.15. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-4942",
        "vendor": "Globex Ltd",
        "quantity": "144",
        "total_usd": "1395.15"
      }
    },
    {
      "input": "Invoice INV-2013 from Cyberdyne, dated 2025-01-18. Line item: 144 units of steel bolts at a total of USD 5628.36. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-2013",
        "vendor": "Cyberdyne",
        "quantity": "144",
        "total_usd": "5628.36"
      }
    },
    {
      "input": "Invoice INV-8053 from Initech, dated 2025-11-13. Line item: 50 units of ink cartridges at a total of USD 1973.95. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-8053",
        "vendor": "Initech",
        "quantity": "50",
        "total_usd": "1973.95"
      }
    },
    {
      "input": "Invoice INV-3961 from Pied Piper, dated 2025-04-12. Line item: 10 units of floor mats at a total of USD 234.91. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-3961",
        "vendor": "Pied Piper",
        "quantity": "10",
        "total_usd": "234.91"
      }
    },
    {
      "input": "Invoice INV-7049 from Pied Piper, dated 2025-09-20. Line item: 100 units of office chairs at a total of USD 2808.40. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-7049",
        "vendor": "Pied Piper",
        "quantity": "100",
        "total_usd": "2808.40"
      }
    },
    {
      "input": "Invoice INV-1306 from Pied Piper, dated 2025-03-06. Line item: 200 units of office chairs at a total of USD 4985.87. Payment due within 30 days.",
      "expected": {
        "invoice_number": "INV-1306",
        "vendor": "Pied Piper",
        "quantity": "200",
        "total_usd": "4985.87"
      }
    }
  ]
}