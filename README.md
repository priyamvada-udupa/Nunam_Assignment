# Nunam_Assignment

Python assignment repository for Nunam

## Assessment task for Data Engineer

**2 identical XLS files are shared which contains data sampled at `1 sample/second`**

These 2 data files are from the same data source and represents same data, due to space restrictions of the file type it is divided into 2 separate files named _'data.xls'_ and _'data_1.xls'_ and while saving the data, it is also saved not accordingly, follow the index column named _'Record Index'_ to see the parity.

## Tasks

1. Create 3 separate _'_.csv'\* files named `'detail.csv'`, `'detailVol.csv'` and `'detailTemp.csv'`. 1. Combine all the data in sheets named like "Detail*67*" only, among the two data files provided, and save into `'detail.csv'` 2. Combine all the data in sheets named like "DetailVol*67*" only, among the two data files provided, and save into `'detailVol.csv'` 3. Combine all the data in sheets named like "DetailTemp*67*" only, among the two data files provided, and save into `'detailTemp.csv'`
   Provide attention to the column `'Record Index'` which provided index values to avoid mismatching the rows while combining multiple files.

2. Apply down-sampling method to reduce the sampling rate to `1 sample/minute`. Appy the same to `'detail.csv'`, `'detailVol.csv'` and `'detailTemp.csv'` and creating 3 files named `'detailDownsampled.csv'`, `'detailVolDownsampled.csv'` and `'detailTempDownsampled.csv'`
3. Apply `low pass filter` technique for noise removal on the data set for `'detailVolDownsampled.csv'` and show the distribution of the dataset through visualization, also provide explanantion of the same.

4. Run profile for all the functions; use `cProfile` for profiling of individual functions.

5. Run unit test on each function,i.e., write test cases for each function. Use `unittest` for the same
6. Try to implement Coding Style Guide **[PEP-8]**, and use pylint or flake8 to check the code for PEP-8 violations.

## Delivarables

1. One _'\*.py'_ file with detailed commented code on the working for _`Task 1`_ and its subtasks. The intention is to see how the code is architected rather than simple execution. Try employing functional programming concepts and making the code look clean by following PEP-8 coding style.
   1. The code should be reproducible on any environment; i.e. system agnostic and the intended data files should be generated running the code
2. One _'\*.py'_ file with detailed commented code on the working for _`Task 2`_ and its subtasks. Try employing functional programming concepts and making the code look clean by following PEP-8 coding style.
   1. The code should be reproducible on any environment; i.e. system agnostic and the intended data files should be generated running the code
3. One Jupyter NoteBook file for `Task 3` along with visualization
4. Profile testing result in a _"\*.txt"_ file for all the functions runtime; use `cProfile`
5. Unit testing result in a _"\*.txt"_ file for all the functions ; use `unittest`
