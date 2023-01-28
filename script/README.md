# This file includes the process for reproducing our analysis.

## Steps
* `Step 1`: We use `calculate_build_investiment.py` and `Project_Filtering.ipynb` to filter projects.
```
parallel -j 20 --joblog joblog-loc-repos.txt --colsep ',' python3 calculate_build_investiment.py {4} {3}  :::: ../data/repolist.csv > ../data/loc_results.csv
```

* `Step 2`: We clone GitHub repositories from `../data/repolist.csv`.
```
parallel -j 20 --joblog joblog-buildfiles-repos.txt --colsep ',' git clone  {3} {1} :::: ../data/repolist.csv
```

* `Step 3`: We use `extract_SATD_comments.py` to extract SATD comments and Non-SATD comments.
```
parallel -j 20 --joblog joblog-extract_comments-repos.txt --colsep ',' python3 extract_SATD_comments.py {1} {11} {36} :::: ../data/data_filter_repolist_with_full_info_no_header_fixed.csv 
```

* `Step 4`: We use other .ipynb files for analysis in RQ1-3.

## Required libraries and tools to extract SATD comments
* GNU parallel [1].
* Required python libraries:
```
beautifulsoup4==4.11.1
lxml==4.6.1
antlr4-python3-runtime==4.10
```

[1] Tange (2011): GNU Parallel - The Command-Line Power Tool,
  ;login: The USENIX Magazine, February 2011:42-47.