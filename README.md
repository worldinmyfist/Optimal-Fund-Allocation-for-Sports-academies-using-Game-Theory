# Optimal-Fund-Allocation-for-State-Sports-Academies-using-Game-Theory-and-Mechanism-Design
This a way for allocating funds to sports academies based on game theory. Refer to [this](https://github.com/worldinmyfist/Optimal-Fund-Allocation-for-State-Sports-Academies-using-Game-Theory-and-Mechanism-Design/blob/main/Report.pdf) for more details

## INPUT FORMAT
    #Line 1 : Number of Recognised Players from each academy separated by commas (sum of these should be L)
    #Line 2 to 2+n-1 : Type Set for each academic representative separated by commas, total n in number
    
## SAMPLE INPUT
    1,1,2
    7,8,6,5,0,0,0
    7,8,6,5,0,0,0
    6,6,8,7,0,0,0
 
 [ex1.txt](https://github.com/worldinmyfist/Optimal-Fund-Allocation-for-State-Sports-Academies-using-Game-Theory-and-Mechanism-Design/blob/main/ex1.txt) and [ex2.txt](https://github.com/worldinmyfist/Optimal-Fund-Allocation-for-State-Sports-Academies-using-Game-Theory-and-Mechanism-Design/blob/main/ex2.txt) contain more samples.
    
## HOW TO RUN THE CODE
    ```usage : python3 useCase.py <input_file> <a> <b> <M> <MAF>```
    where
    - a,b : Parameters used in Social Choice Function (Float/Int)
    - M : Maximum Possible Fund Allocation Points for Recognised players (Int)
    - MAF : Maximum Possible Reward Funds for Academy Representatives (Int)
    
## AUTHOR
[ARYAN AGARWAL](https://github.com/worldinmyfist/)

## CONTRIBUTION
Pull requests are welcome. For major changes, please open an issue to discuss what you would like to change.

