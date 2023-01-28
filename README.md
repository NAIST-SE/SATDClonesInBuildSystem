# Research Artifact: The Prevalence, Authorship, and Characteristics of Self-Admitted Technical Debt Clones in Build Systems

This is a research artifact for the paper: **The Prevalence, Authorship, and Characteristics of Self-Admitted Technical Debt Clones in Build Systems**. This artifact is a repository consisting of raw data, our SATD dataset for RQ1-3, our labeled SATD comments dataset for RQ4,  and scripts. The purposes of this artifact are to enable researchers to reuse the dataset for further software engineering research.


## Abstract
Self-Admitted Technical Debt (SATD) has raised significant interest in the SE community, which annotates technical debt that intentionally trades long-term software artifact quality for short-term goals. Recent work started to explore the existence of SATD clones (duplicate or near duplicate SATD comments) in source codes. However, SATD clones in build systems remain unexplored. In this paper, we conduct a large-scale study on 50,608 SATD comments extracted from various build systems (i.e., Autotools, CMake, Maven, and Ant) to investigate the prevalence of SATD clones and cloning of build specifications, analyze the authorship of SATD clones, and characterize these clones. The key results are summarized: (i) our results show that SATD clones are a frequent phenomenon in build systems, accounting for 62-95\% of SATD comments; (ii) we find that build specifications around SATD clones are highly similar, with similarity scores being greater than 0.8; (iii) we observe that approximately a quarter of SATD clones were introduced by the same author; and (iv) our qualitative results reveal that for those commonly cloned SATD comments, the external factors are the most frequent locations (e.g., platform and tool configuration), that limitations in tools and libraries are the major causes, and that developers often leave SATD comments as issues to be fixed later. Our work presents the first step toward systematically understanding SATD clones in build systems and opens up avenues for future work, such as tool support to track, manage, and repay SATD.

## Contents
* `data` - a directory of the dataset
	* `SATD_comment` - a directory of completed row SATD comments dataset.
	* `Comments_with_no_keywords` - a directory of completed row Non-SATD comments dataset.
	* `C.csv` - C repository list from [Dabic et al.](https://ieeexplore.ieee.org/abstract/document/9463094/).
	* `Cpp.csv ` - Cpp repository list from [Dabic et al.](https://ieeexplore.ieee.org/abstract/document/9463094/).
	* `Java.csv` - Java repository list from [Dabic et al.](https://ieeexplore.ieee.org/abstract/document/9463094/).
	* `ObjectiveC.csv` - Objective C repository list from [Dabic et al.](https://ieeexplore.ieee.org/abstract/document/9463094/).
	* `keywords_list.txt ` - SATD keyword list from [Xiao et al.](https://ieeexplore.ieee.org/abstract/document/9551792). 
	* `data_filter_repolist_with_full_info.csv` - full information of repository list that is used in this study.
	* `top_286_SATD_clone_group_fix.csv` - Coded SATD clones in the data preparation.
	* `SATD_clones.csv` - results of cloned SATD comments in RQ1.
	* `Non_SATD_clones.csv` - results of cloned Non-SATD comments in RQ1.
	* `SATD_clones_with_code.csv` - results of cloned SATD with code snippets in RQ2.
	* `Non_SATD_clones_with_code.csv` - results of cloned Non-SATD with code snippets in RQ2.
	* `RQ2_SATD_stat.csv` - statistics results of cloned SATD for significant tests in RQ2.
	* `RQ2_Non_SATD_stat.csv` - statistics results of cloned Non-SATD for significant tests in RQ2.
	* `SATD_clones_with_authorship.csv` - results of cloned SATD with authorship in RQ3.
	* `Non_SATD_clones_with_authorship.csv` - results of cloned Non-SATD with authorship in RQ3.
	* `RQ3_SATD_stat.csv` - statistics results of cloned SATD for significant tests in RQ3.
	* `RQ3_Non_SATD_stat.csv` - statistics results of cloned Non-SATD for significant tests in RQ3.
	* `Coded_SATD_clones.csv` - coded SATD clones in RQ4.
	* `Coded_cross_system_SATD_clones.csv` - coded SATD cross system clones in the Discussion.
	* `Coded_cross_language_SATD_clones.csv` - coded SATD cross language clones in the Discussion.
* `script` - a directory of scripts.
	* `lexer` - a directory of ANTLR4 grammar files.
	* `README.md` - a readme file for the script directory.
	* `Project_Filtering.ipynb` - script for filtering projects.
	* `calculate_build_investiment.py` - script for calculating build investment.
	* `extract_SATD_comments.py` - script for extracting SATD comments and Non-SATD comments.
	* `RQ1.ipynb` - a script that is used in RQ1 for SATD clones.
	* `RQ1_Non_SATD.ipynb` - a script that is used in RQ1 for Non-SATD clones.
	* `RQ2.ipynb` - a script that is used in RQ2 for SATD clones.
	* `RQ2_Non_SATD.ipynb` - a script that is used in RQ2 for Non-SATD clones.
	* `RQ3.ipynb` - a script that is used in RQ3 for SATD clones.
	* `RQ3_Non_SATD.ipynb` - a script that is used in RQ3 for SNon-ATD clones.
	* `thresholds_plot_commits.pdf` - threshold plot for the number of commits.
	* `thresholds_plot_code.pdf` - threshold plot for lines of code in build systems.
	* `thresholds_plot_comment.pdf` - threshold plot for lines of comments in build systems.
	* `thresholds_clone_groups.pdf` - threshold plot for the number of coding SATD clone groups. 
* `LICENSE` - [Apache License 2.0](http://www.apache.org/licenses/)
* `README.md` - this file.