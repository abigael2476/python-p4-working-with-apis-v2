# TODO List - Working with APIs Assignment

## Status: In Progress

### Step 1: Remove interactive input code from open_library_api.py

- [x] Remove the `input()` call and interactive print statements at the bottom of the file
- This code will block automated testing

### Step 2: Update codegrade_test.py with proper tests

- [x] Test `get_search_results()` returns bytes
- [x] Test `get_search_results_json()` returns a dict with proper structure
- [x] Test `get_user_search_results(search_term)` returns formatted string

### Step 3: Run tests to verify

- [ ] Run `pytest` to verify all tests pass
