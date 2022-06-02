# Input File Format
    
    #Line 1 : Number of Recognised Players from each academy separated by commas (sum of these should be L)
    #Line 2 to 2+n-1 : Type Set for each academic representative separated by commas, total n in number
## Sample Input File
    1,1,2
    7,8,6,5,0,0,0
    7,8,6,5,0,0,0
    6,6,8,7,0,0,0

# How To Run
    ```usage : python3 useCase.py <input_file> <a> <b> <M> <MAF>```
    where
    - a,b : Parameters used in Social Choice Function (Float/Int)
    - M : Maximum Possible Fund Allocation Points for Recognised players (Int)
    - MAF : Maximum Possible Reward Funds for Academy Representatives (Int)
