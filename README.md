# usecase

Claim filter example:
1. With claim type
http://127.0.0.1:8000/claims/filterlist?claim_type=Medical
2. With period
http://127.0.0.1:8000/claims/filterlist?claim_type=Medical&claim_periods_in_months=6
3. With daterange:
http://127.0.0.1:8000/claims/filterlist?claim_type=Medical&claim_start_date=2017-08-31&claim_end_date=2020-08-31
