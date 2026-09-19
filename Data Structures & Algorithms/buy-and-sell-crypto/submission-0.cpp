class Solution {
public:
    int maxProfit(vector<int>& p) {
        int i = 0;
        int res = 0;
        for(i; i < p.size() - 1; i ++) 
        {
            int j = i + 1;
            for (; j < p.size(); j ++)
            {
                int tmp = p[j] - p[i];
                if (tmp > res)
                {
                    res = tmp;
                }
            }
        }

        if (res > 0)
        {
            return res;
        }else
        {
            return 0;
        }
    }
};
