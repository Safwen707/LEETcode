#define rep(i, a, b) for (int i = a; i < (b); ++i) // Forward loop
void backtrack( vector<vector<string>>& res, vector<string> &sol,vector<bool>& cols,int row ,vector<bool>& diag1,int n,vector<bool>&diag2,int & k){
    if (row==n){
        res.push_back(sol);
        k+=1;
        return;

    }
    rep(col,0,n){
        if (cols[col] && diag1[col-row+n-1]&& diag2[row+col]){
            sol[row][col]='Q';
            cols[col]=false;
            diag1[col-row+n-1]=false;
            diag2[row+col]=false; 
            backtrack(res,sol,cols,row+1,diag1,n,diag2,k);
            sol[row][col]='.';
            cols[col]=true;
            diag1[col-row+n-1]=true;
            diag2[row+col]=true; 
            



        }
    }
    

}

class Solution {
public:
    int totalNQueens(int n) {
        vector<vector<string>> res;
        vector<string> sol(n,string(n,'.'));
        int k=0;
        vector<bool>cols(n,true) ;
        vector<bool>diag1(n,true) ;
        vector<bool>diag2(n,true) ;
        backtrack(res,sol,cols,0,diag1,n,diag2,k);
        return k;
        
    }
};