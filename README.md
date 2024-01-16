# Research Artifact: Quantifying and Characterizing Clones of Self-Admitted Technical Debt in Build Systems

This is a research artifact for the paper: **Quantifying and Characterizing Clones of Self-Admitted Technical Debt in Build Systems**. This artifact is a repository consisting of raw data, our SATD dataset for RQ1-3, our labeled SATD comments dataset for RQ4, and scripts. The purposes of this artifact are to enable researchers to reuse the dataset for further software engineering research.


## Abstract
Self-Admitted Technical Debt (SATD) annotates development decisions that intentionally exchange long-term software artifact quality for short-term goals. Recent work explores the existence of SATD clones (duplicate or near duplicate SATD comments) in source code. Cloning of SATD in build systems (i.e., Autotools, CMake, Maven, and Ant) may propagate suboptimal design choices, threatening qualities of the build system that stakeholders rely upon (e.g., maintainability, reliability, repeatability). Hence, we conduct a large-scale study on 50,608 SATD comments extracted from Autotools, CMake, Maven, and Ant build systems to investigate the prevalence of SATD clones and to characterize their incidences. We observe that: (i) prior work suggests that 41–65% of SATD comments in source code are clones, but in our studied build system context, the rates range from 62% to 95%, suggesting that SATD clones are a more prevalent phenomenon in build systems than in source code; (ii) statements surrounding SATD clones are highly similar, with 76% of occurrences having similarity scores greater than 0.8; (iii) a quarter of SATD clones are introduced by the author of the original SATD statements; and (iv) among the most commonly cloned SATD comments, external factors (e.g., platform and tool configuration) are the most frequent locations, limitations in tools and libraries are the most frequent causes, and developers often copy SATD comments that describe issues to be fixed later. Our work presents the first step toward systematically understanding SATD clones in build systems and opens up avenues for future work, such as tool support to track, manage, and repay SATD in the context of build systems

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
	* `Coded_Non_SATD_Sample.csv` - coded Non-SATD sample for testing the missing rate of the SATD keyword-based approach.
	* `Coded_SATD_clones.csv` - coded SATD clones in RQ4.
	* `Coded_cross_tool_SATD_clones.csv` - coded SATD cross-tool clones for their behind reasons.
	* `Coded_cross_language_SATD_clones.csv` - coded SATD cross-language clones for their behind reasons.
	* `Coded_cross_tool_Non_SATD_clones.csv` - coded SATD cross-tool clones for their behind reasons.
	* `Coded_cross_language_Non_SATD_clones.csv` - coded SATD cross-language clones for their behind reasons.
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
* `materials` - a directory of supplementary materials.
	* `thresholds_plot_commits.pdf` - threshold plot for the number of commits.
	* `thresholds_plot_code.pdf` - threshold plot for lines of code in build systems.
	* `thresholds_plot_comment.pdf` - threshold plot for lines of comments in build systems.
	* `thresholds_clone_groups.pdf` - threshold plot for the number of coding SATD clone groups.
	* `similarity_scores_of_commit_messages.pdf` - box plot for similarity scores of commit messages that introduced SATD clones.
	* `clone_time_interval.pdf` - box plot for the clone time interval that introduced SATD clones.
	* `definition.pdf` - detailed definitions of coding guides for SATD locations, reasons, and purposes in RQ4.
* `LICENSE` - [Apache License 2.0](http://www.apache.org/licenses/)
* `README.md` - this file.
