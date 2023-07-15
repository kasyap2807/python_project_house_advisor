# python_project_house_advisor
This program helps us to get details of by taking dataset and taking inputs like cost,no of bedrooms and cost giving output like bathrooms ,hospital ,cost difference between last year and now etc…
output:
s.no   place  cost  house type  bedrooms  bathrooms  floor no    hosipatal    \                                                                     
1      nsp  10000           1         3          4         0          2.0   
2      nsp   6000           2         2          3         1          3.0   
3      nsp   5000           2         1          2         2          4.0   
4      nsp  11000           1         2          3         0          6.0   
5      nsp   5000           2         1          2         5          7.0   

      bazaar  bus stand   last year price  actual price  diff  
s.no                                                           
1          3           2             9000         10000     0  
2          2           3             5000          8000 -2000  
3          2           4             3000          6000 -1000  
4          5           1             8000          8000  3000  
5          4           1             4000          6000 -1000  
               cost  house type   bedrooms  bathrooms   floor no  hosipatal    \
count     10.000000   10.000000  10.000000  10.000000  10.000000    10.000000   
mean   11300.000000    1.500000   2.300000   3.300000   1.400000     3.070000   
std     6750.308635    0.527046   1.159502   1.159502   1.837873     2.327158   
min     5000.000000    1.000000   1.000000   2.000000   0.000000     0.500000   
25%     6250.000000    1.000000   1.250000   2.250000   0.000000     1.125000   
50%     9500.000000    1.500000   2.000000   3.000000   0.500000     2.500000   
75%    14000.000000    2.000000   3.000000   4.000000   2.000000     4.750000   
max    25000.000000    2.000000   4.000000   5.000000   5.000000     7.000000   

          bazaar  bus stand   last year price  actual price          diff  
count  10.000000   10.000000         10.00000     10.000000     10.000000  
mean    2.600000    2.700000       9900.00000   8600.000000   2700.000000  
std     1.264911    1.337494       7324.99526   2319.003617   5271.516754  
min     1.000000    1.000000       3000.00000   6000.000000  -2000.000000  
25%     2.000000    2.000000       5000.00000   6500.000000  -1000.000000  
50%     2.500000    2.500000       7500.00000   8000.000000   1500.000000  
75%     3.000000    3.750000      12000.00000  10000.000000   3000.000000  
max     5.000000    5.000000      25000.00000  12000.000000  15000.000000  
place               object
cost                 int64
house type           int64
bedrooms             int64
bathrooms            int64
floor no             int64
hosipatal          float64
bazaar               int64
bus stand            int64
last year price      int64
actual price         int64
diff                 int64
dtype: object
the avg cost inc between last and this year is 2700.0 among all types
enter no of bedrooms3
enter house type (1 for individual 2 for portions2
enter prce upto10000
the best houses under 10000 are:
     place   cost  house type  bedrooms  bathrooms  floor no  hosipatal    \
s.no                                                                        
3      nsp   5000           2         1          2         2          4.0   
5      nsp   5000           2         1          2         5          7.0   
2      nsp   6000           2         2          3         1          3.0   
7      nsp   7000           2         2          3         2          1.5   
6      nsp   9000           2         1          2         4          1.0   
1      nsp  10000           1         3          4         0          2.0   

      bazaar  bus stand   last year price  actual price  diff  
s.no                                                           
3          2           4             3000          6000 -1000  
5          4           1             4000          6000 -1000  
2          2           3             5000          8000 -2000  
7          2           3             5000          8000 -1000  
6          3           2             7000          6000  3000  
1          3           2             9000         10000     0  
the avg cost  7000.0 for 3 bedrooms
